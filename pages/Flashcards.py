import streamlit as st
from utils.file_reader import extract_text
from models.flashcards import generate_flashcards

st.set_page_config(page_title="AI Flashcards", page_icon="🎴")

st.title("🎴 AI Flashcard Generator")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    if st.button("Generate Flashcards"):

        with st.spinner("Generating Flashcards..."):

            cards = generate_flashcards(text)

        st.success("Flashcards Ready!")

        st.markdown(cards)