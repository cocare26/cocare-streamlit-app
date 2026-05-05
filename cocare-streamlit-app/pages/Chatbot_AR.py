import streamlit as st
import streamlit.components.v1 as components
import base64, html as html_lib, os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cocare import process_message

st.set_page_config(page_title="المساعد الذكي", layout="centered")

CHAT_KEY = "chat_ar_original_design_v2"

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

robot = img_to_base64("robot_head.png") or img_to_base64("robot.png")

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "مرحبًا 👋 كيف أقدر أساعدك؟")
    ]

def fallback_reply(text):
    t = str(text).strip().lower()

    if t in ["هاي", "هلا", "مرحبا", "hi", "hello", "كيفو", "كيفك"]:
        return "هلا وغلا 👋 كيف فيني أساعدك؟"

    if "شبكة" in t or "نت" in t or "انترنت" in t or "إنترنت" in t:
        return "خليني أشيك حالة الشبكة عندك.\nأي منطقة موجود فيها؟"

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

    try:
        result = process_message(msg, user_id="customer_1", region="Amman")
        response = str(result.get("response", "")).strip()
        followup = str(result.get("followup_response", "")).strip()
        reply = f"{response}\n\n{followup}".strip()

        if not reply or "ممكن توضح" in reply or "احكيلي تفاصيل أكثر" in reply:
            return fallback_reply(user_text)

        return reply

    except Exception:
        return fallback_reply(user_text)

msg = st.query_params.get("msg", "")
if msg:
    msg = str(msg).strip()
    st.session_state[CHAT_KEY].append(("user", msg))
    st.session_state[CHAT_KEY].append(("bot", get_bot_reply(msg)))
    st.query_params.clear()
    st.rerun()

messages_html = ""
for role, m in st.session_state[CHAT_KEY]:
    cls = "user" if role == "user" else "bot"
    messages_html += f'<div class="msg {cls}">{html_lib.escape(str(m))}</div>'

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

.menu div {{
    font-size:13px;
    padding:7px 13px;
    color:#222;
    cursor:pointer;
}}

.menu div:hover {{
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
    background:linear-gradient(135deg,#6ec6ff,#1c6fa4);
    color:white;
    text-align:center;
    line-height:40px;
    font-size:20px;
    cursor:pointer;
}}
</style>
</head>

<body>
<div class="phone">

    <div class="topbar">
        <div class="back">›</div>
        <img class="avatar" src="data:image/png;base64,{robot}">
        <div class="dot"></div>
        <div class="status">جاهز للمساعدة</div>
    </div>

    <div id="chatBox" class="chat-box">
        {messages_html}
    </div>

    <div id="menu" class="menu">
        <div onclick="quickMsg('فحص الشبكة')">فحص الشبكة</div>
        <div onclick="quickMsg('استهلاك الإنترنت')">استهلاك الإنترنت</div>
        <div onclick="quickMsg('تجديد الباقة')">تجديد الباقة</div>
        <div onclick="quickMsg('المكالمات الدولية')">المكالمات الدولية</div>
        <div onclick="quickMsg('العروض')">العروض</div>
        <div onclick="quickMsg('الدعم')">الدعم</div>
    </div>

    <div class="bottom">
        <div class="hamburger" onclick="toggleMenu()">≡</div>
        <input id="chatInput" class="chat-input" placeholder="اكتب سؤالك..." onkeydown="checkEnter(event)">
        <div class="send" onclick="sendMessage()">➤</div>
    </div>

</div>

<script>
function toggleMenu(){{
    const menu = document.getElementById("menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}}

function sendToPython(text){{
    const url = new URL(window.parent.location.href);
    url.searchParams.set("msg", text);

    const a = document.createElement("a");
    a.href = url.toString();
    a.target = "_parent";
    document.body.appendChild(a);
    a.click();
}}

function sendMessage(){{
    const input = document.getElementById("chatInput");
    const text = input.value.trim();
    if(text === "") return;
    sendToPython(text);
}}

function quickMsg(text){{
    document.getElementById("menu").style.display = "none";
    sendToPython(text);
}}

function checkEnter(event){{
    if(event.key === "Enter"){{
        sendMessage();
    }}
}}

const chatBox = document.getElementById("chatBox");
chatBox.scrollTop = chatBox.scrollHeight;
</script>

</body>
</html>
"""

components.html(html, height=730)
