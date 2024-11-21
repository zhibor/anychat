import os

import openai_gradio

from utils import get_app

demo = get_app(
    models=[
        "gpt-4o-2024-11-20",
        "gpt-4o",
        "gpt-4o-2024-08-06",
        "gpt-4o-2024-05-13",
        "chatgpt-4o-latest",
        "gpt-4o-mini",
        "gpt-4o-mini-2024-07-18",
        "o1-preview",
        "o1-preview-2024-09-12",
        "o1-mini",
        "o1-mini-2024-09-12",
        "gpt-4-turbo",
        "gpt-4-turbo-2024-04-09",
        "gpt-4-turbo-preview",
        "gpt-4-0125-preview",
        "gpt-4-1106-preview",
        "gpt-4",
        "gpt-4-0613",
    ],
    default_model="gpt-4o-2024-11-20",
    registry=openai_gradio.registry,
    accept_token=not os.getenv("OPENAI_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
