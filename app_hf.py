from utils import get_app

demo = get_app(
    models=[
        "microsoft/Phi-3.5-mini-instruct",
        "HuggingFaceTB/SmolLM2-1.7B-Instruct",
        "google/gemma-2-2b-it",
        "openai-community/gpt2",
        "microsoft/phi-2",
        "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    ],
    default_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    src="models",
)

if __name__ == "__main__":
    demo.launch()
