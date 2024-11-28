import gradio as gr
import spaces
import transformers_gradio

# Load models
llama_demo = gr.load(name="allenai/Llama-3.1-Tulu-3-8B", src=transformers_gradio.registry)
llama_demo.fn = spaces.GPU()(llama_demo.fn)

olmo_demo = gr.load(name="akhaliq/olmo-anychat", src="spaces")

# Create the interface
with gr.Blocks() as demo:
    model_dropdown = gr.Dropdown(
        choices=["allenai/Llama-3.1-Tulu-3-8B", "akhaliq/olmo-anychat"],
        value="allenai/Llama-3.1-Tulu-3-8B",
        label="Select Model"
    )
    
    def chat(message, model_name):
        if model_name == "allenai/Llama-3.1-Tulu-3-8B":
            return llama_demo.fn(message)
        else:
            return olmo_demo.fn(message)

    chatinterface = gr.ChatInterface(chat, additional_inputs=[model_dropdown])

# Disable API names
for fn in demo.fns.values():
    fn.api_name = False


