import os

import cohere_gradio

from utils import get_app

demo = get_app(
    models=[
        "command-r",
        "command-r-08-2024",
        "command-r-plus",
        "command-r-plus-08-2024",
        "command-r7b-12-2024",
    ],
    default_model="command-r7b-12-2024",
    src=cohere_gradio.registry,
    accept_token=not os.getenv("COHERE_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()