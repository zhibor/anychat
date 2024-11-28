import os
import random
from typing import Dict, List

import google.generativeai as genai
import gradio as gr
import openai
from anthropic import Anthropic
from openai import OpenAI  # Add explicit OpenAI import


def get_all_models():
    """Get all available models from the registries."""
    return [
        "SambaNova: Meta-Llama-3.2-1B-Instruct",
        "SambaNova: Meta-Llama-3.2-3B-Instruct",
        "SambaNova: Llama-3.2-11B-Vision-Instruct",
        "SambaNova: Llama-3.2-90B-Vision-Instruct",
        "SambaNova: Meta-Llama-3.1-8B-Instruct",
        "SambaNova: Meta-Llama-3.1-70B-Instruct",
        "SambaNova: Meta-Llama-3.1-405B-Instruct",
        "Hyperbolic: Qwen/Qwen2.5-Coder-32B-Instruct",
        "Hyperbolic: meta-llama/Llama-3.2-3B-Instruct",
        "Hyperbolic: meta-llama/Meta-Llama-3.1-8B-Instruct",
        "Hyperbolic: meta-llama/Meta-Llama-3.1-70B-Instruct",
        "Hyperbolic: meta-llama/Meta-Llama-3-70B-Instruct",
        "Hyperbolic: NousResearch/Hermes-3-Llama-3.1-70B",
        "Hyperbolic: Qwen/Qwen2.5-72B-Instruct",
        "Hyperbolic: deepseek-ai/DeepSeek-V2.5",
        "Hyperbolic: meta-llama/Meta-Llama-3.1-405B-Instruct",
    ]


def generate_discussion_prompt(original_question: str, previous_responses: List[str]) -> str:
    """Generate a prompt for models to discuss and build upon previous
    responses."""
    prompt = f"""You are participating in a multi-AI discussion about this question: "{original_question}"

Previous responses from other AI models:
{chr(10).join(f"- {response}" for response in previous_responses)}

Please provide your perspective while:
1. Acknowledging key insights from previous responses
2. Adding any missing important points
3. Respectfully noting if you disagree with anything and explaining why
4. Building towards a complete answer

Keep your response focused and concise (max 3-4 paragraphs)."""
    return prompt


def generate_consensus_prompt(original_question: str, discussion_history: List[str]) -> str:
    """Generate a prompt for final consensus building."""
    return f"""Review this multi-AI discussion about: "{original_question}"

Discussion history:
{chr(10).join(discussion_history)}

As a final synthesizer, please:
1. Identify the key points where all models agreed
2. Explain how any disagreements were resolved
3. Present a clear, unified answer that represents our collective best understanding
4. Note any remaining uncertainties or caveats

Keep the final consensus concise but complete."""


def chat_with_openai(model: str, messages: List[Dict], api_key: str | None) -> str:
    import openai

    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(model=model, messages=messages)
    return response.choices[0].message.content


def chat_with_anthropic(messages: List[Dict], api_key: str | None) -> str:
    """Chat with Anthropic's Claude model."""
    client = Anthropic(api_key=api_key)
    response = client.messages.create(model="claude-3-sonnet-20240229", messages=messages, max_tokens=1024)
    return response.content[0].text


def chat_with_gemini(messages: List[Dict], api_key: str | None) -> str:
    """Chat with Gemini Pro model."""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    # Convert messages to Gemini format
    gemini_messages = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        gemini_messages.append({"role": role, "parts": [msg["content"]]})

    response = model.generate_content([m["parts"][0] for m in gemini_messages])
    return response.text


def chat_with_sambanova(
    messages: List[Dict], api_key: str | None, model_name: str = "Llama-3.2-90B-Vision-Instruct"
) -> str:
    """Chat with SambaNova's models using their OpenAI-compatible API."""
    client = openai.OpenAI(
        api_key=api_key,
        base_url="https://api.sambanova.ai/v1",
    )

    response = client.chat.completions.create(
        model=model_name, messages=messages, temperature=0.1, top_p=0.1  # Use the specific model name passed in
    )
    return response.choices[0].message.content


def chat_with_hyperbolic(
    messages: List[Dict], api_key: str | None, model_name: str = "Qwen/Qwen2.5-Coder-32B-Instruct"
) -> str:
    """Chat with Hyperbolic's models using their OpenAI-compatible API."""
    client = OpenAI(api_key=api_key, base_url="https://api.hyperbolic.xyz/v1")

    # Add system message to the start of the messages list
    full_messages = [
        {"role": "system", "content": "You are a helpful assistant. Be descriptive and clear."},
        *messages,
    ]

    response = client.chat.completions.create(
        model=model_name,  # Use the specific model name passed in
        messages=full_messages,
        temperature=0.7,
        max_tokens=1024,
    )
    return response.choices[0].message.content


def multi_model_consensus(
    question: str, selected_models: List[str], rounds: int = 3, progress: gr.Progress = gr.Progress()
) -> list[tuple[str, str]]:
    if not selected_models:
        raise gr.Error("Please select at least one model to chat with.")

    chat_history = []
    discussion_history = []

    # Initial responses
    progress(0, desc="Getting initial responses...")
    initial_responses = []
    for i, model in enumerate(selected_models):
        provider, model_name = model.split(": ", 1)

        try:
            if provider == "Anthropic":
                api_key = os.getenv("ANTHROPIC_API_KEY")
                response = chat_with_anthropic(messages=[{"role": "user", "content": question}], api_key=api_key)
            elif provider == "SambaNova":
                api_key = os.getenv("SAMBANOVA_API_KEY")
                response = chat_with_sambanova(
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant"},
                        {"role": "user", "content": question},
                    ],
                    api_key=api_key,
                )
            elif provider == "Hyperbolic":  # Add Hyperbolic case
                api_key = os.getenv("HYPERBOLIC_API_KEY")
                response = chat_with_hyperbolic(messages=[{"role": "user", "content": question}], api_key=api_key)
            else:  # Gemini
                api_key = os.getenv("GEMINI_API_KEY")
                response = chat_with_gemini(messages=[{"role": "user", "content": question}], api_key=api_key)

            initial_responses.append(f"{model}: {response}")
            discussion_history.append(f"Initial response from {model}:\n{response}")
            chat_history.append((f"Initial response from {model}", response))
        except Exception as e:
            chat_history.append((f"Error from {model}", str(e)))

    # Discussion rounds
    for round_num in range(rounds):
        progress((round_num + 1) / (rounds + 2), desc=f"Discussion round {round_num + 1}...")
        round_responses = []

        random.shuffle(selected_models)  # Randomize order each round
        for model in selected_models:
            provider, model_name = model.split(": ", 1)

            try:
                discussion_prompt = generate_discussion_prompt(question, discussion_history)
                if provider == "Anthropic":
                    api_key = os.getenv("ANTHROPIC_API_KEY")
                    response = chat_with_anthropic(
                        messages=[{"role": "user", "content": discussion_prompt}], api_key=api_key
                    )
                elif provider == "SambaNova":
                    api_key = os.getenv("SAMBANOVA_API_KEY")
                    response = chat_with_sambanova(
                        messages=[
                            {"role": "system", "content": "You are a helpful assistant"},
                            {"role": "user", "content": discussion_prompt},
                        ],
                        api_key=api_key,
                    )
                elif provider == "Hyperbolic":  # Add Hyperbolic case
                    api_key = os.getenv("HYPERBOLIC_API_KEY")
                    response = chat_with_hyperbolic(
                        messages=[{"role": "user", "content": discussion_prompt}], api_key=api_key
                    )
                else:  # Gemini
                    api_key = os.getenv("GEMINI_API_KEY")
                    response = chat_with_gemini(
                        messages=[{"role": "user", "content": discussion_prompt}], api_key=api_key
                    )

                round_responses.append(f"{model}: {response}")
                discussion_history.append(f"Round {round_num + 1} - {model}:\n{response}")
                chat_history.append((f"Round {round_num + 1} - {model}", response))
            except Exception as e:
                chat_history.append((f"Error from {model} in round {round_num + 1}", str(e)))

    # Final consensus
    progress(0.9, desc="Building final consensus...")
    model = selected_models[0]
    provider, model_name = model.split(": ", 1)

    try:
        consensus_prompt = generate_consensus_prompt(question, discussion_history)
        if provider == "Anthropic":
            api_key = os.getenv("ANTHROPIC_API_KEY")
            final_consensus = chat_with_anthropic(
                messages=[{"role": "user", "content": consensus_prompt}], api_key=api_key
            )
        elif provider == "SambaNova":
            api_key = os.getenv("SAMBANOVA_API_KEY")
            final_consensus = chat_with_sambanova(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": consensus_prompt},
                ],
                api_key=api_key,
            )
        elif provider == "Hyperbolic":  # Add Hyperbolic case
            api_key = os.getenv("HYPERBOLIC_API_KEY")
            final_consensus = chat_with_hyperbolic(
                messages=[{"role": "user", "content": consensus_prompt}], api_key=api_key
            )
        else:  # Gemini
            api_key = os.getenv("GEMINI_API_KEY")
            final_consensus = chat_with_gemini(
                messages=[{"role": "user", "content": consensus_prompt}], api_key=api_key
            )
    except Exception as e:
        final_consensus = f"Error getting consensus from {model}: {str(e)}"

    chat_history.append(("Final Consensus", final_consensus))

    progress(1.0, desc="Done!")
    return chat_history


with gr.Blocks() as demo:
    gr.Markdown("# Experimental Multi-Model Consensus Chat")
    gr.Markdown(
        """Select multiple models to collaborate on answering your question.
                The models will discuss with each other and attempt to reach a consensus.
                Maximum 3 models can be selected at once."""
    )

    with gr.Row():
        with gr.Column():
            model_selector = gr.Dropdown(
                choices=get_all_models(),
                multiselect=True,
                label="Select Models (max 3)",
                info="Choose up to 3 models to participate in the discussion",
                value=["SambaNova: Llama-3.2-90B-Vision-Instruct", "Hyperbolic: Qwen/Qwen2.5-Coder-32B-Instruct"],
                max_choices=3,
            )
            rounds_slider = gr.Slider(
                minimum=1,
                maximum=2,
                value=1,
                step=1,
                label="Discussion Rounds",
                info="Number of rounds of discussion between models",
            )

    chatbot = gr.Chatbot(height=600, label="Multi-Model Discussion")
    msg = gr.Textbox(label="Your Question", placeholder="Ask a question for the models to discuss...")

    def respond(message, selected_models, rounds):
        chat_history = multi_model_consensus(message, selected_models, rounds)
        return chat_history

    msg.submit(respond, [msg, model_selector, rounds_slider], [chatbot], api_name="consensus_chat")

for fn in demo.fns.values():
    fn.api_name = False

if __name__ == "__main__":
    demo.launch()
