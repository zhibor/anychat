import os

import dashscope_gradio

from utils import get_app

demo = get_app(
    models=[
        "qwen-turbo-latest",
        "qwen-turbo",
        "qwen-plus",
        "qwen-max",
        "qwen1.5-110b-chat",
        "qwen1.5-72b-chat",
        "qwen1.5-32b-chat",
        "qwen1.5-14b-chat",
        "qwen1.5-7b-chat",
    ],
    default_model="qwen-turbo-latest",
    src=dashscope_gradio.registry,
    accept_token=not os.getenv("DASHSCOPE_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
