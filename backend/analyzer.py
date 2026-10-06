import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

PROMPT = """
You are a scam and phishing detection expert. Analyze the following message and return ONLY a valid JSON object with this exact structure:

{
  "risk_score": <integer 0-100>,
  "risk_level": <"LOW" | "MEDIUM" | "HIGH">,
  "threat_type": <string>,
  "signals": [
    {
      "name": <string>,
      "severity": <"LOW" | "MEDIUM" | "HIGH">,
      "evidence": <string>
    }
  ],
  "explanation": <string>,
  "recommended_action": <string>
}

Message to analyze:
\"\"\"{message}\"\"\"
"""

def analyze_message(content: str) -> dict:
    response = model.generate_content(PROMPT.format(message=content))
    text = response.text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(text)
