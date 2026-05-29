from fastapi import FastAPI

app = FastAPI(title="Product Agent Service")

@app.get("/")
def read_root():
    return {"message": "Product Agent Service is running"}
