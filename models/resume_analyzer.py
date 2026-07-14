from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze this resume.

Provide:

1. Resume Score out of 100
2. Strengths
3. Weaknesses
4. Missing Skills
5. Suggestions

Resume:

{text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response.choices[0].message.content