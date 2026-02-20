from pydantic import BaseModel

class ConversationRequest(BaseModel):
    conversation: str