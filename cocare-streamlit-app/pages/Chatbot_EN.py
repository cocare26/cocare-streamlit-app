import streamlit as st
import base64
import html as html_lib
import os
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

PHONE_WIDTH = 430
CHAT_KEY = "chat_en_messages_v3"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hello 👋 I am CoCare AI assistant, how can I help you today?")
    ]


def save_chat_history():
    pass


def reset_context():
    pass


def get_bot_response(message):
    message = str(message).lower()

    if "network" in message or "check" in message:
        return "Checking the network status now..."

    elif "usage" in message or "internet" in message:
        return "You can check your internet usage in the Usage section."

    elif "renew" in message or "plan" in message:
        return "You can renew your plan from the Plans section."

    elif "international" in message or "calls" in message:
        return "International calling services are available based on your line type."

    elif "offers" in message or "gaming" in message:
        return "You can view offers and gaming bundles in the Offers section."

    elif "support" in message or "contact" in message:
        return "Your request has been sent to the support team."

    else:
        return "CoCare assistant is processing your request."


def send_message(text):
    if not text or not text.strip():
        return

    st.session_state[CHAT_KEY].append(("user", text.strip()))
    st.session_state[CHAT_KEY].append(("bot", "Typing..."))

    time.sleep(0.25)

    st.session_state[CHAT_KEY].pop()

    reply = get_bot_response(text)

    st.session_state[CHAT_KEY].append(("bot", reply))

    save_chat_history()


def img_to_base64(path):
    paths = [
        os.path.join(os.path.dirname(__file__), path),
        os.path.join(os.path.dirname(__file__), "..", path),
        path
    ]

    for full_path in paths:
        try:
            if os.path.exists(full_path):
                with open(full_path, "rb") as f:
                    return base64.b64encode(f.read()).decode()
        except Exception:
            pass

    return ""


robot = (
    img_to_base64("robot_black.png")
    or img_to_base64("robot_black(2).png")
    or img_to_base64("robot_head.png")
    or img_to_base64("robot.png")
)

if robot:
    avatar_top = f'<img class="avatar-top" src="data:image/png;base64,{robot}">'
    avatar_msg = f'<img class="msg-avatar" src="data:image/png;base64,{robot}">'
else:
    avatar_top = '<div class="avatar-top fallback-avatar">AI</div>'
    avatar_msg = '<div class="msg-avatar fallback-small">AI</div>'


st.markdown(f"""
<style>

html, body, [data-testid="stAppViewContainer"] {{
    background:#eef2f7 !important;
    direction:ltr; /* Changed to Left-to-Right */
}}

header, footer, #MainMenu, [data-testid="stToolbar"] {{
    display:none !important;
    visibility:hidden !important;
}}

.block-container {{
    width:430px !important;
    max-width:430px !important;
    min-height:700px !important;
    margin:24px auto !important;
    padding:24px 16px 18px !important;
    background:linear-gradient(180deg,#c7e6fb,#dff1ff) !important;
    border-radius:38px !important;
    box-shadow:0 12px 35px rgba(0,0,0,.12) !important;
    overflow:hidden !important;
}}

.top-card {{
    background:white;
    border-radius:18px;
    padding:9px 12px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 5px 15px rgba(0,0,0,.10);
    margin-bottom:16px;
}}

.location {{
    font-size:11px;
    font-weight:800;
    color:#0f2446;
}}

.ready {{
    font-size:13px;
    font-weight:900;
    color:#111827;
    display:flex;
    align-items:center;
    gap:6px;
}}

.dot {{
    width:7px;
    height:7px;
    background:#22c55e;
    border-radius:50%;
    display:inline-block;
}}

.avatar-top {{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
    background:#111827;
    box-shadow:0 3px 10px rgba(0,0,0,.15);
}}

.fallback-avatar {{
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:900;
}}

.quick-title {{
    color:#0f2446;
    font-size:12px;
    font-weight:900;
    margin:8px 0 10px;
    text-align:left; /* Changed to left */
}}

div[data-testid="column"] {{
    padding:4px !important;
}}

div[data-testid="stButton"] button {{
    width:100%;
    min-height:40px;
    border:none !important;
    border-radius:18px !important;
    background:white !important;
    color:#003f88 !important;
    font-weight:700 !important;
    font-size:12px !important;
    box-shadow:0 5px 14px rgba(0,0,0,.10) !important;
}}

div[data-testid="stButton"] button:hover {{
    background:#eef7ff !important;
}}

.chat-area {{
    height:315px;
    overflow-y:auto;
    padding:12px 8px;
    margin-top:12px;
    margin-bottom:10px;
}}

.message-row {{
    display:flex;
    align-items:flex-end;
    gap:8px;
    margin-bottom:12px;
}}

.bot-row {{
    justify-content:flex-start;
}}

.user-row {{
    justify-content:flex-end;
    flex-direction: row-reverse; /* Align avatar to the right for user */
}}

.msg {{
    max-width:72%;
    padding:9px 13px;
    border-radius:15px;
    font-size:13px;
    line-height:1.5;
    word-wrap:break-word;
    white-space:pre-wrap;
    box-shadow:0 3px 10px rgba(0,0,0,.08);
}}

.bot {{
    background:white;
    color:#111827;
    border-bottom-left-radius:5px; /* Flipped for English */
    text-align:left;
}}

.user {{
    background:#1677e8;
    color:white;
    border-bottom-right-radius:5px; /* Flipped for English */
    text-align:left;
}}

.msg-avatar {{
    width:34px;
    height:34px;
    border-radius:50%;
    object-fit:cover;
    background:white;
    flex-shrink:0;
    box-shadow:0 2px 8px rgba(0,0,0,.12);
}}

.user-avatar {{
    width:34px;
    height:34px;
    border-radius:50%;
    background:#dbeafe;
    color:#0f4f91;
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:900;
    flex-shrink:0;
    font-size: 10px;
}}

div[data-testid="stTextInput"] input {{
    width:100% !important;
    height:44px !important;
    border:none !important;
    border-radius:24px !important;
    background:white !important;
    box-shadow:0 3px 10px rgba(0,0,0,.08) !important;
    padding:0 18px !important;
    color:#111827 !important;
    direction:ltr !important;
    text-align:left !important;
    font-size:14px !important;
}}

div[data-testid="stTextInput"] input::placeholder {{
    color:#8b95a7 !important;
    text-align:left !important;
}}

div[data-testid="stFormSubmitButton"] {{
    display:flex !important;
    justify-content:flex-end !important;
}}

div[data-testid="stFormSubmitButton"] button {{
    width:92px !important;
    height:42px !important;
    min-height:42px !important;
    border:none !important;
    border-radius:22px !important;
    background:#1677e8 !important;
    color:white !important;
    font-weight:900 !important;
    font-size:15px !important;
    box-shadow:0 4px 12px rgba(22,119,232,.25) !important;
    margin-top:4px !important;
}}

</style>
""", unsafe_allow_html=True)


st.markdown(f"""
<div class="top-card">
    {avatar_top}
    <div class="ready">
        <span class="dot"></span>
        Ready to help
    </div>
    <div class="location">📍 Amman</div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="quick-title">Quick Services</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Network Check"):
        send_message("Network Check")
        st.rerun()

with c2:
    if st.button("Internet Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("Renew Plan"):
        send_message("Renew Plan")
        st.rerun()

c4, c5, c6 = st.columns(3)

with c4:
    if st.button("Intl. Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("Gaming Offers"):
        send_message("Offers and Gaming")
        st.rerun()

with c6:
    if st.button("Support"):
        send_message("Contact Support")
        st.rerun()


chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:

    safe_msg = html_lib.escape(str(message))

    if role == "user":
        chat_html += f"""
        <div class="message-row user-row">
            <div class="user-avatar">YOU</div>
            <div class="msg user">{safe_msg}</div>
        </div>
        """
    else:
        chat_html += f"""
        <div class="message-row bot-row">
            {avatar_msg}
            <div class="msg bot">{safe_msg}</div>
        </div>
        """

chat_html += "</div>"

st.markdown(chat_html, unsafe_allow_html=True)


if st.button("Clear Chat"):
    st.session_state[CHAT_KEY] = [
        ("bot", "Hello 👋 I am CoCare AI assistant, how can I help you today?")
    ]
    reset_context()
    st.rerun()


with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "",
        placeholder="Type your message here...",
        label_visibility="collapsed"
    )
    send_btn = st.form_submit_button("Send")

    if send_btn and user_input.strip():
        send_message(user_input)
        st.rerun()
