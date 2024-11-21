import os

import xai_gradio

from utils import get_app

demo = get_app(
    models=[
        "grok-beta",
        "grok-vision-beta",
    ],
    default_model="grok-vision-beta",
    registry=xai_gradio.registry,
    accept_token=not os.getenv("XAI_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
