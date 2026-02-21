# 🚀 Business Insight Automation System

Multimodal Enterprise Conversation Intelligence Engine

---

## 📌 Overview

This system analyzes customer conversations (Text or Audio) and generates structured business intelligence including:

- Sentiment
- Intent
- Urgency
- Topics
- Named Entities
- Risk Score
- Churn Risk Classification
- Escalation Routing
- Compliance Detection

---

## 🏗 Architecture

User Input (Text / Audio)  
↓  
Speech-to-Text (Whisper - Local)  
↓  
Summarization + Language Detection (Groq LLM)  
↓  
AI Intelligence Extractor (Groq LLM)  
↓  
Rule Engine (Config-Driven Risk Scoring)  
↓  
Final Structured JSON Output  

---

## 🛠 Tech Stack

Backend:
- FastAPI
- Groq LLM (Llama Models)
- OpenAI Whisper (Local Speech-to-Text)
- Python 3.12

Frontend:
- HTML
- CSS
- JavaScript (Fetch API)

Audio Processing:
- FFmpeg

---

## 📂 Project Structure
# 🚀 Business Insight Automation System

Multimodal Enterprise Conversation Intelligence Engine

---

## 📌 Overview

This system analyzes customer conversations (Text or Audio) and generates structured business intelligence including:

- Sentiment
- Intent
- Urgency
- Topics
- Named Entities
- Risk Score
- Churn Risk Classification
- Escalation Routing
- Compliance Detection

---

## 🏗 Architecture

User Input (Text / Audio)  
↓  
Speech-to-Text (Whisper - Local)  
↓  
Summarization + Language Detection (Groq LLM)  
↓  
AI Intelligence Extractor (Groq LLM)  
↓  
Rule Engine (Config-Driven Risk Scoring)  
↓  
Final Structured JSON Output  

---

## 🛠 Tech Stack

Backend:
- FastAPI
- Groq LLM (Llama Models)
- OpenAI Whisper (Local Speech-to-Text)
- Python 3.12

Frontend:
- HTML
- CSS
- JavaScript (Fetch API)

Audio Processing:
- FFmpeg

---

## 📂 Project Structure
app/
├── main.py
├── services/
│ ├── ai_module.py
│ ├── summarizer.py
│ ├── rule_engine.py
│ ├── speech_to_text.py
│ └── config_loader.py
└── config/
└── client_config.json

---

## ⚙️ Configuration Driven Design

Client configuration is externalized in:

---

## ⚙️ Configuration Driven Design

Client configuration is externalized in:
app/config/client_config.json

Supports:
- Business Domain
- Products
- Risk Triggers
- Risk Weights
- High Value Products

No code changes required to adapt to a new industry.

---

## 📊 Risk Score Calculation

Risk score is computed using weighted scoring:

Risk = Sentiment + Intent + Urgency + Topic + Product Weight

Score Range: 0 to 1

Churn Classification:
- ≥ 0.75 → High
- ≥ 0.4 → Medium
- < 0.4 → Low

---

## ▶ How to Run

### 1️⃣ Activate Virtual Environment

Supports:
- Business Domain
- Products
- Risk Triggers
- Risk Weights
- High Value Products

No code changes required to adapt to a new industry.

---

## 📊 Risk Score Calculation

Risk score is computed using weighted scoring:

Risk = Sentiment + Intent + Urgency + Topic + Product Weight

Score Range: 0 to 1

Churn Classification:
- ≥ 0.75 → High
- ≥ 0.4 → Medium
- < 0.4 → Low

---

## ▶ How to Run

### 1️⃣ Activate Virtual Environment
venv\Scripts\activate

### 2️⃣ Run Backend

uvicorn app.main:app --reload

Backend runs on:

http://127.0.0.1:8000


### 3️⃣ Run Frontend

Use VS Code Live Server or open HTML file.

---

## 🌍 Features

✔ Multilingual Support  
✔ Audio + Text Input  
✔ AI-Based Extraction  
✔ Configurable Rule Engine  
✔ Enterprise Risk Scoring  
✔ Escalation Classification  

---

## 📌 Sample Output

```json
{
  "summary": "...",
  "detected_language": "English",
  "sentiment": "negative",
  "intent": "refund_request",
  "urgency_level": "high",
  "product_mentioned": "premium plan",
  "churn_risk": "high",
  "risk_score": 0.9
}

👨‍💻 Authors

Hackathon Project Submission
Enterprise Conversation Intelligence System


---

# ✅ STEP 4 — Save File

Press:


---

# ✅ STEP 4 — Save File

Press:

Ctrl + S


---

# ✅ STEP 5 — Push to GitHub (If Needed)

If using Git:

git add README.md
git commit -m "Added README documentation"
git push


---

# 🎯 Why README Is Important

Judges check:

- Architecture clarity
- Configurable design
- Risk logic explanation
- Tech stack
- How to run

You now have all of that.

---

If you want, I can now:

- 🔥 Make a more professional README
- 🎨 Add badges and formatting
- 📊 Add diagrams
- 🧠 Prepare demo explanation
- 🏆 Prepare hackathon presentation script

Just tell me what level you want.