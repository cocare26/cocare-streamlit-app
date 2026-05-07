import streamlit as st
import base64
import os

from engine.chatbot_engine import process_message
# إذا اسم الدالة عندك مختلف، غيّري process_message لاسم الدالة الموجودة عندك

st.set_page_config(page_title="AI Agent", layout="centered")

robot = ""
if os.path.exists("robot_head.png"):
    with open("robot_head.png", "rb") as f:
        robot = base64.b64encode(f.read()).decode()

st.markdown("""
<style>
.phone {
    width: 420px;
    height: 700px;
    margin: auto;
    border-radius: 42px;
    overflow: hidden;
    position: relative;
    background: linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    padding: 14px 18px;
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
}

.back {
    font-size: 28px;
    color: #436577;
}

.avatar {
    width: 42px;
    height: 42px;
    border-radius: 50%;
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

.chat-box {
    height: 465px;
    overflow-y: auto;
    padding: 15px 0;
}

.msg {
    max-width: 75%;
    padding: 9px 12px;
    border-radius: 16px;
    margin-bottom: 8px;
    font-size: 13px;
    line-height: 1.4;
}

.bot {
    background: white;
    color: #222;
    margin-right: auto;
}

.user {
    background: #1c6fa4;
    color: white;
    margin-left: auto;
}

div[data-testid="stTextInput"] input {
    border-radius: 22px;
    height: 38px;
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "bot", "text": "Hi, how can I help you?"}
    ]

def get_reply(message):
    result = process_message(message)

    if isinstance(result, dict):
        return result.get("response") or result.get("reply") or str(result)

    return str(result)

st.markdown('<div class="phone">', unsafe_allow_html=True)

avatar_html = f'<img class="avatar" src="data:image/png;base64,{robot}">' if robot else ""

st.markdown(f"""
<div class="topbar">
    <a href="/?page=customer" target="_self" style="text-decoration:none;">
        <div class="back">‹</div>
    </a>
    {avatar_html}
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-box">', unsafe_allow_html=True)

 for_msg = st.session_state.messages
for msg in for_msg:
    css_class = "user" if msg["role"] == "user" else "bot"
    st.markdown(
        f'<div class="msg {css_class}">{msg["text"]}</div>',
        unsafe_allow_html=True
    )

st.markdown("</div>", unsafe_allow_html=True)

quick_options = [
    "Network Test",
    "Internet Usage",
    "Renew Package",
    "International Calls",
    "Offers & Games",
    "Contact Support"
]

cols = st.columns(3)

for i, option in enumerate(quick_options):
    if cols[i % 3].button(option):
        st.session_state.messages.append({"role": "user", "text": option})
        reply = get_reply(option)
        st.session_state.messages.append({"role": "bot", "text": reply})
        st.rerun()

with st.form("chat_form", clear_on_submit=True):
    message = st.text_input(
        "Message",
        placeholder="Type your question here...",
        label_visibility="collapsed"
    )
    send = st.form_submit_button("➤")

if send and message.strip():
    st.session_state.messages.append({"role": "user", "text": message})
    reply = get_reply(message)
    st.session_state.messages.append({"role": "bot", "text": reply})
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
