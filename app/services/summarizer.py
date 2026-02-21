import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_summary(text: str) -> dict:

    if not text:
        return {
            "summary": "No conversation provided.",
            "detected_language": "Unknown"
        }

    prompt = f"""
You are a multilingual customer support AI.

Return STRICT JSON with:
- summary (2-3 sentence business summary)
- detected_language (English, Hindi, Tamil, Spanish, etc.)

Conversation:
{text}

Return only valid JSON.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Return strictly valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        if content.startswith("```"):
            content = content.replace("```json", "").replace("```", "").strip()

        match = re.search(r"\{.*\}", content, re.DOTALL)

        if match:
            return json.loads(match.group())

    except Exception as e:
        print("Summary Error:", str(e))

    return {
        "summary": "Summary generation failed.",
        "detected_language": "Unknown"
    }