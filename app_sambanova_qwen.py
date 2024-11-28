import os

import sambanova_gradio

from utils import get_app

demo = get_app(
    models=[
        "Qwen2.5-Coder-0.5B-Instruct",
        "Qwen2.5-0.5B-Instruct",
        "Qwen2.5-Coder-32B-Instruct",
        "Qwen2.5-72B-Instruct",
    ],
    default_model="Qwen2.5-Coder-32B-Instruct",
    src=sambanova_gradio.registry,
    accept_token=not os.getenv("SAMBANOVA_API_KEY"),
    multimodal=True,
)

if __name__ == "__main__":
    demo.launch()
