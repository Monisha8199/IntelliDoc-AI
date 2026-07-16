import streamlit as st
import os
from PyPDF2 import PdfReader
from docx import Document

st.set_page_config(
    page_title="Upload Documents",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Upload Documents")

uploaded_file = st.file_uploader(
    "Choose a PDF, DOCX or TXT file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    text = ""

    # Read PDF
    if uploaded_file.name.endswith(".pdf"):
        pdf = PdfReader(uploaded_file)
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    # Read DOCX
    elif uploaded_file.name.endswith(".docx"):
        doc = Document(uploaded_file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    # Read TXT
    elif uploaded_file.name.endswith(".txt"):
        text = uploaded_file.read().decode("utf-8")

    # Save text for other pages
    st.session_state["document_text"] = text

    st.subheader("📄 Extracted Text")
    st.text_area("Document Content", text, height=300)