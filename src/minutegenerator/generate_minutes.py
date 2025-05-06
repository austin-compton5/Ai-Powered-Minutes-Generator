
from helper_functions import call_api, client, parsejson
from prompts import prompts
from render import render
import sys 

def generate_minutes(templates_dir, template, model, prompt, data_model):


    youtube_file_path = sys.argv[1]
    genai_client = client.setup_client(youtube_file_path)

    response = call_api.call_gemini(
        genai_client["client"], 
        model, 
        genai_client["video_file"], 
        prompt,
        data_model)

    parsed_json = parsejson.parse_json(response)
    rendered_html = render.render_html(templates_dir, template, parsed_json)

    return rendered_html