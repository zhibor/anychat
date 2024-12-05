import gradio as gr

# Load the Gradio space
demo = gr.load(name="akhaliq/paligemma2-10b-ft-docci-448", src="spaces")


# Disable API access for all functions
if hasattr(demo, 'fns'):
    for fn in demo.fns.values():
        fn.api_name = False
