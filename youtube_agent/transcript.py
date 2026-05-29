from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs


def get_video_id(url: str):

    parsed = urlparse(url)

    if parsed.netloc == "youtu.be":

        return parsed.path.lstrip("/")

    query_params = parse_qs(parsed.query)

    if "v" in query_params:

        return query_params["v"][0]

    return parsed.path.lstrip("/")


def fetch_transcript(url: str):

    video_id = get_video_id(url)

    transcript = YouTubeTranscriptApi().fetch(video_id)

    text = " ".join(
        chunk.text if hasattr(chunk, "text") else chunk["text"]
        for chunk in transcript
    )

    return text