from dataclasses import dataclass, field
import re

@dataclass
class ToolSpec:
    name: str
    service: str
    description: str
    category: str
    required_parameters: list[str] = field(default_factory=list)
    risk_level: str = "read"
    requires_confirmation: bool = False
    version: str = "v1"

TOOLS = [
    ToolSpec("paypal.create_invoice", "paypal", "Create an invoice for a customer with amount and recipient email.", "invoices", ["amount", "email"], "write", True),
    ToolSpec("paypal.send_invoice", "paypal", "Send an existing invoice to its recipient.", "invoices", ["invoice_id"], "write", True),
    ToolSpec("paypal.get_sales_report", "paypal", "Retrieve sales volume for a date range.", "reports", ["start_date", "end_date"]),
    ToolSpec("paypal.get_dispute", "paypal", "Retrieve an open dispute for a customer reference.", "disputes", ["customer_id"]),
    ToolSpec("rag.query", "internal", "Retrieve product and API documentation from the knowledge base.", "knowledge", ["query"]),
    ToolSpec("system.search", "internal", "Search tools, capabilities, and request status in the system.", "system", ["query"]),
]

class ToolRegistry:
    def __init__(self, tools=TOOLS):
        self.tools = {t.name: t for t in tools}

    def search(self, query: str, top_k: int = 8) -> list[str]:
        q = set(re.findall(r"[a-z0-9_]+", query.lower()))
        scored = []
        for t in self.tools.values():
            text = f"{t.name} {t.service} {t.category} {t.description}".lower()
            words = set(re.findall(r"[a-z0-9_]+", text))
            score = len(q & words)
            # Lightweight intent aliases; production can add embeddings + reranking.
            aliases = {
                "invoice": "invoices", "invoicing": "invoices", "dispute": "disputes",
                "sales": "reports", "revenue": "reports", "documentation": "knowledge",
                "available": "system", "status": "system"
            }
            for token in q:
                if aliases.get(token) == t.category:
                    score += 2
            if score:
                scored.append((score, t.name))
        scored.sort(reverse=True)
        return [name for _, name in scored[:top_k]]

    def get(self, name: str) -> ToolSpec:
        return self.tools[name]
