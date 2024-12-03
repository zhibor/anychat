import fal_gradio

from utils import get_app

demo = get_app(
    models=[
        "fal-ai/ltx-video",
        "fal-ai/ltx-video/image-to-video",
        "fal-ai/luma-photon",
    ],
    default_model="fal-ai/luma-photon",
    src=fal_gradio.registry,
)

if __name__ == "__main__":
    demo.launch()
