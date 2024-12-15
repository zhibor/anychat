from typing import Callable, Literal, Dict, Union

import gradio as gr


def get_app(
    models: list[str],
    default_model: str,
    src: Union[Callable[[str, str | None], gr.Blocks], Literal["models"], Dict[str, gr.Blocks]],
    accept_token: bool = False,
    dropdown_label: str = "Select Model",
    **kwargs,
) -> gr.Blocks:
    def update_model(new_model: str) -> list[gr.Column]:
        return [gr.Column(visible=model_name == new_model) for model_name in models]

    with gr.Blocks() as demo:
        model = gr.Dropdown(label=dropdown_label, choices=models, value=default_model)

        columns = []
        for model_name in models:
            with gr.Column(visible=model_name == default_model) as column:
                if isinstance(src, dict):
                    src[model_name].render()
                else:
                    gr.load(name=model_name, src=src, accept_token=accept_token, **kwargs)
            columns.append(column)

        model.change(
            fn=update_model,
            inputs=model,
            outputs=columns,
            api_name=False,
            queue=False,
        )

    for fn in demo.fns.values():
        fn.api_name = False

    return demo
