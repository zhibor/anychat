import gradio as gr
import gemini_gradio
import openai_gradio

with gr.Blocks() as demo:
    with gr.Tab("Gemini"):
        gr.load(
            name='gemini-1.5-pro-002',
            src=gemini_gradio.registry,
             accept_token=True
        )
    with gr.Tab("ChatGPT"):
        gr.load(
        name='gpt-4-turbo',
        src=openai_gradio.registry,
        accept_token=True
        )

demo.launch()


