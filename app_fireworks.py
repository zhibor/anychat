import os

import fireworks_gradio

from utils import get_app

demo = get_app(
    models=[
        "f1-preview",
        "f1-mini-preview",
        "llama-v3p3-70b-instruct",
    ],
    default_model="llama-v3p3-70b-instruct",
    src=fireworks_gradio.registry,
    accept_token=not os.getenv("FIREWORKS_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
