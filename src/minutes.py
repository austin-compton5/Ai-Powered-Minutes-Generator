from helper_functions import call_api, client, parsejson, download
from render import render
import io
from prompts import prompts
from data_models import city_commission_model
from dotenv import load_dotenv
from pathlib import Path
import streamlit as stm
import os
from weasyprint import HTML

script_dir = os.path.dirname(__file__)
templates_dir = os.path.join(script_dir, "..", "templates")

template  = "sustainability_commission.html"
prompt = prompts.prompt_options["sustainability_commission"]
model = "gemini-2.0-flash"
data_model = city_commission_model.MeetingMinutes

dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path)

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = stm.secrets.get("GOOGLE_API_KEY", "")

def generate_minutes(templates_dir, client, template, model, prompt, data_model):

    response = call_api.call_gemini(
        client["client"], 
        model, 
        client["video_file"], 
        prompt,
        data_model)
    print(response)
    
    parsed_json = parsejson.parse_json(response)
    rendered_html = render.render_html(templates_dir, template, parsed_json)

    return rendered_html

def generate_minutes_from_youtube(youtube_url):

    audio_path = download.download_audio(youtube_url)
    genai_client = client.setup_client(audio_path)
    minutes = generate_minutes(templates_dir, genai_client, template=template, model=model, prompt=prompt, data_model=data_model)
    return minutes


def convert_html_to_pdf(html_string: str) -> bytes:
    pdf_io = io.BytesIO()
    HTML(string=html_string).write_pdf(target=pdf_io)
    return pdf_io.getvalue()
