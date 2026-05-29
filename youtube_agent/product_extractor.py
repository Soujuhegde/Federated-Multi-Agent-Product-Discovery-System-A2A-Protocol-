import json

import google.generativeai as genai

from shared.prompts import (
    PRODUCT_EXTRACTION_PROMPT
)

from shared.config import GEMINI_API_KEY

genai.configure(
    api_key=GEMINI_API_KEY
)


def extract_product(text):

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    response = model.generate_content(
        PRODUCT_EXTRACTION_PROMPT +
        "\n\n" +
        text[:5000]
    )

    try:
        return json.loads(
            response.text
        )

    except Exception:

        return {
            "error": response.text
        }