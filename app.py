import gradio as gr
import gemini_gradio
import openai_gradio
import anthropic_gradio
import sambanova_gradio
import xai_gradio
import hyperbolic_gradio
import perplexity_gradio
import mistral_gradio
import fireworks_gradio
import cerebras_gradio
import groq_gradio
import together_gradio
import nvidia_gradio
import dashscope_gradio

# Common helper functions for all tabs
def create_interface(model_name, src_registry, **kwargs):
    return gr.load(
        name=model_name,
        src=src_registry,
        fill_height=True,
        **kwargs
    )

def update_model(new_model, container, src_registry, **kwargs):
    with container:
        container.load_none()
        new_interface = create_interface(new_model, src_registry, **kwargs)
        new_interface.render()

with gr.Blocks(fill_height=True) as demo:
    # Meta Llama Tab
    with gr.Tab("Meta Llama"):
        with gr.Row():
            llama_model = gr.Dropdown(
                choices=[
                    'Meta-Llama-3.2-1B-Instruct',
                    'Meta-Llama-3.2-3B-Instruct',
                    'Llama-3.2-11B-Vision-Instruct',
                    'Llama-3.2-90B-Vision-Instruct',
                    'Meta-Llama-3.1-8B-Instruct',
                    'Meta-Llama-3.1-70B-Instruct',
                    'Meta-Llama-3.1-405B-Instruct'
                ],
                value='Llama-3.2-90B-Vision-Instruct',
                label="Select Llama Model",
                interactive=True
            )
        
        with gr.Column() as llama_container:
            llama_interface = create_interface(llama_model.value, sambanova_gradio.registry, multimodal=True)
        
        llama_model.change(
            fn=lambda new_model: update_model(new_model, llama_container, sambanova_gradio.registry, multimodal=True),
            inputs=[llama_model],
            outputs=[]
        )
        
        gr.Markdown("**Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/).")

    # Gemini Tab
    with gr.Tab("Gemini"):
        with gr.Row():
            gemini_model = gr.Dropdown(
                choices=[
                    'gemini-1.5-flash',
                    'gemini-1.5-flash-8b',
                    'gemini-1.5-pro',
                    'gemini-exp-1114'
                ],
                value='gemini-1.5-pro',
                label="Select Gemini Model",
                interactive=True
            )
        
        with gr.Column() as gemini_container:
            gemini_interface = create_interface(gemini_model.value, gemini_gradio.registry)
        
        gemini_model.change(
            fn=lambda new_model: update_model(new_model, gemini_container, gemini_gradio.registry),
            inputs=[gemini_model],
            outputs=[]
        )

    # ChatGPT Tab
    with gr.Tab("ChatGPT"):
        with gr.Row():
            model_choice = gr.Dropdown(
                choices=[
                    'gpt-4o-2024-11-20',
                    'gpt-4o',
                    'gpt-4o-2024-08-06',
                    'gpt-4o-2024-05-13',
                    'chatgpt-4o-latest',
                    'gpt-4o-mini',
                    'gpt-4o-mini-2024-07-18',
                    'o1-preview',
                    'o1-preview-2024-09-12',
                    'o1-mini',
                    'o1-mini-2024-09-12',
                    'gpt-4-turbo',
                    'gpt-4-turbo-2024-04-09',
                    'gpt-4-turbo-preview',
                    'gpt-4-0125-preview',
                    'gpt-4-1106-preview',
                    'gpt-4',
                    'gpt-4-0613'
                ],
                value='gpt-4o-2024-11-20',
                label="Select Model",
                interactive=True
            )
        
        with gr.Column() as chatgpt_container:
            chatgpt_interface = create_interface(model_choice.value, openai_gradio.registry)
        
        model_choice.change(
            fn=lambda new_model: update_model(new_model, chatgpt_container, openai_gradio.registry),
            inputs=[model_choice],
            outputs=[]
        )

    # Claude Tab
    with gr.Tab("Claude"):
        with gr.Row():
            claude_model = gr.Dropdown(
                choices=[
                    'claude-3-5-sonnet-20241022',
                    'claude-3-5-haiku-20241022',
                    'claude-3-opus-20240229',
                    'claude-3-sonnet-20240229',
                    'claude-3-haiku-20240307'
                ],
                value='claude-3-5-sonnet-20241022',
                label="Select Model",
                interactive=True
            )
        
        with gr.Column() as claude_container:
            claude_interface = create_interface(claude_model.value, anthropic_gradio.registry, accept_token=True)
        
        claude_model.change(
            fn=lambda new_model: update_model(new_model, claude_container, anthropic_gradio.registry, accept_token=True),
            inputs=[claude_model],
            outputs=[]
        )

    # Grok Tab
    with gr.Tab("Grok"):
        with gr.Row():
            grok_model = gr.Dropdown(
                choices=[
                    'grok-beta',
                    'grok-vision-beta'
                ],
                value='grok-vision-beta',
                label="Select Grok Model",
                interactive=True
            )
        
        with gr.Column() as grok_container:
            grok_interface = create_interface(grok_model.value, xai_gradio.registry)
        
        grok_model.change(
            fn=lambda new_model: update_model(new_model, grok_container, xai_gradio.registry),
            inputs=[grok_model],
            outputs=[]
        )

    # Hugging Face Tab
    with gr.Tab("Hugging Face"):
        with gr.Row():
            hf_model = gr.Dropdown(
                choices=[
                    'Qwen/Qwen2.5-Coder-32B-Instruct',
                    'Qwen/Qwen2.5-72B-Instruct',
                    'meta-llama/Llama-3.1-70B-Instruct',
                    'mistralai/Mixtral-8x7B-Instruct-v0.1',
                    'meta-llama/Llama-3.1-8B-Instruct',
                    'google/gemma-2-9b-it',
                    'mistralai/Mistral-7B-v0.1',
                    'meta-llama/Llama-2-7b-chat-hf',
                    'meta-llama/Llama-3.2-3B-Instruct',
                    'meta-llama/Llama-3.2-1B-Instruct',
                    'Qwen/Qwen2.5-1.5B-Instruct',
                    'microsoft/Phi-3.5-mini-instruct',
                    'HuggingFaceTB/SmolLM2-1.7B-Instruct',
                    'google/gemma-2-2b-it',
                    'meta-llama/Llama-3.2-3B',
                    'meta-llama/Llama-3.2-1B',
                    'openai-community/gpt2'
                ],
                value='HuggingFaceTB/SmolLM2-1.7B-Instruct',
                label="Select Hugging Face Model",
                interactive=True
            )
        
        with gr.Column() as hf_container:
            hf_interface = create_interface(hf_model.value, "models")
        
        hf_model.change(
            fn=lambda new_model: update_model(new_model, hf_container, "models"),
            inputs=[hf_model],
            outputs=[]
        )
        
        gr.Markdown("""
        **Note:** These models are loaded directly from Hugging Face Hub. Some models may require authentication.
        """)

    # Groq Tab
    with gr.Tab("Groq"):
        with gr.Row():
            groq_model = gr.Dropdown(
                choices=[
                    'llama3-groq-8b-8192-tool-use-preview',
                    'llama3-groq-70b-8192-tool-use-preview',
                    'llama-3.2-1b-preview',
                    'llama-3.2-3b-preview',
                    'llama-3.2-11b-text-preview',
                    'llama-3.2-90b-text-preview',
                    'mixtral-8x7b-32768',
                    'gemma2-9b-it',
                    'gemma-7b-it'
                ],
                value='llama3-groq-70b-8192-tool-use-preview',
                label="Select Groq Model",
                interactive=True
            )
        
        with gr.Column() as groq_container:
            groq_interface = create_interface(groq_model.value, groq_gradio.registry)
        
        groq_model.change(
            fn=lambda new_model: update_model(new_model, groq_container, groq_gradio.registry),
            inputs=[groq_model],
            outputs=[]
        )

    # Hyperbolic Tab
    with gr.Tab("Hyperbolic"):
        with gr.Row():
            hyperbolic_model = gr.Dropdown(
                choices=[
                    'Qwen/Qwen2.5-Coder-32B-Instruct',
                    'meta-llama/Llama-3.2-3B-Instruct',
                    'meta-llama/Meta-Llama-3.1-8B-Instruct',
                    'meta-llama/Meta-Llama-3.1-70B-Instruct',
                    'meta-llama/Meta-Llama-3-70B-Instruct',
                    'NousResearch/Hermes-3-Llama-3.1-70B',
                    'Qwen/Qwen2.5-72B-Instruct',
                    'deepseek-ai/DeepSeek-V2.5',
                    'meta-llama/Meta-Llama-3.1-405B-Instruct'
                ],
                value='Qwen/Qwen2.5-Coder-32B-Instruct',
                label="Select Hyperbolic Model",
                interactive=True
            )
        
        with gr.Column() as hyperbolic_container:
            hyperbolic_interface = create_interface(hyperbolic_model.value, hyperbolic_gradio.registry)
        
        hyperbolic_model.change(
            fn=lambda new_model: update_model(new_model, hyperbolic_container, hyperbolic_gradio.registry),
            inputs=[hyperbolic_model],
            outputs=[]
        )

    # Qwen Tab
    with gr.Tab("Qwen"):
        with gr.Row():
            qwen_model = gr.Dropdown(
                choices=[
                    'qwen-turbo-latest',
                    'qwen-turbo',
                    'qwen-plus',
                    'qwen-max',
                    'qwen1.5-110b-chat',
                    'qwen1.5-72b-chat',
                    'qwen1.5-32b-chat',
                    'qwen1.5-14b-chat',
                    'qwen1.5-7b-chat'
                ],
                value='qwen-turbo-latest',
                label="Select Qwen Model",
                interactive=True
            )
        
        with gr.Column() as qwen_container:
            qwen_interface = create_interface(qwen_model.value, dashscope_gradio.registry)
        
        qwen_model.change(
            fn=lambda new_model: update_model(new_model, qwen_container, dashscope_gradio.registry),
            inputs=[qwen_model],
            outputs=[]
        )

    # Perplexity Tab
    with gr.Tab("Perplexity"):
        with gr.Row():
            perplexity_model = gr.Dropdown(
                choices=[
                    'llama-3.1-sonar-small-128k-online',
                    'llama-3.1-sonar-large-128k-online',
                    'llama-3.1-sonar-huge-128k-online',
                    'llama-3.1-sonar-small-128k-chat',
                    'llama-3.1-sonar-large-128k-chat',
                    'llama-3.1-8b-instruct',
                    'llama-3.1-70b-instruct'
                ],
                value='llama-3.1-sonar-large-128k-online',
                label="Select Perplexity Model",
                interactive=True
            )
        
        with gr.Column() as perplexity_container:
            perplexity_interface = create_interface(perplexity_model.value, perplexity_gradio.registry, accept_token=True)
        
        perplexity_model.change(
            fn=lambda new_model: update_model(new_model, perplexity_container, perplexity_gradio.registry, accept_token=True),
            inputs=[perplexity_model],
            outputs=[]
        )

    # Mistral Tab
    with gr.Tab("Mistral"):
        with gr.Row():
            mistral_model = gr.Dropdown(
                choices=[
                    'mistral-large-latest',
                    'pixtral-large-latest',
                    'ministral-3b-latest',
                    'ministral-8b-latest',
                    'mistral-small-latest',
                    'codestral-latest',
                    'mistral-embed',
                    'mistral-moderation-latest',
                    'pixtral-12b-2409',
                    'open-mistral-nemo',
                    'open-codestral-mamba'
                ],
                value='pixtral-large-latest',
                label="Select Mistral Model",
                interactive=True
            )
        
        with gr.Column() as mistral_container:
            mistral_interface = create_interface(mistral_model.value, mistral_gradio.registry)
        
        mistral_model.change(
            fn=lambda new_model: update_model(new_model, mistral_container, mistral_gradio.registry),
            inputs=[mistral_model],
            outputs=[]
        )

    # Fireworks Tab
    with gr.Tab("Fireworks"):
        with gr.Row():
            fireworks_model = gr.Dropdown(
                choices=[
                    'f1-preview',
                    'f1-mini-preview'
                ],
                value='f1-preview',
                label="Select Fireworks Model",
                interactive=True
            )
        
        with gr.Column() as fireworks_container:
            fireworks_interface = create_interface(fireworks_model.value, fireworks_gradio.registry)
        
        fireworks_model.change(
            fn=lambda new_model: update_model(new_model, fireworks_container, fireworks_gradio.registry),
            inputs=[fireworks_model],
            outputs=[]
        )

    # Cerebras Tab
    with gr.Tab("Cerebras"):
        with gr.Row():
            cerebras_model = gr.Dropdown(
                choices=[
                    'llama3.1-8b',
                    'llama3.1-70b',
                    'llama3.1-405b'
                ],
                value='llama3.1-70b',
                label="Select Cerebras Model",
                interactive=True
            )
        
        with gr.Column() as cerebras_container:
            cerebras_interface = create_interface(cerebras_model.value, cerebras_gradio.registry, accept_token=True)
        
        cerebras_model.change(
            fn=lambda new_model: update_model(new_model, cerebras_container, cerebras_gradio.registry, accept_token=True),
            inputs=[cerebras_model],
            outputs=[]
        )

    # Together Tab
    with gr.Tab("Together"):
        with gr.Row():
            together_model = gr.Dropdown(
                choices=[
                    'meta-llama/Llama-Vision-Free',
                    'meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo',
                    'meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo',
                    'meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo',
                    'meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo',
                    'meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo',
                    'meta-llama/Meta-Llama-3-8B-Instruct-Turbo',
                    'meta-llama/Meta-Llama-3-70B-Instruct-Turbo',
                    'meta-llama/Llama-3.2-3B-Instruct-Turbo',
                    'meta-llama/Meta-Llama-3-8B-Instruct-Lite',
                    'meta-llama/Meta-Llama-3-70B-Instruct-Lite',
                    'meta-llama/Llama-3-8b-chat-hf',
                    'meta-llama/Llama-3-70b-chat-hf',
                    'nvidia/Llama-3.1-Nemotron-70B-Instruct-HF',
                    'Qwen/Qwen2.5-Coder-32B-Instruct',
                    'microsoft/WizardLM-2-8x22B',
                    'google/gemma-2-27b-it',
                    'google/gemma-2-9b-it',
                    'databricks/dbrx-instruct',
                    'mistralai/Mixtral-8x7B-Instruct-v0.1',
                    'mistralai/Mixtral-8x22B-Instruct-v0.1',
                    'Qwen/Qwen2.5-7B-Instruct-Turbo',
                    'Qwen/Qwen2.5-72B-Instruct-Turbo',
                    'Qwen/Qwen2-72B-Instruct',
                    'deepseek-ai/deepseek-llm-67b-chat',
                    'google/gemma-2b-it',
                    'Gryphe/MythoMax-L2-13b',
                    'meta-llama/Llama-2-13b-chat-hf',
                    'mistralai/Mistral-7B-Instruct-v0.1',
                    'mistralai/Mistral-7B-Instruct-v0.2',
                    'mistralai/Mistral-7B-Instruct-v0.3',
                    'NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO',
                    'togethercomputer/StripedHyena-Nous-7B',
                    'upstage/SOLAR-10.7B-Instruct-v1.0'
                ],
                value='meta-llama/Llama-3.2-11B-Vision-Instruct-Turbo',
                label="Select Together Model",
                interactive=True
            )
        
        with gr.Column() as together_container:
            together_interface = create_interface(together_model.value, together_gradio.registry, multimodal=True)
        
        together_model.change(
            fn=lambda new_model: update_model(new_model, together_container, together_gradio.registry, multimodal=True),
            inputs=[together_model],
            outputs=[]
        )

    # NVIDIA Tab
    with gr.Tab("NVIDIA"):
        with gr.Row():
            nvidia_model = gr.Dropdown(
                choices=[
                    'nvidia/llama3-chatqa-1.5-70b',
                    'nvidia/llama3-chatqa-1.5-8b',
                    'nvidia-nemotron-4-340b-instruct',
                    'meta/llama-3.1-70b-instruct',
                    'meta/codellama-70b',
                    'meta/llama2-70b',
                    'meta/llama3-8b',
                    'meta/llama3-70b',
                    'mistralai/codestral-22b-instruct-v0.1',
                    'mistralai/mathstral-7b-v0.1',
                    'mistralai/mistral-large-2-instruct',
                    'mistralai/mistral-7b-instruct',
                    'mistralai/mistral-7b-instruct-v0.3',
                    'mistralai/mixtral-8x7b-instruct',
                    'mistralai/mixtral-8x22b-instruct',
                    'mistralai/mistral-large',
                    'google/gemma-2b',
                    'google/gemma-7b',
                    'google/gemma-2-2b-it',
                    'google/gemma-2-9b-it',
                    'google/gemma-2-27b-it',
                    'google/codegemma-1.1-7b',
                    'google/codegemma-7b',
                    'google/recurrentgemma-2b',
                    'google/shieldgemma-9b',
                    'microsoft/phi-3-medium-128k-instruct',
                    'microsoft/phi-3-medium-4k-instruct',
                    'microsoft/phi-3-mini-128k-instruct',
                    'microsoft/phi-3-mini-4k-instruct',
                    'microsoft/phi-3-small-128k-instruct',
                    'microsoft/phi-3-small-8k-instruct',
                    'qwen/qwen2-7b-instruct',
                    'databricks/dbrx-instruct',
                    'deepseek-ai/deepseek-coder-6.7b-instruct',
                    'upstage/solar-10.7b-instruct',
                    'snowflake/arctic'
                ],
                value='meta/llama-3.1-70b-instruct',
                label="Select NVIDIA Model",
                interactive=True
            )
        
        with gr.Column() as nvidia_container:
            nvidia_interface = create_interface(nvidia_model.value, nvidia_gradio.registry, accept_token=True)
        
        nvidia_model.change(
            fn=lambda new_model: update_model(new_model, nvidia_container, nvidia_gradio.registry, accept_token=True),
            inputs=[nvidia_model],
            outputs=[]
        )

demo.launch(ssr_mode=False)


