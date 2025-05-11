from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from minutes import generate_minutes_from_youtube
from helper_functions import download 

app = FastAPI()

@app.get("/")
def home():
    return HTMLResponse("""
    <body>
        <form action="/generate" method="post">
            <input name="youtube_url" placeholder="Paste YouTube URL">
            <button type="submit">Generate Minutes</button>
        </form>
    </body>
    """)

@app.post("/generate")
def generate(youtube_url: str = Form(...)):
    print("Received YouTube URL:", youtube_url)
    audio_path = download.download_audio(youtube_url) 
    html_output = generate_minutes_from_youtube(audio_path)
    return HTMLResponse(html_output)




 
#  <body>
#             <form action="/generate" method="post">
#                 <input name="youtube_url" placeholder="Paste YouTube URL">
#                 <button type="submit">Generate Minutes</button>
#             </form>
#         </body>

#  <!DOCTYPE html>
#     <html>
#     <head>
#         <meta charset="UTF-8">
#         <title>Generate Meeting Minutes</title>
#         <style>
#             body {
#                 background: #eee;
#                 font-family: Arial, sans-serif;
#             }

#             .wrapper {
#                 margin-top: 80px;
#                 margin-bottom: 80px;
#             }

#             .form-submitlink {
#                 max-width: 380px;
#                 padding: 15px 35px 45px;
#                 margin: 0 auto;
#                 background-color: #fff;
#                 border: 1px solid rgba(0,0,0,0.1);
#                 border-radius: 10px;
#                 box-shadow: 0 4px 8px rgba(0,0,0,0.05);
#             }

#             .form-submitlink-heading {
#                 margin-bottom: 30px;
#                 text-align: center;
#             }

#             .form-control {
#                 width: 100%;
#                 font-size: 16px;
#                 padding: 10px;
#                 margin-bottom: 20px;
#                 box-sizing: border-box;
#                 border: 1px solid #ccc;
#                 border-radius: 4px;
#             }

#             button {
#                 width: 100%;
#                 padding: 10px;
#                 font-size: 16px;
#                 background-color: #4CAF50;
#                 color: white;
#                 border: none;
#                 border-radius: 4px;
#                 cursor: pointer;
#             }

#             button:hover {
#                 background-color: #45a049;
#             }
#         </style>
#     </head>
#     <body>
#         <div class="wrapper">
#             <form action = "/generate" method="post" class="form-submitlink">       
#                 <h2 class="form-submitlink-heading">Paste YouTube Commission Link</h2>
#                 <input class="form-control" name="youtube_url" placeholder="Paste link here" required/>      
#                 <button type="submit">Generate Minutes</button>   
#             </form>
#         </div>
#     </body>
#     </html>