from tools.paypal.mock_api import MockPayPalAPI
from tools.rag import rag_query
from tools.system_search import system_search

class ToolExecutor:
    def __init__(self):
        self.paypal = MockPayPalAPI()

    def run(self, tool_name: str, args: dict):
        if tool_name == "paypal.create_invoice": return self.paypal.create_invoice(**args)
        if tool_name == "paypal.send_invoice": return self.paypal.send_invoice(**args)
        if tool_name == "paypal.get_sales_report": return self.paypal.get_sales_report(**args)
        if tool_name == "paypal.get_dispute": return self.paypal.get_dispute(**args)
        if tool_name == "rag.query": return rag_query(**args)
        if tool_name == "system.search": return system_search(**args)
        raise ValueError(f"Unknown tool: {tool_name}")
