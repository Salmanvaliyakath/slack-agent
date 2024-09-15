from fastapi import FastAPI
from agent import agent_setup
from pydantic import BaseModel
from typing import List
from utils import initialise_setup

setup = initialise_setup()

from dotenv import load_dotenv
load_dotenv()

class ItemRequest(BaseModel):
    questions: List[str]  # List of strings
    pdf_path: str  # Single string

# Create a FastAPI instance
app = FastAPI()

agent = agent_setup()

# Define a route with a path parameter
@app.post("/invoke_agent")
def slack_agent(request: ItemRequest):

    questions = request.questions
    setup.create_db(request.pdf_path)


    agent.answer_and_slack(questions)
    return {"item_id": "All OK"}



# Define a root route
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}