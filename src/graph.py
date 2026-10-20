from langgraph.graph import StateGraph, END
from typing import TypedDict
from src.agents import (
    study_design_agent,
    sample_size_agent,
    confounding_checker_agent,
    protocol_drafter_agent,
)


class ResearchState(TypedDict):
    research_question: str
    study_design: str
    sample_size: str
    confounders: str
    protocol: str


def build_graph() -> StateGraph:
    graph = StateGraph(ResearchState)

    graph.add_node("study_design", study_design_agent)
    graph.add_node("sample_size", sample_size_agent)
    graph.add_node("confounding_checker", confounding_checker_agent)
    graph.add_node("protocol_drafter", protocol_drafter_agent)

    graph.set_entry_point("study_design")
    graph.add_edge("study_design", "sample_size")
    graph.add_edge("sample_size", "confounding_checker")
    graph.add_edge("confounding_checker", "protocol_drafter")
    graph.add_edge("protocol_drafter", END)

    return graph.compile()