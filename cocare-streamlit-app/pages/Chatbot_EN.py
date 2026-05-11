import streamlit as st
import base64
import html as html_lib
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

PHONE_WIDTH = 430
PHONE_HEIGHT = 820

CHAT_KEY = "chat_en_messages"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi, I am CoCare AI Assistant. How can I help you?")
    ]


def save_chat_history():
    pass


def reset_context():
    pass


def get_bot_response(message):
    message = message.lower()

    if "network" in message:
        return "Running network diagnostics now..."

    elif "usage" in message:
        return "Your current internet usage is 82 GB."

    elif "renew" in message:
        return "You can renew your package from the payments section."

    elif "international" in message:
        return "International call packages are available now."

    elif "offers" in message or "games" in message:
        return "Latest offers and gaming packages are available."

    elif "support" in message:
        return "Your request has been sent to the support team."

    else:
        return "CoCare Assistant is processing your request."


def send_message(text):
    st.session_state[CHAT_KEY].append(("user", text))
    st.session_state[CHAT_KEY].append(("bot", "Typing..."))
    time.sleep(0.5)
    st.session_state[CHAT_KEY].pop()

    bot_reply = get_bot_response(text)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))
    save_chat_history()


def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


robot = img_to_base64("robot_black.png")


st.markdown(f"""
<style>

html, body, [data-testid="stAppViewContainer"]{{
    background:#d8e9f8;
    direction:ltr;
}}

.block-container{{
    width:{PHONE_WIDTH}px !important;
    max-width:{PHONE_WIDTH}px !important;
    min-height:{PHONE_HEIGHT}px !important;
    margin:auto;
    padding-top:18px;
}}

header, footer, #MainMenu{{
    visibility:hidden;
}}

.phone{{
    background:#f7fbff;
    border-radius:38px;
    padding:18px;
    box-shadow:0 12px 35px rgba(0,0,0,.15);
    min-height:{PHONE_HEIGHT}px;
    border:1px solid #d9e8f7;
    overflow:hidden;
}}

.top-bar{{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:18px;
}}

.title{{
    font-size:28px;
    font-weight:900;
    color:#0f2446;
}}

.sub{{
    color:#5b6472;
    font-size:14px;
}}

.chat-area{{
    height:420px;
    overflow-y:auto;
    padding:12px;
    background:#eef5fc;
    border-radius:24px;
    margin-bottom:18px;
    border:1px solid #d8e7f6;
}}

.message-row{{
    display:flex;
    align-items:flex-end;
    margin-bottom:14px;
}}

.user-row{{
    justify-content:flex-end;
}}

.bot-row{{
    justify-content:flex-start;
}}

.msg{{
    padding:13px 18px;
    border-radius:18px;
    max-width:75%;
    font-size:15px;
    line-height:1.7;
    word-wrap:break-word;
}}

.user{{
    background:linear-gradient(135deg,#4da3ff,#1677e8);
    color:white;
    border-bottom-right-radius:6px;
}}

.bot{{
    background:white;
    color:#111827;
    border-bottom-left-radius:6px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
}}

.msg-avatar{{
    width:42px;
    height:42px;
    border-radius:50%;
    margin:0 8px;
    object-fit:cover;
    background:white;
}}

.user-avatar{{
    background:#dbeafe;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
}}

.quick-title{{
    margin-top:5px;
    margin-bottom:12px;
    font-size:16px;
    font-weight:900;
    color:#0f2446;
}}

.stButton button{{
    width:100%;
    min-height:72px;
    border:none;
    border-radius:18px;
    padding:12px;
    background:white;
    color:#0f4f91;
    font-weight:800;
    box-shadow:0 4px 14px rgba(0,0,0,.08);
    transition:0.2s;
}}

.stButton button:hover{{
    background:#eef6ff;
    color:#2f80ed;
    transform:translateY(-2px);
}}

[data-testid="stChatInput"]{{
    width:100% !important;
}}

[data-testid="stChatInput"] textarea{{
    border-radius:24px !important;
    border:none !important;
    background:white !important;
    box-shadow:0 3px 12px rgba(0,0,0,.08);
}}

</style>
""", unsafe_allow_html=True)


st.markdown('<div class="phone">', unsafe_allow_html=True)

st.markdown(f"""
<div class="top-bar">

    <div>
        <div class="title">CoCare AI</div>
        <div class="sub">Smart Telecom Assistant</div>
    </div>

    <img class="msg-avatar"
    src="data:image/png;base64,{robot}"
    style="width:70px;height:70px;">

</div>
""", unsafe_allow_html=True)


st.markdown(
    '<div class="quick-title">Quick Services</div>',
    unsafe_allow_html=True
)

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


chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:

    safe_msg = html_lib.escape(str(message))

    if role == "user":

        chat_html += f"""
<div class="message-row user-row">
    <div class="msg user">{safe_msg}</div>
    <div class="msg-avatar user-avatar">U</div>
</div>
"""

    else:

        avatar_html = f'<img class="msg-avatar" src="data:image/png;base64,{robot}">'

        chat_html += f"""
<div class="message-row bot-row">
    {avatar_html}
    <div class="msg bot">{safe_msg}</div>
</div>
"""

chat_html += """
</div>

<script>
const chatArea = window.parent.document.querySelector('.chat-area');

if (chatArea) {
    chatArea.scrollTop = chatArea.scrollHeight;
}
</script>
"""

st.markdown(chat_html, unsafe_allow_html=True)


if st.button("Clear Chat"):

    st.session_state[CHAT_KEY] = [
        ("bot", "Hi, I am CoCare AI Assistant. How can I help you?")
    ]

    reset_context()
    save_chat_history()
    st.rerun()


user_input = st.chat_input("Type your message here...")

if user_input:
    send_message(user_input)
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
