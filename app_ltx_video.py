import os
import fal_gradio
from utils import get_app

demo = get_app(
    models=[
        "fal-ai/ltx-video",
    ],
    default_model="fal-ai/ltx-video",
    src=fal_gradio.registry,
)

if __name__ == "__main__":
    demo.launch()
