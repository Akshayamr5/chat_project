def generate_business_output(rule_output):

    if rule_output["churn_risk"] == "high":
        action = "Escalate Immediately"
    elif rule_output["churn_risk"] == "medium":
        action = "Follow-up"
    else:
        action = "Monitor"

    return {
        "churn_risk": rule_output["churn_risk"],
        "refund_detection": rule_output["refund_detection"],
        "escalation_routing": rule_output["escalation_routing"],
        "risk_score": rule_output["risk_score"],
        "recommended_action": action
    }