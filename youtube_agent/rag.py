import google.generativeai as genai

from shared.config import GEMINI_API_KEY

from youtube_agent.embeddings import (
    get_embedding
)

from youtube_agent.pinecone_store import (
    query_similar
)

genai.configure(
    api_key=GEMINI_API_KEY
)


def ask_question(question):

    question_embedding = get_embedding(
        question
    )

    matches = query_similar(
        question_embedding
    )

    context = ""

    for match in matches["matches"]:

        context += (
            match["metadata"]["text"]
            + "\n"
        )

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
Context:
{context}

Question:
{question}

Answer the question based on the provided Context. If the Context contains song lyrics, transcripts, or audio text, you may also use your broad knowledge to identify the song title, artist, or provide additional helpful context about the song.
"""

    response = model.generate_content(
        prompt
    )

    return response.text