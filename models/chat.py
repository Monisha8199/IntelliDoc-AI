import os
from dotenv import load_dotenv
from google import genai

# Load API Key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("Groq_API_KEY")
)

def chat_with_document(document_text, question):
    if not document_text.strip():
        return "Please upload a document first."

    prompt = f"""
You are an AI assistant.

Document:
{document_text}

Question:
{question}

Answer the question only using the document.
If the answer is not present, say:
'I couldn't find the answer in the document.'
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"