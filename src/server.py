from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from minutes import generate_minutes_from_youtube
from helper_functions import download 

app = FastAPI()

@app.get("/")
def home():
    return HTMLResponse("""
        <form action="/generate" method="post">
            <input name="youtube_url" placeholder="Paste YouTube URL">
            <button type="submit">Generate Minutes</button>
        </form>
    """)

@app.post("/generate")
def generate(youtube_url: str = Form(...)):
    audio_path = download.download_audio(youtube_url) 
    html_output = generate_minutes_from_youtube(audio_path)
    return HTMLResponse(html_output)