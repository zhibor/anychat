import gradio as gr
import spaces
import transformers_gradio

demo = gr.load(name="AIDC-AI/Marco-o1", src=transformers_gradio.registry)
demo.fn = spaces.GPU()(demo.fn)

if __name__ == "__main__":
    demo.launch()