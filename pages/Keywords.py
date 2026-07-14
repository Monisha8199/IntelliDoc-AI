import streamlit as st
from utils.file_reader import extract_text
from models.keyword_extractor import extract_keywords

st.set_page_config(page_title="Keyword Extraction", page_icon="🔑")

st.title("🔑 AI Keyword Extraction")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    st.subheader("Top Keywords")

    keywords = extract_keywords(text)

    for keyword in keywords:
        st.success(keyword)