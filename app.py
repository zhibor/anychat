import gradio as gr
import gemini_gradio
import openai_gradio
import anthropic_gradio
import sambanova_gradio
import xai_gradio
import hyperbolic_gradio


with gr.Blocks(fill_height=True) as demo:
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
    with gr.Tab("Claude"):
        gr.load(
        name='claude-3-opus-20240229',
        src=anthropic_gradio.registry,
        accept_token=True
        )
    with gr.Tab("Meta Llama 405B"):
        gr.load(
        name='Meta-Llama-3.1-405B-Instruct',
        src=sambanova_gradio.registry,
        accept_token=True,
        multimodal = True
        )
    with gr.Tab("Grok"):
        gr.load(
        name='grok-beta',
        src=xai_gradio.registry,
        accept_token=True
        )
    with gr.Tab("Qwen2.5 72B"):
        gr.load(
        name='Qwen/Qwen2.5-72B-Instruct',
        src=hyperbolic_gradio.registry,
        accept_token=True
    )


demo.launch()


