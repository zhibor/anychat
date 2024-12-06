from gradio_client import Client, handle_file
import gradio as gr
import os

MODELS = {
    "Paligemma-10B": "akhaliq/paligemma2-10b-ft-docci-448"
}

def create_chat_fn(client, system_prompt, temperature, max_tokens, top_k, rep_penalty, top_p):
    def chat(message, history):
        text = message.get("text", "")
        files = message.get("files", [])
        processed_files = [handle_file(f) for f in files]
        
        response = client.predict(
            message={"text": text, "files": processed_files},
            system_prompt=system_prompt,
            temperature=temperature,
            max_new_tokens=max_tokens,
            top_k=top_k,
            repetition_penalty=rep_penalty,
            top_p=top_p,
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

def safe_chat_fn(message, history, client, system_prompt, temperature, 
                 max_tokens, top_k, rep_penalty, top_p):
    if client is None:
        return "Error: Client not initialized. Please refresh the page."
    try:
        return create_chat_fn(client, system_prompt, temperature, 
                            max_tokens, top_k, rep_penalty, top_p)(message, history)
    except Exception as e:
        print(f"Error during chat: {str(e)}")
        return f"Error during chat: {str(e)}"

with gr.Blocks() as demo:
    client = gr.State()
    
    with gr.Row():
        model_dropdown = gr.Dropdown(
            choices=list(MODELS.keys()),
            value="paligemma2-10b-ft-docci-448",
            label="Select Model",
            interactive=True
        )
    
    with gr.Accordion("Advanced Settings", open=False):
        system_prompt = gr.Textbox(
            value="You are a helpful AI assistant.",
            label="System Prompt"
        )
        with gr.Row():
            temperature = gr.Slider(
                minimum=0.0, maximum=2.0, value=0.7,
                label="Temperature"
            )
            top_p = gr.Slider(
                minimum=0.0, maximum=1.0, value=0.95,
                label="Top P"
            )
        with gr.Row():
            top_k = gr.Slider(
                minimum=1, maximum=100, value=40, step=1,
                label="Top K"
            )
            rep_penalty = gr.Slider(
                minimum=1.0, maximum=2.0, value=1.1,
                label="Repetition Penalty"
            )
        max_tokens = gr.Slider(
            minimum=64, maximum=4096, value=1024, step=64,
            label="Max Tokens"
        )
    
    chat_interface = gr.ChatInterface(
        fn=safe_chat_fn,
        additional_inputs=[client, system_prompt, temperature, 
                         max_tokens, top_k, rep_penalty, top_p],
        multimodal=True
    )
    
    # Add model change handler
    model_dropdown.change(
        fn=set_client_for_session,
        inputs=[model_dropdown],
        outputs=[client]
    )
    
    # Initialize client on page load
    demo.load(
        fn=set_client_for_session,
        inputs=[gr.State("Paligemma-10B")],
        outputs=[client]
    )

# Move the API access check here, after demo is defined
if hasattr(demo, 'fns'):
    for fn in demo.fns.values():
        fn.api_name = False

demo.launch()