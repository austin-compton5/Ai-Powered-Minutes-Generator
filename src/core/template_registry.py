from minute_models import city_commission_model, tbac
from pydantic import BaseModel
from typing import Type, Optional
from prompts import prompts

class TemplateConfig(BaseModel):
    template: str
    data_model: type
    prompt: str 

TEMPLATE_REGISTRY = {
   "city_commission": TemplateConfig(
       template = "sustainability_commission.html",
       data_model= city_commission_model.MeetingMinutes,
       prompt = prompts.prompt_options["sustainability_commission"]
   ), 
   "tbac" : TemplateConfig(
       template= "tbac_meeting.html",
       data_model= tbac.MeetingMinutes,
       prompt = prompts.prompt_options["tbac"]
   )
}