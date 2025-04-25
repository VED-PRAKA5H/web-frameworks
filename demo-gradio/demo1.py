import gradio as gr


def demo(name):
    return "Hello " + name + "!, Nice to meet you."


demo = gr.Interface(fn=demo, inputs="text", outputs="text")

demo.launch()
