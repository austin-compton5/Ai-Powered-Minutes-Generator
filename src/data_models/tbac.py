from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Comment(BaseModel):
    speaker: Optional[str]
    comment: str

class AgendaItem(BaseModel):
    number: str
    title: str
    notes: Optional[str] = None
    discussion: Optional[List[Comment]] = None
    was_discussed: bool = True

class EventAnnouncement(BaseModel):
    title: str
    description: Optional[str]
    date: Optional[datetime]

class MeetingMinutes(BaseModel):
    meeting_date: datetime
    start_time: str
    end_time: Optional[str]
    location: str
    chair: str
    quorum_confirmed: bool
    agenda: List[AgendaItem]
    event_announcements_internal: Optional[List[EventAnnouncement]]
    event_announcements_external: Optional[List[EventAnnouncement]]
    public_comments: Optional[List[Comment]]
    next_meeting_date: Optional[datetime]
    adjournment_time: Optional[str]