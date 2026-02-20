def generate_summary(text):
    """
    Temporary basic summary.
    Later we will replace this with AI.
    """

    if not text:
        return "No conversation provided."

    # simple short summary
    if len(text) <= 80:
        return text

    return text[:80] + "..."