import replicate_gradio

from utils import get_app

demo = get_app(
    models=[
        "black-forest-labs/flux-depth-pro",
        "black-forest-labs/flux-canny-pro",
        "black-forest-labs/flux-fill-pro",
        "black-forest-labs/flux-depth-dev",
        "zsxkib/hunyuan-video:349dbe0feb6e8e4a6fab3c6a4dd642413e6c10735353de8b40f12abeee203617",
    ],
    default_model="zsxkib/hunyuan-video:349dbe0feb6e8e4a6fab3c6a4dd642413e6c10735353de8b40f12abeee203617",
    src=replicate_gradio.registry,
)

if __name__ == "__main__":
    demo.launch()
