from core import call_api, download, client
from prompts import prompts
from minute_models import city_commission_model
from dotenv import load_dotenv
from pathlib import Path
import streamlit as stm
import os

templates_dir = Path(__file__).resolve().parents[2] / "templates"
template  = "sustainability_commission.html"
prompt = prompts.prompt_options["sustainability_commission"]
model = "gemini-2.0-flash"
data_model = city_commission_model.MeetingMinutes

dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = stm.secrets.get("GOOGLE_API_KEY", "")

def generate_minutes_from_youtube(youtube_url):
    audio_path = download.download_audio(youtube_url)
    genai_client = client.setup_client(audio_path)
    minutes = call_api.generate_minutes(templates_dir, genai_client, template=template, model=model, prompt=prompt, data_model=data_model)
    return minutes

