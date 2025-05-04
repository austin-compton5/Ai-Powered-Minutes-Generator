from pydantic import BaseModel
import json 
from datetime import datetime

def json_serial(obj):

    if isinstance(obj, datetime):
        # Convert datetime objects to ISO 8601 strings
        return obj.isoformat()
    # If the object is of another type not handled here, raise the default error
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def parse_json(result):

    parsed_meeting = result.parsed 
    meeting_dict = parsed_meeting.model_dump() 

    with open("./raw_output_debug.json", "w", encoding="utf-8") as f:
        json.dump(meeting_dict, f, indent=4, default=json_serial)

    return meeting_dict