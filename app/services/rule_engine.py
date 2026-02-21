from app.config.config_loader import load_config


def apply_rules(data):

    # Load client configuration
    config = load_config()
    weights = config["weights"]

    # Extract AI outputs
    intent = data.get("intent", "general_query")
    sentiment = data.get("sentiment", "neutral")
    urgency = data.get("urgency_level", "medium")
    product = data.get("product_mentioned", "not_specified")
    topics = data.get("topics", [])
    entities = data.get("entities", {})

    # --------------------------------
    # Risk Score Calculation
    # --------------------------------

    risk_score = 0.0

    if sentiment == "negative":
        risk_score += weights["negative_sentiment"]

    if intent in ["complaint", "refund_request"]:
        risk_score += weights["complaint_intent"]

    if urgency == "high":
        risk_score += weights["high_urgency"]

    if any(topic in topics for topic in ["subscription_problem", "billing_issue"]):
        risk_score += weights["topic_issue"]

    if product in config["high_value_products"]:
        risk_score += weights["high_value_product"]

    # Cap risk score at 1.0
    risk_score = round(min(risk_score, 1.0), 2)

    # --------------------------------
    # Churn Risk Classification
    # --------------------------------

    if risk_score >= 0.75:
        churn_risk = "high"
    elif risk_score >= 0.4:
        churn_risk = "medium"
    else:
        churn_risk = "low"

    # --------------------------------
    # Refund Detection (Config Driven)
    # --------------------------------

    refund_detection = any(
        trigger in intent.lower() or trigger in " ".join(topics).lower()
        for trigger in config["risk_triggers"]
    )

    # --------------------------------
    # Compliance Violation Detection
    # --------------------------------

    compliance_keywords = [
        "fraud",
        "scam",
        "chargeback",
        "unauthorized",
        "legal action",
        "court",
        "regulator",
        "rbi complaint",
        "ombudsman"
    ]

    combined_text = (
        intent + " " +
        " ".join(topics) + " " +
        str(entities)
    ).lower()

    compliance_violation = any(
        keyword in combined_text
        for keyword in compliance_keywords
    )

    # --------------------------------
    # Escalation Routing Logic
    # --------------------------------

    if compliance_violation:
        escalation_routing = "compliance_team"
    elif churn_risk == "high":
        escalation_routing = "retention_team"
    elif urgency == "high":
        escalation_routing = "priority_support"
    else:
        escalation_routing = "normal_support"

    # --------------------------------
    # Final Output
    # --------------------------------

    return {
        "business_domain": config["business_domain"],
        "churn_risk": churn_risk,
        "refund_detection": refund_detection,
        "compliance_violation": compliance_violation,
        "escalation_routing": escalation_routing,
        "risk_score": risk_score
    }