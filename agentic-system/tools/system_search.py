from .registry import TOOLS

def system_search(query: str, request_status: dict | None = None):
    q = query.lower()
    if "status" in q and request_status:
        return {"request_status": request_status}
    matches = []
    for t in TOOLS:
        text = f"{t.name} {t.category} {t.description}".lower()
        if any(token in text for token in q.split()):
            matches.append(t.name)
    return {"matching_tools": matches}
