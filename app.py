import gradio as gr

from app_meta import demo as demo_meta
from app_lumaai import demo as demo_lumaai
from app_paligemma import demo as demo_paligemma
from app_replicate import demo as demo_replicate
from app_huggingface import demo as demo_huggingface
from app_playai import demo as demo_playai
from app_allenai import demo as demo_allenai
from app_claude import demo as demo_claude
from app_experimental import demo as demo_experimental
from app_fireworks import demo as demo_fireworks
from app_gemini import demo as demo_gemini
from app_groq import demo as demo_groq
from app_hyperbolic import demo as demo_hyperbolic
from app_fal import demo as demo_fal
from app_marco_o1 import demo as demo_marco_o1
from app_mistral import demo as demo_mistral
from app_nvidia import demo as demo_nvidia
from app_openai import demo as demo_openai
from app_perplexity import demo as demo_perplexity
from app_qwen import demo as demo_qwen
from app_sailor import demo as demo_sailor
from app_sambanova import demo as demo_sambanova
from app_together import demo as demo_together
from app_xai import demo as demo_grok
from app_showui import demo as demo_showui
from app_omini import demo as demo_omini

with gr.Blocks(fill_height=True) as demo:
    with gr.Tab("Hyperbolic (New Meta Llama 3.3 70B)"):
        demo_hyperbolic.render()
        gr.Markdown(
            """
        <div>
            <img src="https://storage.googleapis.com/public-arena-asset/hyperbolic_logo.png" alt="Hyperbolic Logo" style="height: 50px; margin-right: 10px;">
        </div>

        **Note:** This model is supported by Hyperbolic. Build your AI apps at [Hyperbolic](https://app.hyperbolic.xyz/).
        
        This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.
        """
        )
    with gr.Tab("Fireworks (New Meta Llama 3.3 70B)"):
        demo_fireworks.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Together (New Meta Llama 3.3 70B)"):
        demo_together.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Groq (New Meta Llama 3.3 70B)"):
        demo_groq.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Hugging Face (New Meta Llama 3.3 70B)"):
        demo_meta.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("LumaAI"):
        demo_lumaai.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio.<img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>")
    with gr.Tab("Paligemma 2"):
        gr.Markdown("paligemma2-10b-ft-docci-448 is a fine-tuned version of Paligemma 2 on the DOCCI dataset, which can accomplish a wide range of captioning tasks, including text rendering, capturing spatial relations, and including world knowledge in captions.")
        demo_paligemma.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Qwen"):
        demo_qwen.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Replicate"):
        demo_replicate.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Sailor"):
        demo_sailor.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Huggingface"):
        demo_huggingface.render()
    with gr.Tab("Fal"):
        demo_fal.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("ShowUI"):
        demo_showui.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("PlayAI"):
        demo_playai.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Grok"):
        demo_grok.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Gemini"):
        demo_gemini.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("ChatGPT"):
        demo_openai.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Claude"):
        demo_claude.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Allen AI"):
        demo_allenai.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Perplexity"):
        demo_perplexity.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Experimental"):
        demo_experimental.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Meta Llama"):
        demo_sambanova.render()
        gr.Markdown(
            """
        **Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/).
        
        This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.
        """
        )
    with gr.Tab("Marco-o1"):
        demo_marco_o1.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("Mistral"):
        demo_mistral.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("NVIDIA"):
        demo_nvidia.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")
    with gr.Tab("OminiControl"):
        demo_omini.render()
        gr.Markdown("This app is built with gradio, check out gradio github and star: <a href='https://github.com/gradio-app/gradio'>Gradio <img src='https://img.shields.io/github/stars/gradio-app/gradio'></a>.")


if __name__ == "__main__":
    demo.queue(api_open=False).launch(show_api=False)
