
# AI-Powered Meeting Minutes Generator for Local Government Internship 

```
This tool automates the creation of structured meeting minutes for government commission meetings. It leverages the Google Gemini API to extract relevant content, uses Pydantic to validate and structure the data, and Jinja2 templates to convert the output into an HTML summary. The result is a fully automated, end-to-end pipeline that significantly reduces the manual effort required by staff to document commission meetings. 
```
## Why I built this
```
During my internship, recording minutes for commission meetings was a slow, time-intensive process.
This tool automates the meeting-minutes workflow, saving me hours of repetitive work while ensuring consistent, structured outputs for each meeting. 
```

## Tech Stack
```
Python – Core logic and data handling
Bash – Automation and file management
Google Gemini API – Extract key meeting content
Pydantic – Structured API Data 
Jinja2 – Formats the minutes using a template
HTML – Final output format
AI Tools – Used to generate initial HTML templates and troubleshoot formatting issues
```
## Setup 
```

1. Clone the repository:

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

2: Set up your python environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Create a .env file in the root directory with your Gemini API key
GOOGLE_API_KEY=your_google_api_key


4. Run the automation script 
Run the create_minutes.sh file with ./create_minutes.sh, and provide a link to the commission meeting recording when prompted. The completed minutes will be created in meeting_minutes.html at the root of your directory.

5. When prompted, enter the youtube link to the commission meeting.

The completed meeting_minutes.html file will be generated at the root of your project directory.
```
## Key Contributions 
```
Adapted an existing finance bot’s architecture to handle commission meeting data workflows

Designed custom Pydantic models to structure and guide AI-generated outputs

Created dynamic Jinja2 templates for readable, well-structured meeting summaries

Automated end-to-end process with Bash and Python

Ensured output matches the format and quality standards of meeting minutes for my government internship.
```
## Project Lineage & Acknowledgements

```

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

Credit to the original developer(s) for their solid foundational architecture.


```
