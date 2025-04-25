import gradio as gr
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
model = tf.keras.models.load_model("model.keras")


def predict_digit(drawing):
    if drawing is None:
        return {str(i): 'Draw something' for i in range(10)}
    else:
        img_array = drawing['composite']
        img = Image.fromarray(img_array.astype('uint8'), 'RGBA')
        # Resize image to 28x28 pixels
        img = img.resize((28, 28))
        # Convert RGB to grayscale
        img = img.convert('L')
        img = np.array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img / 255.0
        img = 1 - img  # Invert colors (white on black)

        # Predicting
        res = model.predict([img])[0]
        return {str(i): float(res[i]) for i in range(10)}


# Build the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## ✏️ Draw a digit (0–9)")

    with gr.Row():
        sketch_input = gr.Sketchpad(interactive=True, fixed_canvas=True, render=True, type='numpy', label="Draw here")
        prediction_output = gr.Label(num_top_classes=3, label="Top Predictions")

    sketch_input.change(fn=predict_digit, inputs=sketch_input, outputs=prediction_output)
gr.Brush()
# Run the app
if __name__ == "__main__":
    demo.launch()
