import gradio as gr
import gemini_gradio

gr.load(
    name='gemini-1.5-pro-002',
    src=gemini_gradio.registry,
).launch()