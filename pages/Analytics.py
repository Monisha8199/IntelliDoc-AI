import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

st.set_page_config(page_title="Document Analytics", page_icon="📊")

st.title("📊 Document Analytics")

uploaded_file = st.file_uploader(
    "Upload a PDF, DOCX or TXT file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:

    text = ""

    if uploaded_file.name.endswith(".pdf"):
        pdf = PdfReader(uploaded_file)
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")

    words = len(text.split())
    characters = len(text)
    sentences = len([s for s in text.split(".") if s.strip()])
    paragraphs = len([p for p in text.split("\n") if p.strip()])

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📝 Words", words)
        st.metric("📄 Paragraphs", paragraphs)

    with col2:
        st.metric("🔠 Characters", characters)
        st.metric("📌 Sentences", sentences)

    st.subheader("Document Preview")
    st.text_area("", text, height=300)