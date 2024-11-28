import gradio as gr
import spaces
import transformers_gradio

demo = gr.load(name="allenai/Llama-3.1-Tulu-3-8B", src=transformers_gradio.registry)
demo.fn = spaces.GPU()(demo.fn)

for fn in demo.fns.values():
    fn.api_name = False

if __name__ == "__main__":
    demo.launch()
