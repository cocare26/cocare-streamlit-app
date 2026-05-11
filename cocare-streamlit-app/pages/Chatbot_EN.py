import streamlit as st
import base64
import html as html_lib
import os
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

CHAT_KEY = "chat_en_messages_v3"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hello 👋 I am CoCare AI assistant, how can I help you today?")
    ]

def get_bot_response(message):
    message = str(message).lower()
    if "network" in message: return "Checking the network status now..."
    elif "usage" in message: return "You can check your internet usage in the Usage section."
    elif "renew" in message: return "You can renew your plan from the Plans section."
    elif "support" in message: return "Your request has been sent to the support team."
    else: return "CoCare assistant is processing your request."

def send_message(text):
    if not text or not text.strip(): return
    st.session_state[CHAT_KEY].append(("user", text.strip()))
    reply = get_bot_response(text)
    st.session_state[CHAT_KEY].append(("bot", reply))

def img_to_base64(path):
    # دالة وهمية للتبسيط، تأكد من وجود الصورة فعلياً
    return "" 

robot_b64 = img_to_base64("robot.png")
avatar_img = f'data:image/png;base64,{robot_b64}' if robot_b64 else "https://cdn-icons-png.flaticon.com/512/4712/4712035.png"

# --- CSS المحسن ---
st.markdown(f"""
<style>
    [data-testid="stAppViewContainer"] {{ background:#eef2f7; direction:ltr; }}
    .block-container {{
        max-width:430px; margin:auto; padding:20px;
        background: linear-gradient(180deg,#c7e6fb,#dff1ff);
        border-radius:35px; box-shadow:0 10px 25px rgba(0,0,0,0.1);
    }}
    .top-card {{
        background:white; border-radius:15px; padding:10px;
        display:flex; align-items:center; justify-content:space-between; margin-bottom:15px;
    }}
    .chat-area {{
        height: 350px; overflow-y: auto; padding: 10px;
        display: flex; flex-direction: column; gap: 10px;
    }}
    .msg-box {{
        max-width: 80%; padding: 10px 15px; border-radius: 15px;
        font-size: 14px; line-height: 1.4; position: relative;
    }}
    .bot-msg {{
        background: white; align-self: flex-start;
        border-bottom-left-radius: 2px; color: #333;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }}
    .user-msg {{
        background: #1677e8; color: white; align-self: flex-end;
        border-bottom-right-radius: 2px;
    }}
    .avatar {{ width: 30px; height: 30px; border-radius: 50%; margin-right: 8px; }}
    .row {{ display: flex; align-items: flex-end; margin-bottom: 10px; }}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown(f"""
<div class="top-card">
    <img src="{avatar_img}" style="width:40px; border-radius:50%;">
    <div style="font-weight:bold; color:#22c55e;">● Ready to help</div>
    <div style="font-size:12px;">📍 Amman</div>
</div>
""", unsafe_allow_html=True)

# --- Quick Actions ---
st.write("Quick Services")
cols = st.columns(3)
actions = ["Network Check", "Internet Usage", "Renew Plan", "Intl. Calls", "Gaming Offers", "Support"]
for i, action in enumerate(actions):
    if cols[i % 3].button(action, key=action):
        send_message(action)
        st.rerun()

# --- Chat Display ---
chat_container = ""
for role, msg in st.session_state[CHAT_KEY]:
    if role == "bot":
        chat_container += f'''
        <div class="row">
            <img src="{avatar_img}" class="avatar">
            <div class="msg-box bot-msg">{msg}</div>
        </div>'''
    else:
        chat_container += f'''
        <div class="row" style="justify-content: flex-end;">
            <div class="msg-box user-msg">{msg}</div>
        </div>'''

st.markdown(f'<div class="chat-area">{chat_container}</div>', unsafe_allow_html=True)

# --- Input ---
with st.form("input_form", clear_on_submit=True):
    user_input = st.text_input("Message", placeholder="Type here...", label_visibility="collapsed")
    if st.form_submit_button("Send") and user_input:
        send_message(user_input)
        st.rerun()

if st.button("Clear Chat"):
    st.session_state[CHAT_KEY] = [("bot", "Hello 👋 I am CoCare AI assistant...")]
    st.rerun()
