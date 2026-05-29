import google.generativeai as genai

from shared.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)


def get_embedding(text: str):

    result = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text,
        output_dimensionality=768
    )

    return result["embedding"]
    