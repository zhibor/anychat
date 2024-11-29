import gradio as gr
import spaces
from utils import get_app

# Create the combined demo using the utility function
demo = get_app(
    models=["akhaliq/allen-test", "akhaliq/olmo-anychat"],
    default_model="akhaliq/allen-test",
    src="spaces"
)



