import streamlit as st
import base64
import html
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from cocare import process_message
CHAT_KEY = "chat_messages_ar_final_clean"

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا، كيف أقدر أساعدك؟")
    ]

def get_bot_reply(text):
    original_text = str(text).strip()
    text_clean = original_text.lower()

    if text_clean in ["هاي", "هلا", "مرحبا", "hi", "hello"]:
        return "هلا وغلا 👋 كيف فيني أساعدك؟\n\nشو حاب تعرف؟"

    quick_map = {
        "فحص الشبكة": "افحص حالة الشبكة عندي",
        "استهلاك الإنترنت": "بدي أعرف استهلاك الإنترنت",
        "تجديد الباقة": "بدي أجدد الباقة",
        "المكالمات الدولية": "بدي أعرف عن المكالمات الدولية",
        "العروض": "شو العروض المتاحة؟",
        "الدعم": "بدي أتواصل مع الدعم الفني",
    }

    original_text = quick_map.get(text_clean, original_text)

    try:
        result = process_message(
            original_text,
            user_id="customer_1",
            region="Amman"
        )

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()
        reply = f"{response}\n\n{followup}".strip()

        if not reply or "تم استلام طلبك" in reply:
            return "ممكن توضحيلي أكثر؟\n\nاحكيلي تفاصيل أكثر"

        return reply

    except Exception as e:
        return f"صار خطأ بالربط:\n{e}"

def send_message(text):
    text = str(text).strip()
    if not text:
        return

    st.session_state[CHAT_KEY].append(("user", text))
    st.session_state[CHAT_KEY].append(("bot", get_bot_reply(text)))

st.markdown("""
<style>
.stApp { background:#eef2f7; }
.block-container { padding-top:20px; max-width:460px; }

.phone {
    width:420px;
    height:700px;
    margin:auto;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    direction:rtl;
}

.topbar {
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
}

.avatar {
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}

.avatar-fallback {
    width:42px;
    height:42px;
    border-radius:50%;
    background:#d9eefc;
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
}

.chat-box {
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:75px;
    overflow-y:auto;
    padding:10px;
}

.msg {
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.5;
    white-space:pre-wrap;
    font-family:Arial;
    direction:rtl;
    text-align:right;
}

.bot {
    background:white;
    color:#222;
    margin-left:auto;
    margin-right:0;
}

.user {
    background:#1c6fa4;
    color:white;
    margin-right:auto;
    margin-left:0;
}

.input-area {
    width:420px;
    margin:12px auto 0 auto;
}

div[data-testid="stButton"] button {
    border-radius:20px;
    font-size:12px;
    background:white;
    color:#1c6fa4;
    border:1px solid #d7e8f4;
}

div[data-testid="stTextInput"] input {
    border-radius:22px;
    height:42px;
    font-size:13px;
    direction:rtl;
    text-align:right;
}

div[data-testid="stFormSubmitButton"] button {
    width:100%;
    border-radius:22px;
    background:#1c6fa4;
    color:white;
    border:none;
}
</style>
""", unsafe_allow_html=True)

messages_html = ""
for role, msg in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    safe_msg = html.escape(str(msg))
    messages_html += f'<div class="msg {cls}">{safe_msg}</div>'

avatar_html = (
    f'<img class="avatar" src="data:image/png;base64,{robot}">'
    if robot else
    '<div class="avatar-fallback"></div>'
)

st.markdown(f"""
<div class="phone">
    <div class="topbar">
        {avatar_html}
        <div class="dot"></div>
        <div class="status">جاهز للمساعدة</div>
    </div>

    <div class="chat-box">
        {messages_html}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='input-area'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("فحص الشبكة"):
        send_message("فحص الشبكة")
        st.rerun()

    if st.button("تجديد الباقة"):
        send_message("تجديد الباقة")
        st.rerun()

with col2:
    if st.button("استهلاك الإنترنت"):
        send_message("استهلاك الإنترنت")
        st.rerun()

    if st.button("العروض"):
        send_message("العروض")
        st.rerun()

with col3:
    if st.button("المكالمات الدولية"):
        send_message("المكالمات الدولية")
        st.rerun()

    if st.button("الدعم"):
        send_message("الدعم")
        st.rerun()

with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="اكتب سؤالك...")
    submitted = st.form_submit_button("إرسال")

if submitted and user_input.strip():
    send_message(user_input.strip())
    st.rerun()

if st.button("مسح الشات"):
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا، كيف أقدر أساعدك؟")
    ]
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
