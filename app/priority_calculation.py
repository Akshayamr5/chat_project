def calculate_priority(rule_output):

    risk_score = rule_output["risk_score"]

    priority_score = round(risk_score * 10)

    return priority_score