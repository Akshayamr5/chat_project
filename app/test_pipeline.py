import json
from rule_engine import apply_rules

input_data = {
    "intent": "complaint",
    "sentiment": "negative",
    "urgency_level": "high",
    "product_mentioned": "premium plan"
}

final_output = apply_rules(input_data)

print(json.dumps(final_output, indent=4))