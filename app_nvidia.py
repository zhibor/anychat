import os

import nvidia_gradio

from utils import get_app

demo = get_app(
    models=[
        "nvidia/llama3-chatqa-1.5-70b",
        "nvidia/llama3-chatqa-1.5-8b",
        "nvidia-nemotron-4-340b-instruct",
        "meta/llama-3.1-70b-instruct",
        "meta/codellama-70b",
        "meta/llama2-70b",
        "meta/llama3-8b",
        "meta/llama3-70b",
        "mistralai/codestral-22b-instruct-v0.1",
        "mistralai/mathstral-7b-v0.1",
        "mistralai/mistral-large-2-instruct",
        "mistralai/mistral-7b-instruct",
        "mistralai/mistral-7b-instruct-v0.3",
        "mistralai/mixtral-8x7b-instruct",
        "mistralai/mixtral-8x22b-instruct",
        "mistralai/mistral-large",
        "google/gemma-2b",
        "google/gemma-7b",
        "google/gemma-2-2b-it",
        "google/gemma-2-9b-it",
        "google/gemma-2-27b-it",
        "google/codegemma-1.1-7b",
        "google/codegemma-7b",
        "google/recurrentgemma-2b",
        "google/shieldgemma-9b",
        "microsoft/phi-3-medium-128k-instruct",
        "microsoft/phi-3-medium-4k-instruct",
        "microsoft/phi-3-mini-128k-instruct",
        "microsoft/phi-3-mini-4k-instruct",
        "microsoft/phi-3-small-128k-instruct",
        "microsoft/phi-3-small-8k-instruct",
        "qwen/qwen2-7b-instruct",
        "databricks/dbrx-instruct",
        "deepseek-ai/deepseek-coder-6.7b-instruct",
        "upstage/solar-10.7b-instruct",
        "snowflake/arctic",
    ],
    default_model="meta/llama-3.1-70b-instruct",
    src=nvidia_gradio.registry,
    accept_token=not os.getenv("NVIDIA_API_KEY"),
)

if __name__ == "__main__":
    demo.launch()
