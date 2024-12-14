import os

import xai_gradio

from utils import get_app

demo = get_app(
    models=[
        "grok-beta",
        "grok-vision-beta",
        "grok-2-vision-1212",
        "grok-2-1212",
    ],
    default_model="grok-2-vision-1212",
    src=xai_gradio.registry,
    accept_token=not os.getenv("XAI_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
