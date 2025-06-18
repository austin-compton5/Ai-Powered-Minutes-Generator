from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pipeline import pipeline
from pathlib import Path
from typing import Optional
from pydantic import BaseModel
from core import template_registry

app = FastAPI(title="Civic Meeting Minutes Generator",  version="1.0.0") 

class MinutesResponse(BaseModel):
    html: str

class MinutesRequest(BaseModel):
    youtube_link: str 
    selected_template: Optional[str]

@app.get("/")
async def health_check():
    return {"status": "ok"}

@app.get("/templates")
async def get_templates():
    return {"available_templates" : list(template_registry.TEMPLATE_REGISTRY.keys())}

@app.get("/example") 
async def get_example():
    return FileResponse(
        Path(__file__).parent / "example_data" / "example.json",
        media_type="application/json"
    )

@app.post("/generate", response_model=MinutesResponse)
async def generate_minutes(request : MinutesRequest):
    selected_template = None 

    if request.selected_template:
        selected_template = template_registry.TEMPLATE_REGISTRY[request.selected_template]
        if selected_template is None:
            raise HTTPException(
                status_code=400,
                detail=f"Template '{request.selected_template}' not found. Using no name will apply defaults."
            )
        
    try:
        html = pipeline.generate_minutes_from_youtube(request.youtube_link, selected_template)
        return {"html": html}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



