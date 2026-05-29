from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from youtube_agent.main import ingest_video
from orchestrator.graph import build_graph

app = FastAPI(title="Orchestrator Service")

class ProcessRequest(BaseModel):
    youtube_url: str

class RunRequest(BaseModel):
    youtube_url: str
    user_query: str

@app.get("/")
def read_root():
    return {"message": "Orchestrator Service is running"}

@app.post("/process")
def process_video(request: ProcessRequest):
    try:
        result = ingest_video(request.youtube_url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/run")
def run_orchestrator(request: RunRequest):
    try:
        graph = build_graph()
        result_state = graph.invoke({
            "youtube_url": request.youtube_url,
            "user_query": request.user_query,
            "transcript_answer": None,
            "extracted_product": None,
            "recommendations": None,
            "final_response": None
        })
        return {
            "answer": result_state.get("transcript_answer"),
            "recommendations": result_state.get("recommendations", [])
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
