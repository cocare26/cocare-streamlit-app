import streamlit as st
import base64

# عدلي الاسم حسب ملفك
from cocare import process_message

st.set_page_config(page_title="CoCare AI Agent", layout="centered")

# =========================
# IMAGE
# =========================
def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

robot = img_to_base64("robot_head.png")

# =========================
# SESSION
# =========================
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("bot", "أهلاً 👋 كيف أقدر أساعدك؟")
    ]

# =========================
# CHATBOT RESPONSE
# =========================
def get_bot_reply(user_text):
    result = process_message(
        user_text,
        user_id="customer_1",
        region="Amman"
    )

    reply = result.get("response", "")
    followup = result.get("followup_response", "")

    final_reply = f"{reply}\n\n{followup}".strip()
    return final_reply


def send_message(text):
    if not text:
        return

    st.session_state.messages.append(("user", text))

    try:
        bot_reply = get_bot_reply(text)
    except Exception as e:
        bot_reply = "صار خطأ أثناء معالجة الرسالة، حاول مرة ثانية."

    st.session_state.messages.append(("bot", bot_reply))


# =========================
# CSS
# =========================
st.markdown("""
<style>
.stApp {
    background:#eef2f7;
}

.block-container {
    padding-top: 20px;
}

.phone {
    width:420px;
    height:700px;
    margin:auto;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    box-shadow:0 10px 35px rgba(0,0,0,.18);
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

.back {
    font-size:28px;
    color:#436577;
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

.chat-box {
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:145px;
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
}

.bot {
    background:white;
    color:#222;
    margin-right:auto;
    margin-left:0;
    text-align:right;
    direction:rtl;
}

.user {
    background:#1c6fa4;
    color:white;
    margin-left:auto;
    margin-right:0;
    text-align:right;
    direction:rtl;
}

.quick-box {
    position:absolute;
    left:18px;
    right:18px;
    bottom:70px;
    display:flex;
    flex-wrap:wrap;
    gap:6px;
}

.quick-btn {
    background:white;
    border-radius:14px;
    padding:6px 10px;
    font-size:12px;
    color:#1c6fa4;
    border:1px solid #d7e8f4;
    display:inline-block;
}

.bottom-space {
    height: 700px;
}

div[data-testid="stTextInput"] {
    width:420px;
    margin:auto;
}

div[data-testid="stTextInput"] input {
    border-radius:22px;
    height:42px;
    font-size:13px;
}

div[data-testid="stButton"] button {
    border-radius:20px;
    font-size:12px;
    padding:5px 10px;
    background:white;
    color:#1c6fa4;
    border:1px solid #d7e8f4;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HTML PHONE
# =========================
messages_html = ""

for role, msg in st.session_state.messages:
    cls = "user" if role == "user" else "bot"
    messages_html += f'<div class="msg {cls}">{msg}</div>'

avatar_html = (
    f'<img class="avatar" src="data:image/png;base64,{robot}">'
    if robot else
    '<div class="avatar"></div>'
)

st.markdown(f"""
<div class="phone">
    <div class="topbar">
        <div class="back">‹</div>
        {avatar_html}
        <div class="dot"></div>
        <div class="status">جاهز للمساعدة</div>
    </div>

    <div class="chat-box">
        {messages_html}
    </div>

    <div class="quick-box">
        <span class="quick-btn">فحص الشبكة</span>
        <span class="quick-btn">استهلاك الإنترنت</span>
        <span class="quick-btn">تجديد الباقة</span>
        <span class="quick-btn">المكالمات الدولية</span>
        <span class="quick-btn">العروض والألعاب</span>
        <span class="quick-btn">الدعم الفني</span>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# QUICK SERVICES
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("فحص الشبكة"):
        send_message("افحص حالة الشبكة عندي")
        st.rerun()

    if st.button("تجديد الباقة"):
        send_message("بدي أجدد الباقة")
        st.rerun()

with col2:
    if st.button("استهلاك الإنترنت"):
        send_message("بدي أعرف استهلاك الإنترنت")
        st.rerun()

    if st.button("العروض والألعاب"):
        send_message("شو العروض المتاحة؟")
        st.rerun()

with col3:
    if st.button("المكالمات الدولية"):
        send_message("بدي أعرف عن المكالمات الدولية")
        st.rerun()

    if st.button("الدعم الفني"):
        send_message("بدي أتواصل مع الدعم الفني")
        st.rerun()

# =========================
# INPUT
# =========================
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "",
        placeholder="اكتب سؤالك هون..."
    )
    submitted = st.form_submit_button("إرسال")

if submitted and user_input.strip():
    send_message(user_input.strip())
    st.rerun()
