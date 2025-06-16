from pydantic import BaseModel


class MinutesResponse(BaseModel):
    json: dict
    html: str

class MinutesRequest(BaseModel):
    youtube_link: str 