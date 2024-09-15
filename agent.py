from langchain.tools import tool
from langchain.agents import create_openai_tools_agent, AgentExecutor
from utils import initialise_setup
from tools import get_answer, post_on_slack

from dotenv import load_dotenv
load_dotenv()

setup = initialise_setup()

class agent_setup:
    
    def __init__(self):
        self.llm = setup.model_inilialise()
        self.prompt = setup.custom_prompt()
        self.toolkit = [get_answer, post_on_slack]
        self.agent = create_openai_tools_agent(self.llm, self.toolkit, self.prompt)
        self.agent_executor = AgentExecutor(agent=self.agent, tools=self.toolkit, verbose=True)
    
    
    def answer_and_slack(self, user_questions):
        # user_questions = ["who is the ceo of the comapny?"]

        #             #   "What is their vacation policy?", 
        #             #   "What is the termination policy?"

        user_questions_formatted = ', '.join(user_questions)
        self.agent_executor.invoke({"input": user_questions_formatted})






