from fastapi import APIRouter
from app.models import ConversationRequest
from app.services.summary import generate_summary

router = APIRouter()

@router.post("/chat")
def chat(request: ConversationRequest):

    summary = generate_summary(request.conversation)

    return {
        "message": request.conversation,
        "summary": summary
    }