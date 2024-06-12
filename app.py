from audiocraft.models import MusicGen  #Open-source library for music generation by MetaAI
import streamlit as st
import os
import torch
import torchaudio
import numpy as np
import base64

@st.cache_resource
#Loading the music-small model from MetaAI github repository
def load_model():
    model = MusicGen.get_pretrained("facebook/musicgen-melody")
    return model

def generate_music_tensors(description, time_duration:int):
    print("Description:", description)
    print("Time Duration:", time_duration)
    model = load_model()

    model.set_generation_params(
        use_sampling=True,
        top_k=250,
        duration=time_duration,
    )

    output = model.generate( #Holds the tensor values
        descriptions = [description],
        progress=True,
        return_tokens=True
    )

    return output[0] #Return tensors of decoded audio samples

def save_audio_file(samples: torch.Tensor):
    sample_rate = 32000 #standard sample rate for audio
    save_path = "generatedMusic/"

    assert samples.dim() == 2 or samples.dim() == 3
    samples = samples.detach().cpu()

    if samples.dim() ==2:
        samples = samples[None, ...]

    for i, audio in enumerate(samples):
        audio_path = os.path.join(save_path, f"audio_{i}.wav")
        torchaudio.save(audio_path, audio, sample_rate)

def get_binary_file_download_html(bin_file, file_label='File'): #For user to download the generated audio file
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href


st.set_page_config(page_title="Music Generation App", page_icon="🎵")
def main():
    st.title("Music Generation with Audiocraft")

    with st.expander("See Explanation"):
        st.write("This app uses the `facebook/music-small` model from Hugging Face to generate music. "
                 "You can upload a MIDI file and the model will generate music based on the input.")

    text_area = st.text_area("Enter your MIDI file here:")
    time_slider = st.slider("Select time duration to generate(in seconds)", 2, 5, 10)

    if text_area and time_slider:
        st.json({
            "Your description": text_area,
            "Selected time duration in seconds": time_slider
        })

        st.subheader("Generating music...")

        music_tensors = generate_music_tensors(text_area, time_slider)
        print("Music Tensors:", music_tensors)

        save_music_file = save_audio_file(music_tensors)

        save_filepath = 'generatedMusic/audio_0.wav'

        audio_file = open(save_filepath, 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/wav')
        st.markdown(get_binary_file_download_html(save_filepath, 'Audio'),
                    unsafe_allow_html=True)

if __name__ == "__main__":
    main()