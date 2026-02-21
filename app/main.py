from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uuid

# Import services
from app.services.summarizer import generate_summary
from app.services.ai_module import analyze_with_ai
from app.services.rule_engine import apply_rules
from app.services.speech_to_text import transcribe_audio


# ---------------------------------------------------
# App Initialization
# ---------------------------------------------------

app = FastAPI(
    title="Business Insight Automation System",
    description="Multimodal Conversation Intelligence Engine",
    version="1.0.0"
)


# ---------------------------------------------------
# Enable CORS
# ---------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------
# Request Model
# ---------------------------------------------------

class ConversationRequest(BaseModel):
    conversation: str


# ---------------------------------------------------
# Health Check
# ---------------------------------------------------

@app.get("/")
def home():
    return {"status": "Customer Intelligence Engine Running"}


# ---------------------------------------------------
# TEXT INPUT ENDPOINT
# ---------------------------------------------------

@app.post("/analyze-text")
def analyze_text(data: ConversationRequest):

    transcript = data.conversation

    # 1️⃣ Generate summary + language detection
    summary_data = generate_summary(transcript)

    # 2️⃣ Extract structured AI intelligence
    ai_data = analyze_with_ai(transcript)

    # 3️⃣ Apply business rules
    rule_data = apply_rules(ai_data)

    # 4️⃣ Merge everything
    return {
        **summary_data,
        **ai_data,
        **rule_data
    }


# ---------------------------------------------------
# AUDIO INPUT ENDPOINT
# ---------------------------------------------------

@app.post("/analyze-audio")
async def analyze_audio(file: UploadFile = File(...)):

    temp_filename = f"temp_{uuid.uuid4()}.wav"

    try:
        contents = await file.read()

        with open(temp_filename, "wb") as f:
            f.write(contents)

        # 1️⃣ Convert speech to text
        transcript = transcribe_audio(temp_filename)

        # 2️⃣ Summary + language
        summary_data = generate_summary(transcript)

        # 3️⃣ AI extraction
        ai_data = analyze_with_ai(transcript)

        # 4️⃣ Rule engine
        rule_data = apply_rules(ai_data)

        return {
            "transcribed_text": transcript,
            **summary_data,
            **ai_data,
            **rule_data
        }

    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)