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
    referenced_meeting_date: Optional[datetime] = None
    moved_by: str
    seconded_by: str
    ayes: List[str]

class AgendaItem(BaseModel):
    item_number: int
    title: str
    type: Literal["Action", "Report", "Oral Communication", "Update", "Other"]
    presenter: Optional[str]
    summary: Optional[str]
    commissioner_comments: List[SpeakerComment] = []

    class Config:
        extra = "allow"

class MeetingMinutes(BaseModel):
    meeting_title: str 
    meeting_date: datetime
    start_time: str
    end_time: str
    roll_call: RollCall
    pledge_of_allegiance: bool
    land_acknowledgement: bool
    agenda_posted_date: Optional[datetime] = None

    approval_of_minutes: Optional[ApprovalOfMinutes] = None
    general_commissioner_comments: List[SpeakerComment] = []
    agenda_items: List[AgendaItem] = []
    oral_communications: List[SpeakerComment] = []
    adjournment_moved_by: Optional[str] = None
    adjournment_seconded_by: Optional[str] = None

    class Config:
        extra = "allow"