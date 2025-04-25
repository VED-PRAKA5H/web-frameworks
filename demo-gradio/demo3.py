import gradio as gr

# Define the function with proper indentation and formatting
def demo3(text, is_true, num):
    return f"Checkbox selected: {is_true}. Hello, {text}! The quotient of the given number is:", num // 2

# Create the Gradio interface with multiple inputs and outputs
demo3_interface = gr.Interface(
    fn=demo3,
    inputs=["text", "checkbox", gr.Slider(50, 100)],  # Inputs are text, checkbox, and a slider
    outputs=["text", "number"]  # Outputs are text and a number
)

# Launch the Gradio interface
demo3_interface.launch()

