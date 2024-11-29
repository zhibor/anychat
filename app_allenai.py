from gradio_client import Client
import gradio as gr

MODELS = {
    "OLMo-2-1124-13B-Instruct": "akhaliq/olmo-anychat",
    "Llama-3.1-Tulu-3-8B": "akhaliq/allen-test"
}

def create_chat_fn(client):
    def chat(message, history):
        response = client.predict(
            message=message,
            system_prompt="You are a helpful AI assistant.",
            temperature=0.7,
            max_new_tokens=1024,
            top_k=40,
            repetition_penalty=1.1,
            top_p=0.95,
            api_name="/chat"
        )
        return response
    return chat

def set_client_for_session(model_name, request=None):
    headers = {}
    if request and hasattr(request, 'request') and hasattr(request.request, 'headers'):
        x_ip_token = request.request.headers.get('x-ip-token')
        if x_ip_token:
            headers["X-IP-Token"] = x_ip_token
    
    return Client(MODELS[model_name], headers=headers)

def safe_chat_fn(message, history, client):
    if client is None:
        return "Error: Client not initialized. Please refresh the page."
    return create_chat_fn(client)(message, history)

with gr.Blocks() as interface:
    
    client = gr.State()
    
    model_dropdown = gr.Dropdown(
        choices=list(MODELS.keys()),
        value="OLMo-2-1124-13B-Instruct",
        label="Select Model",
        interactive=True
    )
    
    chat_interface = gr.ChatInterface(
        fn=safe_chat_fn,
        additional_inputs=[client]
    )
    
    # Update client when model changes
    def update_model(model_name, request):
        return set_client_for_session(model_name, request)
    
    model_dropdown.change(
        fn=update_model,
        inputs=[model_dropdown],
        outputs=[client],
    )
    
    # Initialize client on page load
    interface.load(
        fn=set_client_for_session,
        inputs=gr.State("OLMo-2-1124-13B-Instruct"),
        outputs=client,
    )



