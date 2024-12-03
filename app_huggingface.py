from gradio_client import Client, handle_file
import gradio as gr
import os


MODELS = {
    "SmolVLM-Instruct": "akhaliq/SmolVLM-Instruct"
}

def create_chat_fn(client):
    def chat(message, history):
        # Extract text and files from the message
        text = message.get("text", "")
        files = message.get("files", [])
        
        # Handle file uploads if present
        processed_files = [handle_file(f) for f in files]
        
        response = client.predict(
            message={"text": text, "files": processed_files},
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

def set_client_for_session(model_name, request: gr.Request):
    headers = {}
    if request and hasattr(request, 'headers'):
        x_ip_token = request.headers.get('x-ip-token')
        if x_ip_token:
            headers["X-IP-Token"] = x_ip_token
    
    return Client(MODELS[model_name], headers=headers)

def safe_chat_fn(message, history, client):
    if client is None:
        return "Error: Client not initialized. Please refresh the page."
    try:
        return create_chat_fn(client)(message, history)
    except Exception as e:
        print(f"Error during chat: {str(e)}")
        return f"Error during chat: {str(e)}"

with gr.Blocks() as demo:
    
    client = gr.State()
    
    model_dropdown = gr.Dropdown(
        choices=list(MODELS.keys()),
        value="SmolVLM-Instruct",
        label="Select Model",
        interactive=True
    )
    
    chat_interface = gr.ChatInterface(
        fn=safe_chat_fn,
        additional_inputs=[client],
        multimodal=True
    )
    
    # Update client when model changes
    model_dropdown.change(
        fn=set_client_for_session,
        inputs=[model_dropdown],
        outputs=[client]
    )
    
    # Initialize client on page load
    demo.load(
        fn=set_client_for_session,
        inputs=[gr.State("SmolVLM-Instruct")],
        outputs=[client]
    )

demo = demo

