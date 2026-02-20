from fastapi import FastAPI
from app.models import ConversationRequest

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.post("/chat")
def chat(request: ConversationRequest):
    return {"message": request.conversation}