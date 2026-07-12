import streamlit as st
from pages.Home import show_home


# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="IntelliDoc AI",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Load CSS ----------------
with open("assets/css/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

show_home()