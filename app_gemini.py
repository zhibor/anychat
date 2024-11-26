import os

import gemini_gradio

from utils import get_app

demo = get_app(
    models=[
        "gemini-1.5-flash",
        "gemini-1.5-flash-8b",
        "gemini-1.5-pro",
        "gemini-exp-1114",
        "gemini-exp-1121"
    ],
    default_model="gemini-1.5-pro",
    src=gemini_gradio.registry,
    accept_token=not os.getenv("GEMINI_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
