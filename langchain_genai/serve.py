#!/usr/bin/env python
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import RemoteRunnable, add_routes
from dotenv import load_dotenv , find_dotenv
import os

load_dotenv(find_dotenv())  

#)1  Create Prompt Template
sys_template = "Translate the following into {language}:"
prompt_temp = ChatPromptTemplate.from_messages(
    [
        ("system", sys_template),
        ("human", "{input}")
    ]
)   

#)2 Create Model
llm = ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"),model="models/gemini-1.5-flash",temperature=0,max_retries=2  )

#)3 Create Parser
parser = StrOutputParser()

#)4 Create Chain
chain = prompt_temp |llm  |parser

# Create FastAPI app

app = FastAPI(
    title="Langchain Google Generative AI",
    description= "A simple API server using LangChain's Runnable interfaces",
    version="0.1",  
    
)

# Add chain routes
add_routes(app , chain , path='/chain')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


remote_chain = RemoteRunnable("http://localhost:8000/chain/")
remote_chain.invoke({"language": "italian", "text": "hi"})