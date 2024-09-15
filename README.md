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
