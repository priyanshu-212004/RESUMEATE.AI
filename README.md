# RESUMEATE.AI 🚀

**AI-Powered Resume Analyzer & Career Assistant**

RESUMEATE.AI is a smart web application that analyzes resumes using AI and provides actionable insights to improve job readiness. It helps candidates optimize their resumes for ATS systems, identify missing skills, and prepare for interviews.

---

## 🔥 Features

* 📄 Upload Resume (PDF / DOCX / TXT)
* 🎯 Analyze based on target job role
* 📊 ATS Match Score with breakdown
* 🧠 AI-powered skill extraction
* ⚠️ Missing / Weak Skills Detection
* 🛠️ Personalized “What to Fix” Suggestions
* 🧭 Career Roadmap Generation
* 🎤 Interview Questions Generator

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, JavaScript
* **AI Engine:** Groq API (LLaMA 3 Model)
* **File Processing:** PyPDF2, python-docx
* **Environment Management:** python-dotenv

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resumeate-ai.git
cd resumeate-ai
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
python app.py
```

Then open:
👉 http://127.0.0.1:5000
---

## 🚀 Future Enhancements

* User Authentication (Login/Signup)
* Resume History Dashboard
* Downloadable PDF Reports
* Job Description vs Resume Matching
* Cover Letter Generator
* Live Deployment (AWS / Render)

---

## 🧠 How It Works

1. User uploads resume
2. Text is extracted (PDF/DOCX/TXT)
3. AI analyzes resume based on target role
4. Structured JSON response is generated
5. Data is displayed as scores, insights, and suggestions

---

## 🔒 Security Note

Sensitive data like API keys are stored in environment variables (`.env`) and are not exposed in the repository.

---

## 👨‍💻 Author

**Priyanshu**
B.Tech CSE | AI Enthusiast | Developer

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
