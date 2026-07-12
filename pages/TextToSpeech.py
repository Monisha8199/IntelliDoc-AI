import streamlit as st
from gtts import gTTS

st.title("🔊 Text To Speech")

text = st.text_area("Enter text")

if st.button("Speak"):

    if text:
        tts = gTTS(text=text, lang="en")

        file = "speech.mp3"
        tts.save(file)

        st.audio(file)

        st.success("Speech generated successfully!")

    else:
        st.warning("Please enter some text")