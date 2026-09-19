import sys
sys.path.insert(0, ".")
from app.agent import Agent

def test_dispute():
    state, result = Agent().run("Is there a dispute open from user_123?")
    assert state.status == "completed"
    assert result["open"] is True

def test_sales():
    state, result = Agent().run("What was my total sales volume last month?")
    assert state.status == "completed"
    assert result["total_sales_volume"] > 0

def test_invalid_email():
    state, result = Agent().run("Send an invoice for $50 to bad-email")
    assert state.status in {"failed", "awaiting_confirmation"}
