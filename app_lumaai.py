import gradio as gr
import lumaai_gradio

demo = gr.load(
    name='dream-machine',
    src=lumaai_gradio.registry,
)