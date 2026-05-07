import streamlit as st
from engine.chatbot_engine import chatbot_engine

st.set_page_config(page_title="AI Agent", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: #eef3f6;
}

.phone {
    width: 420px;
    height: 700px;
    margin: auto;
    border-radius: 42px;
    background: linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    padding: 18px;
    box-sizing: border-box;
}

.topbar {
    height: 58px;
    background: white;
    border-radius: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0 14px;
    box-shadow: 0 3px 10px rgba(0,0,0,.12);
    margin-bottom: 15px;
}

.back {
    font-size: 28px;
    color: #436577;
    text-decoration: none;
}

.dot {
    width: 8px;
    height: 8px;
    background: #36c06a;
    border-radius: 50%;
}

.status {
    font-size: 15px;
    font-weight: 700;
    color: #222;
}

.chat-area {
    height: 455px;
    overflow-y: auto;
    padding: 5px;
}

.bot-msg {
    background: white;
    color: #222;
    padding: 9px 12px;
    border-radius: 16px;
    max-width: 75%;
    margin-bottom: 8px;
    font-size: 13px;
}

.user-msg {
    background: #1c6fa4;
    color: white;
    padding: 9px 12px;
    border-radius: 16px;
    max-width: 75%;
    margin-left: auto;
    margin-bottom: 8px;
    font-size: 13px;
}

div[data-testid="stChatInput"] {
    width: 420px;
    margin: auto;
}

div[data-testid="stChatInput"] textarea {
    border-radius: 22px;
    font-size: 13px;
}

.stButton > button {
    border-radius: 18px;
    font-size: 12px;
    background: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

if "messages_en" not in st.session_state:
    st.session_state.messages_en = [
        {"role": "bot", "text": "Hi, how can I help you?"}
    ]

def handle_message(text):
    st.session_state.messages_en.append({
        "role": "user",
        "text": text
    })

    try:
        result = chatbot_engine(text)
        reply = result.get("response", "No response generated.")
    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.messages_en.append({
        "role": "bot",
        "text": reply
    })

st.markdown('<div class="phone">', unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
    <a class="back" href="/?page=customer">‹</a>
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-area">', unsafe_allow_html=True)

for msg in st.session_state.messages_en:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-msg">{msg["text"]}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="bot-msg">{msg["text"]}</div>',
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

quick_actions = [
    "Network Test",
    "Internet Usage",
    "Renew Package",
    "International Calls",
    "Offers & Games",
    "Contact Support"
]

cols = st.columns(3)

for i, action in enumerate(quick_actions):
    if cols[i % 3].button(action, key=f"quick_{i}"):
        handle_message(action)
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)

user_text = st.chat_input("Type your question here...")

if user_text:
    handle_message(user_text)
    st.rerun()
