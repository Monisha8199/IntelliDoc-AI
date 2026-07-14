import streamlit as st
from models.analytics import analyze_document
from utils.file_reader import extract_text

st.set_page_config(page_title="Document Analytics", page_icon="📊")

st.title("📊 Document Analytics")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    result = analyze_document(text)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📄 Words", result["Words"])
        st.metric("📑 Paragraphs", result["Paragraphs"])

    with col2:
        st.metric("🔤 Characters", result["Characters"])
        st.metric("⏱ Reading Time", result["Reading Time"])

    st.subheader("Document Preview")

    st.text_area("", text[:1500], height=250)