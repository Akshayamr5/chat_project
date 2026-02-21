import os
from openai import OpenAI

# Groq client configuration
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_summary(text):

    if not text:
        return "No conversation provided."

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                "role": "system",
                "content": """
                You are a customer support AI.

                Return output in JSON format:
                {
                "summary": "...",
                "sentiment": "positive | neutral | negative"
                }

                Detect sentiment based on customer emotion.
                """
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        import json

        content = response.choices[0].message.content

        try:
            result = json.loads(content)
            return result
        except:
            return {
                "summary": content,
                "sentiment": "neutral"
            }

    except Exception as e:
        return f"Summary generation failed:{str(e)}"