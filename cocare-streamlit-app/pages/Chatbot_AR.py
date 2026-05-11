import streamlit as st
import base64
import html as html_lib
import time
import os

st.set_page_config(page_title="CoCare AI", layout="centered")

# =========================
# PHONE SIZE
# =========================

PHONE_WIDTH = 430
PHONE_HEIGHT = 820

# =========================
# SESSION
# =========================

CHAT_KEY = "chat_messages"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا 👋 أنا مساعد CoCare الذكي، كيف أقدر أساعدك؟")
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

    if "شبكة" in message or "network" in message:
        return "📡 جاري فحص الشبكة الآن..."

    elif "استهلاك" in message or "usage" in message:
        return "📊 استهلاكك الحالي للإنترنت هو 82 GB."

    elif "تجديد" in message or "renew" in message:
        return "🔄 يمكنك تجديد الباقة من قسم المدفوعات."

    elif "دولي" in message or "international" in message:
        return "🌍 باقات المكالمات الدولية متوفرة الآن."

    elif "العروض" in message or "offers" in message:
        return "🎮 أحدث العروض والباقات متوفرة حالياً."

    elif "الدعم" in message or "support" in message:
        return "☎️ تم إرسال طلبك إلى فريق الدعم."

    else:
        return "🤖 مساعد CoCare يقوم بمعالجة طلبك."


def send_message(text):

    st.session_state[CHAT_KEY].append(("user", text))

    st.session_state[CHAT_KEY].append(("bot", "Typing..."))

    time.sleep(0.5)

    st.session_state[CHAT_KEY].pop()

    bot_reply = get_bot_response(text)

    st.session_state[CHAT_KEY].append(("bot", bot_reply))

    save_chat_history()

# =========================
# IMAGE
# =========================

def img_to_base64(filename):

    possible_paths = [
        os.path.join(os.path.dirname(__file__), filename),
        os.path.join(os.path.dirname(__file__), "..", filename),
        filename
    ]

    for path in possible_paths:

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

# fallback avatar
if robot:

    robot_avatar = f'''
    <img class="msg-avatar"
    src="data:image/png;base64,{robot}"
    style="width:70px;height:70px;">
    '''

else:

    robot_avatar = '''
    <div class="msg-avatar user-avatar"
    style="
    width:70px;
    height:70px;
    background:#111827;
    color:white;
    font-size:28px;
    font-weight:900;
    ">
    AI
    </div>
    '''

# =========================
# STYLE
# =========================

st.markdown(f"""
<style>

html, body, [data-testid="stAppViewContainer"]{{
    background:#d8e9f8;
    direction:rtl;
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
    justify-content:flex-start;
}}

.bot-row{{
    justify-content:flex-end;
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
    border-bottom-left-radius:6px;
}}

.bot{{
    background:white;
    color:#111827;
    border-bottom-right-radius:6px;
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

# =========================
# PHONE CONTAINER
# =========================

st.markdown('<div class="phone">', unsafe_allow_html=True)

# =========================
# TOP BAR
# =========================

st.markdown(f"""
<div class="top-bar">

    <div>
        <div class="title">CoCare AI</div>
        <div class="sub">مساعد الاتصالات الذكي</div>
    </div>

    {robot_avatar}

</div>
""", unsafe_allow_html=True)

# =========================
# QUICK SERVICES
# =========================

st.markdown(
    '<div class="quick-title">⚡ الخدمات السريعة</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("📡\nفحص الشبكة"):
        send_message("فحص الشبكة")
        st.rerun()

with c2:
    if st.button("📊\nاستهلاك الإنترنت"):
        send_message("استهلاك الإنترنت")
        st.rerun()

with c3:
    if st.button("🔄\nتجديد الباقة"):
        send_message("تجديد الباقة")
        st.rerun()

with c4:
    if st.button("🌍\nالمكالمات الدولية"):
        send_message("المكالمات الدولية")
        st.rerun()

with c5:
    if st.button("🎮\nالعروض والألعاب"):
        send_message("العروض والألعاب")
        st.rerun()

with c6:
    if st.button("☎️\nالتواصل مع الدعم"):
        send_message("التواصل مع الدعم")
        st.rerun()

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

        if robot:
            avatar_html = f'<img class="msg-avatar" src="data:image/png;base64,{robot}">'
        else:
            avatar_html = '<div class="msg-avatar user-avatar">🤖</div>'

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

# =========================
# CLEAR CHAT
# =========================

if st.button("🗑 مسح المحادثة"):

    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا 👋 أنا مساعد CoCare الذكي، كيف أقدر أساعدك؟")
    ]

    reset_context()

    save_chat_history()

    st.rerun()

# =========================
# CHAT INPUT
# =========================

user_input = st.chat_input("اكتب رسالتك هنا...")

if user_input:

    send_message(user_input)

    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)
