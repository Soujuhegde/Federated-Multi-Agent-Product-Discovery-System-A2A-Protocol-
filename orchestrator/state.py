from typing import TypedDict, Optional


class AgentState(TypedDict):
    youtube_url: str
    user_query: str

    transcript_answer: Optional[str]

    extracted_product: Optional[dict]

    recommendations: Optional[list]

    final_response: Optional[dict]