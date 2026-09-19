from dataclasses import dataclass, field
from typing import Any

@dataclass
class AgentState:
    request_id: str
    user_message: str
    candidates: list[str] = field(default_factory=list)
    selected_tool: str | None = None
    arguments: dict[str, Any] = field(default_factory=dict)
    tool_results: list[Any] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    status: str = "running"
