import gradio as gr
import spaces
import transformers_gradio

# Load Llama model
demo = gr.load(name="allenai/Llama-3.1-Tulu-3-8B", src=transformers_gradio.registry)
demo.fn = spaces.GPU()(demo.fn)

# Load OLMo model
olmo_demo = gr.load(name="akhaliq/olmo-anychat", src="spaces")


# Disable API names for both demos
for fn in demo.fns.values():
    fn.api_name = False
for fn in olmo_demo.fns.values():
    fn.api_name = False

if __name__ == "__main__":
    # Launch both demos
    gr.TabbedInterface([demo, olmo_demo], ["Llama", "OLMo"]).launch()
