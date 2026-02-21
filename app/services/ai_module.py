import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_with_ai(text: str) -> dict:

    prompt = f"""
You are an enterprise conversation intelligence system.

Analyze the conversation below and return STRICT JSON with EXACTLY these fields:

- sentiment (positive | negative | neutral)
- intent (complaint | refund_request | inquiry | upgrade_request | general_query)
- urgency_level (low | medium | high)
- product_mentioned (subscription | premium plan | basic plan | pro version | not_specified)
- topics (array of clearly identifiable business topics.
  ONLY include a topic if it is explicitly mentioned in the conversation.
  DO NOT assume billing, subscription, refund, or product issues unless directly stated.
  If no clear topic is mentioned, return an empty list [])
- entities (object containing ONLY explicitly mentioned named entities such as product, payment_method, account_id, location.
  If none are present, return empty object {{}})

CRITICAL RULES:
- Do NOT infer hidden meaning.
- Do NOT guess.
- Do NOT assume product or billing unless clearly stated.
- If uncertain, return safe defaults.
- Return ONLY valid JSON.
- No explanation.
- No markdown.

Conversation:
{text}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You return only raw valid JSON. Never add explanation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )

        content = response.choices[0].message.content.strip()

        # Remove accidental markdown formatting
        content = content.replace("```json", "").replace("```", "").strip()

        # Extract JSON safely
        match = re.search(r"\{.*\}", content, re.DOTALL)

        if match:
            parsed = json.loads(match.group())

            # Final safety normalization
            parsed.setdefault("sentiment", "neutral")
            parsed.setdefault("intent", "general_query")
            parsed.setdefault("urgency_level", "low")
            parsed.setdefault("product_mentioned", "not_specified")
            parsed.setdefault("topics", [])
            parsed.setdefault("entities", {})

            return parsed

    except Exception as e:
        print("AI Extraction Error:", str(e))

    # Safe fallback
    return {
        "sentiment": "neutral",
        "intent": "general_query",
        "urgency_level": "low",
        "product_mentioned": "not_specified",
        "topics": [],
        "entities": {}
    }