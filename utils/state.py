from typing import TypedDict, List

class ThisIsState(TypedDict):
    """
    LangGraph state for state management over the workflow execution.
    """
    user_query: str
    db_schema: List
    sql_query: str
    data: List
    result: str
    