import streamlit as st
import base64
import os
import sys
import html as html_lib
import pandas as pd

# =========================
# IMPORT COCARE ENGINE
# =========================
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Agent", layout="centered")

CHAT_KEY = "chat_en_messages"

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
    try:
        full_path = os.path.join(os.path.dirname(__file__), "..", path)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        pass
    return ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

# =========================
# INIT CHAT
# =========================
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi, how can I help you?")
    ]

if "chat_logs" not in st.session_state:
    st.session_state.chat_logs = []

# =========================
# BOT REPLY
# =========================
def get_bot_reply(user_text):
    quick_map = {
        "Network Test": "Check my network status",
        "Internet Usage": "I want to check my internet usage",
        "Renew Package": "I want to renew my package",
        "International Calls": "Tell me about international calls",
        "Offers & Games": "What offers are available?",
        "Contact Support": "I need technical support",
    }

    msg = quick_map.get(user_text, user_text)

    user_id = st.session_state.get("user_id", "customer_1")
    region = st.session_state.get("region", "Amman")

    try:
        result = process_message(
            msg,
            user_id=user_id,
            region=region
        )

        st.session_state.chat_logs.append(result)

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()

        reply = f"{response}\n\n{followup}".strip()

        if not reply:
            return "Could you clarify more?"

        return reply

    except Exception as e:
        return f"Connection error: {e}"

def send_message(text):
    if not text:
        return

    st.session_state[CHAT_KEY].append(("user", text))
    bot_reply = get_bot_reply(text)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))

# =========================
# STYLE
# =========================
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#eef2f7;
    direction:ltr;
}

header, footer, #MainMenu {
    visibility:hidden;
}

.block-container {
    max-width:430px;
    height:730px;
    margin:auto;
    padding:14px 16px 8px;
    border-radius:42px;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    box-shadow:0 12px 30px rgba(0,0,0,.15);
    overflow:hidden;
}

.topbar {
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
    margin-bottom:10px;
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

.region-label {
    margin-left:auto;
    font-size:11px;
    color:#436577;
    font-weight:700;
}

.quick-title {
    font-size:13px;
    font-weight:800;
    color:#102646;
    margin:4px 0 6px;
}

div[data-testid="stButton"] button {
    border-radius:18px;
    border:none;
    background:white;
    color:#102646;
    font-weight:800;
    font-size:11px;
    box-shadow:0 3px 8px rgba(0,0,0,.10);
    height:36px;
}

div[data-testid="stButton"] button:hover {
    background:#eef6ff;
    color:#1c6fa4;
}

.chat-area {
    height:350px;
    overflow-y:auto;
    padding:10px 4px;
    margin-top:10px;
    margin-bottom:8px;
}

.msg {
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.5;
    white-space:pre-wrap;
    text-align:left;
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

.input-wrap {
    background:rgba(255,255,255,.65);
    border-radius:22px;
    padding:8px;
    margin-top:4px;
}

div[data-testid="stChatInput"] {
    position:relative !important;
    bottom:auto !important;
    background:transparent !important;
    padding:0 !important;
}

div[data-testid="stChatInput"] textarea {
    direction:ltr;
    border-radius:22px;
    border:none;
    background:white;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# TOP BAR
# =========================
st.markdown(f"""
<div class="topbar">
    <a href="/Customer" target="_self" style="text-decoration:none;">
        <div class="back">‹</div>
    </a>
    <img class="avatar" src="data:image/png;base64,{robot}">
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
    <div class="region-label">📍 {html_lib.escape(region)}</div>
</div>
""", unsafe_allow_html=True)

# =========================
# QUICK SERVICES
# =========================
st.markdown('<div class="quick-title">Quick Services</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("Network Test"):
        send_message("Network Test")
        st.rerun()

with c2:
    if st.button("Internet Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("Renew Package"):
        send_message("Renew Package")
        st.rerun()

with c4:
    if st.button("International Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("Offers & Games"):
        send_message("Offers & Games")
        st.rerun()

with c6:
    if st.button("Contact Support"):
        send_message("Contact Support")
        st.rerun()

# =========================
# CHAT DISPLAY
# =========================
chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    safe_msg = html_lib.escape(str(message))
    chat_html += f'<div class="msg {cls}">{safe_msg}</div>'

chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)

# =========================
# INPUT
# =========================
st.markdown('<div class="input-wrap">', unsafe_allow_html=True)

user_input = st.chat_input("Type your question here...")

st.markdown('</div>', unsafe_allow_html=True)

if user_input:
    send_message(user_input)
    st.rerun()

# =========================
# OPTIONAL DASHBOARD DATA
# =========================
if st.session_state.chat_logs:
    with st.expander("Chatbot Dashboard"):
        df = pd.DataFrame(st.session_state.chat_logs)

        st.metric("Total Messages", len(df))

        if "sentiment" in df.columns:
            st.metric("Negative Sentiment", len(df[df["sentiment"] == "negative"]))

        if "network_problem" in df.columns:
            st.metric("Network Problems", len(df[df["network_problem"] == True]))

        st.dataframe(df)
