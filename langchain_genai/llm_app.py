from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.messages import SystemMessage , HumanMessage
from dotenv import load_dotenv , find_dotenv
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

parser = StrOutputParser()
load_dotenv(find_dotenv())

llm = ChatGoogleGenerativeAI(api_key=os.getenv("GEMINI_API_KEY"),model="models/gemini-1.5-flash")

system_template = "Translate the following into {language}:"

prompt_temp = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("human", "{input}")
    ]
)

result = prompt_temp.invoke({"language": "English", "input": "Chutiya hai kya?"})

# print(result)
# print(result.to_messages())



# messages : list[SystemMessage, HumanMessage]  = [
#     SystemMessage(content= "Translate the following from Roman Urdu to English"),
#     HumanMessage(content="Kia haal bhau")
# ]

chain = llm | parser

response = chain.invoke(result)

print(type(response))
print(response)

