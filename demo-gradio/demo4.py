import numpy as np
import gradio as gr


def reverse_audio(audio):
    sr, data = audio
    return (sr, np.flipud(data))


input_audio = gr.Audio(sources=["microphone", "upload"],
                       waveform_options=gr.WaveformOptions(
                           waveform_color="#01C6FF",
                           waveform_progress_color="#0066B4",
                           skip_length=2,
                           show_controls=False,
                       ),
                       )
audio_interface = gr.Interface(fn=reverse_audio, inputs=input_audio, outputs="audio")


# Function to convert the image to black and white (grayscale)
def image_black_white(image):
    if image is None:
        return "No image uploaded"
    image_array = np.array(image)
    # Calculate grayscale using the luminosity method
    if len(image_array.shape) == 3:  # Ensure the image has color channels
        grayscale = np.dot(image_array[..., :3], [0.2989, 0.5870, 0.1140]).astype(np.uint8)
    else:
        grayscale = image_array  # Already grayscale
    return grayscale


# Create the Gradio interface
image_interface = gr.Interface(fn=image_black_white, inputs=gr.Image(type="numpy"), outputs="image")

# Use Gradio Blocks for tabs
with gr.Blocks() as app:
    with gr.Tab("Audio Upload"):
        audio_interface.render()
    with gr.Tab("Image Upload"):
        image_interface.render()

# Launch the app
app.launch()
