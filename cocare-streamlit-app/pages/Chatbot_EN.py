import streamlit as st
import base64
import os
import sys
import html as html_lib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

st.set_page_config(page_title="AI Agent", layout="centered")

CHAT_KEY = "chat_en_messages"

if "region" not in st.session_state:
    st.session_state["region"] = "Amman"

region = st.session_state["region"]

def img_to_base64(path):
    full_path = os.path.join(os.path.dirname(__file__), "..", path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi, how can I help you?")
    ]

def get_bot_reply(user_text):
    quick_map = {
        "Network Test": "Check my network status",
        "Internet Usage": "I want to check internet usage",
        "Renew Package": "I want to renew my package",
        "International Calls": "Tell me about international calls",
        "Offers & Games": "What offers are available?",
        "Contact Support": "I need technical support",
    }

    msg = quick_map.get(user_text, user_text)

    try:
        result = process_message(
            msg,
            user_id=st.session_state.get("user_id", "customer_1"),
            region=region
        )

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()

        reply = f"{response}\n\n{followup}".strip()
        return reply if reply else "Could you clarify more?"

    except Exception as e:
        return f"Connection error: {e}"

def send_message(text):
    if not text or not text.strip():
        return

    st.session_state[CHAT_KEY].append(("user", text))
    st.session_state[CHAT_KEY].append(("bot", get_bot_reply(text)))

st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#eef2f7;
    font-family:Arial;
}

header, footer, #MainMenu {
    visibility:hidden;
}

.block-container {
    width:420px;
    height:700px;
    margin:auto;
    padding:0;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
}

.phone {
    width:420px;
    height:700px;
    position:relative;
}

.topbar {
    position:absolute;
    top:14px;
    left:18px;
    right:18px;
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
}

.back {
    font-size:28px;
    color:#436577;
    text-decoration:none;
}

.avatar {
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}

.dot {
    width:8px;
    height:8px;
    background:#36c06a;
    border-radius:50%;
}

.status {
    font-size:15px;
    font-weight:700;
    color:#222;
}

.chat-box {
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:75px;
    overflow-y:auto;
    padding:10px;
}

.msg {
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.4;
    white-space:pre-wrap;
}

.bot {
    background:white;
    color:#222;
    margin-right:auto;
}

.user {
    background:#1c6fa4;
    color:white;
    margin-left:auto;
}

.quick-menu {
    position:absolute;
    left:38px;
    bottom:90px;
    width:150px;
    background:white;
    border-radius:8px;
    box-shadow:0 4px 12px rgba(0,0,0,.18);
    padding:8px 0;
    z-index:5;
}

div[data-testid="stButton"] button {
    width:150px;
    height:auto;
    background:white;
    color:#222;
    border:none;
    border-radius:0;
    padding:7px 13px;
    font-size:13px;
    text-align:left;
    box-shadow:none;
}

div[data-testid="stButton"] button:hover {
    background:#eef3f6;
    color:#222;
}

.bottom {
    position:absolute;
    bottom:18px;
    left:18px;
    right:18px;
    height:42px;
    display:flex;
    align-items:center;
    gap:8px;
}

.fake-menu {
    width:32px;
    height:32px;
    border-radius:50%;
    background:white;
    text-align:center;
    line-height:32px;
    font-size:22px;
    color:#50768a;
}

.input-area {
    position:absolute;
    bottom:18px;
    left:58px;
    right:66px;
}

.input-area input {
    height:34px;
    background:white;
    border-radius:22px;
    color:#444;
    font-size:12px;
    padding-left:14px;
    border:none;
}

.send-area {
    position:absolute;
    bottom:18px;
    right:18px;
}

.send-area button {
    width:40px !important;
    height:40px !important;
    border-radius:50% !important;
    background:linear-gradient(135deg,#6ec6ff,#1c6fa4) !important;
    color:white !important;
    text-align:center !important;
    font-size:20px !important;
    padding:0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="phone">', unsafe_allow_html=True)

st.markdown(f"""
<div class="topbar">
    <a href="/Customer" target="_self" style="text-decoration:none;">
        <div class="back">‹</div>
    </a>
    <img class="avatar" src="data:image/png;base64,{robot}">
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
</div>
""", unsafe_allow_html=True)

chat_html = '<div class="chat-box">'
for role, msg in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    chat_html += f'<div class="msg {cls}">{html_lib.escape(str(msg))}</div>'
chat_html += '</div>'
st.markdown(chat_html, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="quick-menu">', unsafe_allow_html=True)

    if st.button("Network Test"):
        send_message("Network Test")
        st.rerun()

    if st.button("Internet Usage"):
        send_message("Internet Usage")
        st.rerun()

    if st.button("Renew Package"):
        send_message("Renew Package")
        st.rerun()

    if st.button("International Calls"):
        send_message("International Calls")
        st.rerun()

    if st.button("Offers & Games"):
        send_message("Offers & Games")
        st.rerun()

    if st.button("Contact Support"):
        send_message("Contact Support")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="bottom"><div class="fake-menu">≡</div></div>', unsafe_allow_html=True)

st.markdown('<div class="input-area">', unsafe_allow_html=True)
user_text = st.text_input(
    "chat_input_hidden",
    placeholder="Type your question here...",
    label_visibility="collapsed"
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="send-area">', unsafe_allow_html=True)
if st.button("➤"):
    send_message(user_text)
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
