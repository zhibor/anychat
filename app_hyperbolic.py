import os

import hyperbolic_gradio

from utils import get_app

demo = get_app(
    models=[
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        "meta-llama/Llama-3.2-3B-Instruct",
        "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "meta-llama/Meta-Llama-3.1-70B-Instruct",
        "meta-llama/Meta-Llama-3-70B-Instruct",
        "NousResearch/Hermes-3-Llama-3.1-70B",
        "Qwen/Qwen2.5-72B-Instruct",
        "deepseek-ai/DeepSeek-V2.5",
        "meta-llama/Meta-Llama-3.1-405B-Instruct",
        "Qwen/QwQ-32B-Preview",
    ],
    default_model="Qwen/QwQ-32B-Preview",
    src=hyperbolic_gradio.registry,
    accept_token=not os.getenv("HYPERBOLIC_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
