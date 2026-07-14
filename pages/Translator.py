import streamlit as st
from models.translator import translate_text
from utils.file_reader import extract_text

st.set_page_config(page_title="AI Translator", page_icon="🌐")

st.title("🌐 AI Document Translator")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

languages = [
    "Tamil",
    "Hindi",
    "French",
    "German",
    "Spanish",
    "Japanese",
    "Korean",
    "Chinese"
]

language = st.selectbox("Select Language", languages)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    st.subheader("Document Preview")
    st.text_area("", text[:1500], height=200)

    if st.button("🌐 Translate Document"):

        with st.spinner("Translating..."):

            translated = translate_text(text, language)

        st.success("Translation Complete!")

        st.subheader("Translated Document")

        st.write(translated)