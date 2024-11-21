import fireworks_gradio

from utils import get_app

demo = get_app(
    models=[
        "f1-preview",
        "f1-mini-preview",
    ],
    default_model="f1-preview",
    registry=fireworks_gradio.registry,
    accept_token=False,
)

if __name__ == "__main__":
    demo.launch()
