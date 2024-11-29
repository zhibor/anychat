import os

import perplexity_gradio

from utils import get_app

demo = get_app(
    models=[
        "llama-3.1-sonar-large-128k-online",
        "llama-3.1-sonar-small-128k-online",
        "llama-3.1-sonar-huge-128k-online",
        "llama-3.1-sonar-small-128k-chat",
        "llama-3.1-sonar-large-128k-chat",
        "llama-3.1-8b-instruct",
        "llama-3.1-70b-instruct",
    ],
    default_model="llama-3.1-sonar-huge-128k-online",
    src=perplexity_gradio.registry,
    accept_token=not os.getenv("PERPLEXITY_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
