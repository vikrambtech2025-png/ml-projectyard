import os

import gradio as gr

INPUT_TYPE = os.environ.get("APP_INPUT", "image")


def _handle(image=None, text=None, audio=None):
    msg = (
        "This scaffold is wired for the ML-ProjectYard project. "
        "Add your model call inside `app.py` to activate the real behavior. "
        "See README.production.md for the integration guide."
    )
    if image is not None:
        return f"Received image input. {msg}"
    if text is not None:
        return f"Received text input. {msg}"
    if audio is not None:
        return f"Received audio input. {msg}"
    return msg


def _inputs():
    if INPUT_TYPE == "text":
        return gr.Textbox(lines=4, label="Input text")
    if INPUT_TYPE == "audio":
        return gr.Audio(type="filepath", label="Input audio")
    return gr.Image(type="filepath", label="Input image")


def _outputs():
    if INPUT_TYPE == "audio":
        return [gr.Audio(label="Output audio"), gr.Textbox(label="Status")]
    return gr.Textbox(label="Output")


def _fn(image=None, text=None, audio=None):
    if INPUT_TYPE == "audio":
        return audio, _handle(audio=audio)
    if INPUT_TYPE == "text":
        return _handle(text=text)
    return _handle(image=image)


title = "ML-ProjectYard"
description = "Production Gradio app for the ML-ProjectYard project."
demo = gr.Interface(
    fn=_fn,
    inputs=_inputs(),
    outputs=_outputs(),
    title=title,
    description=description,
)

if __name__ == "__main__":
    demo.launch()
