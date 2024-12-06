import os

import together_gradio

from utils import get_app

demo = get_app(
    models=[
        "meta-llama/Llama-Vision-Free",
        "meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo",
        "meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3-8B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3-70B-Instruct-Turbo",
        "meta-llama/Llama-3.2-3B-Instruct-Turbo",
        "meta-llama/Meta-Llama-3-8B-Instruct-Lite",
        "meta-llama/Meta-Llama-3-70B-Instruct-Lite",
        "meta-llama/Llama-3-8b-chat-hf",
        "meta-llama/Llama-3-70b-chat-hf",
        "nvidia/Llama-3.1-Nemotron-70B-Instruct-HF",
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        "microsoft/WizardLM-2-8x22B",
        "google/gemma-2-27b-it",
        "google/gemma-2-9b-it",
        "databricks/dbrx-instruct",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "mistralai/Mixtral-8x22B-Instruct-v0.1",
        "Qwen/Qwen2.5-7B-Instruct-Turbo",
        "Qwen/Qwen2.5-72B-Instruct-Turbo",
        "Qwen/Qwen2-72B-Instruct",
        "deepseek-ai/deepseek-llm-67b-chat",
        "google/gemma-2b-it",
        "Gryphe/MythoMax-L2-13b",
        "meta-llama/Llama-2-13b-chat-hf",
        "mistralai/Mistral-7B-Instruct-v0.1",
        "mistralai/Mistral-7B-Instruct-v0.2",
        "mistralai/Mistral-7B-Instruct-v0.3",
        "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO",
        "togethercomputer/StripedHyena-Nous-7B",
        "upstage/SOLAR-10.7B-Instruct-v1.0",
        "meta-llama/Llama-3.3-70B-Instruct-Turbo",
    ],
    default_model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
    src=together_gradio.registry,
    accept_token=not os.getenv("TOGETHER_API_KEY"),
    multimodal=True,
)

if __name__ == "__main__":
    demo.launch()
