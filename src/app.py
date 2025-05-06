from minutegenerator import generate_minutes
from prompts import prompts
from data_models import city_commission_model
from dotenv import load_dotenv
from pathlib import Path
import os


script_dir = os.path.dirname(__file__)
templates_dir = os.path.join(script_dir, "..", "templates")

template  = "sustainability_commission.html"
prompt = prompts.prompt_options["sustainability_commission"]
model = "gemini-2.0-flash"
data_model = city_commission_model.MeetingMinutes

dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path)


minutes = generate_minutes.generate_minutes(templates_dir, template, model, prompt, data_model)

with open("meeting_minutes.html", "w", encoding="utf-8") as f:
    f.write(minutes)

    print("Meeting minutes HTML generated successfully.")

