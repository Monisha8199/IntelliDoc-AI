import streamlit as st
from models.summarizer import generate_summary
from utils.file_reader import extract_text
from database.history import save_history
from utils.pdf_export import create_pdf
import os
import time


# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Summary",
    page_icon="📄",
    layout="wide"
)



# ---------------------------------------------------
# Dark Blue Theme
# ---------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: #0b1f3a;
}


/* Text */

h1, h2, h3, p, label {
    color: white !important;
}



/* Upload Box */

[data-testid="stFileUploader"] {

    background: #132f52;
    padding: 20px;
    border-radius: 15px;

}



/* Text Area */

.stTextArea textarea {

    background-color: #173b63 !important;
    color: white !important;
    border-radius: 12px;

}



/* Buttons */

.stButton button {

    background: #2563eb;

    color:white;

    border-radius:12px;

    height:45px;

    font-weight:bold;

}



/* Download Button */

.stDownloadButton button {

    background:#1d4ed8;

    color:white;

    border-radius:12px;

    font-weight:bold;

}


</style>
""", unsafe_allow_html=True)



# ---------------------------------------------------
# Header
# ---------------------------------------------------

st.markdown("""
<div style="
background:#102a4c;
padding:35px;
border-radius:20px;
box-shadow:0 8px 25px rgba(0,0,0,0.5);
">

<h1 style="color:white;">
📄 AI Document Summarizer
</h1>

<p style="
color:#cbd5e1;
font-size:18px;
">
Upload a PDF, DOCX, or TXT file and generate an AI summary instantly.
</p>

</div>
""", unsafe_allow_html=True)



st.write("")



# ---------------------------------------------------
# File Upload
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload PDF, DOCX or TXT",
    type=[
        "pdf",
        "docx",
        "txt"
    ]
)



# ---------------------------------------------------
# Generate Summary
# ---------------------------------------------------

if uploaded_file is not None:


    text = extract_text(uploaded_file)



    st.markdown(
        """
        <h3>
        📄 Document Preview
        </h3>
        """,
        unsafe_allow_html=True
    )



    st.text_area(
        "",
        text[:1500],
        height=250
    )



    st.write("")



    if st.button(
        "🚀 Generate AI Summary",
        use_container_width=True
    ):


        start_time = time.time()



        with st.spinner(
            "🤖 AI is generating your summary..."
        ):

            summary = generate_summary(text)



        end_time = time.time()


        total_time = round(
            end_time - start_time,
            2
        )



        st.success(
            "✅ Summary Generated Successfully!"
        )



        # ---------------------------------------------------
        # Summary Display
        # ---------------------------------------------------

        st.markdown("""
        <div style="
        background:#102a4c;
        padding:20px;
        border-radius:20px;
        margin-top:20px;
        ">

        <h3 style="color:white;">
        🤖 AI Summary
        </h3>

        </div>
        """,
        unsafe_allow_html=True)



        st.markdown(
            f"""
            <div style="
            background:#173b63;
            color:white;
            padding:25px;
            border-radius:15px;
            font-size:17px;
            line-height:1.6;
            ">

            {summary}

            </div>
            """,
            unsafe_allow_html=True
        )



        # ---------------------------------------------------
        # Statistics
        # ---------------------------------------------------

        st.write("")


        col1, col2, col3 = st.columns(3)



        with col1:

            st.metric(
                "📝 Summary Words",
                len(summary.split())
            )



        with col2:

            st.metric(
                "📄 Original Words",
                len(text.split())
            )



        with col3:

            st.metric(
                "⏱ Time Taken",
                f"{total_time}s"
            )



        # ---------------------------------------------------
        # Save History
        # ---------------------------------------------------

        save_history(
            "Summary",
            uploaded_file.name,
            summary
        )



        # ---------------------------------------------------
        # PDF Export
        # ---------------------------------------------------

        os.makedirs(
            "exports",
            exist_ok=True
        )



        pdf_path = "exports/summary.pdf"



        create_pdf(
            summary,
            pdf_path
        )



        with open(
            pdf_path,
            "rb"
        ) as pdf:


            st.download_button(
                label="📥 Download Summary PDF",
                data=pdf,
                file_name="summary.pdf",
                mime="application/pdf",
                use_container_width=True
            )



# ---------------------------------------------------
# Footer Tips
# ---------------------------------------------------

st.markdown("---")


st.info(
    "💡 Tip: Upload clear documents for better AI summaries."
)


st.info(
    "📄 Supported formats: PDF, DOCX and TXT."
)


st.info(
    "🔒 Your summary can be downloaded as PDF."
)