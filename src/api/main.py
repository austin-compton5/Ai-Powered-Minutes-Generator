from fastapi import FastAPI
from pipeline import pipeline
from models import MinutesRequest, MinutesResponse

app = FastAPI()

@app.post("/generate/{youtube_link}", response_model=MinutesResponse)
async def generate_minutes(response : MinutesResponse):
    return pipeline.generate_minutes_from_youtube(response.youtube_link)