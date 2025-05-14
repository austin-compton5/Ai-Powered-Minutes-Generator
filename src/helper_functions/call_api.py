
from google.genai import types

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
