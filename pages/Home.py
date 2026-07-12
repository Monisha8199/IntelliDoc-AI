import streamlit as st

def show_home():

    st.markdown("<h1 class='main-title'>🤖 IntelliDoc AI</h1>", unsafe_allow_html=True)

    st.markdown(
        "<p class='sub-title'>AI-Powered Document Analysis & Report Generation</p>",
        unsafe_allow_html=True
    )

    st.divider()

    left, right = st.columns([2,1])

    with left:
        st.header("📄 Analyze Documents Smarter")

        st.write("""
Welcome to IntelliDoc AI.

This software helps you:

✔ Upload PDF, DOCX and TXT files

✔ Generate AI Summaries

✔ Ask AI Questions

✔ Generate Reports

✔ View Analytics
        """)

        st.button("🚀 Get Started")

    with right:

        st.success("🤖 AI Powered")

        st.info("🔒 Secure")

        st.warning("⚡ Fast")

    st.divider()

    st.header("✨ Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("📂 Document Upload")

    with c2:
        st.success("🤖 AI Summary")

    with c3:
        st.warning("💬 AI Chat")

    st.divider()

    st.caption("© 2026 IntelliDoc AI")