import os
import json
from mistralai.client.sdk import Mistral
from dotenv import load_dotenv

load_dotenv()
client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))

PROMPT = """You are a scam and phishing detection expert. Analyze the following message and return ONLY a valid JSON object with this exact structure, no markdown, no extra text:

{{
  "risk_score": <integer 0-100>,
  "risk_level": "<LOW|MEDIUM|HIGH>",
  "threat_type": "<string>",
  "signals": [
    {{
      "name": "<string>",
      "severity": "<LOW|MEDIUM|HIGH>",
      "evidence": "<string>"
    }}
  ],
  "explanation": "<string>",
  "recommended_action": "<string>"
}}

Message to analyze:
\"\"\"{message}\"\"\"
"""

def analyze_message(content: str) -> dict:
    response = client.chat.complete(
        model="open-mistral-nemo",
        messages=[{"role": "user", "content": PROMPT.format(message=content)}]
    )
    text = response.choices[0].message.content.strip()
    if "```" in text:
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    return json.loads(text.strip())
