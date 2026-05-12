import streamlit as st
import base64
import html as html_lib
import os
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

PHONE_WIDTH = 430
CHAT_KEY = "chat_ar_messages_v3"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحباً 👋 أنا مساعد CoCare الذكي، كيف أقدر أساعدك؟")
    ]


def save_chat_history():
    pass


def reset_context():
    pass


def get_bot_response(message):
    message = str(message).lower()

    if "شبكة" in message or "فحص" in message:
        return "جاري فحص الشبكة الآن..."

    elif "استهلاك" in message or "الانترنت" in message:
        return "يمكنك معرفة استهلاك الإنترنت من قسم الاستخدام."

    elif "تجديد" in message or "الباقة" in message:
        return "يمكنك تجديد الباقة من قسم الباقات."

    elif "دولي" in message or "مكالمات" in message:
        return "خدمة المكالمات الدولية متوفرة حسب نوع خطك."

    elif "عروض" in message or "ألعاب" in message:
        return "يمكنك الاطلاع على العروض وباقات الألعاب من قسم العروض."

    elif "دعم" in message or "التواصل" in message:
        return "تم إرسال طلبك إلى فريق الدعم."

    else:
        return "يقوم مساعد CoCare بمعالجة طلبك."


def send_message(text):
    if not text or not text.strip():
        return

    st.session_state[CHAT_KEY].append(("user", text.strip()))
    st.session_state[CHAT_KEY].append(("bot", "جاري الكتابة..."))

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


st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#eef2f7 !important;
}

[data-testid="stSidebar"] {
    display: none;
}

.phone {
    width: 430px;
    height: 820px;
    margin: auto;
    background: #ffffff;
    border-radius: 32px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.18);
    overflow: hidden;
}

.chat-area {
    height: 520px;
    overflow-y: auto;
    padding: 14px;
    background: #f7f9fc;
}

.user-msg {
    background: #7b3ff2;
    color: white;
    padding: 10px 14px;
    border-radius: 18px 18px 4px 18px;
    margin: 8px 0;
    max-width: 78%;
    margin-left: auto;
    direction: rtl;
}

.bot-msg {
    background: #eef2f7;
    color: #222;
    padding: 10px 14px;
    border-radius: 18px 18px 18px 4px;
    margin: 8px 0;
    max-width: 78%;
    margin-right: auto;
    direction: rtl;
}
</style>
""", unsafe_allow_html=True)


st.markdown(f"""
<div class="top-card">
    {avatar_top}
    <div class="ready">
        <span class="dot"></span>
        جاهز للمساعدة
    </div>
    <div class="location">📍 عمان</div>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="quick-title">الخدمات السريعة</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

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

c4, c5, c6 = st.columns(3)

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

        chat_html += f"""
        <div class="message-row user-row">
            <div class="user-avatar">أنت</div>
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
        ("bot", "مرحباً 👋 أنا مساعد CoCare الذكي، كيف أقدر أساعدك؟")
    ]

    reset_context()

    save_chat_history()

    st.rerun()


with st.form("chat_form", clear_on_submit=True):

    user_input = st.text_input(
        "",
        placeholder="اكتب رسالتك هنا...",
        label_visibility="collapsed"
    )

    send_btn = st.form_submit_button("إرسال")

    if send_btn and user_input.strip():

        send_message(user_input)

        st.rerun()
