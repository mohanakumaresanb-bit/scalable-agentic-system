from app.agent import Agent

if __name__ == "__main__":
    agent = Agent()
    examples = [
        "Send an invoice for $50 to customer@example.com",
        "What was my total sales volume last month?",
        "Is there a dispute open from user_123?",
        "What tools are available for managing invoices?",
        "How do PayPal invoices work?",
    ]
    for q in examples:
        state, result = agent.run(q)
        print("\nUSER:", q)
        print("CANDIDATES:", state.candidates)
        print("STATUS:", state.status)
        print("RESULT:", result)
