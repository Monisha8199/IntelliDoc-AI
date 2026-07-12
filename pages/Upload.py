import streamlit as st
import os

st.set_page_config(page_title="Upload Documents", page_icon="📂", layout="wide")

st.title("📂 Upload Documents")

st.write("Upload your PDF, DOCX, or TXT files for AI analysis.")

uploaded_file = st.file_uploader(
    "Choose a document",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ {uploaded_file.name} uploaded successfully!")

    st.info(f"Saved to: {file_path}")