from utils import get_app

demo = get_app(
    models=[
        "Qwen/Qwen2.5-Coder-32B-Instruct",
        "Qwen/Qwen2.5-72B-Instruct",
        "meta-llama/Llama-3.1-70B-Instruct",
        "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "meta-llama/Llama-3.1-8B-Instruct",
        "google/gemma-2-9b-it",
        "mistralai/Mistral-7B-v0.1",
        "meta-llama/Llama-2-7b-chat-hf",
        "meta-llama/Llama-3.2-3B-Instruct",
        "meta-llama/Llama-3.2-1B-Instruct",
        "Qwen/Qwen2.5-1.5B-Instruct",
        "microsoft/Phi-3.5-mini-instruct",
        "HuggingFaceTB/SmolLM2-1.7B-Instruct",
        "google/gemma-2-2b-it",
        "meta-llama/Llama-3.2-3B",
        "meta-llama/Llama-3.2-1B",
        "openai-community/gpt2",
    ],
    default_model="HuggingFaceTB/SmolLM2-1.7B-Instruct",
    src="models",
)

if __name__ == "__main__":
    demo.launch()
