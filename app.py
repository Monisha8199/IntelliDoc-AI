import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="IntelliDoc-AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Load CSS ----------------
try:
    with open("assets/css/style.css") as css:
        st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

# ---------------- Main Page ----------------
st.title("🤖 IntelliDoc-AI")
st.subheader("AI Powered Intelligent Document Analysis Platform")

st.info("👈 Use the sidebar to navigate through all AI features.")

st.markdown("---")

st.markdown("""
### 🚀 Features

- 📄 AI Document Summary
- 💬 AI Chat
- 🌐 Translator
- 📊 Analytics
- 😊 Sentiment Analysis
- 🔑 Keyword Extraction
- 📝 Quiz Generator
- 🎴 Flashcards
- 📄 Resume Analyzer
- 📑 Reports
- 🔊 Text To Speech
""")