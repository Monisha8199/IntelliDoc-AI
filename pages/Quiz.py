import streamlit as st
from utils.file_reader import extract_text
from models.quiz_generator import generate_quiz

st.set_page_config(page_title="AI Quiz Generator", page_icon="📝")

st.title("📝 AI Quiz Generator")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    if st.button("Generate Quiz"):

        with st.spinner("Generating Quiz..."):

            quiz = generate_quiz(text)

        st.success("Quiz Generated Successfully!")

        st.markdown(quiz)