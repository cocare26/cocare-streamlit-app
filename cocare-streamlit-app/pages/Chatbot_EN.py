import streamlit as st
from engine.chatbot_engine import chatbot_engine

st.set_page_config(page_title="AI Agent", layout="centered")

st.markdown("""
<style>

.main {
    background:#eef3f6;
}

.chat-container {
    width:420px;
    margin:auto;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:32px;
    padding:18px;
    min-height:700px;
}

.topbar {
    background:white;
    border-radius:18px;
    padding:14px;
    margin-bottom:18px;
    display:flex;
    align-items:center;
    gap:10px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
}

.dot {
    width:10px;
    height:10px;
    background:#36c06a;
    border-radius:50%;
}

.status {
    font-size:15px;
    font-weight:bold;
}

.msg-user {
    background:#1c6fa4;
    color:white;
    padding:10px 14px;
    border-radius:18px;
    width:fit-content;
    max-width:75%;
    margin-left:auto;
    margin-bottom:10px;
}

.msg-bot {
    background:white;
    color:#222;
    padding:10px 14px;
    border-radius:18px;
    width:fit-content;
    max-width:75%;
    margin-right:auto;
    margin-bottom:10px;
}

.quick-buttons {
    margin-top:15px;
}

</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role":"bot",
            "text":"Hi, how can I help you?"
        }
    ]

st.markdown('<div class="chat-container">', unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
</div>
""", unsafe_allow_html=True)

for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f'<div class="msg-user">{msg["text"]}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="msg-bot">{msg["text"]}</div>',
            unsafe_allow_html=True
        )

quick_cols = st.columns(3)

quick_actions = [
    "Network Test",
    "Internet Usage",
    "Renew Package",
    "International Calls",
    "Offers & Games",
    "Contact Support"
]

for i, action in enumerate(quick_actions):

    if quick_cols[i % 3].button(action):

        st.session_state.messages.append({
            "role":"user",
            "text":action
        })

        result = chatbot_engine(action)

        st.session_state.messages.append({
            "role":"bot",
            "text":result["response"]
        })

        st.rerun()

message = st.chat_input("Type your question here...")

if message:

    st.session_state.messages.append({
        "role":"user",
        "text":message
    })

    result = chatbot_engine(message)

    st.session_state.messages.append({
        "role":"bot",
        "text":result["response"]
    })

    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
