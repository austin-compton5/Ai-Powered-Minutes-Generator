from minutegenerator import generate_minutes
from dotenv import load_dotenv
from pathlib import Path
import sys 
import os


script_dir = os.path.dirname(__file__)
templates_path = os.path.join(script_dir, "..", "templates")

dotenv_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path)



minutes = generate_minutes.generate_minutes(templates_path, "gemini-2.0-flash")

with open("meeting_minutes.html", "w", encoding="utf-8") as f:
    f.write(minutes)

    print("Meeting minutes HTML generated successfully.")

