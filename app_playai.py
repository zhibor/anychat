import gradio as gr
import playai_gradio

demo =gr.load(
    name='PlayDialog',
    src=playai_gradio.registry,
)