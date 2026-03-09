import streamlit as st
from app import get_response

st.set_page_config(page_title="Gemini Chatbot")

st.title("AI Chatbot using Gemini")

# initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# user input box
prompt = st.chat_input("Ask something...")

if prompt:

    # show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # get response
    response = get_response(prompt)

    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })