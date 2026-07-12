import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
import models.summarizer as summarizer

st.title("🤖 AI Document Summarizer")

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

    else:
        text = uploaded_file.read().decode("utf-8")

    st.subheader("Extracted Text")

    st.text_area("", text, height=250)

    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):

            summary = summarizer.generate_summary(text)

        st.success(summary)