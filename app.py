import gradio as gr

from app_claude import demo as demo_claude
from app_fireworks import demo as demo_fireworks
from app_gemini import demo as demo_gemini
from app_groq import demo as demo_groq
from app_hf import demo as demo_hf
from app_hyperbolic import demo as demo_hyperbolic
from app_mistral import demo as demo_mistral
from app_nvidia import demo as demo_nvidia
from app_openai import demo as demo_openai
from app_perplexity import demo as demo_perplexity
from app_qwen import demo as demo_qwen
from app_sambanova import demo as demo_sambanova
from app_together import demo as demo_together
from app_xai import demo as demo_grok
from app_flux import demo as demo_flux
from app_sambanova_qwen import demo as demo_sambanova_qwen

with gr.Blocks(fill_height=True) as demo:
    with gr.Tab("Meta Llama"):
        demo_sambanova.render()
        gr.Markdown(
            "**Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/)."
        )
    with gr.Tab("Gemini"):
        demo_gemini.render()
    with gr.Tab("ChatGPT"):
        demo_openai.render()
    with gr.Tab("Claude"):
        demo_claude.render()
    with gr.Tab("SambaNova Qwen"):
        demo_sambanova_qwen.render()
    with gr.Tab("Grok"):
        demo_grok.render()
    with gr.Tab("Hugging Face"):
        demo_hf.render()
    with gr.Tab("Groq"):
        demo_groq.render()
    with gr.Tab("Hyperbolic"):
        demo_hyperbolic.render()
    with gr.Tab("Qwen"):
        demo_qwen.render()
    with gr.Tab("Perplexity"):
        demo_perplexity.render()
    with gr.Tab("Mistral"):
        demo_mistral.render()
    with gr.Tab("Fireworks"):
        demo_fireworks.render()
    with gr.Tab("Together"):
        demo_together.render()
    with gr.Tab("NVIDIA"):
        demo_nvidia.render()
    with gr.Tab("Flux"):
        demo_flux.render()


if __name__ == "__main__":
    demo.queue(api_open=False).launch(ssr_mode=False, show_api=False)
