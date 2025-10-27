from utils.nodes import fetch_context, generate_sql_query, execute_sql_query, present_data
from utils.state import ThisIsState
from langgraph.graph import StateGraph, START, END

graph = StateGraph(ThisIsState)

graph.add_node("context", fetch_context)
graph.add_node("query_generation", generate_sql_query)
graph.add_node("query_execution", execute_sql_query)
graph.add_node("data_representation", present_data)

graph.add_edge(START, "context")
graph.add_edge("context", "query_generation")
graph.add_edge("query_generation", "query_execution")
graph.add_edge("query_execution", "data_representation")
graph.add_edge("data_representation", END)

workflow = graph.compile()
