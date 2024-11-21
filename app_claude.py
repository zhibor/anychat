import anthropic_gradio

from utils import get_app

demo = get_app(
    models=[
        "claude-3-5-sonnet-20241022",
        "claude-3-5-haiku-20241022",
        "claude-3-opus-20240229",
        "claude-3-sonnet-20240229",
        "claude-3-haiku-20240307",
    ],
    default_model="claude-3-5-sonnet-20241022",
    registry=anthropic_gradio.registry,
    accept_token=True,
)

if __name__ == "__main__":
    demo.launch()
