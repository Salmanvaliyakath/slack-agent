from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain_core.documents.base import Document
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

import os
from dotenv import load_dotenv
load_dotenv()

class initialise_setup:
    def __init__(self):
        pass

    def model_inilialise(self):

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

        return llm

    # # def initialize_db(self, pdf_path):

    #     chroma_store_folder = 'chroma_store'

    #     def preprocess_text(text):
    #         # Basic cleaning steps such as removing extra spaces and handling line breaks
    #         clean_text = text.replace("\n", " ").strip()
    #         return clean_text

    #     if os.path.isdir(chroma_store_folder):
    #         print('Loading from the persistant DB')
    #         vectordb = Chroma(persist_directory="chroma_store", embedding_function=OpenAIEmbeddings())
    #         print(vectordb._collection.count())

    #     else:
    #         print('Creating the Chroma DB and storing')

    #         loader = PyPDFLoader(pdf_path)
    #         documents = loader.load()
    #         documents = [Document(page_content=preprocess_text(doc.page_content), metadata=doc.metadata) for doc in documents]

    #         text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    #         chunked_documents = text_splitter.split_documents(documents)


    #         vectordb = Chroma.from_documents(
    #             documents=chunked_documents,
    #             embedding=OpenAIEmbeddings(),
    #             persist_directory="chroma_store"
    #         )

    #     return vectordb
    
    def custom_prompt(self):
        prompt = ChatPromptTemplate.from_messages([
            ("system", """
            You are a helpfull assistant. use your tools to achieve the task.
            If you do not have a tool to perform the task, say so. 
            
            Answer the following list of question seperated by comma and post the all the questions entire response json on the slack channel
            """),
            MessagesPlaceholder("chat_history", optional=True),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),])

        return prompt
    
    def existing_db(chroma_store_folder):
        print('Loading from the persistant DB')
        vectordb = Chroma(persist_directory="chroma_store", embedding_function=OpenAIEmbeddings())
        print(vectordb._collection.count())
        return vectordb
    
    def create_db(self, pdf_path):

        chroma_store_folder = 'chroma_store'

        def preprocess_text(text):
            # Basic cleaning steps such as removing extra spaces and handling line breaks
            clean_text = text.replace("\n", " ").strip()
            return clean_text

        print('Creating the Chroma DB and storing')

        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        documents = [Document(page_content=preprocess_text(doc.page_content), metadata=doc.metadata) for doc in documents]

        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
        chunked_documents = text_splitter.split_documents(documents)


        vectordb = Chroma.from_documents(
            documents=chunked_documents,
            embedding=OpenAIEmbeddings(),
            persist_directory=chroma_store_folder
        )

        return vectordb