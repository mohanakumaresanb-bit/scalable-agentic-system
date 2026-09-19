import re
from datetime import date, timedelta

class SimpleIntentRouter:
    """Deterministic demo router. Replace this with an LLM tool-calling policy in production."""
    def choose(self, message: str, candidates: list[str]):
        m = message.lower()
        if "invoice" in m and "send" in m and "paypal.create_invoice" in candidates:
            amount = float(re.search(r"\$\s*(\d+(?:\.\d+)?)", m).group(1)) if re.search(r"\$\s*(\d+(?:\.\d+)?)", m) else None
            email = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", m)
            return "paypal.create_invoice", {"amount": amount, "email": email.group(0) if email else None}
        if "sales" in m and "paypal.get_sales_report" in candidates:
            today = date.today(); first = today.replace(day=1); last = first - timedelta(days=1)
            start = last.replace(day=1).isoformat(); end = last.isoformat()
            return "paypal.get_sales_report", {"start_date": start, "end_date": end}
        if "dispute" in m and "paypal.get_dispute" in candidates:
            customer = re.search(r"user_[a-z0-9]+", m)
            return "paypal.get_dispute", {"customer_id": customer.group(0) if customer else None}
        if "available" in m or "tools" in m or "status" in m:
            return "system.search", {"query": message}
        return "rag.query", {"query": message}
