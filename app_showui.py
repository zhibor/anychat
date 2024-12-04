import gradio as gr

# Load the Gradio space
demo = gr.load(name="showlab/ShowUI", src="spaces")


# Disable API access for all functions
if hasattr(demo, 'fns'):
    for fn in demo.fns.values():
        fn.api_name = False
