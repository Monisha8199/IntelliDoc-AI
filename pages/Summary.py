import streamlit as st
from models.summarizer import generate_summary
from utils.file_reader import extract_text
from database.history import save_history
from utils.pdf_export import create_pdf
import os

st.set_page_config(page_title="AI Summary", page_icon="📄")

st.title("📄 AI Document Summarizer")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    st.subheader("Document Preview")
    st.text_area("", text[:1500], height=250)

    if st.button("Generate Summary"):

        with st.spinner("Generating Summary..."):

            summary = generate_summary(text)

        st.success("Summary Generated Successfully!")

        st.subheader("Summary")

        st.write(summary)

        save_history(
          "Summary",
           uploaded_file.name,
           summary
       )

        # Create exports folder if it doesn't exist
        os.makedirs("exports", exist_ok=True)

        pdf_path = "exports/summary.pdf"

        create_pdf(summary, pdf_path)

        with open(pdf_path, "rb") as pdf:
            st.download_button(
                label="📥 Download Summary as PDF",
                data=pdf,
                file_name="summary.pdf",
                mime="application/pdf"
            )