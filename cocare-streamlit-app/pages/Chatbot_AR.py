import streamlit as st
import base64
import os
import sys
import html as html_lib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

st.set_page_config(page_title="المساعد الذكي", layout="centered")

CHAT_KEY = "chat_ar_messages"
CONTEXT_KEY = "chat_context"

if "region" not in st.session_state:
    st.session_state["region"] = "عمان"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا 👋 كيف أقدر أساعدك؟")
    ]

if CONTEXT_KEY not in st.session_state:
    st.session_state[CONTEXT_KEY] = {
        "last_intent": None,
        "awaiting_details": False,
        "last_network_problem": False
    }


def img_to_base64(path):
    try:
        full_path = os.path.join(os.path.dirname(__file__), "..", path)
        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    except Exception:
        pass
    return ""


robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")


def prepare_context_message(user_text):
    context = st.session_state[CONTEXT_KEY]
    text = str(user_text).strip()

    if context.get("awaiting_details") and len(text.split()) <= 6:
        last_intent = context.get("last_intent") or "network_complaint"
        return f"{last_intent}: {text}"

    return text


def get_bot_reply(user_text):
    quick_map = {
        "فحص الشبكة": "افحص حالة الشبكة عندي",
        "استهلاك الإنترنت": "بدي أعرف استهلاك الإنترنت",
        "تجديد الباقة": "بدي أجدد الباقة",
        "المكالمات الدولية": "بدي أعرف عن المكالمات الدولية",
        "العروض": "شو العروض المتاحة؟",
        "الدعم": "بدي أتواصل مع الدعم الفني",
    }

    original_msg = quick_map.get(user_text, user_text)
    msg_for_engine = prepare_context_message(original_msg)

    user_id = st.session_state.get("user_id", "customer_1")
    region = st.session_state.get("region", "عمان")

    try:
        result = process_message(
            msg_for_engine,
            user_id=user_id,
            region=region
        )

        st.session_state[CONTEXT_KEY]["last_intent"] = result.get("intent")
        st.session_state[CONTEXT_KEY]["last_network_problem"] = result.get("network_problem", False)

        if result.get("network_problem", False):
            st.session_state[CONTEXT_KEY]["awaiting_details"] = True
        else:
            st.session_state[CONTEXT_KEY]["awaiting_details"] = False

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()

        reply = f"{response}\n\n{followup}".strip()

        if not reply:
            return "ممكن توضحي أكثر؟"

        return reply

    except Exception as e:
        return f"صار خطأ بالربط: {e}"


def send_message(text):
    if not text:
        return

    st.session_state[CHAT_KEY].append(("user", text))
    bot_reply = get_bot_reply(text)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))


st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#eef2f7;
    direction:rtl;
}

header, footer, #MainMenu {
    visibility:hidden;
}

.block-container {
    max-width:430px;
    height:730px;
    margin:auto;
    padding:14px 16px 8px;
    border-radius:42px;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    box-shadow:0 12px 30px rgba(0,0,0,.15);
    overflow:hidden;
}

.topbar {
    height:58px;
    background:white;
    border-radius:18px;
    display:flex;
    align-items:center;
    gap:10px;
    padding:0 14px;
    box-shadow:0 3px 10px rgba(0,0,0,.12);
    margin-bottom:10px;
}

.avatar {
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
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
    color:#222;
}

.region-label {
    margin-right:auto;
    font-size:11px;
    color:#436577;
    font-weight:700;
}

.quick-title {
    font-size:13px;
    font-weight:800;
    color:#102646;
    margin:4px 0 6px;
}

div[data-testid="stButton"] button {
    border-radius:18px;
    border:none;
    background:white;
    color:#102646;
    font-weight:800;
    font-size:12px;
    box-shadow:0 3px 8px rgba(0,0,0,.10);
    height:36px;
}

div[data-testid="stButton"] button:hover {
    background:#eef6ff;
    color:#1c6fa4;
}

.chat-area {
    height:350px;
    overflow-y:auto;
    padding:10px 4px;
    margin-top:10px;
    margin-bottom:8px;
}

.msg {
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.5;
    white-space:pre-wrap;
    text-align:right;
}

.bot {
    background:white;
    color:#222;
    margin-left:auto;
}

.user {
    background:#1c6fa4;
    color:white;
    margin-right:auto;
}

div[data-testid="stChatInput"] {
    position:relative !important;
    bottom:auto !important;
    background:transparent !important;
    padding:0 !important;
}

div[data-testid="stChatInput"] textarea {
    direction:rtl;
    border-radius:22px;
    border:none;
    background:white;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)


region = st.session_state.get("region", "عمان")

st.markdown(f"""
<div class="topbar">
    <img class="avatar" src="data:image/png;base64,{robot}">
    <div class="dot"></div>
    <div class="status">جاهز للمساعدة</div>
    <div class="region-label">📍 {html_lib.escape(region)}</div>
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
    if st.button("العروض"):
        send_message("العروض")
        st.rerun()

with c6:
    if st.button("الدعم"):
        send_message("الدعم")
        st.rerun()


chat_html = '<div class="chat-area">'

for role, message in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    safe_msg = html_lib.escape(str(message))
    chat_html += f'<div class="msg {cls}">{safe_msg}</div>'

chat_html += '</div>'

st.markdown(chat_html, unsafe_allow_html=True)


user_input = st.chat_input("اكتب سؤالك...")

if user_input:
    send_message(user_input)
    st.rerun()
