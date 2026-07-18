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
# Quick Actions
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.button("📄 Upload Document", use_container_width=True)

with col2:
    st.button("💬 Start AI Chat", use_container_width=True)

st.write("")

# ---------------------------------------------------
# Welcome
# ---------------------------------------------------

st.success("🎉 Welcome to IntelliDoc-AI Pro!")

st.write("""
Upload your documents and use Artificial Intelligence to:

- 📄 Summarize documents
- 💬 Chat with PDFs
- 🌐 Translate documents
- 📊 Analyze documents
- 😊 Perform Sentiment Analysis
- 🔑 Extract Keywords
- 📝 Generate AI Quizzes
- 🎴 Create Flashcards
- 👤 Analyze Resumes
- 📑 Compare Documents
- 🔊 Convert Text to Speech
""")

# ---------------------------------------------------
# Dashboard
# ---------------------------------------------------

st.markdown("---")
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

# ---------------------------------------------------
# Features
# ---------------------------------------------------

st.markdown("---")
st.subheader("🚀 Available AI Features")

features = [
    ("📄 AI Summary", "Generate concise summaries from lengthy documents."),
    ("💬 AI Chat", "Chat with your uploaded documents using AI."),
    ("🌐 Translator", "Translate documents into multiple languages."),
    ("📊 Analytics", "View document statistics instantly."),
    ("😊 Sentiment Analysis", "Identify positive, neutral or negative sentiment."),
    ("🔑 Keyword Extraction", "Extract important keywords automatically."),
    ("📝 Quiz Generator", "Generate quizzes from your document."),
    ("🎴 Flashcards", "Create flashcards for quick revision."),
    ("👤 Resume Analyzer", "Analyze resumes using AI."),
    ("📑 Document Comparison", "Compare two documents side-by-side."),
    ("📂 History", "View previous AI responses."),
    ("🔊 Text To Speech", "Convert document text into speech.")
]

col1, col2, col3 = st.columns(3)

for i, (title, desc) in enumerate(features):

    with [col1, col2, col3][i % 3]:

        st.markdown(f"""
        <div class="feature-card">

        <h3>{title}</h3>

        <p>{desc}</p>

        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------
# Quick Access
# ---------------------------------------------------

st.markdown("---")
st.subheader("⚡ Quick Access")

q1, q2, q3, q4 = st.columns(4)

with q1:
    st.button("📄 Summary", use_container_width=True)

with q2:
    st.button("💬 Chat", use_container_width=True)

with q3:
    st.button("🌐 Translator", use_container_width=True)

with q4:
    st.button("📊 Analytics", use_container_width=True)

# ---------------------------------------------------
# System Status
# ---------------------------------------------------

st.markdown("---")
st.subheader("🖥️ System Status")

s1, s2, s3 = st.columns(3)

with s1:
    st.success("🟢 AI Services Online")

with s2:
    st.info("📂 Ready to Upload Documents")

with s3:
    st.success("🔒 Secure Processing Enabled")

# ---------------------------------------------------
# Tips
# ---------------------------------------------------

st.markdown("---")
st.subheader("💡 Tips")

st.info("📄 Upload a document before using AI Summary, AI Chat, Analytics, Translation or Document Comparison.")

st.info("💬 Use the sidebar to access all IntelliDoc-AI features.")

st.info("🔒 Your documents remain under your control while using the application.")

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

st.markdown("""
<div style="text-align:center;padding:20px;color:#BFD8FF;">

<h3>🤖 IntelliDoc-AI Pro</h3>

<p>
AI Powered Intelligent Document Analysis Platform
</p>

<p>
Developed by <b>Monisha S</b>
</p>

<p>
© 2026 All Rights Reserved
</p>

</div>
""", unsafe_allow_html=True)