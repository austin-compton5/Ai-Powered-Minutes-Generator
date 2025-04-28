import json, time, os
import sys 
from google import genai

from google.genai import types
from pydantic import BaseModel

# load environment variables
from dotenv import load_dotenv
load_dotenv()

# set up gemini
client = genai.Client()
model = "gemini-2.0-flash"

youtube_file_path = sys.argv[1]
print(youtube_file_path)
if len(sys.argv) < 2:
    print("Usage: Please provdide a youtube link to the commmission meeting. ")

try:
    print('uploading')
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
class Comment(BaseModel):
    Commissioner_speaking: str
    comment: str
    topic: str

class RollCall(BaseModel):
    name: list[str]

extract_rollcall_from_video = """
Please return a list of all Names of Commissioners that are present at the meeting. The best way to find this information 
"""
extract_notes_from_video = """
Please summarize comments made by each commissioner throughout this commission meeting. Briefly describe every comment, as well as who made it, as succinctly as possible. Avoid repetitive notes, focusing on comments made on key issues discussed.
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

rollcalltext = json.loads(rollcall.text)
minutetext = json.loads(result.text)

print(rollcalltext)
print(minutetext)