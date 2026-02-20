from fastapi import APIRouter
from app.models import ConversationRequest

router = APIRouter()

@router.post("/chat")
def chat(request: ConversationRequest):
    return {"message": request.conversation}