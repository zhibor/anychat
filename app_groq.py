import os

import groq_gradio

from utils import get_app

demo = get_app(
    models=[
        "llama3-groq-8b-8192-tool-use-preview",
        "llama3-groq-70b-8192-tool-use-preview",
        "llama-3.2-1b-preview",
        "llama-3.2-3b-preview",
        "llama-3.2-11b-vision-preview",
        "llama-3.2-90b-vision-preview",
        "mixtral-8x7b-32768",
        "gemma2-9b-it",
        "gemma-7b-it",
        "llama-3.3-70b-versatile",
        "llama-3.3-70b-specdec",
    ],
    default_model="llama-3.3-70b-specdec",
    src=groq_gradio.registry,
    accept_token=not os.getenv("GROQ_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
