import streamlit as st
import base64
import html

from cocare import process_message   # إذا اسم ملفك غير cocare عدليه هون

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
        ("bot", "مرحباً، كيف أقدر أساعدك؟")
    ]

# =========================
# BOT LOGIC
# =========================
def get_bot_reply(user_text):
    text = str(user_text).strip().lower()

    # ردود عربية مباشرة قبل process_message
    if text in ["هاي", "هلا", "مرحبا", "hello", "hi"]:
        return "هلا وغلا 👋 كيف فيني أساعدك؟\n\nشو حاب تعرف؟"

    if "كيفك" in text:
        return "تمام الحمدلله 👋 كيف أقدر أساعدك؟"

    if "بطي" in text or "ضعيف" in text or "النت" in text:
        return "واضح إن عندك مشكلة بالإنترنت.\n\nخليني أشيك حالة الشبكة عندك."

    if "اشارة" in text or "إشارة" in text:
        return "فهمت عليك، واضح في مشكلة بالإشارة.\n\nوين موقعك تقريباً؟"

    if "الدعم" in text:
        return "تمام، رح يتم تحويل طلبك للدعم الفني.\n\nاحكيلي شو المشكلة بالتفصيل؟"

    if "الباقة" in text or "جدد" in text:
        return "أكيد، بتقدري تجددي الباقة من قسم الباقات.\n\nبدك أساعدك بخطوات التجديد؟"

    try:
        result = process_message(
            user_text,
            user_id="customer_1",
            region="Amman"
        )

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()
        reply = f"{response}\n\n{followup}".strip()

        if not reply or "تم استلام طلبك" in reply:
            return "ممكن توضحيلي أكثر؟"

        return reply

    except Exception as e:
        return f"صار خطأ بالربط:\n{e}"
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
    color:#222;
}

.chat-box {
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:125px;
    overflow-y:auto;
    padding:10px;
}

.msg {
    max-width:76%;
    padding:10px 14px;
    border-radius:18px;
    margin-bottom:10px;
    font-size:13px;
    line-height:1.6;
    white-space:pre-wrap;
    font-family:Arial;
    direction:rtl;
    text-align:right;
}

.bot {
    background:white;
    color:#222;
    margin-right:auto;
    margin-left:0;
}

.user {
    background:#1c6fa4;
    color:white;
    margin-left:auto;
    margin-right:0;
}

.quick-box {
    position:absolute;
    left:18px;
    right:18px;
    bottom:70px;
    display:flex;
    flex-wrap:wrap;
    gap:6px;
    justify-content:center;
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

.input-area {
    width:420px;
    margin:12px auto 0 auto;
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

div[data-testid="stButton"] button {
    border-radius:20px;
    font-size:12px;
    padding:6px 10px;
    background:white;
    color:#1c6fa4;
    border:1px solid #d7e8f4;
}
</style>
""", unsafe_allow_html=True)

# =========================
# PHONE HTML
# =========================
messages_html = ""

for role, msg in st.session_state.messages:
    cls = "user" if role == "user" else "bot"
    safe_msg = html.escape(str(msg))
    messages_html += f'<div class="msg {cls}">{safe_msg}</div>'

if robot:
    avatar_html = f'<img class="avatar" src="data:image/png;base64,{robot}">'
else:
    avatar_html = '<div class="avatar-fallback"></div>'

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
# REAL QUICK BUTTONS
# =========================
st.markdown("<div class='input-area'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("فحص الشبكة", key="q_network"):
        send_message("افحص حالة الشبكة عندي")
        st.rerun()

    if st.button("تجديد الباقة", key="q_renew"):
        send_message("بدي أجدد الباقة")
        st.rerun()

with col2:
    if st.button("استهلاك الإنترنت", key="q_usage"):
        send_message("بدي أعرف استهلاك الإنترنت")
        st.rerun()

    if st.button("العروض والألعاب", key="q_offers"):
        send_message("شو العروض المتاحة؟")
        st.rerun()

with col3:
    if st.button("المكالمات الدولية", key="q_calls"):
        send_message("بدي أعرف عن المكالمات الدولية")
        st.rerun()

    if st.button("الدعم الفني", key="q_support"):
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

st.markdown("</div>", unsafe_allow_html=True)
