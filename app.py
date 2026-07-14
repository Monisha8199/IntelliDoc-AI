import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="IntelliDoc-AI Pro",
    page_icon="🤖",
    layout="wide"
)

# -------------------- LOAD CSS --------------------
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------- TITLE --------------------
st.markdown(
    "<h1 class='main-title'>🤖 IntelliDoc-AI Pro</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='subtitle'>AI Powered Intelligent Document Analysis Platform</p>",
    unsafe_allow_html=True
)

st.divider()

# -------------------- METRICS --------------------
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("📄 AI Modules", "12")

with c2:
    st.metric("📂 Documents", "Unlimited")

with c3:
    st.metric("🌍 Languages", "8+")

with c4:
    st.metric("🟢 Status", "Online")

st.divider()

st.markdown("## 🚀 Available Features")

# -------------------- ROW 1 --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card summary">
        <h3>📄 AI Summary</h3>
        <p>Generate concise summaries from long documents instantly.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card translate">
        <h3>🌐 AI Translator</h3>
        <p>Translate documents into multiple languages using AI.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card chat">
        <h3>💬 AI Chat</h3>
        <p>Ask questions and chat with your uploaded document.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- ROW 2 --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card analytics">
        <h3>📊 Analytics</h3>
        <p>View document statistics, word count and reading time.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card keyword">
        <h3>🔑 Keyword Extraction</h3>
        <p>Automatically find important keywords from documents.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card sentiment">
        <h3>😊 Sentiment Analysis</h3>
        <p>Identify whether the document is positive, neutral or negative.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- ROW 3 --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card quiz">
        <h3>📝 Quiz Generator</h3>
        <p>Create AI-generated quizzes from your study materials.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card flashcard">
        <h3>🎴 Flashcards</h3>
        <p>Generate smart flashcards for revision and learning.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card resume">
        <h3>📄 Resume Analyzer</h3>
        <p>Analyze resumes and receive AI-powered suggestions.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------- ROW 4 --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card compare">
        <h3>📑 Document Comparison</h3>
        <p>Compare two documents and highlight similarities & differences.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card history">
        <h3>🗂️ History</h3>
        <p>Access summaries, quizzes, chats and previous analyses.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card tts">
        <h3>🔊 Text to Speech</h3>
        <p>Listen to your documents with AI-powered voice output.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -------------------- ABOUT --------------------
st.subheader("🌟 Why IntelliDoc-AI?")

st.write("""
IntelliDoc-AI Pro is an AI-powered document analysis platform designed for students,
researchers, and professionals. Upload PDFs, DOCX, or TXT files and perform multiple
AI-powered tasks such as summarization, translation, chatting with documents,
keyword extraction, sentiment analysis, quiz generation, flashcard creation,
resume analysis, and document comparison—all in one place.
""")

st.divider()

# -------------------- FOOTER --------------------
st.markdown(
"""
<div class="footer">
🚀 IntelliDoc-AI Pro | Built with ❤️ using Python, Streamlit & Groq AI
</div>
""",
unsafe_allow_html=True
)