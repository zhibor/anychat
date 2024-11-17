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
        with gr.Row():
            model_choice = gr.Dropdown(
                choices=['gpt-4-turbo', 'gpt-4', 'gpt-3.5-turbo'],
                value='gpt-4-turbo',
                label="Select Model"
            )
        gr.load(
            name=model_choice.value,
            src=openai_gradio.registry,
            accept_token=True
        )
    with gr.Tab("Claude"):
        with gr.Row():
            claude_model = gr.Dropdown(
                choices=['claude-3-sonnet-20240229', 'claude-3-opus-20240229'],
                value='claude-3-sonnet-20240229',
                label="Select Model"
            )
        gr.load(
            name=claude_model.value,
            src=anthropic_gradio.registry,
            accept_token=True
        )
    with gr.Tab("Meta Llama-3.2-90B-Vision-Instruct"):
        gr.load(
            name='Llama-3.2-90B-Vision-Instruct',
            src=sambanova_gradio.registry,
            accept_token=True,
            multimodal=True,
            description="Requires SambaNova API key"
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


