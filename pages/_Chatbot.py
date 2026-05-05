import streamlit as st
import base64
from engine import process_message

st.set_page_config(page_title="AI Agent", layout="centered")

with open("robot_head.png", "rb") as f:
    robot = base64.b64encode(f.read()).decode()

if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = [
        {"type": "bot", "text": "Hi, how can I help you?"}
    ]

if "user_id" not in st.session_state:
    st.session_state.user_id = "customer_1"

if "region" not in st.session_state:
    st.session_state.region = "Amman"

quick_replies = {
    "Network Test": "Your network signal is strong.",
    "Internet Usage": "Your current internet usage is available in your dashboard.",
    "Renew Package": "You can renew your package from the packages section.",
    "International Calls": "International call options are available for your line.",
    "Offers & Games": "Current offers and games are available in the offers section.",
    "Contact Support": "Support team will contact you soon."
}

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background:#eef2f7;
}
.block-container {
    max-width:430px;
    min-height:700px;
    margin:auto;
    padding:20px 18px;
    border-radius:42px;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    box-shadow:0 8px 25px rgba(0,0,0,.25);
}
header, footer { visibility:hidden; }

.topbar {
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
    margin-bottom:14px;
}
.back { font-size:28px; color:#436577; text-decoration:none; }
.avatar { width:42px; height:42px; border-radius:50%; object-fit:cover; }
.dot { width:8px; height:8px; background:#36c06a; border-radius:50%; }
.status { font-size:15px; font-weight:700; color:#222; }

.msg {
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.4;
    word-wrap:break-word;
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

.chat-box {
    height:360px;
    overflow-y:auto;
    padding:10px;
}
div.stButton > button {
    width:100%;
    border-radius:20px;
    border:none;
    background:white;
    color:#1c6fa4;
    font-size:12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="topbar">
    <a href="/?page=customer" target="_top" class="back">‹</a>
    <img class="avatar" src="data:image/png;base64,{robot}">
    <div class="dot"></div>
    <div class="status">Ready to assist</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="chat-box">', unsafe_allow_html=True)

for msg in st.session_state.chat_messages:
    css_class = "user" if msg["type"] == "user" else "bot"
    st.markdown(
        f'<div class="msg {css_class}">{msg["text"]}</div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("**Quick Services**")

qcols = st.columns(2)
quick_keys = list(quick_replies.keys())

for i, key in enumerate(quick_keys):
    with qcols[i % 2]:
        if st.button(key):
            st.session_state.chat_messages.append({"type": "user", "text": key})
            st.session_state.chat_messages.append({"type": "bot", "text": quick_replies[key]})
            st.rerun()

with st.form("chat_form", clear_on_submit=True):
    user_message = st.text_input(
        "message",
        placeholder="Type your question here...",
        label_visibility="collapsed"
    )
    submitted = st.form_submit_button("➤ Send")

if submitted and user_message.strip():
    st.session_state.chat_messages.append({"type": "user", "text": user_message})

    try:
        result = process_message(
            user_message=user_message,
            user_id=st.session_state.user_id,
            region=st.session_state.region
        )

        bot_text = result.get("response", "I received your request.")
        followup = result.get("followup_response")

        if followup:
            bot_text += "\n\n" + followup

    except Exception as e:
        bot_text = "Sorry, something went wrong while analyzing your message."
        print("Chatbot engine error:", e)

    st.session_state.chat_messages.append({"type": "bot", "text": bot_text})
    st.rerun()
