from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_resume(text, goal):
    prompt = f"""
You are an expert resume analyzer.

Analyze this resume for the target role: {goal}

Resume:
{text[:4000]}

Return ONLY valid JSON.
No explanation. No markdown.

Format:
{{
  "score": 85,
  "keywords": 80,
  "ats": 75,
  "impact": 70,
  "missing_skills": ["Flask", "AWS"],
  "suggestions": ["Improve bullet points", "Add metrics"]
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        raw = response.choices[0].message.content.strip()

        raw = raw.replace("```json", "").replace("```", "").strip()

        start = raw.find("{")
        end = raw.rfind("}") + 1
        raw = raw[start:end]

        return json.loads(raw)

    except Exception as e:
        print("AI ERROR:", str(e))

        return {
            "score": 65,
            "skills": ["Python"],
            "missing_skills": ["Communication", "Projects"],
            "roadmap": ["Build Projects", "Improve Resume", "Practice Interview"]
        }