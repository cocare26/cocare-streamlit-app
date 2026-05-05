import streamlit as st
from engine import process_message

st.set_page_config(page_title="CoCare Chatbot", layout="centered")

st.title("🤖 CoCare Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi, how can I help you?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

prompt = st.chat_input("Type your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        result = process_message(
            user_message=prompt,
            user_id="customer_1",
            region="Amman"
        )

        reply = result.get("response", "I received your request.")
        followup = result.get("followup_response")

        if followup:
            reply = reply + "\n\n" + followup

    except Exception as e:
        reply = "Sorry, something went wrong."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
