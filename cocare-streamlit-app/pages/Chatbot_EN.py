import streamlit as st
import streamlit.components.v1 as components
import base64
import os
import sys
from urllib.parse import unquote

# =========================
# IMPORT MODEL
# =========================
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Agent", layout="centered")

# =========================
# REGION
# =========================
if "region" not in st.session_state:
    st.session_state["region"] = "Amman"

region = st.session_state["region"]

# =========================
# IMAGE
# =========================
def img_to_base64(path):
    full_path = os.path.join(os.path.dirname(__file__), "..", path)

    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    return ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

# =========================
# HANDLE MESSAGE
# =========================
params = st.query_params

if "msg" in params:

    user_msg = unquote(params["msg"])

    result = process_message(
        user_msg,
        user_id="customer_1",
        region=region
    )

    response = str(result.get("response", "")).strip()
    followup = str(result.get("followup_response", "")).strip()

    bot_reply = f"{response}\n\n{followup}".strip()

    st.session_state["last_user_msg"] = user_msg
    st.session_state["last_bot_reply"] = bot_reply

else:

    if "last_user_msg" not in st.session_state:
        st.session_state["last_user_msg"] = ""

    if "last_bot_reply" not in st.session_state:
        st.session_state["last_bot_reply"] = "Hi, how can I help you?"

# =========================
# CHAT CONTENT
# =========================
last_user_msg = st.session_state.get("last_user_msg", "")
last_bot_reply = st.session_state.get("last_bot_reply", "")

user_msg_html = ""

if last_user_msg:
    user_msg_html = f'''
    <div class="msg user">
        {last_user_msg}
    </div>
    '''

# =========================
# HTML UI
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
    white-space:pre-wrap;
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

        <img class="avatar"
             src="data:image/png;base64,{robot}">

        <div class="dot"></div>

        <div class="status">
            Ready to assist
        </div>

    </div>

    <div id="chatBox" class="chat-box">

        {user_msg_html}

        <div class="msg bot">
            {last_bot_reply}
        </div>

    </div>

    <div id="menu" class="menu">

        <div onclick="sendToModel('Network Test')">
            Network Test
        </div>

        <div onclick="sendToModel('Internet Usage')">
            Internet Usage
        </div>

        <div onclick="sendToModel('Renew Package')">
            Renew Package
        </div>

        <div onclick="sendToModel('International Calls')">
            International Calls
        </div>

        <div onclick="sendToModel('Offers & Games')">
            Offers & Games
        </div>

        <div onclick="sendToModel('Contact Support')">
            Contact Support
        </div>

    </div>

    <div class="bottom">

        <div class="hamburger"
             onclick="toggleMenu()">
             ≡
        </div>

        <input
            id="chatInput"
            class="chat-input"
            placeholder="Type your question here..."
            onkeydown="checkEnter(event)"
        >

        <div class="send"
             onclick="sendInput()">
             ➤
        </div>

    </div>

</div>

<script>

function toggleMenu(){{
    const menu = document.getElementById("menu");

    menu.style.display =
        menu.style.display === "block"
        ? "none"
        : "block";
}}

function sendToModel(text){{
    const url =
        new URL(window.parent.location.href);

    url.searchParams.set("msg", text);

    window.parent.location.href =
        url.toString();
}}

function sendInput(){{
    const input =
        document.getElementById("chatInput");

    const text =
        input.value.trim();

    if(text === "") return;

    const url =
        new URL(window.parent.location.href);

    url.searchParams.set("msg", text);

    window.parent.location.href =
        url.toString();
}}

function checkEnter(event){{
    if(event.key === "Enter"){{
        sendInput();
    }}
}}

</script>

</body>
</html>
"""

components.html(html, height=730)
