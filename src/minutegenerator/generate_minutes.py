
from helper_functions import call_api, client, parsejson
from data_models import city_commission_model
from prompts import prompts
from render import render
import sys 

def generate_minutes(path, model):


    youtube_file_path = sys.argv[1]
    genai_client = client.setup_client(youtube_file_path)

    response = call_api.call_gemini(
        genai_client["client"], 
        model, 
        genai_client["video_file"], 
        prompts.prompt_options["sustainability_commission"],
        city_commission_model.MeetingMinutes)

    parsed_json = parsejson.parse_json(response)
    rendered_html = render.render_html(path, parsed_json)

    return rendered_html