from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class GraphState(TypedDict):
    """
    LangGraph state for state management over the workflow execution.
    """
    messages: Annotated[list[BaseMessage], add_messages]
