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

def handle_message(text):
    st.session_state.chat_messages.append({
        "role": "user",
        "text": text
    })

    try:
        result = chatbot_engine(text)
        reply = result.get("response", "No response generated.")
    except Exception as e:
        reply = f"Error: {e}"

    st.session_state.chat_messages.append({
        "role": "bot",
        "text": reply
    })

robot = ""

if os.path.exists("robot_head.png"):
    with open("robot_head.png", "rb") as f:
        robot = base64.b64encode(f.read()).decode()

avatar_html = ""

if robot:
    avatar_html = f'<img class="avatar" src="data:image/png;base64,{robot}">'

messages_html = ""

for m in st.session_state.chat_messages:
    cls = "user" if m["role"] == "user" else "bot"
    safe_text = html_lib.escape(m["text"])
    messages_html += f'<div class="msg {cls}">{safe_text}</div>'

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
    display:block;
    position:absolute;
    left:38px;
    bottom:18px;
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

</div>

<script>
const chatBox = document.getElementById("chatBox");
chatBox.scrollTop = chatBox.scrollHeight;
</script>

</body>
</html>
"""

components.html(html, height=730)

st.markdown("""
<style>
div[data-testid="stChatInput"] {
    width:420px;
    margin:auto;
    margin-top:-78px;
}

div[data-testid="stChatInput"] textarea {
    border-radius:22px;
    min-height:42px;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(3)

quick_actions = [
    "Network Test",
    "Internet Usage",
    "Renew Package",
    "International Calls",
    "Offers & Games",
    "Contact Support"
]

for i, action in enumerate(quick_actions):
    if cols[i % 3].button(action, key=f"quick_{i}"):
        handle_message(action)
        st.rerun()

user_text = st.chat_input("Type your question here...")

if user_text:
    handle_message(user_text)
    st.rerun()
