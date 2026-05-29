from youtube_agent.transcript import fetch_transcript
from youtube_agent.product_extractor import extract_product

from product_agent.product_api import (
    recommend_similar
)

from youtube_agent.rag import ask_question


def youtube_agent_node(state):

    answer = ask_question(
        state["user_query"]
    )

    state["transcript_answer"] = answer

    return state


def product_extraction_node(state):

    transcript = fetch_transcript(
        state["youtube_url"]
    )

    product = extract_product(
        transcript
    )

    state["extracted_product"] = product

    return state


def recommendation_node(state):

    product = state["extracted_product"]

    if not product:

        state["recommendations"] = []

        return state

    category = product.get(
        "category",
        "Smartphone"
    )

    recommendations = recommend_similar(
        category
    )

    state["recommendations"] = recommendations

    return state