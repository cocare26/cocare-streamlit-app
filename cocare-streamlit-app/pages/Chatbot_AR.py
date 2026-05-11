import streamlit as st
import base64
import html as html_lib
import time
import os

st.set_page_config(page_title="CoCare AI", layout="centered")

PHONE_WIDTH = 430
PHONE_HEIGHT = 820
CHAT_KEY = "chat_ar_messages"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا، أنا مساعد CoCare الذكي، كيف أقدر أساعدك؟")
    ]


def save_chat_history():
    pass


def reset_context():
    pass


def img_to_base64(filename):
    paths = [
        os.path.join(os.path.dirname(__file__), filename),
        os.path.join(os.path.dirname(__file__), "..", filename),
        filename
    ]

    for path in paths:
        try:
            if os.path.exists(path):
                with open(path, "rb") as f:
                    return base64.b64encode(f.read()).decode()
        except Exception:
            pass

    return ""


robot = (
    img_to_base64("robot_black.png")
    or img_to_base64("robot.png")
    or img_to_base64("robot_head.png")
)


def get_bot_response(message):
    message = str(message).lower()

    if "شبكة" in message or "فحص" in message or "network" in message:
        return "جاري فحص الشبكة الآن..."

    if "استهلاك" in message or "usage" in message:
        return "يمكنك معرفة استهلاك الإنترنت من قسم الحساب أو الاستهلاك."

    if "تجديد" in message or "باقة" in message or "renew" in message:
        return "يمكنك تجديد الباقة من قسم الباقات أو المدفوعات."

    if "دولي" in message or "مكالمات" in message:
        return "خدمة المكالمات الدولية متاحة حسب نوع خطك."

    if "عروض" in message or "العروض" in message:
        return "العروض الحالية متاحة من قسم العروض."

    if "دعم" in message or "support" in message:
        return "تم إرسال طلبك إلى فريق الدعم."

    return "مساعد CoCare يقوم بمعالجة طلبك."


def send_message(text):
    if not text:
        return

    st.session_state[CHAT_KEY].append(("user", text))
    st.session_state[CHAT_KEY].append(("bot", "Typing..."))
    time.sleep(0.3)
    st.session_state[CHAT_KEY].pop()

    bot_reply = get_bot_response(text)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))
    save_chat_history()


if robot:
    robot_avatar_top = f'''
    <img class="top-avatar" src="data:image/png;base64,{robot}">
    '''
else:
    robot_avatar_top = '''
    <div class="top-avatar fallback-avatar">AI</div>
    '''


st.markdown(f"""
<style>
html, body, [data-testid="stAppViewContainer"] {{
    background:#d8e9f8;
    direction:rtl;
}}

header, footer, #MainMenu {{
    visibility:hidden;
}}

.block-container {{
    width:{PHONE_WIDTH}px !important;
    max-width:{PHONE_WIDTH}px !important;
    min-height:{PHONE_HEIGHT}px !important;
    margin:auto;
    padding:18px 12px 10px !important;
}}

.phone {{
    background:#f7fbff;
    border-radius:38px;
    padding:18px;
    box-shadow:0 12px 35px rgba(0,0,0,.15);
    min-height:{PHONE_HEIGHT}px;
    border:1px solid #d9e8f7;
    overflow:hidden;
}}

.top-bar {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:16px;
}}

.title {{
    font-size:28px;
    font-weight:900;
    color:#0f2446;
}}

.sub {{
    color:#5b6472;
    font-size:14px;
    margin-top:4px;
}}

.top-avatar {{
    width:72px;
    height:72px;
    border-radius:50%;
    object-fit:cover;
    background:white;
    box-shadow:0 4px 14px rgba(0,0,0,.12);
}}

.fallback-avatar {{
    display:flex;
    align-items:center;
    justify-content:center;
    background:#111827;
    color:white;
    font-size:28px;
    font-weight:900;
}}

.quick-title {{
    margin-top:8px;
    margin-bottom:12px;
    font-size:17px;
    font-weight:900;
    color:#0f2446;
    text-align:right;
}}

div[data-testid="stButton"] button {{
    width:100%;
    min-height:64px;
    border:none;
    border-radius:18px;
    padding:8px;
    background:white;
    color:#0f4f91;
    font-weight:800;
    font-size:13px;
    box-shadow:0 4px 14px rgba(0,0,0,.08);
}}

.chat-area {{
    height:410px;
    overflow-y:auto;
    padding:12px;
    background:#eef5fc;
    border-radius:24px;
    margin-top:14px;
    margin-bottom:12px;
    border:1px solid #d8e7f6;
}}

.message-row {{
    display:flex;
    align-items:flex-end;
    margin-bottom:14px;
    gap:8px;
}}

.user-row {{
    justify-content:flex-start;
}}

.bot-row {{
    justify-content:flex-end;
}}

.msg {{
    padding:12px 16px;
    border-radius:18px;
    max-width:75%;
    font-size:15px;
    line-height:1.7;
    word-wrap:break-word;
    white-space:pre-wrap;
    text-align:right;
}}

.user {{
    background:linear-gradient(135deg,#4da3ff,#1677e8);
    color:white;
    border-bottom-left-radius:6px;
}}

.bot {{
    background:white;
    color:#111827;
    border-bottom-right-radius:6px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
}}

.msg-avatar {{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
    background:white;
    box-shadow:0 3px 8px rgba(0,0,0,.10);
}}

.user-avatar {{
    display:flex;
    align-items:center;
    justify-content:center;
    background:#dbeafe;
    color:#0f4f91;
    font-weight:900;
}}

section[data-testid="stChatInput"] {{
    width:{PHONE_WIDTH - 24}px !important;
    max-width:{PHONE_WIDTH - 24}px !important;
    margin:auto !important;
}}

div[data-testid="stChatInput"] textarea {{
    direction:rtl;
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
        <div class="sub">مساعد الاتصالات الذكي</div>
    </div>
    {robot_avatar_top}
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="quick-title">الخدمات السريعة</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("فحص الشبكة"):
        send_message("فحص الشبكة")
        st.rerun()

with c2:
    if st.button("استهلاك الإنترنت"):
        send_message("استهلاك الإنترنت")
        st.rerun()

with c3:
    if st.button("تجديد الباقة"):
        send_message("تجديد الباقة")
        st.rerun()

with c4:
    if st.button("المكالمات الدولية"):
        send_message("المكالمات الدولية")
        st.rerun()

with c5:
    if st.button("العروض والألعاب"):
        send_message("العروض والألعاب")
        st.rerun()

with c6:
    if st.button("التواصل مع الدعم"):
        send_message("التواصل مع الدعم")
        st.rerun()


chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    safe_msg = html_lib.escape(str(message))

    if role == "user":
        chat_html += f'''
<div class="message-row user-row">
    <div class="msg user">{safe_msg}</div>
    <div class="msg-avatar user-avatar">U</div>
</div>
'''
    else:
        if robot:
            avatar_html = f'<img class="msg-avatar" src="data:image/png;base64,{robot}">'
        else:
            avatar_html = '<div class="msg-avatar user-avatar">AI</div>'

        chat_html += f'''
<div class="message-row bot-row">
    {avatar_html}
    <div class="msg bot">{safe_msg}</div>
</div>
'''

chat_html += '''
</div>
<script>
const chatArea = window.parent.document.querySelector(".chat-area");
if (chatArea) {
    chatArea.scrollTop = chatArea.scrollHeight;
}
</script>
'''

st.markdown(chat_html, unsafe_allow_html=True)

if st.button("مسح المحادثة"):
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا، أنا مساعد CoCare الذكي، كيف أقدر أساعدك؟")
    ]
    reset_context()
    save_chat_history()
    st.rerun()

user_input = st.chat_input("اكتب رسالتك هنا...")

if user_input:
    send_message(user_input)
    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
