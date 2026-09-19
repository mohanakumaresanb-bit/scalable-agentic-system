import re

def validate(tool_name: str, args: dict):
    required = {
        "paypal.create_invoice": {"amount", "email"},
        "paypal.send_invoice": {"invoice_id"},
        "paypal.get_sales_report": {"start_date", "end_date"},
        "paypal.get_dispute": {"customer_id"},
        "rag.query": {"query"},
        "system.search": {"query"},
    }[tool_name]
    missing = required - set(args)
    if missing:
        raise ValueError(f"missing required parameters: {sorted(missing)}")
    if "amount" in args and float(args["amount"]) <= 0:
        raise ValueError("amount must be positive")
    if "email" in args and not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", args["email"]):
        raise ValueError("invalid email")
