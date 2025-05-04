from google import genai
import time 


def setup_client(file_path):

    client = genai.Client()

    try:
        print('uploading: this may take a few minutes')
        video_file = client.files.upload(file=file_path)
        print("File uploaded successfully")
    except Exception as e:
        print(f"Error during file upload: {e}")
    while video_file.state.name == "PROCESSING":
        print("processing video...")
        time.sleep(5)
        print("video file name:")
        print(video_file.name)
        video_file = client.files.get(name=video_file.name)

    return {"client" : client, "video_file": video_file}