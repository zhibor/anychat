import sambanova_gradio

from utils import get_app

demo = get_app(
    models=[
        "Meta-Llama-3.2-1B-Instruct",
        "Meta-Llama-3.2-3B-Instruct",
        "Llama-3.2-11B-Vision-Instruct",
        "Llama-3.2-90B-Vision-Instruct",
        "Meta-Llama-3.1-8B-Instruct",
        "Meta-Llama-3.1-70B-Instruct",
        "Meta-Llama-3.1-405B-Instruct",
    ],
    default_model="Llama-3.2-90B-Vision-Instruct",
    registry=sambanova_gradio.registry,
    accept_token=False,
    multimodal=True,
)

if __name__ == "__main__":
    demo.launch()
