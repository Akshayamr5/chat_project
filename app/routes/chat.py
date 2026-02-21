from fastapi import APIRouter
from pydantic import BaseModel

from app.services.summary import generate_summary
from app.services.rule_engine import apply_rules

router = APIRouter()


# request model
class ConversationRequest(BaseModel):
    conversation: str


@router.post("/chat")
def chat(request: ConversationRequest):

    # STEP 1 — AI summary + sentiment
    analysis = generate_summary(request.conversation)

    # STEP 2 — Send structured data to rule engine
    rule_output = apply_rules({
        "sentiment": analysis.get("sentiment", "neutral"),
        "intent": analysis.get("intent", "query"),
        "urgency_level": analysis.get("urgency_level", "medium"),
        "product_mentioned": analysis.get("product_mentioned", "general")
    })

    # STEP 3 — Final combined output
    return {
        "message": request.conversation,
        "summary": analysis.get("summary"),
        "sentiment": analysis.get("sentiment"),
        "rule_output": rule_output
    }