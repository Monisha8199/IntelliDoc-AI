import streamlit as st
from utils.file_reader import extract_text
from models.sentiment import analyze_sentiment

st.set_page_config(page_title="Sentiment Analysis", page_icon="😊")

st.title("😊 AI Sentiment Analysis")

uploaded_file = st.file_uploader(
    "Upload PDF, DOCX or TXT",
    type=["pdf", "docx", "txt"]
)

if uploaded_file is not None:

    text = extract_text(uploaded_file)

    sentiment, score = analyze_sentiment(text)

    st.metric("Sentiment", sentiment)
    st.metric("Polarity Score", score)

    st.subheader("Preview")

    st.text_area("", text[:1000], height=200)