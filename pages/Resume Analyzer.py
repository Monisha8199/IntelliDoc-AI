import streamlit as st
from utils.file_reader import extract_text
from models.resume_analyzer import analyze_resume

st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx","txt"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            result = analyze_resume(text)

        st.success("Analysis Complete!")

        st.markdown(result)