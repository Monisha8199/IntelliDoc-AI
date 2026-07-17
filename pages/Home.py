import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="IntelliDoc-AI Pro",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# Hero Section
# ---------------------------------------------------
st.markdown("""
<div style="
padding:45px;
border-radius:25px;
background:linear-gradient(135deg,#2563eb,#1d4ed8,#0f172a);
box-shadow:0px 12px 40px rgba(0,0,0,0.35);
text-align:center;
">

<h1 style="
color:white;
font-size:60px;
font-weight:800;
margin-bottom:10px;
">
🤖 IntelliDoc-AI Pro
</h1>

<p style="
color:#DCEBFF;
font-size:22px;
margin-bottom:15px;
">
Transform Documents into Intelligent Insights
</p>

<p style="
color:#BFD8FF;
font-size:17px;
">
Summarize • Chat • Translate • Analyze • Resume Analysis • Reports
</p>

</div>
""", unsafe_allow_html=True)

st.write("")

# ---------------------------------------------------
# Quick Action Buttons
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.button("📄 Upload Document", use_container_width=True)

with col2:
    st.button("💬 Start AI Chat", use_container_width=True)

st.write("")

# ---------------------------------------------------
# Welcome Message
# ---------------------------------------------------

st.success("🎉 Welcome to IntelliDoc-AI Pro!")

st.write(
"""
Upload your documents and use Artificial Intelligence to:

- 📄 Summarize documents
- 💬 Chat with PDFs
- 🌐 Translate files
- 📊 Analyze documents
- 😊 Perform Sentiment Analysis
- 🔑 Extract Keywords
- 📝 Generate Quizzes
- 🎴 Create Flashcards
- 👤 Analyze Resumes
- 📑 Compare Documents
- 🔊 Convert Text to Speech
"""
)

st.write("")

# ---------------------------------------------------
# Dashboard Statistics
# ---------------------------------------------------

st.subheader("📊 Dashboard Overview")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("📄 AI Modules", "12")

with m2:
    st.metric("📁 Documents", "Unlimited")

with m3:
    st.metric("🌍 Languages", "8+")

with m4:
    st.metric("🟢 Status", "Online")

st.write("")

# ---------------------------------------------------
# Available Features
# ---------------------------------------------------

st.subheader("🚀 Available AI Features")

col1, col2, col3 = st.columns(3)

features = [
    ("📄 AI Summary", "Generate concise summaries from lengthy documents."),
    ("💬 AI Chat", "Chat with your uploaded documents using AI."),
    ("🌐 Translator", "Translate documents into multiple languages."),
    ("📊 Analytics", "View document statistics instantly."),
    ("😊 Sentiment Analysis", "Identify emotions and sentiment."),
    ("🔑 Keyword Extraction", "Extract important keywords automatically."),
    ("📝 Quiz Generator", "Create quizzes from any document."),
    ("🎴 Flashcards", "Generate study flashcards instantly."),
    ("👤 Resume Analyzer", "Analyze resumes with AI suggestions."),
    ("📑 Document Comparison", "Compare two documents side-by-side."),
    ("📂 History", "View previous uploads and AI responses."),
    ("🔊 Text To Speech", "Convert document text into speech.")
]

for i, (title, desc) in enumerate(features):

    with [col1, col2, col3][i % 3]:

        st.markdown(f"""
        <div style="
        background:rgba(255,255,255,0.08);
        padding:20px;
        border-radius:18px;
        margin-bottom:18px;
        border:1px solid rgba(255,255,255,0.10);
        box-shadow:0 6px 15px rgba(0,0,0,0.15);
        ">

        <h4 style="color:white;">{title}</h4>

        <p style="color:#DCE7FF;">
        {desc}
        </p>

        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------
# Quick Access
# ---------------------------------------------------

st.write("")
st.subheader("⚡ Quick Access")

a1, a2, a3, a4 = st.columns(4)

with a1:
    st.button("📄 Summary", use_container_width=True)

with a2:
    st.button("💬 Chat", use_container_width=True)

with a3:
    st.button("🌐 Translate", use_container_width=True)

with a4:
    st.button("📊 Analytics", use_container_width=True)

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.write("")
st.markdown("---")

st.markdown("""
<div style="text-align:center;color:#BFD8FF;padding:20px;">

<h3>🤖 IntelliDoc-AI Pro</h3>

<p>
Developed by <b>Monisha S</b><br>
AI Powered Intelligent Document Analysis Platform
</p>

<p>
© 2026 All Rights Reserved
</p>

</div>
""", unsafe_allow_html=True)