
from google.genai import types
from core import parser, render

def call_gemini(client, model, video_file, prompt, schema):

    # count the tokens in the prompt and file
    print(client.models.count_tokens(model=model, contents=[video_file, prompt]))

    try:
        result = client.models.generate_content(
                    model=model,
                    contents=[video_file, prompt], 
                    config=types.GenerateContentConfig(
                        response_mime_type="application/json", 
                        response_schema=schema
                    )
                )
    except Exception as e: 
        print(f"Error during api call: {e}")
        
    return result 

def generate_minutes(templates_dir, client, template, model, prompt, data_model):

    response = call_gemini(
        client["client"], 
        model, 
        client["video_file"], 
        prompt,
        data_model)
    print(response)
    
    parsed_json = parser.parse_json(response)
    rendered_html = render.render_html(templates_dir, template, parsed_json)

    return rendered_html
