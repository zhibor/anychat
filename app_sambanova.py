import os

import sambanova_gradio

from utils import get_app

demo = get_app(
    models=[
        "Meta-Llama-3.2-1B-Instruct",
        "Meta-Llama-3.2-3B-Instruct",
        "Llama-3.2-11B-Vision-Instruct",
        "Llama-3.2-90B-Vision-Instruct",
        "Meta-Llama-3.1-8B-Instruct",
        "Meta-Llama-3.1-70B-Instruct",
        "Meta-Llama-3.1-405B-Instruct",
        "Qwen2.5-72B-Instruct",
        "Qwen2.5-Coder-32B-Instruct",
        "Meta-Llama-3.3-70B-Instruct",
        "QwQ-32B-Preview",
    ],
    default_model="QwQ-32B-Preview",
    src=sambanova_gradio.registry,
    accept_token=not os.getenv("SAMBANOVA_API_KEY"),
    multimodal=True,
)

if __name__ == "__main__":
    demo.launch()
