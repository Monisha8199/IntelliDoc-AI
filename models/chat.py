import os
from dotenv import load_dotenv
from groq import Groq

# Load API Key
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
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
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=1500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"