def structure_understanding(input_data):

    structured_data = {
        "intent": input_data.get("intent", "query"),
        "sentiment": input_data.get("sentiment", "neutral"),
        "urgency_level": input_data.get("urgency_level", "medium"),
        "product_mentioned":input_data.get("product_mentioned","general")
    }

    return structured_data
       