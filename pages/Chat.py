import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from models.chat import chat_with_document

st.set_page_config(page_title="AI Chat", page_icon="💬")

st.title("💬 AI Chat with Document")

uploaded_file = st.file_uploader(
    "Upload a PDF, DOCX or TXT file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

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

    st.success("✅ Document uploaded successfully!")

    question = st.text_input("Ask a question about your document")

    if st.button("Ask AI"):
        if question.strip():

            with st.spinner("Thinking..."):
                answer = chat_with_document(text, question)

            st.success(answer)

        else:
            st.warning("Please enter a question.")