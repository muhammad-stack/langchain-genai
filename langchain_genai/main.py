from dotenv import load_dotenv , find_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate  # Add this import
load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"),model="models/gemini-1.5-flash")

prompts = PromptTemplate.from_template("What's your {name}")
intent = "greet"
dest_prompt = PromptTemplate.from_template("and ask what is he {studying} in college")

prompt = (prompts + intent + dest_prompt)
response = llm.invoke(prompt.format_prompt(name="Harrison", studying="Computer Science"))
print(response.content)