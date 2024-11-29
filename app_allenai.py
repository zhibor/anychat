import gradio as gr
import spaces
import transformers_gradio

# Load Llama model
demo = gr.load(name="akhaliq/allen-test", src="spaces")

# Load OLMo model
olmo_demo = gr.load(name="akhaliq/olmo-anychat", src="spaces")

# Disable API names for both demos
for fn in demo.fns.values():
    fn.api_name = False
for fn in olmo_demo.fns.values():
    fn.api_name = False

# Create a dropdown to select the model
with gr.Blocks() as combined_demo:
    model_choice = gr.Dropdown(
        choices=["Llama", "OLMo"],
        value="Llama",
        label="Select Model"
    )
    
    with gr.Tab("Model Interface"):
        # Create placeholder for the selected model's interface
        placeholder = gr.HTML()
        
        def update_interface(choice):
            if choice == "Llama":
                return demo
            else:
                return olmo_demo
        
        model_choice.change(
            fn=update_interface,
            inputs=[model_choice],
            outputs=[placeholder]
        )



