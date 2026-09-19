from uuid import uuid4
from app.state import AgentState
from app.router import SimpleIntentRouter
from app.validators import validate
from tools.registry import ToolRegistry
from tools.executor import ToolExecutor

class Agent:
    def __init__(self):
        self.registry = ToolRegistry()
        self.router = SimpleIntentRouter()
        self.executor = ToolExecutor()

    def run(self, message: str):
        state = AgentState(request_id=str(uuid4()), user_message=message)
        state.candidates = self.registry.search(message, top_k=8)
        try:
            tool, args = self.router.choose(message, state.candidates)
            if any(v is None for v in args.values()):
                raise ValueError("Could not extract all required parameters from the request")
            state.selected_tool, state.arguments = tool, args
            spec = self.registry.get(tool)
            # Safety boundary: write operations would normally require a confirmation token.
            if spec.requires_confirmation:
                state.status = "awaiting_confirmation"
                return state, {"message": f"Confirmation required before executing {tool}.", "arguments": args}
            validate(tool, args)
            result = self.executor.run(tool, args)
            state.tool_results.append(result)
            state.status = "completed"
            return state, result
        except Exception as exc:
            state.errors.append(str(exc))
            state.status = "failed"
            return state, {"error": str(exc)}
