import streamlit as st
import base64
import html as html_lib
import os
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

CHAT_KEY = "chat_en_final_v3"

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
    # إضافة رد تلقائي بسيط للعرض
    reply = get_bot_response(text)
    st.session_state[CHAT_KEY].append(("bot", reply))

# --- CSS لتصحيح التصميم وجعله مطابقاً للصورة ---
st.markdown(f"""
<style>
    /* الحاوية الأساسية */
    [data-testid="stAppViewContainer"] {{
        background:#eef2f7;
        direction: ltr !important;
    }}
    .block-container {{
        max-width: 430px !important;
        margin: auto;
        padding: 20px 15px !important;
        background: linear-gradient(180deg, #c7e6fb, #dff1ff);
        border-radius: 35px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }}
    
    /* الكرت العلوي */
    .top-card {{
        background: white;
        border-radius: 15px;
        padding: 10px 15px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }}
    
    /* منطقة الشات */
    .chat-scroll {{
        height: 380px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding: 10px;
        margin-bottom: 10px;
    }}
    
    /* فقاعات الكلام */
    .bubble {{
        max-width: 80%;
        padding: 10px 15px;
        border-radius: 18px;
        font-size: 14px;
        line-height: 1.4;
    }}
    .bot-bubble {{
        background: white;
        color: #333;
        align-self: flex-start;
        border-bottom-left-radius: 2px;
    }}
    .user-bubble {{
        background: #1677e8;
        color: white;
        align-self: flex-end;
        border-bottom-right-radius: 2px;
    }}

    /* الأزرار */
    div[data-testid="stButton"] button {{
        width: 100%;
        border-radius: 12px !important;
        background: white !important;
        color: #1677e8 !important;
        border: none !important;
        font-size: 12px !important;
        height: 45px;
    }}
</style>
""", unsafe_allow_html=True)

# --- Header (Top Card) ---
st.markdown(f"""
<div class="top-card">
    <div style="display:flex; align-items:center; gap:10px;">
        <div style="width:35px; height:35px; background:#000; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-size:10px;">AI</div>
        <div style="font-weight:bold; font-size:14px; color:#333;">Ready to help</div>
    </div>
    <div style="color:#777; font-size:12px;">📍 Amman</div>
</div>
""", unsafe_allow_html=True)

# --- Quick Services Grid ---
st.write("**Quick Services**")
c1, c2, c3 = st.columns(3)
with c1: 
    if st.button("Network Check"): send_message("Network Check"); st.rerun()
with c2: 
    if st.button("Internet Usage"): send_message("Internet Usage"); st.rerun()
with c3: 
    if st.button("Renew Plan"): send_message("Renew Plan"); st.rerun()

c4, c5, c6 = st.columns(3)
with c4: 
    if st.button("Intl. Calls"): send_message("Intl. Calls"); st.rerun()
with c5: 
    if st.button("Gaming Offers"): send_message("Gaming Offers"); st.rerun()
with c6: 
    if st.button("Support"): send_message("Support"); st.rerun()

st.write("---")

# --- Chat Display ---
# هنا يتم بناء الشات كـ HTML واحد لضمان عدم ظهور الأكواد
chat_html = '<div class="chat-scroll">'
for role, msg in st.session_state[CHAT_KEY]:
    if role == "bot":
        chat_html += f'<div class="bubble bot-bubble">{msg}</div>'
    else:
        chat_html += f'<div class="bubble user-bubble">{msg}</div>'
chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)

# --- Input Area ---
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="Type your message here...", label_visibility="collapsed")
    submit = st.form_submit_button("Send")
    if submit and user_input:
        send_message(user_input)
        st.rerun()

if st.button("Clear Chat"):
    st.session_state[CHAT_KEY] = [("bot", "Hello 👋 I am CoCare AI assistant...")]
    st.rerun()
