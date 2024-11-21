import os

import mistral_gradio

from utils import get_app

demo = get_app(
    models=[
        "mistral-large-latest",
        "pixtral-large-latest",
        "ministral-3b-latest",
        "ministral-8b-latest",
        "mistral-small-latest",
        "codestral-latest",
        "mistral-embed",
        "mistral-moderation-latest",
        "pixtral-12b-2409",
        "open-mistral-nemo",
        "open-codestral-mamba",
    ],
    default_model="pixtral-large-latest",
    src=mistral_gradio.registry,
    accept_token=not os.getenv("MISTRAL_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
