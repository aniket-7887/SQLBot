import streamlit as st
from graph import sql_agent 
import time

st.set_page_config(page_title='SQLBot', page_icon="🤖", layout="wide")
st.title("SQLBot")

user_query = st.text_area("Enter your query here...")
run_button = st.button("Invoke Agent")



if run_button:
    st.markdown("### Thinking")

    reasoning_box = st.empty()
    final_box = st.empty()

    with st.spinner("Agnet is thinking..."):
        response = sql_agent.invoke({'messages': user_query})

    if "messages" in response:
        messages = response["messages"]

        for msg in messages:
            if msg.type == "ai":
                content = msg.content.strip()
                if "**Final Ansewer**" not in content:
                    reasoning_box.markdown(f"```\n{content}\n```")
                    time.sleep(0.8)

        final_message = messages[-1].content
        final_box.markdown('### Final Answer')
        final_box.markdown(final_message)
