import streamlit as st
from models.chat import chat_with_document
from utils.file_reader import extract_text

st.set_page_config(page_title="AI Chat", page_icon="💬")

st.title("💬 AI Chat with Document")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    document_text = extract_text(uploaded_file)

    st.success("Document uploaded successfully!")

    question = st.text_input("Ask a question about the document")

    if st.button("Ask AI"):

        if question:

            with st.spinner("Thinking..."):

                answer = chat_with_document(document_text, question)

            st.subheader("🤖 AI Answer")

            st.write(answer)