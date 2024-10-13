from dotenv import load_dotenv , find_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage , HumanMessage

load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"),model="models/gemini-1.5-flash")

messages : list[SystemMessage, HumanMessage]  = [
    SystemMessage(content= "Translate the following from Roman Urdu to English"),
    HumanMessage(content="Kia haal bhau")
]

response : str = llm.invoke(messages)

print(response.content)
print(type(response))