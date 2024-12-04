import replicate_gradio

from utils import get_app

demo = get_app(
    models=[
        "black-forest-labs/flux-depth-pro",
        "black-forest-labs/flux-canny-pro",
        "black-forest-labs/flux-fill-pro",
        "black-forest-labs/flux-depth-dev",
        "tencent/hunyuan-video:140176772be3b423d14fdaf5403e6d4e38b85646ccad0c3fd2ed07c211f0cad1",
    ],
    default_model="tencent/hunyuan-video:140176772be3b423d14fdaf5403e6d4e38b85646ccad0c3fd2ed07c211f0cad1",
    src=replicate_gradio.registry,
)

if __name__ == "__main__":
    demo.launch()
