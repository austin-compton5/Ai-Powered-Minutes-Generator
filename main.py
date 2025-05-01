import json, time, os
import sys 
from google import genai

from google.genai import types
from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime

from jinja2 import Environment, FileSystemLoader

# load environment variables
from dotenv import load_dotenv
load_dotenv()

# set up gemini
client = genai.Client()
model = "gemini-2.0-flash"

youtube_file_path = sys.argv[1]
print(youtube_file_path)

#set up ninja2html generation 
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("minutes_template.html")

if len(sys.argv) < 2:
    print("Usage: Please provdide a youtube link to the commmission meeting. ")

try:
    print('uploading: this may take a few minutes')
    video_file = client.files.upload(file=youtube_file_path)
    print("File uploaded successfully")
except Exception as e:
    print(f"Error during file upload: {e}")
    
while video_file.state.name == "PROCESSING":
    print("processing video...")
    time.sleep(5)
    print("video file name:")
    print(video_file.name)
    video_file = client.files.get(name=video_file.name)

# set up pydantic models for companies and themes

class SpeakerComment(BaseModel):
    speaker: str
    comment: str
    timestamp: Optional[str] = None  # Optional time marker from audio

class RollCall(BaseModel):
    present: List[str]
    absent: List[str]

class ApprovalOfMinutes(BaseModel):
    referenced_meeting_date: datetime
    moved_by: str
    seconded_by: str
    ayes: List[str]

class AgendaItem(BaseModel):
    item_number: int
    title: str
    type: Literal["Action", "Report", "Oral Communication", "Update", "Other"]
    presenter: Optional[str]
    summary: Optional[str]
    commissioner_comments: List[SpeakerComment]

class MeetingMinutes(BaseModel):
    meeting_date: datetime
    start_time: str
    end_time: str
    roll_call: RollCall
    pledge_of_allegiance: bool
    land_acknowledgement: bool
    agenda_posted_date: Optional[datetime]

    approval_of_minutes: Optional[ApprovalOfMinutes]
    general_commissioner_comments: List[SpeakerComment]  # e.g. comments during Item 3
    agenda_items: List[AgendaItem]
    oral_communications: List[SpeakerComment]  # Item 4 speakers not tied to specific topics
    adjournment_moved_by: str
    adjournment_seconded_by: str

def json_serial(obj):

    if isinstance(obj, datetime):
        # Convert datetime objects to ISO 8601 strings
        return obj.isoformat()
    # If the object is of another type not handled here, raise the default error
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


generate_minutes= """
Generate complete and structured meeting minutes using the provided schema, capturing each agenda item and commissioner comment in full with emphasis on meaning and key points, grouping them correctly and in order, covering the entire meeting from start to adjournment without omitting or prematurely stopping, and avoiding word-for-word transcription unless necessary for clarity.
"""

# count the tokens in the prompt and file
print(client.models.count_tokens(model=model, contents=[video_file, generate_minutes ]))


# send the prompt and file to gemini
result = client.models.generate_content(
            model=model,
            contents=[video_file, generate_minutes], 
            config=types.GenerateContentConfig(
                response_mime_type="application/json", response_schema=MeetingMinutes
            )
        )


parsed_meeting = result.parsed 

meeting_dict = parsed_meeting.model_dump() 

with open("raw_output_debug.json", "w", encoding="utf-8") as f:
    json.dump(meeting_dict, f, indent=4, default=json_serial)

# Render with Jinja2
env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("minutes_template.html")

# Render the template, passing the Python dictionary
# Jinja2 can now access meeting_dict['meeting_date'] or meeting_dict.meeting_date
rendered_html = template.render(meeting=meeting_dict)

with open("meeting_minutes.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("Meeting minutes HTML generated successfully.")