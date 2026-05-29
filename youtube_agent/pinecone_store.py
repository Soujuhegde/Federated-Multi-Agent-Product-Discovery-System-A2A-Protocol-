from pinecone import Pinecone

from shared.config import (
    PINECONE_API_KEY,
    PINECONE_INDEX
)

pc = Pinecone(
    api_key=PINECONE_API_KEY
)

index = pc.Index(
    PINECONE_INDEX
)


def upsert_chunk(
    chunk_id,
    embedding,
    text
):

    index.upsert(
        vectors=[
            {
                "id": chunk_id,
                "values": embedding,
                "metadata": {
                    "text": text
                }
            }
        ]
    )


def query_similar(
    embedding,
    top_k=5
):

    result = index.query(
        vector=embedding,
        top_k=top_k,
        include_metadata=True
    )

    return result