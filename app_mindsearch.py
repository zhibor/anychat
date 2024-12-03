import gradio as gr
import spaces

# Load the Gradio space
demo = gr.load(name="internlm/MindSearch", src="spaces")

# Ensure the main function runs on a GPU
# if hasattr(demo, 'fn'):
#     demo.fn = spaces.GPU()(demo.fn)

# Disable API access for all functions
if hasattr(demo, 'fns'):
    for fn in demo.fns.values():
        fn.api_name = False

if __name__ == "__main__":
    demo.launch()