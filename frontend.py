import streamlit as st 
from graph import workflow

st.title("Database ChatBot")

user_query = st.chat_input("Enter your question here....")

if user_query:
    with st.chat_message('user'):
        st.text(user_query)

    # with st.chat_message('ai'):
    #     response = workflow.invoke({'user_query': user_query})['result']
    #     st.write(response)
    ai_response = st.write_stream(
        message_chunk.content for message_chunk, metadata in workflow.stream(
            {"user_query": user_query},
            stream_mode='messages'
        )
    )
    