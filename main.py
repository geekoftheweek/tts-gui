import datetime
import io
import json
from pathlib import Path
import re

import numpy as np
import scipy.io
import streamlit as st
import torch
from TTS.api import TTS

voices = [
    "Aaron Dreschner",
    "Abrahan Mack",
    "Adde Michal",
    "Alexandra Hisakawa",
    "Alison Dietlinde",
    "Alma María",
    "Ana Florence",
    "Andrew Chipper",
    "Annmarie Nele",
    "Asya Anara",
    "Badr Odhiambo",
    "Baldur Sanjin",
    "Barbora MacLean",
    "Brenda Stern",
    "Camilla Holmström",
    "Chandra MacFarland",
    "Claribel Dervla",
    "Craig Gutsy",
    "Daisy Studious",
    "Damien Black",
    "Damjan Chapman",
    "Dionisio Schuyler",
    "Eugenio Mataracı",
    "Ferran Simen",
    "Filip Traverse",
    "Gilberto Mathias",
    "Gitta Nikolina",
    "Gracie Wise",
    "Henriette Usha",
    "Ige Behringer",
    "Ilkin Urbano",
    "Kazuhiko Atallah",
    "Kumar Dahl",
    "Lidiya Szekeres",
    "Lilya Stainthorpe",
    "Ludvig Milivoj",
    "Luis Moray",
    "Maja Ruoho",
    "Marcos Rudaski"
    "Narelle Moon",
    "Nova Hogarth",
    "Rosemary Okafor",
    "Royston Min",
    "Sofia Hellen",
    "Suad Qasim",
    "Szofi Granger",
    "Tammie Ema",
    "Tammy Grit",
    "Tanja Adelina",
    "Torcull Diarmuid",
    "Uta Obando",
    "Viktor Eka",
    "Viktor Menelaos",
    "Vjollca Johnnie",
    "Wulf Carlevaro",
    "Xavier Hayasaka",
    "Zacharie Aimilios",
    "Zofija Kendrick",
]

language_codes = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Polish": "pl",
    "Turkish": "tr",
    "Russian": "ru",
    "Dutch": "nl",
    "Czech": "cs",
    "Arabic": "ar",
    "Chinese": "zh-cn",
    "Japanese": "ja",
    "Hungarian": "hu",
    "Korean": "ko",
    "Hindi": "hi"
}
language_strings = sorted(language_codes.keys())

@st.cache_resource
def load_model():
    return TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

device = "cuda" if torch.cuda.is_available() else "cpu"
model = load_model()


def audio_to_wav(audio, sample_rate=24000):
    f = io.BytesIO()
    scipy.io.wavfile.write(f, sample_rate, audio)
    return f.getvalue()

def main():
    st.title("Voiceover Generator")
    with st.expander("How to use:"):
        st.write("""
* Choose a voice
* Choose a language
* Type the message
* Click `Run`
  * If it sounds weird, run it again for a new version.
* Download the result (Optional)
""")

    voice = st.selectbox("Voice", voices, index=voices.index("Viktor Menelaos"))
    language = st.selectbox("Language", language_strings, index=language_strings.index("English"))
    language_code = language_codes[language]
    message = st.text_area(
        "Dialogue",
        placeholder="She sells seashells by the seashore."
    )
    speak = st.button('Run')

    request = {
        'message': message,
        'voice': voice,
        'timestamp': datetime.datetime.now().isoformat()
    }

    if speak:
        audio = np.array(model.tts(text=message, speaker=voice, language=language_code))
        st.audio(audio, sample_rate=24000, autoplay=True)

        wav_audio = audio_to_wav(audio)
        msg_filename = re.sub(r'[^a-zA-Z]+', '_', message).strip('_')[:100]
        st.download_button("Download .wav", wav_audio, f"{msg_filename}.wav")


if __name__ == "__main__":
    main()
