from fastapi import APIRouter
from app.models import ConversationRequest
from app.services.summary import generate_summary
from app.services.rule_engine import apply_rules

router = APIRouter()

@router.post("/chat")
def chat(request: ConversationRequest):

    analysis = generate_summary(request.conversation)
    rule_output = apply_rules({
    "sentiment": analysis["sentiment"],
    "intent": "complaint",
    "urgency_level": "high",
    "product_mentioned": "premium plan"
})

    return {
        "message": request.conversation,
        "summary": analysis["summary"],
        "sentiment":analysis["sentiment"],
        "rule_output":rule_output
    }