import cerebras_gradio

from utils import get_app

demo = get_app(
    models=[
        "llama3.1-8b",
        "llama3.1-70b",
        "llama3.1-405b",
    ],
    default_model="llama3.1-70b",
    registry=cerebras_gradio.registry,
    accept_token=True,
)

if __name__ == "__main__":
    demo.launch()
