from langgraph.graph import (
    StateGraph,
    END
)

from orchestrator.state import (
    AgentState
)

from orchestrator.router import (
    youtube_agent_node,
    product_extraction_node,
    recommendation_node
)


def build_graph():

    workflow = StateGraph(
        AgentState
    )

    workflow.add_node(
        "youtube_agent",
        youtube_agent_node
    )

    workflow.add_node(
        "extract_product",
        product_extraction_node
    )

    workflow.add_node(
        "recommend",
        recommendation_node
    )

    workflow.set_entry_point(
        "youtube_agent"
    )

    workflow.add_edge(
        "youtube_agent",
        "extract_product"
    )

    workflow.add_edge(
        "extract_product",
        "recommend"
    )

    workflow.add_edge(
        "recommend",
        END
    )

    return workflow.compile()