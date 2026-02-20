def generate_summary(text):

    if not text:
        return "No conversation provided."

    # simple basic summary
    sentences = text.split(".")
    summary = ". ".join(sentences[:2])

    return summary.strip()