from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv
import os
import json
import PyPDF2
import docx

app = Flask(__name__)

# ---------- LOAD ENV ----------
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ---------- READ FILE ----------
def extract_text(file):
    filename = file.filename.lower()

    if filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text

    elif filename.endswith(".docx"):
        doc = docx.Document(file)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

    return ""


# ---------- DEFAULT FALLBACK ----------
def fallback_json():
    return {
        "score": 65,
        "keywords": 60,
        "ats": 58,
        "impact": 55,

        "skills": ["Python", "SQL"],

        "missing_skills": [
            "Communication",
            "Projects",
            "Leadership"
        ],

        "fixes": [
            "Improve bullet points",
            "Use ATS keywords",
            "Add measurable achievements"
        ],

        "questions": [
            "Tell me about yourself",
            "Explain one project from your resume",
            "Why should we hire you?",
            "What are your strengths?"
        ],

        "suggestions": [
            "Improve summary section",
            "Add certifications",
            "Make formatting cleaner"
        ]
    }


# ---------- AI ANALYSIS ----------
def analyze_resume(text, goal):

    prompt = f"""
You are an expert ATS resume analyzer.

Analyze this resume for target role: {goal}

Resume:
{text[:4000]}

Return ONLY valid JSON.
Do not use markdown.
Do not miss any key.

Format:
{{
  "score": 85,
  "keywords": 80,
  "ats": 75,
  "impact": 70,

  "skills": ["Python","SQL","Flask"],

  "missing_skills": [
    "AWS",
    "Docker",
    "Communication"
  ],

  "fixes": [
    "Improve bullet points",
    "Use ATS keywords",
    "Add quantified achievements"
  ],

  "questions": [
    "Tell me about yourself",
    "Explain your main project",
    "Why this role?",
    "How do you solve problems?"
  ],

  "suggestions": [
    "Improve resume summary",
    "Add certifications",
    "Highlight achievements"
  ]
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        raw = response.choices[0].message.content.strip()

        raw = raw.replace("```json", "").replace("```", "").strip()

        start = raw.find("{")
        end = raw.rfind("}") + 1
        raw = raw[start:end]

        data = json.loads(raw)

        result = {
            "score": data.get("score", 0),
            "keywords": data.get("keywords", 0),
            "ats": data.get("ats", 0),
            "impact": data.get("impact", 0),

            "skills": data.get("skills", []),

            "missing_skills": data.get("missing_skills", []),

            "fixes": data.get("fixes", []),

            "questions": data.get("questions", []),

            "suggestions": data.get("suggestions", [])
        }

        return result

    except Exception as e:
        print("AI ERROR:", e)
        return fallback_json()


# ---------- ROUTE ----------
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        file = request.files["file"]
        role = request.form["role"]

        text = extract_text(file)

        if not text.strip():
            return jsonify(fallback_json())

        result = analyze_resume(text, role)

        return jsonify(result)

    return render_template("index.html")


# ---------- RUN ----------
if __name__ == "__main__":
    app.run(debug=True)