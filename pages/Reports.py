import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from models.summarizer import generate_summary

st.set_page_config(page_title="AI Report", page_icon="📑")

st.title("📑 AI Report Generator")

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

    st.subheader("📄 Document Preview")
    st.text_area("Content", text, height=250)

    if st.button("Generate Report"):

        with st.spinner("Generating AI Report..."):

            report = generate_summary(
                f"""
                Create a professional report for the following document.

                Include:
                1. Executive Summary
                2. Key Points
                3. Important Insights
                4. Conclusion

                Document:
                {text}
                """
            )

        st.success("✅ Report Generated")

        st.subheader("📑 AI Report")

        st.write(report)