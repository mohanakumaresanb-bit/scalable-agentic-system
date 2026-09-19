from datetime import date

class MockPayPalAPI:
    def __init__(self):
        self.invoices = {}
        self.disputes = {"user_123": {"open": True, "id": "DSP-1001", "amount": 35.0}}
        self.sales = 12500.50
        self._counter = 0

    def create_invoice(self, amount: float, email: str):
        self._counter += 1
        invoice_id = f"INV-{1000 + self._counter}"
        self.invoices[invoice_id] = {"id": invoice_id, "amount": amount, "email": email, "status": "DRAFT"}
        return self.invoices[invoice_id]

    def send_invoice(self, invoice_id: str):
        if invoice_id not in self.invoices:
            raise ValueError("invoice not found")
        self.invoices[invoice_id]["status"] = "SENT"
        return self.invoices[invoice_id]

    def get_sales_report(self, start_date: str, end_date: str):
        return {"start_date": start_date, "end_date": end_date, "total_sales_volume": self.sales, "currency": "USD"}

    def get_dispute(self, customer_id: str):
        return self.disputes.get(customer_id, {"open": False, "customer_id": customer_id})
