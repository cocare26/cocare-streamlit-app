import streamlit as st
import streamlit.components.v1 as components
import base64
import html as html_lib
import os
import sys

# =========================
# IMPORT COCARE ENGINE
# =========================
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="المساعد الذكي", layout="centered")

CHAT_KEY = "chat_ar_original_design_v2"

# =========================
# REGION SETUP
# =========================
REGIONS = [
    "عمان", "الزرقاء", "إربد", "البلقاء", "مادبا", "الكرك",
    "الطفيلة", "معان", "العقبة", "جرش", "عجلون", "المفرق"
]

if "region" not in st.session_state:
    st.session_state["region"] = "عمان"

selected_region = st.selectbox(
    "اختر المحافظة",
    REGIONS,
    index=REGIONS.index(st.session_state["region"]) if st.session_state["region"] in REGIONS else 0
)

st.session_state["region"] = selected_region

# =========================
# IMAGE TO BASE64
# =========================
def img_to_base64(path):
    try:
        full_path = os.path.join(os.path.dirname(__file__), "..", path)

        if os.path.exists(full_path):
            with open(full_path, "rb") as f:
                return base64.b64encode(f.read()).decode()

        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()

    except Exception:
        pass

    return ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

# =========================
# INITIAL CHAT
# =========================
if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا 👋 كيف أقدر أساعدك؟")
    ]

# =========================
# FALLBACK REPLY
# =========================
def fallback_reply(text):
    t = str(text).strip().lower()

    if t in ["هاي", "هلا", "مرحبا", "hi", "hello", "كيفو", "كيفك"]:
        return "هلا وغلا 👋 كيف فيني أساعدك؟"

    if "شبكة" in t or "نت" in t or "انترنت" in t or "إنترنت" in t:
        return f"خليني أشيك حالة الشبكة عندك في {st.session_state.get('region', 'عمان')}."

    if "باقة" in t or "تجديد" in t:
        return "أكيد، بتقدر تجدد الباقة من قسم الباقات."

    if "دعم" in t:
        return "رح يتم تحويلك للدعم الفني 👨‍💻\nاحكيلي شو المشكلة؟"

    if "عروض" in t or "العروض" in t:
        return "العروض الحالية متاحة من قسم العروض 🎁"

    if "مكالمات" in t or "الدولية" in t:
        return "خدمة المكالمات الدولية متاحة حسب نوع خطك."

    if "استهلاك" in t:
        return "تقدر تشوف استهلاك الإنترنت من لوحة الحساب."

    return "تم استلام طلبك 👍 كيف أقدر أساعدك أكثر؟"

# =========================
# BOT REPLY FROM COCARE
# =========================
def get_bot_reply(user_text):
    quick_map = {
        "فحص الشبكة": "افحص حالة الشبكة عندي",
        "استهلاك الإنترنت": "بدي أعرف استهلاك الإنترنت",
        "تجديد الباقة": "بدي أجدد الباقة",
        "المكالمات الدولية": "بدي أعرف عن المكالمات الدولية",
        "العروض": "شو العروض المتاحة؟",
        "الدعم": "بدي أتواصل مع الدعم الفني",
    }

    msg = quick_map.get(user_text, user_text)

    user_id = st.session_state.get("user_id", "customer_1")
    region = st.session_state.get("region", "عمان")

    try:
        result = process_message(
            msg,
            user_id=user_id,
            region=region
        )

        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()

        reply = f"{response}\n\n{followup}".strip()

        if not reply:
            return fallback_reply(user_text)

        return reply

    except Exception as e:
        return f"صار خطأ بالربط: {e}"

# =========================
# RECEIVE MESSAGE FROM URL
# =========================
msg = st.query_params.get("msg", "")

if msg:
    msg = str(msg).strip()

    st.session_state[CHAT_KEY].append(("user", msg))
    bot_reply = get_bot_reply(msg)
    st.session_state[CHAT_KEY].append(("bot", bot_reply))

    st.query_params.clear()
    st.rerun()

# =========================
# BUILD CHAT HTML
# =========================
messages_html = ""

for role, m in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    messages_html += f'<div class="msg {cls}">{html_lib.escape(str(m))}</div>'

current_region = html_lib.escape(st.session_state.get("region", "عمان"))

html = f"""
<html>
<head>
<style>
body {{
    margin:0;
    background:#eef2f7;
    font-family:Arial;
    direction:rtl;
}}

.phone {{
    width:420px;
    height:700px;
    margin:auto;
    border-radius:42px;
    overflow:hidden;
    position:relative;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
}}

.topbar {{
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
}}

.back {{
    font-size:28px;
    color:#436577;
    cursor:pointer;
}}

.avatar {{
    width:42px;
    height:42px;
    border-radius:50%;
    object-fit:cover;
}}

.dot {{
    width:8px;
    height:8px;
    background:#36c06a;
    border-radius:50%;
}}

.status {{
    font-size:15px;
    font-weight:700;
    color:#222;
}}

.region {{
    margin-right:auto;
    font-size:11px;
    color:#436577;
    font-weight:700;
}}

.chat-box {{
    position:absolute;
    top:90px;
    left:18px;
    right:18px;
    bottom:75px;
    overflow-y:auto;
    padding:10px;
}}

.msg {{
    max-width:75%;
    padding:9px 12px;
    border-radius:16px;
    margin-bottom:8px;
    font-size:13px;
    line-height:1.5;
    white-space:pre-wrap;
    text-align:right;
}}

.bot {{
    background:white;
    color:#222;
    margin-left:auto;
}}

.user {{
    background:#1c6fa4;
    color:white;
    margin-right:auto;
}}

.menu {{
    display:none;
    position:absolute;
    right:38px;
    bottom:90px;
    width:160px;
    background:white;
    border-radius:8px;
    box-shadow:0 4px 12px rgba(0,0,0,.18);
    padding:8px 0;
    z-index:5;
}}

.menu a {{
    display:block;
    font-size:13px;
    padding:7px 13px;
    color:#222;
    cursor:pointer;
    text-decoration:none;
}}

.menu a:hover {{
    background:#eef3f6;
}}

.bottom {{
    position:absolute;
    bottom:18px;
    left:18px;
    right:18px;
    height:42px;
    display:flex;
    align-items:center;
    gap:8px;
    margin:0;
}}

.hamburger {{
    width:32px;
    height:32px;
    border-radius:50%;
    background:white;
    text-align:center;
    line-height:32px;
    font-size:22px;
    color:#50768a;
    cursor:pointer;
    flex-shrink:0;
}}

.chat-input {{
    flex:1;
    height:34px;
    background:white;
    border-radius:22px;
    color:#444;
    font-size:12px;
    padding-right:14px;
    border:none;
    outline:none;
}}

.send {{
    width:40px;
    height:40px;
    border-radius:50%;
    border:none;
    background:linear-gradient(135deg,#6ec6ff,#1c6fa4);
    color:white;
    text-align:center;
    line-height:40px;
    font-size:20px;
    cursor:pointer;
    flex-shrink:0;
}}
</style>
</head>

<body>
<div class="phone">

    <div class="topbar">
        <div class="back" onclick="goBack()">›</div>
        <img class="avatar" src="data:image/png;base64,{robot}">
        <div class="dot"></div>
        <div class="status">جاهز للمساعدة</div>
        <div class="region">📍 {current_region}</div>
    </div>

    <div id="chatBox" class="chat-box">
        {messages_html}
    </div>

    <div id="menu" class="menu">
        <a href="?msg=فحص الشبكة" target="_top">فحص الشبكة</a>
        <a href="?msg=استهلاك الإنترنت" target="_top">استهلاك الإنترنت</a>
        <a href="?msg=تجديد الباقة" target="_top">تجديد الباقة</a>
        <a href="?msg=المكالمات الدولية" target="_top">المكالمات الدولية</a>
        <a href="?msg=العروض" target="_top">العروض</a>
        <a href="?msg=الدعم" target="_top">الدعم</a>
    </div>

    <form class="bottom" method="get" target="_top">
        <div class="hamburger" onclick="toggleMenu()">≡</div>
        <input name="msg" id="chatInput" class="chat-input" placeholder="اكتب سؤالك..." autocomplete="off">
        <button class="send" type="submit">➤</button>
    </form>

</div>

<script>
function toggleMenu(){{
    const menu = document.getElementById("menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}}

function goBack(){{
    window.top.location.href = "../";
}}

const chatBox = document.getElementById("chatBox");
chatBox.scrollTop = chatBox.scrollHeight;
</script>

</body>
</html>
"""

components.html(html, height=730)
