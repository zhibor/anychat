from typing import Callable, Literal

import gradio as gr


def get_app(
    models: list[str],
    default_model: str,
    src: Callable[[str, str | None], gr.Blocks] | Literal["models"],
    accept_token: bool = False,
    is_chat: bool = True,
    **kwargs,
) -> gr.Blocks:
    def update_model(new_model: str) -> list[gr.Column]:
        return [gr.Column(visible=model_name == new_model) for model_name in models]

    with gr.Blocks() as demo:
        model = gr.Dropdown(label="Select Model", choices=models, value=default_model)

        columns = []
        for model_name in models:
            with gr.Column(visible=model_name == default_model) as column:
                gr.load(name=model_name, src=src, accept_token=accept_token, **kwargs)

            columns.append(column)

        model.change(
            fn=update_model,
            inputs=model,
            outputs=columns,
            api_name=False,
            queue=False,
        )

    if not is_chat:
        demo.fns = {}
    else:
        for k, v in list(demo.fns.items()):
            if isinstance(v.api_name, str) and "chat" in v.api_name:
                del demo.fns[k]

    return demo
