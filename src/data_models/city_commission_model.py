from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime 

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