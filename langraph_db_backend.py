import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage
from langgraph_backend import chatbot
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import Tool
import requests
load_dotenv()









llm =ChatGoogleGenerativeAI(model ="gemini-2.5-flash" )


class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}




conn = sqlite3.connect('chatbot.db', check_same_thread=False)
checkpointer = SqliteSaver(conn)



# Checkpointer


graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)

def get_all_threads():
    all_threads = set()

    for checkpoint in checkpointer.list(None):
      all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)



