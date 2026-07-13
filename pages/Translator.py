import streamlit as st
from models.translator import translate_text

st.title("🌐 AI Document Translator")

text = st.text_area("Enter text to translate")

language = st.selectbox(
    "Select Language",
    [
        "Tamil",
        "Hindi",
        "French",
        "German",
        "Spanish",
        "Japanese",
        "Korean",
        "Chinese"
    ]
)

if st.button("Translate"):
    if text:
        with st.spinner("Translating..."):
            result = translate_text(text, language)

        st.success("Translation Complete!")

        st.write(result)