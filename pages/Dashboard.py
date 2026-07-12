import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

st.title("📊 IntelliDoc AI Dashboard")

st.markdown("### Welcome to IntelliDoc AI 👋")
st.write("Manage your AI-powered document analysis from one place.")

st.divider()

# Feature Cards
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📂 Upload Documents")

with col2:
    st.success("🤖 AI Summary")

with col3:
    st.warning("💬 AI Chat")

st.divider()

# Statistics
st.subheader("📈 Quick Statistics")

c1, c2, c3 = st.columns(3)

c1.metric("Documents", "0")
c2.metric("Summaries", "0")
c3.metric("Reports", "0")

st.divider()

# Recent Activity
st.subheader("📋 Recent Activity")
st.write("No recent activity available.")

st.divider()

st.caption("© 2026 IntelliDoc AI")