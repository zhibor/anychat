import gradio as gr
import spaces

demo = gr.load(name="sail/Sailor2-20B-Chat", src="spaces")

for fn in demo.fns.values():
    fn.api_name = False

if __name__ == "__main__":
    demo.launch()
