import streamlit as st
import streamlit.components.v1 as components
import base64
import html as html_lib
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

# =========================
# SESSION
# =========================

CHAT_KEY = "chat_messages"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]

# =========================
# FUNCTIONS
# =========================

def save_chat_history():
    pass

def reset_context():
    pass

def get_bot_response(message):
    message = message.lower()

    if "network" in message:
        return "📡 Running network diagnostics..."

    elif "usage" in message:
        return "📊 Your current internet usage is 82 GB."

    elif "renew" in message:
        return "🔄 Your package can be renewed from the payments section."

    elif "international" in message:
        return "🌍 International call packages are available now."

    elif "offers" in message:
        return "🎮 Latest offers and gaming packages are available."

    elif "support" in message:
        return "☎️ Support team has been notified."

    else:
        return "🤖 CoCare AI is processing your request."

def send_message(text):

    st.session_state[CHAT_KEY].append(("user", text))

    st.session_state[CHAT_KEY].append(("bot", "Typing..."))

    time.sleep(0.5)

    st.session_state[CHAT_KEY].pop()

    bot_reply = get_bot_response(text)

    st.session_state[CHAT_KEY].append(("bot", bot_reply))

    save_chat_history()

# =========================
# PAGE STYLE
# =========================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:480px;
    padding-top:20px;
}

header, footer{
    visibility:hidden;
}

/* PHONE */

.phone{
    background:white;
    border-radius:35px;
    padding:18px;
    box-shadow:0 8px 30px rgba(0,0,0,.15);
}

/* TOP */

.top-bar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:15px;
}

.title{
    font-size:26px;
    font-weight:900;
    color:#0f2446;
}

.sub{
    color:#5b6472;
    font-size:13px;
}

/* CHAT */

.chat-area{
    height:420px;
    overflow-y:auto;
    padding:10px;
    background:#f8fbff;
    border-radius:22px;
    margin-bottom:15px;
}

.message-row{
    display:flex;
    align-items:flex-end;
    margin-bottom:12px;
}

.user-row{
    justify-content:flex-end;
}

.bot-row{
    justify-content:flex-start;
}

.msg{
    padding:12px 16px;
    border-radius:18px;
    max-width:75%;
    font-size:14px;
    line-height:1.5;
    word-wrap:break-word;
}

.user{
    background:#2f80ed;
    color:white;
    border-bottom-right-radius:5px;
}

.bot{
    background:white;
    color:#111827;
    border-bottom-left-radius:5px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
}

.msg-avatar{
    width:38px;
    height:38px;
    border-radius:50%;
    margin:0 8px;
}

.user-avatar{
    background:#dbeafe;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
}

/* QUICK SERVICES */

.quick-title{
    margin-top:5px;
    margin-bottom:10px;
    font-size:15px;
    font-weight:800;
    color:#0f2446;
}

/* BUTTONS */

.stButton button{
    width:100%;
    border:none;
    border-radius:15px;
    padding:10px;
    background:#eef6ff;
    color:#0f2446;
    font-weight:700;
    transition:0.2s;
}

.stButton button:hover{
    background:#dbe9ff;
    color:#2f80ed;
    transform:translateY(-2px);
}

/* CHAT INPUT */

[data-testid="stChatInput"]{
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ROBOT IMAGE
# =========================

robot = ""

# =========================
# PHONE CONTAINER
# =========================

st.markdown('<div class="phone">', unsafe_allow_html=True)

st.markdown("""
<div class="top-bar">
    <div>
        <div class="title">CoCare AI</div>
        <div class="sub">Telecom Assistant</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# CHAT AREA
# =========================

chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:

    safe_msg = html_lib.escape(str(message))

    if role == "user":

        chat_html += f"""
<div class="message-row user-row">
    <div class="msg user">{safe_msg}</div>
    <div class="msg-avatar user-avatar">👤</div>
</div>
"""

    else:

        typing_class = " typing" if str(message) == "Typing..." else ""

        if robot:
            avatar_html = f'<img class="msg-avatar" src="data:image/png;base64,{robot}">'
        else:
            avatar_html = '<div class="msg-avatar user-avatar">🤖</div>'

        chat_html += f"""
<div class="message-row bot-row">
    {avatar_html}
    <div class="msg bot{typing_class}">{safe_msg}</div>
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

# =========================
# QUICK SERVICES
# =========================

st.markdown(
    '<div class="quick-title">⚡ Quick Services</div>',
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

# =========================
# CLEAR CHAT
# =========================

if st.button("🗑 Clear Chat"):

    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]

    reset_context()
    save_chat_history()

    st.rerun()

# =========================
# CHAT INPUT
# =========================

user_input = st.chat_input("Type your question here...")

if user_input:

    send_message(user_input)

    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
