from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chat_with_document(document_text, question):
    prompt = f"""
You are an AI document assistant.

Document:
{document_text}

User Question:
{question}

Answer the question only using the information in the document.
If the answer is not present, say:
'I couldn't find that information in the document.'
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=1024
    )

    return response.choices[0].message.content