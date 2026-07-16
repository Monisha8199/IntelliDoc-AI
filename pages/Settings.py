import streamlit as st

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️"
)

st.title("⚙️ Settings")

st.subheader("Theme")
theme = st.selectbox(
    "Choose Theme",
    ["Light", "Dark"]
)

st.subheader("Language")
language = st.selectbox(
    "Choose Language",
    ["English", "Tamil", "Hindi"]
)

st.subheader("Notifications")
notifications = st.checkbox("Enable Notifications")

st.subheader("About")

st.info("""
IntelliDoc-AI

Version: 1.0

Developer: Monisha S

Built using:
• Python
• Streamlit
• Google Gemini AI
""")

if st.button("Save Settings"):
    st.success("✅ Settings Saved Successfully!")