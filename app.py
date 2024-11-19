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



with gr.Blocks(fill_height=True) as demo:
    with gr.Tab("Meta Llama"):
        with gr.Row():
            llama_model = gr.Dropdown(
                choices=[
                    'Meta-Llama-3.2-1B-Instruct',   # Llama 3.2 1B
                    'Meta-Llama-3.2-3B-Instruct',   # Llama 3.2 3B
                    'Llama-3.2-11B-Vision-Instruct',  # Llama 3.2 11B
                    'Llama-3.2-90B-Vision-Instruct',  # Llama 3.2 90B
                    'Meta-Llama-3.1-8B-Instruct',    # Llama 3.1 8B
                    'Meta-Llama-3.1-70B-Instruct',   # Llama 3.1 70B
                    'Meta-Llama-3.1-405B-Instruct'   # Llama 3.1 405B
                ],
                value='Llama-3.2-90B-Vision-Instruct',  # Default to the most advanced model
                label="Select Llama Model",
                interactive=True
            )
        
        llama_interface = gr.load(
            name=llama_model.value,
            src=sambanova_gradio.registry,
            multimodal=True,
            fill_height=True
        )
        
        def update_llama_model(new_model):
            return gr.load(
                name=new_model,
                src=sambanova_gradio.registry,
                multimodal=True,
                fill_height=True
            )
        
        llama_model.change(
            fn=update_llama_model,
            inputs=[llama_model],
            outputs=[llama_interface]
        )
        
        gr.Markdown("**Note:** You need to use a SambaNova API key from [SambaNova Cloud](https://cloud.sambanova.ai/).")
    with gr.Tab("Gemini"):
        with gr.Row():
            gemini_model = gr.Dropdown(
                choices=[
                    'gemini-1.5-flash',        # Fast and versatile performance
                    'gemini-1.5-flash-8b',     # High volume, lower intelligence tasks
                    'gemini-1.5-pro',           # Complex reasoning tasks
                    'gemini-exp-1114'          # Quality improvements
                ],
                value='gemini-1.5-pro',      # Default to the most advanced model
                label="Select Gemini Model",
                interactive=True
            )
        
        gemini_interface = gr.load(
            name=gemini_model.value,
            src=gemini_gradio.registry,
            fill_height=True
        )
        
        def update_gemini_model(new_model):
            return gr.load(
                name=new_model,
                src=gemini_gradio.registry,
                fill_height=True
            )
        
        gemini_model.change(
            fn=update_gemini_model,
            inputs=[gemini_model],
            outputs=[gemini_interface]
        )
    with gr.Tab("ChatGPT"):
        with gr.Row():
            model_choice = gr.Dropdown(
                choices=[
                    'gpt-4o',                     # Most advanced model
                    'gpt-4o-2024-08-06',          # Latest snapshot
                    'gpt-4o-2024-05-13',          # Original snapshot
                    'chatgpt-4o-latest',          # Latest ChatGPT version
                    'gpt-4o-mini',                # Small model
                    'gpt-4o-mini-2024-07-18',     # Latest mini version
                    'o1-preview',                 # Reasoning model
                    'o1-preview-2024-09-12',      # Latest o1 model snapshot
                    'o1-mini',                    # Faster reasoning model
                    'o1-mini-2024-09-12',         # Latest o1-mini model snapshot
                    'gpt-4-turbo',                # Latest GPT-4 Turbo model
                    'gpt-4-turbo-2024-04-09',     # Latest GPT-4 Turbo snapshot
                    'gpt-4-turbo-preview',         # GPT-4 Turbo preview model
                    'gpt-4-0125-preview',         # GPT-4 Turbo preview model for laziness
                    'gpt-4-1106-preview',         # Improved instruction following model
                    'gpt-4',                      # Standard GPT-4 model
                    'gpt-4-0613'                  # Snapshot of GPT-4 from June 2023
                ],
                value='gpt-4o',                 # Default to the most advanced model
                label="Select Model",
                interactive=True
            )
            
        chatgpt_interface = gr.load(
            name=model_choice.value,
            src=openai_gradio.registry,
            accept_token=True,
            fill_height=True
        )
        
        def update_model(new_model):
            return gr.load(
                name=new_model,
                src=openai_gradio.registry,
                accept_token=True,
                fill_height=True
            )
        
        model_choice.change(
            fn=update_model,
            inputs=[model_choice],
            outputs=[chatgpt_interface]
        )
    with gr.Tab("Claude"):
        with gr.Row():
            claude_model = gr.Dropdown(
                choices=[
                    'claude-3-5-sonnet-20241022',  # Latest Sonnet
                    'claude-3-5-haiku-20241022',   # Latest Haiku
                    'claude-3-opus-20240229',       # Opus
                    'claude-3-sonnet-20240229',     # Previous Sonnet
                    'claude-3-haiku-20240307'       # Previous Haiku
                ],
                value='claude-3-5-sonnet-20241022',  # Default to latest Sonnet
                label="Select Model",
                interactive=True
            )
            
        claude_interface = gr.load(
            name=claude_model.value,
            src=anthropic_gradio.registry,
            accept_token=True,
            fill_height=True
        )
        
        def update_claude_model(new_model):
            return gr.load(
                name=new_model,
                src=anthropic_gradio.registry,
                accept_token=True,
                fill_height=True
            )
        
        claude_model.change(
            fn=update_claude_model,
            inputs=[claude_model],
            outputs=[claude_interface]
        )
    with gr.Tab("Grok"):
        gr.load(
            name='grok-beta',
            src=xai_gradio.registry,
            accept_token=True,
            fill_height=True
        )
    with gr.Tab("Qwen"):
        with gr.Row():
            qwen_model = gr.Dropdown(
                choices=[
                    'Qwen/Qwen2.5-72B-Instruct',
                    'Qwen/Qwen2.5-Coder-32B-Instruct'
                ],
                value='Qwen/Qwen2.5-72B-Instruct',
                label="Select Qwen Model",
                interactive=True
            )
            
        qwen_interface = gr.load(
            name=qwen_model.value,
            src=hyperbolic_gradio.registry,
            fill_height=True
        )
        
        def update_qwen_model(new_model):
            return gr.load(
                name=new_model,
                src=hyperbolic_gradio.registry,
                fill_height=True
            )
        
        qwen_model.change(
            fn=update_qwen_model,
            inputs=[qwen_model],
            outputs=[qwen_interface]
        )
        
        gr.Markdown("""
        <div>
            <img src="https://storage.googleapis.com/public-arena-asset/hyperbolic_logo.png" alt="Hyperbolic Logo" style="height: 50px; margin-right: 10px;">
        </div>    
                    
        **Note:** This model is supported by Hyperbolic. Build your AI apps at [Hyperbolic](https://app.hyperbolic.xyz/).
        """)
    with gr.Tab("Perplexity"):
        with gr.Row():
            perplexity_model = gr.Dropdown(
                choices=[
                    # Sonar Models (Online)
                    'llama-3.1-sonar-small-128k-online',    # 8B params
                    'llama-3.1-sonar-large-128k-online',    # 70B params
                    'llama-3.1-sonar-huge-128k-online',     # 405B params
                    # Sonar Models (Chat)
                    'llama-3.1-sonar-small-128k-chat',      # 8B params
                    'llama-3.1-sonar-large-128k-chat',      # 70B params
                    # Open Source Models
                    'llama-3.1-8b-instruct',                # 8B params
                    'llama-3.1-70b-instruct'                # 70B params
                ],
                value='llama-3.1-sonar-large-128k-online',  # Default to large online model
                label="Select Perplexity Model",
                interactive=True
            )
        
        perplexity_interface = gr.load(
            name=perplexity_model.value,
            src=perplexity_gradio.registry,
            accept_token=True,
            fill_height=True
        )
        
        def update_perplexity_model(new_model):
            return gr.load(
                name=new_model,
                src=perplexity_gradio.registry,
                accept_token=True,
                fill_height=True
            )
        
        perplexity_model.change(
            fn=update_perplexity_model,
            inputs=[perplexity_model],
            outputs=[perplexity_interface]
        )
        
        gr.Markdown("""
        **Note:** Models are grouped into three categories:
        - **Sonar Online Models**: Include search capabilities (beta access required)
        - **Sonar Chat Models**: Standard chat models
        - **Open Source Models**: Based on Hugging Face implementations
        
        For access to Online LLMs features, please fill out the [beta access form](https://perplexity.typeform.com/apiaccessform?typeform-source=docs.perplexity.ai).
        """)
    with gr.Tab("DeepSeek-V2.5"):
        gr.load(
            name='deepseek-ai/DeepSeek-V2.5',
            src=hyperbolic_gradio.registry,
            fill_height=True
        )
        gr.Markdown("""
        <div>
            <img src="https://storage.googleapis.com/public-arena-asset/hyperbolic_logo.png" alt="Hyperbolic Logo" style="height: 50px; margin-right: 10px;">
        </div>    
                    
        **Note:** This model is supported by Hyperbolic. Build your AI apps at [Hyperbolic](https://app.hyperbolic.xyz/).
        """)
    with gr.Tab("Mistral"):
        with gr.Row():
            mistral_model = gr.Dropdown(
                choices=[
                    # Premier Models
                    'mistral-large-latest',          # Top-tier reasoning model (128k)
                    'pixtral-large-latest',          # Frontier-class multimodal model (128k)
                    'ministral-3b-latest',           # Best edge model (128k)
                    'ministral-8b-latest',           # High performance edge model (128k)
                    'mistral-small-latest',          # Enterprise-grade small model (32k)
                    'codestral-latest',              # Code-specialized model (32k)
                    'mistral-embed',                 # Semantic text representation (8k)
                    'mistral-moderation-latest',     # Content moderation service (8k)
                    # Free Models
                    'pixtral-12b-2409',             # Free 12B multimodal model (128k)
                    'open-mistral-nemo',             # Multilingual model (128k)
                    'open-codestral-mamba'           # Mamba-based coding model (256k)
                ],
                value='pixtral-large-latest',    # pixtral for vision
                label="Select Mistral Model",
                interactive=True
            )
            
        mistral_interface = gr.load(
            name=mistral_model.value,
            src=mistral_gradio.registry,
            fill_height=True
        )
        
        def update_mistral_model(new_model):
            return gr.load(
                name=new_model,
                src=mistral_gradio.registry,
                fill_height=True
            )
        
        mistral_model.change(
            fn=update_mistral_model,
            inputs=[mistral_model],
            outputs=[mistral_interface],
        )
        
        gr.Markdown("""
        **Note:** You need a Mistral API key to use these models. Get one at [Mistral AI Platform](https://console.mistral.ai/).
        
        Models are grouped into two categories:
        - **Premier Models**: Require a paid API key
        - **Free Models**: Available with free API keys
        
        Each model has different context window sizes (from 8k to 256k tokens) and specialized capabilities.
        """)
    with gr.Tab("Fireworks"):
        with gr.Row():
            fireworks_model = gr.Dropdown(
                choices=[
                    'f1-preview',              # Latest F1 preview model
                    'f1-mini-preview',         # Smaller, faster model
                ],
                value='f1-preview',            # Default to preview model
                label="Select Fireworks Model",
                interactive=True
            )
            
        fireworks_interface = gr.load(
            name=fireworks_model.value,
            src=fireworks_gradio.registry,
            fill_height=True
        )
        
        def update_fireworks_model(new_model):
            return gr.load(
                name=new_model,
                src=fireworks_gradio.registry,
                fill_height=True
            )
        
        fireworks_model.change(
            fn=update_fireworks_model,
            inputs=[fireworks_model],
            outputs=[fireworks_interface]
        )
        
        gr.Markdown("""
        **Note:** You need a Fireworks AI API key to use these models. Get one at [Fireworks AI](https://app.fireworks.ai/).
        """)
    with gr.Tab("Cerebras"):
        with gr.Row():
            cerebras_model = gr.Dropdown(
                choices=[
                    'llama3.1-8b',
                    'llama3.1-70b',
                    'llama3.1-405b'
                ],
                value='llama3.1-70b',  # Default to mid-size model
                label="Select Cerebras Model",
                interactive=True
            )
            
        cerebras_interface = gr.load(
            name=cerebras_model.value,
            src=cerebras_gradio.registry,
            accept_token=True,  # Added token acceptance
            fill_height=True
        )
        
        def update_cerebras_model(new_model):
            return gr.load(
                name=new_model,
                src=cerebras_gradio.registry,
                accept_token=True,  # Added token acceptance
                fill_height=True
            )

demo.launch(ssr_mode=False)


