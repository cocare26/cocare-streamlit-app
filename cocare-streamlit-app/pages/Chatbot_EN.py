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

# =========================
# IMAGE
# =========================
try:
    with open("robot_head.png", "rb") as f:
        robot = base64.b64encode(f.read()).decode()
except FileNotFoundError:
    robot = ""


# =========================
# CHATBOT UI DESIGN
# =========================
html = f"""
<html>
<head>
<style>
body {{
    margin:0;
    background:#eef2f7;
    font-family:Arial;
}}

.phone {{
    width:420px;
    height:700px;
    margin:auto;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
}}

.topbar {{
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
}}

.back {{
    font-size:28px;
    color:#436577;
}}

.avatar {{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}}

.dot {{
    width:8px;
    height:8px;
    background:#36c06a;
    border-radius:50%;
}}

.status {{
    font-size:15px;
    font-weight:700;
    color:#222;
}}

.chat-box {{
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:75px;
    overflow-y:auto;
    padding:10px;
}}

.msg {{
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.4;
}}

.bot {{
    background:white;
    color:#222;
    margin-right:auto;
}}

.user {{
    background:#1c6fa4;
    color:white;
    margin-left:auto;
}}

.menu {{
    display:none;
    position:absolute;
    left:38px;
    bottom:90px;
    width:150px;
    background:white;
    border-radius:8px;
    box-shadow:0 4px 12px rgba(0,0,0,.18);
    padding:8px 0;
    z-index:5;
}}

.menu div {{
    font-size:13px;
    padding:7px 13px;
    color:#222;
    cursor:pointer;
}}

.menu div:hover {{
    background:#eef3f6;
}}

.bottom {{
    position:absolute;
    bottom:18px;
    left:18px;
    right:18px;
    height:42px;
    display:flex;
    align-items:center;
    gap:8px;
}}

.hamburger {{
    width:32px;
    height:32px;
    border-radius:50%;
    background:white;
    text-align:center;
    line-height:32px;
    font-size:22px;
    color:#50768a;
    cursor:pointer;
}}

.chat-input {{
    flex:1;
    height:34px;
    background:white;
    border-radius:22px;
    color:#444;
    font-size:12px;
    padding-left:14px;
    border:none;
    outline:none;
}}

.send {{
    width:40px;
    height:40px;
    border-radius:50%;
    background:linear-gradient(135deg,#6ec6ff,#1c6fa4);
    color:white;
    text-align:center;
    line-height:40px;
    font-size:20px;
    cursor:pointer;
}}
</style>
</head>

<body>
<div class="phone">

    <div class="topbar">
        <a href="/Customer" target="_self" style="text-decoration:none;">
            <div class="back">‹</div>
        </a>

        <img class="avatar" src="data:image/png;base64,{robot}">
        <div class="dot"></div>
        <div class="status">Ready to assist</div>
    </div>

    <div id="chatBox" class="chat-box">
        <div class="msg bot">Hi, how can I help you?</div>
    </div>

    <div id="menu" class="menu">
        <div>Network Test</div>
        <div>Internet Usage</div>
        <div>Renew Package</div>
        <div>International Calls</div>
        <div>Offers & Games</div>
        <div>Contact Support</div>
    </div>

    <div class="bottom">
        <div class="hamburger">≡</div>
        <input class="chat-input" placeholder="Type your question here...">
        <div class="send">➤</div>
    </div>

</div>
</body>
</html>
"""

components.html(html, height=730)


st.markdown('<div class="quick-title">Quick Services</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("Network"):
        send_message("Network Test")
        st.rerun()

with c2:
    if st.button("Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("Renew"):
        send_message("Renew Package")
        st.rerun()

with c4:
    if st.button("Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("Offers"):
        send_message("Offers & Games")
        st.rerun()

with c6:
    if st.button("Support"):
        send_message("Contact Support")
        st.rerun()
        
chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    safe_msg = html_lib.escape(str(message))
    chat_html += f'<div class="msg {cls}">{safe_msg}</div>'

chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)

st.markdown('<div class="input-wrap">', unsafe_allow_html=True)

user_input = st.chat_input("Type your question here...")

st.markdown('</div>', unsafe_allow_html=True)

if user_input:
    send_message(user_input)
    st.rerun()
