import json, time, os
from google import genai

from google.genai import types
from pydantic import BaseModel
from typing import Optional

# load environment variables
from dotenv import load_dotenv
load_dotenv()

# set up gemini
client = genai.Client()
model = "gemini-2.0-flash"

try:
    print('uploading')
    video_file = client.files.upload(file='files/sustainability_commission.mp3')
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
class Comment(BaseModel):
    Commissioner_speaking: str
    comment: str
    topic: str

class RollCall(BaseModel):
    rollcall: list[str]

extract_rollcall_from_video = """
Please return a list of all Names of Commissioners that are present at the meeting. The best way to find this information 
"""
extract_notes_from_video = """
"Please summarize the key points from this formal commission meeting. Include decisions made, important discussions, action items, and any relevant details about the participants and topics discussed. Focus on clarity, conciseness, and maintaining the formal tone of the meeting."
"""

# count the tokens in the prompt and file
print(client.models.count_tokens(model=model, contents=[video_file, extract_notes_from_video ]))

rollcall = client.models.generate_content(
    model=model, 
    contents = [video_file, extract_rollcall_from_video],
    config = types.GenerateContentConfig(
        response_mime_type="application/json", response_schema= RollCall
    )
)
# send the prompt and file to gemini
result = client.models.generate_content(
            model=model,
            contents=[video_file, extract_notes_from_video ], 
            config=types.GenerateContentConfig(
                response_mime_type="application/json", response_schema=list[Comment]
            )
        )

print(json.loads(rollcall.text))
print(json.loads(result.text))
