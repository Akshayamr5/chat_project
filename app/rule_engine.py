def apply_rules(data):

    intent = data.get("intent", "query")
    sentiment = data.get("sentiment", "neutral")
    urgency = data.get("urgency_level", "medium")
    product = data.get("product_mentioned", "general")

    risk_score = 0.0

    if sentiment == "negative":
        risk_score += 0.4

    if intent == "complaint":
        risk_score += 0.3

    if urgency == "high":
        risk_score += 0.12

    if product == "premium plan":
        risk_score += 0.0  

    risk_score = round(min(risk_score, 1), 2)

    if risk_score >= 0.75:
        churn_risk = "high"
    elif risk_score >= 0.4:
        churn_risk = "medium"
    else:
        churn_risk = "low"

    refund_detection = (
        intent == "complaint"
        and sentiment == "negative"
    )

    if churn_risk == "high":
        escalation_routing = "retention_team"
    elif urgency == "high":
        escalation_routing = "priority_support"
    else:
        escalation_routing = "normal_support"

    output = {
        "churn_risk": churn_risk,
        "refund_detection": refund_detection,
        "escalation_routing": escalation_routing,
        "risk_score": risk_score
    }

    return output