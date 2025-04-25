import gradio as gr

def demo(text):
    return "The length is: " + str(len(text))

demo2 = gr.Interface(
    fn=demo,
    inputs=gr.Textbox(lines=2, placeholder="Input a piece of text to find its length"),
    outputs="text"
)

demo2.launch()

