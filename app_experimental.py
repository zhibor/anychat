import os
import gradio as gr
from typing import List, Dict
import random
import time
from utils import get_app

# Import all the model registries (keeping existing imports)
import anthropic_gradio
import cerebras_gradio
import dashscope_gradio
import fireworks_gradio
import gemini_gradio
import groq_gradio
import hyperbolic_gradio
import mistral_gradio
import nvidia_gradio
import openai_gradio
import perplexity_gradio
import sambanova_gradio
import together_gradio
import xai_gradio

# Define MODEL_REGISTRIES dictionary
MODEL_REGISTRIES = {
    "OpenAI": (openai_gradio.registry, os.getenv("OPENAI_API_KEY")),
    "Anthropic": (anthropic_gradio.registry, os.getenv("ANTHROPIC_API_KEY")),
    "Cerebras": (cerebras_gradio, os.getenv("CEREBRAS_API_KEY")),
    "DashScope": (dashscope_gradio, os.getenv("DASHSCOPE_API_KEY")),
    "Fireworks": (fireworks_gradio, os.getenv("FIREWORKS_API_KEY")),
    "Gemini": (gemini_gradio, os.getenv("GEMINI_API_KEY")),
    "Groq": (groq_gradio, os.getenv("GROQ_API_KEY")),
    "Hyperbolic": (hyperbolic_gradio, os.getenv("HYPERBOLIC_API_KEY")),
    "Mistral": (mistral_gradio, os.getenv("MISTRAL_API_KEY")),
    "NVIDIA": (nvidia_gradio, os.getenv("NVIDIA_API_KEY")),
    "SambaNova": (sambanova_gradio, os.getenv("SAMBANOVA_API_KEY")),
    "Together": (together_gradio, os.getenv("TOGETHER_API_KEY")),
    "XAI": (xai_gradio, os.getenv("XAI_API_KEY")),
}

def get_all_models():
    """Get all available models from the registries."""
    return [
        "OpenAI: gpt-4o",  # From app_openai.py
        "Anthropic: claude-3-5-sonnet-20241022",  # From app_claude.py
    ]

def generate_discussion_prompt(original_question: str, previous_responses: List[str]) -> str:
    """Generate a prompt for models to discuss and build upon previous responses."""
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

def chat_with_openai(model: str, messages: List[Dict], api_key: str) -> str:
    import openai
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content

def chat_with_anthropic(model: str, messages: List[Dict], api_key: str) -> str:
    from anthropic import Anthropic
    client = Anthropic(api_key=api_key)
    # Convert messages to Anthropic format
    prompt = "\n\n".join([f"{m['role']}: {m['content']}" for m in messages])
    response = client.messages.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def multi_model_consensus(
    question: str, 
    selected_models: List[str], 
    rounds: int = 3,
    progress: gr.Progress = gr.Progress()
) -> tuple[str, List[Dict]]:
    if not selected_models:
        return "Please select at least one model to chat with.", []
    
    chat_history = []
    discussion_history = []
    
    # Initial responses
    progress(0, desc="Getting initial responses...")
    initial_responses = []
    for i, model in enumerate(selected_models):
        provider, model_name = model.split(": ", 1)
        registry_fn, api_key = MODEL_REGISTRIES[provider]
        
        if not api_key:
            continue
            
        try:
            # Load the model using the registry function
            predictor = gr.load(
                name=model_name,
                src=registry_fn,
                token=api_key
            )
            
            # Format the request based on the provider
            if provider == "Anthropic":
                response = predictor.predict(
                    messages=[{"role": "user", "content": question}],
                    max_tokens=1024,
                    model=model_name,
                    api_name="chat"
                )
            else:
                response = predictor.predict(
                    question,
                    api_name="chat"
                )
                
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
            registry, api_key = MODEL_REGISTRIES[provider]
            
            if not api_key:
                continue
                
            try:
                discussion_prompt = generate_discussion_prompt(question, discussion_history)
                response = registry.chat(
                    model=model_name,
                    messages=[{"role": "user", "content": discussion_prompt}],
                    api_key=api_key
                )
                round_responses.append(f"{model}: {response}")
                discussion_history.append(f"Round {round_num + 1} - {model}:\n{response}")
                chat_history.append((f"Round {round_num + 1} - {model}", response))
            except Exception as e:
                chat_history.append((f"Error from {model} in round {round_num + 1}", str(e)))
    
    # Final consensus - use the model that's shown most consistency
    progress(0.9, desc="Building final consensus...")
    # Use the first model for final consensus instead of two models
    model = selected_models[0]
    provider, model_name = model.split(": ", 1)
    registry, api_key = MODEL_REGISTRIES[provider]
    
    try:
        consensus_prompt = generate_consensus_prompt(question, discussion_history)
        final_consensus = registry.chat(
            model=model_name,
            messages=[{"role": "user", "content": consensus_prompt}],
            api_key=api_key
        )
    except Exception as e:
        final_consensus = f"Error getting consensus from {model}: {str(e)}"
    
    chat_history.append(("Final Consensus", final_consensus))
    
    progress(1.0, desc="Done!")
    return chat_history

with gr.Blocks() as demo:
    gr.Markdown("# Experimental Multi-Model Consensus Chat")
    gr.Markdown("""Select multiple models to collaborate on answering your question. 
                The models will discuss with each other and attempt to reach a consensus.
                Maximum 5 models can be selected at once.""")
    
    with gr.Row():
        with gr.Column():
            model_selector = gr.Dropdown(
                choices=get_all_models(),
                multiselect=True,
                label="Select Models (max 5)",
                info="Choose up to 5 models to participate in the discussion",
                value=["OpenAI: gpt-4o", "Anthropic: claude-3-5-sonnet-20241022"],  # Updated model names
                max_choices=5
            )
            rounds_slider = gr.Slider(
                minimum=1,
                maximum=5,
                value=3,
                step=1,
                label="Discussion Rounds",
                info="Number of rounds of discussion between models"
            )
    
    chatbot = gr.Chatbot(height=600, label="Multi-Model Discussion")
    msg = gr.Textbox(label="Your Question", placeholder="Ask a question for the models to discuss...")
    
    def respond(message, selected_models, rounds):
        chat_history = multi_model_consensus(message, selected_models, rounds)
        return chat_history
    
    msg.submit(
        respond,
        [msg, model_selector, rounds_slider],
        [chatbot],
        api_name="consensus_chat"
    )

if __name__ == "__main__":
    demo.launch() 