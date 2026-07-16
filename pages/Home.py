import streamlit as st

st.set_page_config(
    page_title="IntelliDoc-AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- HERO SECTION ----------------

st.markdown("""
<div style="text-align:center;padding-top:20px;padding-bottom:30px;">

<h1 style="
font-size:60px;
font-weight:800;
color:white;
margin-bottom:10px;">

🤖 IntelliDoc-AI

</h1>

<h3 style="
color:#9CC6FF;
font-weight:400;">

Transform Documents into Intelligent Insights with AI

</h3>

<p style="
color:#D6E4FF;
font-size:18px;">

Summarize • Chat • Analyze • Translate • Generate Reports • Resume Analysis

</p>

</div>
""", unsafe_allow_html=True)

# ---------------- FEATURE CARDS ----------------

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
<div class="feature-card">

## 📄 AI Summary

Generate short and intelligent summaries from lengthy documents within seconds.

</div>
""", unsafe_allow_html=True)

with col2:
    st.markdown("""
<div class="feature-card">

## 💬 AI Chat

Ask questions and chat naturally with your uploaded documents.

</div>
""", unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
<div class="feature-card">

## 📊 Analytics

View document statistics including words, sentences, and paragraphs.

</div>
""", unsafe_allow_html=True)

with col4:
    st.markdown("""
<div class="feature-card">

## 📄 Resume Analyzer

Analyze resumes and receive AI-powered suggestions.

</div>
""", unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    st.markdown("""
<div class="feature-card">

## 🌐 Translation

Translate documents into multiple languages using AI.

</div>
""", unsafe_allow_html=True)

with col6:
    st.markdown("""
<div class="feature-card">

## 📝 Quiz Generator

Automatically generate quizzes and flashcards from your documents.

</div>
""", unsafe_allow_html=True)

col7, col8 = st.columns(2)

with col7:
    st.markdown("""
<div class="feature-card">

## 😊 Sentiment Analysis

Analyze the emotional tone of your documents.

</div>
""", unsafe_allow_html=True)

with col8:
    st.markdown("""
<div class="feature-card">

## 📑 AI Reports

Generate professional reports with key insights and conclusions.

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.info("🚀 Welcome to IntelliDoc-AI — Your complete AI-powered document assistant.")