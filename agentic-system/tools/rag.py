DOCS = [
    ("PayPal invoices", "Invoices can be created with a recipient email and amount. A created invoice can then be sent."),
    ("PayPal disputes", "Dispute records contain an open/closed status and a dispute identifier."),
    ("PayPal reports", "Sales reports accept a start date and end date and return sales volume."),
]

def rag_query(query: str):
    q = query.lower()
    hits = [(title, text) for title, text in DOCS if any(w in (title + " " + text).lower() for w in q.split())]
    if not hits:
        hits = DOCS[:1]
    return {"sources": [h[0] for h in hits], "context": " ".join(h[1] for h in hits)}
