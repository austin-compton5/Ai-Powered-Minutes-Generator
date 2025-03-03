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

def rollcall(f):
    video_file = client.files.upload(file=f)
    print("processing video...")
    while video_file.state.name == "PROCESSING":
        time.sleep(5)
        print("video file name:")
        print(video_file.name)
        video_file = client.files.get(name=video_file.name)

    print(client.models.count_tokens(model=model, contents=[video_file, extract_rollcall_from_video ]))
    rollcall = client.models.generate_content(
        model=model, 
        contents = [video_file, extract_rollcall_from_video],
        config = types.GenerateContentConfig(
        response_mime_type="application/json", response_schema= RollCall
        )
    )

    return json.loads(rollcall.text)


def uploadSplit(directory):

    combined_notes = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        if os.path.isfile(f):
            try:
                print('uploading')
                video_file = client.files.upload(file=f)
                print("File uploaded successfully")
            except Exception as e:
                print(f"Error during file upload: {e}")

            while video_file.state.name == "PROCESSING":
                print("processing video...")
                time.sleep(5)
                print("video file name:")
                print(video_file.name)
                video_file = client.files.get(name=video_file.name)

            print(client.models.count_tokens(model=model, contents=[video_file, extract_notes_from_video]))

            notes = client.models.generate_content(
                model=model, 
                contents = [video_file, extract_notes_from_video],
                config = types.GenerateContentConfig(
                response_mime_type="application/json", response_schema= RollCall
                    )   
                )
            
            obj = json.loads(notes.text)
            combined_notes.append(obj)

    return combined_notes
    


print(uploadSplit('files/sustainability_commission_split'))