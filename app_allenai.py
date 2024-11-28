import gradio as gr
import spaces
import transformers_gradio
from utils import get_app

# Load Llama model
llama_demo = gr.load(name="allenai/Llama-3.1-Tulu-3-8B", src=transformers_gradio.registry)
llama_demo.fn = spaces.GPU()(llama_demo.fn)

# Load OLMo model
olmo_demo = gr.load(name="akhaliq/olmo-anychat", src="spaces")

# Create combined demo with dropdown
demo = get_app(
    models=["allenai/Llama-3.1-Tulu-3-8B", "akhaliq/olmo-anychat"],
    default_model="allenai/Llama-3.1-Tulu-3-8B",
    src=lambda name, _: llama_demo if name == "allenai/Llama-3.1-Tulu-3-8B" else olmo_demo
)

# Disable API names
for fn in demo.fns.values():
    fn.api_name = False


