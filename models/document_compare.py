from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def compare_documents(text1, text2):

    prompt = f"""
Compare these two documents.

Provide:

1. Similarities
2. Differences
3. Key points unique to Document 1
4. Key points unique to Document 2
5. Overall conclusion

Document 1:
{text1}

Document 2:
{text2}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],
        temperature=0.3,
        max_tokens=1800
    )

    return response.choices[0].message.content