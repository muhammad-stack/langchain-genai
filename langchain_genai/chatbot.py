
from typing import TypedDict
from langchain_core.runnables.config import RunnableConfig
import os
from dotenv import find_dotenv, load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage  , AIMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START , StateGraph  , END
from langgraph.graph.state import CompiledStateGraph #type



class State(TypedDict):
    prompt : list[str]

load_dotenv(find_dotenv())
llm : ChatGoogleGenerativeAI = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash",api_key=os.getenv("GEMINI_API_KEY"),temperature=0 )
# Define a new graph


# Define the function that calls the model
def node_1(state: State)  :
    response = llm.invoke(state["prompt"])
    return {"messages": state["prompt"] + response }

builder : StateGraph = StateGraph(state_schema=State)

# Nodes
builder.add_node("node_1", node_1)

# Edges
builder.add_edge(START, "node_1")
builder.add_edge("node_1", END)

# Compile the graph
graph: CompiledStateGraph = builder.compile()
print(graph)

print(graph.get_graph())

# View
display(Image(graph.get_graph().draw_mermaid_png()))

# Add memory
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "abc234"}}

query = " What is my name ?"


input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()  # output contains all messages in state
# resp = llm.invoke(
#     [
#         HumanMessage(content="Hi! I'm Bob"),
#         AIMessage(content="Hello Bob! How can I assist you today?"),
#         HumanMessage(content="What's my name?"),
#     ]
# )
# print(resp.content)

# messages = [SystemMessage(content='''Act as a senior software engineer
#  at a startup company.'''),
#  HumanMessage(content='''Please can you provide a funny joke
#  about software engineers?''')]


# Synchronous Results
# synchronous_llm_results = llm.batch([messages]*2)
# print(synchronous_llm_results[0].content)

# Runnable Configs
# configs = RunnableConfig(max_concurrency=3)
# Call the .batch() method with the inputs and config:
# print(llm.batch([messages , messages], config=configs)[0].content)


# Streaming

# for chunk in llm.stream(input=messages):
#     print(chunk.content , end = "" ,flush=True)
