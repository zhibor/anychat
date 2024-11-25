import os

import transformers_gradio

from utils import get_app

demo = get_app(
    models=[
        'AIDC-AI/Marco-o1'
    ],
    default_model="AIDC-AI/Marco-o1",
    src=transformers_gradio.registry,
)

if __name__ == "__main__":
    demo.launch()