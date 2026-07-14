import streamlit as st
from utils.file_reader import extract_text
from models.document_compare import compare_documents

st.set_page_config(page_title="Document Comparison", page_icon="📑")

st.title("📑 AI Document Comparison")

file1 = st.file_uploader(
    "Upload First Document",
    type=["pdf", "docx", "txt"],
    key="file1"
)

file2 = st.file_uploader(
    "Upload Second Document",
    type=["pdf", "docx", "txt"],
    key="file2"
)

if file1 and file2:

    text1 = extract_text(file1)
    text2 = extract_text(file2)

    if st.button("Compare Documents"):

        with st.spinner("Comparing..."):

            result = compare_documents(text1, text2)

        st.success("Comparison Complete!")

        st.markdown(result)