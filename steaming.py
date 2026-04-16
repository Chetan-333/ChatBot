import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage, AIMessage

#session state to store messages
if "messages" not in st.session_state:
    st.session_state["messages"] = []

config = {'configurable':{'thread_id': 'thread-1'}}


#loading messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.text(message["content"])
   

chat_input = st.chat_input("Type your message here...")


if chat_input:
    st.session_state['messages'].append({"role": "user", "content": chat_input})

    with st.chat_message("user"):
        st.text(chat_input)
    


    
    with st.chat_message("assistant"):
        ai_message = st.write_stream(
            message_chunk.content for message_chunk,metada in  chatbot.stream(
                {'messages': [HumanMessage(content=chat_input)]
                },
                config={'configurable': {"thread_id": "thread-1"}},
                stream_mode='messages'
            )
        )
    st.session_state['messages'].append({'role': "assistant", 'content': ai_message})    
        

