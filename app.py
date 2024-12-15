from utils import get_app

# Import all demos
from app_cohere import demo as demo_cohere
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
from app_mistral import demo as demo_mistral
from app_nvidia import demo as demo_nvidia
from app_openai import demo as demo_openai
from app_perplexity import demo as demo_perplexity
from app_qwen import demo as demo_qwen
from app_sambanova import demo as demo_sambanova
from app_together import demo as demo_together
from app_xai import demo as demo_grok
from app_showui import demo as demo_showui
from app_omini import demo as demo_omini

# Create mapping of providers to their demos
PROVIDERS = {
    "Gemini": demo_gemini,
    "Grok": demo_grok,
    "Cohere": demo_cohere,
    "SambaNova": demo_sambanova,
    "Hyperbolic": demo_hyperbolic,
    "OminiControl": demo_omini,
    "Fireworks": demo_fireworks,
    "Together": demo_together,
    "Groq": demo_groq,
    "Meta Llama": demo_meta,
    "LumaAI": demo_lumaai,
    "Paligemma": demo_paligemma,
    "Qwen": demo_qwen,
    "Replicate": demo_replicate,
    "Huggingface": demo_huggingface,
    "Fal": demo_fal,
    "ShowUI": demo_showui,
    "PlayAI": demo_playai,
    "ChatGPT": demo_openai,
    "Claude": demo_claude,
    "Allen AI": demo_allenai,
    "Perplexity": demo_perplexity,
    "Experimental": demo_experimental,
    "Mistral": demo_mistral,
    "NVIDIA": demo_nvidia
}

demo = get_app(
    models=list(PROVIDERS.keys()),
    default_model="Gemini",
    src=PROVIDERS,
    dropdown_label="Select Provider"
)

if __name__ == "__main__":
    demo.queue(api_open=False).launch(show_api=False)
