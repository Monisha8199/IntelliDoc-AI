import streamlit as st
from database.history import get_history

st.set_page_config(page_title="History", page_icon="🗂️")

st.title("🗂️ Document History")

history = get_history()

if history:

    for item in history:

        st.subheader(item[1])

        st.write("📄 File:", item[2])

        st.write(item[3])

        st.divider()

else:

    st.info("No history available.")