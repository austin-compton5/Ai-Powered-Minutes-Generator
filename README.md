
##📝 Meeting Minutes Generator

This project automates the creation of structured meeting minutes for government commission meetings. It leverages the Google Gemini API to extract relevant content, uses Pydantic to validate and structure the data, and Jinja2 templates to convert the output into an HTML summary. The result is a fully automated, end-to-end pipeline that reliably generates a solid first draft of minutes for city commission meetings.  


##Demo



## Tech Stack

FastAPI – backend routes and request handling
Gemini API – meeting summarization
yt-dlp – audio extraction from YouTube
Pydantic – data validation
Jinja2 – templated HTML output
Streamlit (optional) – demo interface
AI Tools – Used to generate initial HTML templates and troubleshoot formatting issues

## Setup 

1. Clone the repository:
```
  git clone https://github.com/austin-compton5/Ai-Powered-Minutes-Generator
  cd your-repo-name
```
2: Set up your python environment:
```
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```
3. Create a .env file in the root directory with your Gemini API key
```
  GOOGLE_API_KEY=your_google_api_key
```

5. Run the Streamlit demo
```
 streamlit run src/streamlit_app/app.py 
```

6. Or run the API
```
cd src/api
uvicorn main:app --reload 
```


## Key Contributions 

Adapted an existing finance bot’s architecture to handle commission meeting data workflows

Designed custom Pydantic models to structure and guide AI-generated outputs

Created dynamic Jinja2 templates for readable, well-structured meeting summaries

Automated end-to-end process with Bash and Python

Ensured output matches the format and quality standards of meeting minutes for my government internship.

## Project Lineage & Acknowledgements



This project was initially adapted from an open-source finance application that featured a similar data extraction architecture to fetch market data. While the original use case was entirely different, its structure helped accelerate development.

I changed the python script to:
- Change the data source and format (meeting minutes vs. financial data)
- Design custom Pydantic models for new data types
- Implement a new Jinja2-based templating system for HTML output
- Integrating Google Gemini for NLP-based content extraction

Throughout development, I also used AI tools (Gemini and ChatGPT) to:
- Generate initial Bash scripts for automating file handling
- Troubleshoot Python and templating bugs
- Prototype the HTML structure using Jinja2
- Get structural guidance for designing Pydantic schemas

Original repo: https://github.com/hackingthemarkets/gemini-multimodal-structured-extraction

Thank you to the original developer! I learned a lot building ontop of their project.

```
