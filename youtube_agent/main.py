import uuid

from youtube_agent.transcript import (
    fetch_transcript
)

from youtube_agent.embeddings import (
    get_embedding
)

from youtube_agent.pinecone_store import (
    upsert_chunk
)

CHUNK_SIZE = 1000


def chunk_text(text):

    chunks = []

    for i in range(
        0,
        len(text),
        CHUNK_SIZE
    ):

        chunks.append(
            text[i:i + CHUNK_SIZE]
        )

    return chunks


def ingest_video(url):

    transcript = fetch_transcript(
        url
    )

    chunks = chunk_text(
        transcript
    )

    for chunk in chunks:

        embedding = get_embedding(
            chunk
        )

        upsert_chunk(
            str(uuid.uuid4()),
            embedding,
            chunk
        )

    return {
        "status": "success",
        "chunks": len(chunks)
    }