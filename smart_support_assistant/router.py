def classify_intent(query: str) -> str:
    q = query.lower()
    if "refund" in q: return "refund"
    if "ship" in q or "delivery" in q: return "shipping"
    if "cancel" in q: return "cancellation"
    if "exchange" in q: return "exchange"
    if "complaint" in q or "legal" in q: return "escalation"
    return "general"

def needs_escalation(query, docs):
    q = query.lower()

    # Escalate only for legal/complaint issues
    if "complaint" in q or "legal" in q or "lawyer" in q:
        return True

    # If no docs found, fallback to general response instead of escalation
    if len(docs) == 0:
        return False

    return False
