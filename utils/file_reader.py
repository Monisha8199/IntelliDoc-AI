import PyPDF2
import docx

def extract_text(uploaded_file):
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    elif file_name.endswith(".docx"):
        document = docx.Document(uploaded_file)
        text = ""
        for para in document.paragraphs:
            text += para.text + "\n"
        return text

    elif file_name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        return "Unsupported file format."