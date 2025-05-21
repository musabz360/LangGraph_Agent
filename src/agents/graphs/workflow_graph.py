from tools.appointments.book_appointment import book_appointment    
from tools.appointments.fetch_slots import fetch_slots
from tools.leads.create_lead import create_lead
from tools.leads.fetch_lead import fetch_lead
from tools.tickets.create_ticket import create_ticket
from tools.tickets.fetch_ticket import fetch_ticket

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from langgraph.graph import MessagesState, START, StateGraph
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()



tools = [book_appointment, fetch_slots, create_lead, fetch_lead, create_ticket, fetch_ticket]

# 🤖 Language model setup
llm = ChatOpenAI(model="gpt-4o")    
llm_with_tools = llm.bind_tools(tools)

# 💬 System instruction
sys_msg = SystemMessage(content="You are a customer service assistant. Use tools to when needed.")

# 🧠 Assistant node function
def assistant(state: MessagesState):
    conversation = state["messages"]
    messages = [sys_msg] + conversation
    response = llm_with_tools.invoke(messages)
    return {"messages": conversation + [response]}

# 🛠 Build LangGraph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))

# 🔁 Define flow
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

# 🧩 Compile graph
graph = builder.compile()


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)    
            last_response = value["messages"][-1].content
    return last_response 

stream_graph_updates("book an appointment for 10:00 PM")