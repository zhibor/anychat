import gradio as gr
import spaces
import transformers_gradio

demo = gr.load(name="AIDC-AI/Marco-o1", src=transformers_gradio.registry)
demo.fn = spaces.GPU()(demo.fn)

for fn in demo.fns.values():
    fn.api_name = False

if __name__ == "__main__":
    demo.launch()
