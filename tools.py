from langchain.tools import tool
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain import PromptTemplate
import requests
from utils import initialise_setup
import os

from dotenv import load_dotenv
load_dotenv()

setup = initialise_setup()

llm = setup.model_inilialise()
vectordb = setup.existing_db()


@tool
def post_on_slack(response: str) -> str:
    """post the entire response json on the slack channel"""

    payload = str({"text": response})
    slack_webHook = os.getenv('SLACK_WEBHOOK')
    response = requests.post(slack_webHook, data = payload)
    print(response.text)
    return "response json posted on the slack channel"


@tool
def get_answer(question: str) -> str:
    """get the answer for the question from the context, create the context from the vectordb"""
    
    template = """Answer the question based on the context below. If the
    question cannot be answered using the information provided answer
    with "I don't know".

    {format_instructions}

    Context: {context}

    Question: {question}

    Answer: """

    

    results = vectordb.similarity_search(question)
    results = sorted(results, key=lambda x: x.metadata['page'])
    context = ' '.join([x.page_content for x in results])


    response_schemas = [
    ResponseSchema(name="question", description="user's question"),
    ResponseSchema(name="answer", description="answer to the user's question"),
    ResponseSchema( name="source",description="source used to answer the user's question, should be a website.",),
    ]
    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()

    prompt_template = PromptTemplate(
        input_variables=["question","context"],
        template=template,
        partial_variables={"format_instructions": format_instructions},
    )

    formatted_prompt = prompt_template.format(question=question,context=context)

    response = llm.invoke(formatted_prompt)

    return response.content
