# slack-agent

This project provides a Slack agent that accepts a list of questions and a PDF document, extracts answers from the document using OpenAI LLMs, and posts the results on a specified Slack channel.

# Features
Question Answering: Accepts multiple questions, processes the provided PDF, and finds relevant answers.<br/>
Slack Integration: Automatically posts the extracted answers on Slack.<br/>
FastAPI: Provides an API for interacting with the Slack agent.<br/>

# Project Structure
main.py: Contains the FastAPI application that accepts user inputs and invokes the Slack agent.<br/>
agent.py: Defines the Slack agent setup and handles the logic for processing questions and posting answers.<br/>
tools.py: Contains tools for extracting answers from documents and posting results on Slack.<br/>
utils.py: Contains helper functions like initializing the setup and creating/loading the Chroma DB.<br/>

# Prerequisites
Python 3.8+<br/>
OpenAI API key<br/>
Slack API token - WebHook Token<br/>


# Installation
Clone the repository:<br/>

git clone <repository_url><br/>
cd <repository_name><br/>

# Install dependencies:
pip install -r requirements.txt<br/>

Set up environment variables: Create a .env file in the project root with the following content:<br/>

OPENAI_API_KEY=<your_openai_api_key><br/>
SLACK_API_TOKEN=<your_slack_token><br/>

# Run the FastAPI app:

fastapi dev main.py<br/>

# API Endpoints

POST method /invoke_agent<br/>
This endpoint triggers the agent to process the provided questions and PDF file, then posts the extracted answers on Slack.<br/>

Request Body:<br/>
json<br/>
{
  "questions": ["Question 1", "Question 2", "Question 3"],
  "pdf_path": "path_to_your_pdf_document.pdf"
}

Example:<br/>

curl -X 'POST' \
  'http://127.0.0.1:8000/invoke_agent' \
  -H 'Content-Type: application/json' \
  -d '{
  "questions": ["Who is the CEO?", "What is the company's policy on vacation?"],
  "pdf_path": "/path/to/document.pdf"
}'
