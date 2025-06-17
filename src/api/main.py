from fastapi import FastAPI, HTTPException
from pipeline import pipeline
from pydantic import BaseModel

app = FastAPI()

class MinutesResponse(BaseModel):
    html: str

class MinutesRequest(BaseModel):
    youtube_link: str 

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.post("/generate", response_model=MinutesResponse)
async def generate_minutes(request : MinutesRequest):
    try:
        html = pipeline.generate_minutes_from_youtube(request.youtube_link)
        return {"html": html}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



