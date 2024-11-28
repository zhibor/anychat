import replicate_gradio

from utils import get_app

demo = get_app(
    models=[
        "black-forest-labs/flux-depth-pro",
        "black-forest-labs/flux-canny-pro",
        "black-forest-labs/flux-fill-pro",
        "black-forest-labs/flux-depth-dev",
    ],
    default_model="black-forest-labs/flux-depth-pro",
    src=replicate_gradio.registry,
)

if __name__ == "__main__":
    demo.launch()
