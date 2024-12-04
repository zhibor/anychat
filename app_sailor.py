import gradio as gr
import spaces
import transformers_gradio

demo = gr.load(name="sail/Sailor2-20B-Chat", src=transformers_gradio.registry)
demo.fn = spaces.GPU()(demo.fn)

for fn in demo.fns.values():
    fn.api_name = False
