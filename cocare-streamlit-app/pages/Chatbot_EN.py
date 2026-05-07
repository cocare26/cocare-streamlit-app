import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import html as html_lib

from engine.chatbot_engine import chatbot_engine

st.set_page_config(page_title="AI Agent", layout="centered")

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"role": "bot", "text": "Hi, how can I help you?"}
    ]

if "last_msg" not in st.session_state:
    st.session_state.last_msg = ""

msg = st.query_params.get("msg", "")

if msg and msg != st.session_state.last_msg:
    st.session_state.last_msg = msg

    st.session_state.chat_messages.append({
        "role": "user",
        "text": msg
    })

    try:
        result = chatbot_engine(msg)
        reply = result.get("response", "No response generated.")
    except Exception as e:
        reply = f"Error while processing message: {e}"

    st.session_state.chat_messages.append({
        "role": "bot",
        "text": reply
    })


robot = ""
if os.path.exists("robot_head.png"):
    with open("robot_head.png", "rb") as f:
        robot = base64.b64encode(f.read()).decode()


messages_html = ""

for m in st.session_state.chat_messages:
    cls = "user" if m["role"] == "user" else "bot"
    safe_text = html_lib.escape(m["text"])
    messages_html += f'<div class="msg {cls}">{safe_text}</div>'


avatar_html = ""
if robot:
    avatar_html = f'<img class="avatar" src="data:image/png;base64,{robot}">'


html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
body {{
    margin:0;
    background:#eef3f6;
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
    z-index:10;
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
    clear:both;
    word-wrap:break-word;
}}

.bot {{
    background:white;
    color:#222;
    float:left;
}}

.user {{
    background:#1c6fa4;
    color:white;
    float:right;
}}

.menu {{
    display:none;
    position:absolute;
    left:38px;
    bottom:90px;
    width:160px;
    background:white;
    border-radius:8px;
    box-shadow:0 4px 12px rgba(0,0,0,.18);
    padding:8px 0;
    z-index:20;
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
    z-index:10;
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
    flex-shrink:0;
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
    border:none;
    flex-shrink:0;
}}
</style>
</head>

<body>
<div class="phone">

    <div class="topbar">
        <a href="/?page=customer" target="_parent" style="text-decoration:none;">
            <div class="back">‹</div>
        </a>
        {avatar_html}
        <div class="dot"></div>
        <div class="status">Ready to assist</div>
    </div>

    <div id="chatBox" class="chat-box">
        {messages_html}
    </div>

    <div id="menu" class="menu">
        <div onclick="quickMsg('Network Test')">Network Test</div>
        <div onclick="quickMsg('Internet Usage')">Internet Usage</div>
        <div onclick="quickMsg('Renew Package')">Renew Package</div>
        <div onclick="quickMsg('International Calls')">International Calls</div>
        <div onclick="quickMsg('Offers and Games')">Offers & Games</div>
        <div onclick="quickMsg('Contact Support')">Contact Support</div>
    </div>

    <div class="bottom">
        <div class="hamburger" onclick="toggleMenu()">≡</div>

        <input
            id="chatInput"
            class="chat-input"
            placeholder="Type your question here..."
            onkeydown="checkEnter(event)"
        >

        <button class="send" onclick="sendMessage()">➤</button>
    </div>

</div>

<script>
function toggleMenu() {{
    const menu = document.getElementById("menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}}

function sendToStreamlit(text) {{
    const path = window.parent.location.pathname;
    window.parent.location.href = path + "?msg=" + encodeURIComponent(text);
}}

function sendMessage() {{
    const input = document.getElementById("chatInput");
    const text = input.value.trim();

    if (text === "") return;

    sendToStreamlit(text);
}}

function quickMsg(text) {{
    sendToStreamlit(text);
}}

function checkEnter(event) {{
    if (event.key === "Enter") {{
        sendMessage();
    }}
}}

const chatBox = document.getElementById("chatBox");
chatBox.scrollTop = chatBox.scrollHeight;
</script>

</body>
</html>
"""

components.html(html, height=730)
