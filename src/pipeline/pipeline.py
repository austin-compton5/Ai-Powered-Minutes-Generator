from core import call_api, download, client, template_registry
from prompts import prompts
from minute_models import city_commission_model
from typing import Optional
from dotenv import load_dotenv
from pathlib import Path
import streamlit as stm
import os

templates_dir = Path(__file__).resolve().parents[2] / "templates"
default_template  = "sustainability_commission.html"
default_prompt = prompts.prompt_options["sustainability_commission"]
model = "gemini-2.0-flash"
default_data_model = city_commission_model.MeetingMinutes

dotenv_path = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(dotenv_path)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = stm.secrets.get("GOOGLE_API_KEY", "")

def generate_minutes_from_youtube(youtube_url: str, selected_template: Optional[template_registry.TemplateConfig] = None):

    tpl = getattr(selected_template, "template", default_template)
    mdl_cls = getattr(selected_template, "data_model", default_data_model)
    prmpt = getattr(selected_template, "prompt", default_prompt)

    audio_path = download.download_audio(youtube_url)
    genai_client = client.setup_client(audio_path)
    minutes = call_api.generate_minutes(templates_dir, genai_client, template=tpl, model=model, prompt=prmpt, data_model=mdl_cls)
    return minutes

