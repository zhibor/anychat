import gradio as gr

from app_allenai import demo as demo_allenai
from app_claude import demo as demo_claude
from app_experimental import demo as demo_experimental
from app_fireworks import demo as demo_fireworks
from app_flux import demo as demo_flux
from app_gemini import demo as demo_gemini
from app_groq import demo as demo_groq
from app_hyperbolic import demo as demo_hyperbolic
from app_ltx_video import demo as demo_ltx_video
from app_marco_o1 import demo as demo_marco_o1
from app_mistral import demo as demo_mistral
from app_nvidia import demo as demo_nvidia
from app_openai import demo as demo_openai
from app_perplexity import demo as demo_perplexity
from app_qwen import demo as demo_qwen
from app_sambanova import demo as demo_sambanova
from app_together import demo as demo_together
from app_xai import demo as demo_grok

with gr.Blocks(fill_height=True) as demo:
    with gr.Tab("Hyperbolic"):
        demo_hyperbolic.render()
        gr.Markdown(
            """
        <div>
            <img src="https://storage.googleapis.com/public-arena-asset/hyperbolic_logo.png" alt="Hyperbolic Logo" style="height: 50px; margin-right: 10px;">
        </div>

        **Note:** This model is supported by Hyperbolic. Build your AI apps at [Hyperbolic](https://app.hyperbolic.xyz/).
        """
        )
    with gr.Tab("Gemini"):
        demo_gemini.render()
    with gr.Tab("ChatGPT"):
        demo_openai.render()
    with gr.Tab("Claude"):
        demo_claude.render()
    with gr.Tab("Qwen"):
        demo_qwen.render()
    with gr.Tab("AllenAI"):
        demo_allenai.render()
    with gr.Tab("Grok"):
        demo_grok.render()
    with gr.Tab("Perplexity"):
        demo_perplexity.render()
    with gr.Tab("Experimental"):
        demo_experimental.render()
    with gr.Tab("Meta Llama"):
        demo_sambanova.render()
        gr.Markdown(
            "**Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/)."
        )
    with gr.Tab("Marco-o1"):
        demo_marco_o1.render()
    with gr.Tab("LTX Video"):
        demo_ltx_video.render()
    with gr.Tab("Groq"):
        demo_groq.render()
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
