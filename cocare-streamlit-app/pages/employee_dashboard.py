نص واحد ملصق (78).txt
مستند
ضيفلي هدول على كودي chat_html = '<div class="chat-area">'

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

        typing_class = " typing" if str(message) == "Typing..." else ""

        chat_html += f"""
<div class="message-row bot-row">
    <img class="msg-avatar" src="data:image/png;base64,{robot}">
    <div class="msg bot{typing_class}">{safe_msg}</div>
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

user_input = st.chat_input("Type your question here...") c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("Network Test"):
        send_message("Network Test")
        st.rerun()

with c2:
    if st.button("Internet Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("Renew Package"):
        send_message("Renew Package")
        st.rerun()

with c4:
    if st.button("International Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("Offers & Games"):
        send_message("Offers & Games")
        st.rerun()

with c6:
    if st.button("Contact Support"):
        send_message("Contact Support")
        st.rerun()

if st.button("Clear Chat"):
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]
    reset_context()
    save_chat_history()
    st.rerun() 

ضيفي هاد الجزء بعد عرض الرسائل مباشرة وقبل st.chat_input داخل صفحة الشات تبعتك.
الكود اللي بعتيه فيه شغلتين:

Auto scroll للشات
Quick Services buttons
Clear Chat

وهاد بيركب مع شات CoCare بدون ما يخرب الديزاين.

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

        typing_class = " typing" if str(message) == "Typing..." else ""

        chat_html += f"""
<div class="message-row bot-row">
    <img class="msg-avatar" src="data:image/png;base64,{robot}">
    <div class="msg bot{typing_class}">{safe_msg}</div>
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
# QUICK SERVICES
# =========================

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("Network Test"):
        send_message("Network Test")
        st.rerun()

with c2:
    if st.button("Internet Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("Renew Package"):
        send_message("Renew Package")
        st.rerun()

with c4:
    if st.button("International Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("Offers & Games"):
        send_message("Offers & Games")
        st.rerun()

with c6:
    if st.button("Contact Support"):
        send_message("Contact Support")
        st.rerun()


# =========================
# CLEAR CHAT
# =========================

if st.button("Clear Chat"):

    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]

    reset_context()
    save_chat_history()

    st.rerun()


# =========================
# CHAT INPUT
# =========================

user_input = st.chat_input("Type your question here...")

وضيفي كمان هاد الـ CSS حتى يزبط شكل الأزرار والشات:

st.markdown("""
<style>

.chat-area{
    height:420px;
    overflow-y:auto;
    padding:10px;
    margin-bottom:15px;
}

.message-row{
    display:flex;
    align-items:flex-end;
    margin-bottom:12px;
}

.user-row{
    justify-content:flex-end;
}

.bot-row{
    justify-content:flex-start;
}

.msg{
    padding:12px 16px;
    border-radius:18px;
    max-width:75%;
    font-size:14px;
    line-height:1.5;
}

.user{
    background:#2f80ed;
    color:white;
    border-bottom-right-radius:5px;
}

.bot{
    background:#f1f5f9;
    color:#111827;
    border-bottom-left-radius:5px;
}

.msg-avatar{
    width:36px;
    height:36px;
    border-radius:50%;
    margin:0 8px;
}

.user-avatar{
    background:#dbeafe;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
}

.stButton button{
    width:100%;
    border-radius:14px;
    border:none;
    background:#eef6ff;
    color:#0f2446;
    font-weight:700;
    transition:0.2s;
}

.stButton button:hover{
    background:#d6e9ff;
    color:#2f80ed;
}

</style>
""", unsafe_allow_html=True)
لا اعطيني كل الكود
import streamlit as st
import streamlit.components.v1 as components
import base64
import html as html_lib
import time

st.set_page_config(page_title="CoCare AI", layout="centered")

# =========================
# SESSION
# =========================

CHAT_KEY = "chat_messages"

if CHAT_KEY not in st.session_state:
    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
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

    if "network" in message:
        return "📡 Running network diagnostics..."

    elif "usage" in message:
        return "📊 Your current internet usage is 82 GB."

    elif "renew" in message:
        return "🔄 Your package can be renewed from the payments section."

    elif "international" in message:
        return "🌍 International call packages are available now."

    elif "offers" in message:
        return "🎮 Latest offers and gaming packages are available."

    elif "support" in message:
        return "☎️ Support team has been notified."

    else:
        return "🤖 CoCare AI is processing your request."

def send_message(text):

    st.session_state[CHAT_KEY].append(("user", text))

    st.session_state[CHAT_KEY].append(("bot", "Typing..."))

    time.sleep(0.5)

    st.session_state[CHAT_KEY].pop()

    bot_reply = get_bot_response(text)

    st.session_state[CHAT_KEY].append(("bot", bot_reply))

    save_chat_history()

# =========================
# PAGE STYLE
# =========================

st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:480px;
    padding-top:20px;
}

header, footer{
    visibility:hidden;
}

/* PHONE */

.phone{
    background:white;
    border-radius:35px;
    padding:18px;
    box-shadow:0 8px 30px rgba(0,0,0,.15);
}

/* TOP */

.top-bar{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:15px;
}

.title{
    font-size:26px;
    font-weight:900;
    color:#0f2446;
}

.sub{
    color:#5b6472;
    font-size:13px;
}

/* CHAT */

.chat-area{
    height:420px;
    overflow-y:auto;
    padding:10px;
    background:#f8fbff;
    border-radius:22px;
    margin-bottom:15px;
}

.message-row{
    display:flex;
    align-items:flex-end;
    margin-bottom:12px;
}

.user-row{
    justify-content:flex-end;
}

.bot-row{
    justify-content:flex-start;
}

.msg{
    padding:12px 16px;
    border-radius:18px;
    max-width:75%;
    font-size:14px;
    line-height:1.5;
    word-wrap:break-word;
}

.user{
    background:#2f80ed;
    color:white;
    border-bottom-right-radius:5px;
}

.bot{
    background:white;
    color:#111827;
    border-bottom-left-radius:5px;
    box-shadow:0 2px 10px rgba(0,0,0,.08);
}

.msg-avatar{
    width:38px;
    height:38px;
    border-radius:50%;
    margin:0 8px;
}

.user-avatar{
    background:#dbeafe;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:18px;
}

/* QUICK SERVICES */

.quick-title{
    margin-top:5px;
    margin-bottom:10px;
    font-size:15px;
    font-weight:800;
    color:#0f2446;
}

/* BUTTONS */

.stButton button{
    width:100%;
    border:none;
    border-radius:15px;
    padding:10px;
    background:#eef6ff;
    color:#0f2446;
    font-weight:700;
    transition:0.2s;
}

.stButton button:hover{
    background:#dbe9ff;
    color:#2f80ed;
    transform:translateY(-2px);
}

/* CHAT INPUT */

[data-testid="stChatInput"]{
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# ROBOT IMAGE
# =========================

robot = ""

# =========================
# PHONE CONTAINER
# =========================

st.markdown('<div class="phone">', unsafe_allow_html=True)

st.markdown("""
<div class="top-bar">
    <div>
        <div class="title">CoCare AI</div>
        <div class="sub">Telecom Assistant</div>
    </div>
</div>
""", unsafe_allow_html=True)

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

        typing_class = " typing" if str(message) == "Typing..." else ""

        if robot:
            avatar_html = f'<img class="msg-avatar" src="data:image/png;base64,{robot}">'
        else:
            avatar_html = '<div class="msg-avatar user-avatar">🤖</div>'

        chat_html += f"""
<div class="message-row bot-row">
    {avatar_html}
    <div class="msg bot{typing_class}">{safe_msg}</div>
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
# QUICK SERVICES
# =========================

st.markdown(
    '<div class="quick-title">⚡ Quick Services</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)
c4, c5, c6 = st.columns(3)

with c1:
    if st.button("Network Test"):
        send_message("Network Test")
        st.rerun()

with c2:
    if st.button("Internet Usage"):
        send_message("Internet Usage")
        st.rerun()

with c3:
    if st.button("Renew Package"):
        send_message("Renew Package")
        st.rerun()

with c4:
    if st.button("International Calls"):
        send_message("International Calls")
        st.rerun()

with c5:
    if st.button("Offers & Games"):
        send_message("Offers & Games")
        st.rerun()

with c6:
    if st.button("Contact Support"):
        send_message("Contact Support")
        st.rerun()

# =========================
# CLEAR CHAT
# =========================

if st.button("🗑 Clear Chat"):

    st.session_state[CHAT_KEY] = [
        ("bot", "Hi 👋 I am CoCare AI Assistant. How can I help you?")
    ]

    reset_context()
    save_chat_history()

    st.rerun()

# =========================
# CHAT INPUT
# =========================

user_input = st.chat_input("Type your question here...")

if user_input:

    send_message(user_input)

    st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import os

st.set_page_config(page_title="لوحة الموظف", layout="centered")

st.markdown("""

""", unsafe_allow_html=True)

=========================
الواجهة الأصلية كما هي
=========================

components.html("""

.phone{
width:400px;height:790px;margin;background:#fbfdff;border-radius:42px;
padding:22px 18px 10px;box-shadow:0 8px 25px rgba(0,0,0,.25);
border:1px solid #d9dee8;position;overflow;
}

.page{height:690px;overflow-y;padding-bottom:90px}
.top{display;grid-template-columns:124px 1fr;gap:14px}

.rate-card{
height:124px;background;border-radius:16px;display;
align-items;justify-content;box-shadow:0 4px 14px rgba(0,0,0,.12)
}

.circle{
width:100px;height:100px;border-radius:50%;border:10px solid var(--accent);
display;flex-direction;align-items;justify-content
}
.circle span{font-size:10px}
.circle b{font-size:25px}

.head{display;justify-content;align-items;margin-bottom:10px}

.title{
font-size:17px;font-weight:900;line-height:1.2;color(--navy);
}

.section{
font-size:13px;font-weight:800;margin:14px 0 6px;color(--navy-light);
}

.location{
font-size:11px;border;background;border-radius:8px;padding:7px;
box-shadow:0 2px 8px rgba(0,0,0,.10);max-width:115px;
color(--navy);font-weight:600;
}

.map{
height:98px;background:#e6ecf5;border-radius:13px;position;overflow;
box-shadow 0 0 0 1px #d7deea
}

.road{position;height:3px;width:240px;background;opacity:.9;transform(-35deg)}
.road2{position;height:3px;width:220px;background;opacity:.9;transform(35deg)}
.dot{position;color:#e02020;font-size:21px}

.alerts{display;grid-template-columns(3,1fr);gap:9px}

.alert{
background;border-radius:10px;overflow;min-height:118px;
box-shadow:0 4px 14px rgba(0,0,0,.12);font-size:9.5px;
cursor;transition:.2s;
}
.alert{transform(-5px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
.alert{transform(.95)}

.alert-head{color;padding:8px;font-weight:900;font-size:13px}
.red{background:#e94c4c}
.yellow{background:#f2b72f}
.blue{background:#2f80ed}

.alert-body{padding:8px;line-height:1.35;color:#1f2937}

.metrics{display;grid-template-columns:1fr 1fr;gap:13px}

.chart{
height:145px;background;border-radius:14px;
box-shadow:0 4px 14px rgba(0,0,0,.10);position;overflow;
cursor;transition:.2s;
}
.chart{transform(-5px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
.chart{transform(.95)}

.chart-title{
position;bottom:29px;left:0;width:100%;text-align;font-size:12px
}

.chart-stars{
position;bottom:8px;left:0;width:100%;text-align;color:#1267c9;font-size:18px
}

.line{position;left:35px;bottom:55px;width:130px;height:62px}
.bar{position;bottom:55px;width:19px;background:#2f80ed}

.employee{
background;border-radius:14px;padding:11px;display;gap:12px;align-items;
box-shadow:0 4px 14px rgba(0,0,0,.10);
cursor;transition:.2s;
}
.employee{transform(-5px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
.employee{transform(.95)}

.avatar{
width:58px;height:58px;border-radius:50%;background:#dbeafe;
display;align-items;justify-content;font-size:30px
}

.emp-name{font-size:15px;font-weight:900;color(--navy)}
.emp-text{font-size:10px;line-height:1.25;color:#1f2937}

.nav{
position;
bottom:10px;
left:15px;
right:15px;
display;
justify-content;
gap:10px;
}

.nav form{width:33%;margin:0}

.nav button{
width:100%;
height:58px;
border-radius:18px;
border;
background;
font-weight:900;
font-size:13px;
cursor;
box-shadow:0 4px 10px rgba(0,0,0,.1);
transition:.25s;
}

.nav button{
background:#eef6ff;
color:#2f80ed;
transform(-3px);
}

.nav span{
display;
font-size:22px;
margin-bottom:3px;
color:#376f91;
}

.nav .active-nav{
background:#eef6ff;
color:#2f80ed;
}



    <div>
        <div class="head">
            <div class="title">مشاكل<br>الشبكة</div>

            <select class="location" id="region" onchange="updateRegion()">
                <option value="عمّان">📍 عمّان</option>
                <option value="الزرقاء">📍 الزرقاء</option>
                <option value="إربد">📍 إربد</option>
                <option value="البلقاء">📍 البلقاء</option>
                <option value="المفرق">📍 المفرق</option>
                <option value="جرش">📍 جرش</option>
                <option value="عجلون">📍 عجلون</option>
                <option value="مادبا">📍 مادبا</option>
                <option value="الكرك">📍 الكرك</option>
                <option value="الطفيلة">📍 الطفيلة</option>
                <option value="معان">📍 معان</option>
                <option value="العقبة">📍 العقبة</option>
            </select>
        </div>

        <div class="map">
            <div class="road" style="top:8px;left:-65px;"></div>
            <div class="road" style="top:32px;left:-40px;"></div>
            <div class="road" style="top:60px;left:-65px;"></div>
            <div class="road" style="top:86px;left:-25px;"></div>
            <div class="road2" style="top:18px;left:48px;"></div>
            <div class="road2" style="top:55px;left:70px;"></div>
            <div class="road2" style="top:90px;left:90px;"></div>
            <div class="dot" style="top:22px;left:78px;">●</div>
            <div class="dot" style="top:44px;left:138px;">●</div>
            <div class="dot" style="top:67px;left:148px;">●</div>
            <div class="dot" style="top:13px;left:182px;font-size:13px;">●</div>
        </div>
    </div>
</div>

<div class="section">سجل التنبيهات والمشاكل</div>

<div class="alerts">
    <div class="alert">
        <div class="alert-head red">❗ مشكلة</div>
        <div class="alert-body">
            <b>المنطقة:</b> <span class="region-name">عمّان</span>: يتم عرض مشاكل العملاء من سجل الشات بالأسفل.
        </div>
    </div>

    <div class="alert">
        <div class="alert-head yellow">⚠️ داخلي</div>
        <div class="alert-body">
            تنبيهات الموظف تظهر حسب تحليل رسالة العميل.
        </div>
    </div>

    <div class="alert">
        <div class="alert-head blue">↗ خارجي</div>
        <div class="alert-body">
            إشعارات العميل تظهر عند الحاجة حسب التصعيد.
        </div>
    </div>
</div>

<div class="section">مؤشرات أداء الشبكة</div>

<div class="metrics">
    <div class="chart">
        <svg class="line" viewBox="0 0 140 70">
            <polygon points="0,65 0,55 45,40 95,25 135,5 135,65" fill="#dbeafe"/>
            <polyline points="0,55 45,40 95,25 135,5" fill="none" stroke="#2f80ed" stroke-width="4"/>
        </svg>
        <div style="position:absolute;left:15px;top:25px;font-size:12px;">20</div>
        <div style="position:absolute;left:15px;top:63px;font-size:12px;">10</div>
        <div style="position:absolute;left:15px;top:101px;font-size:12px;">0</div>
        <div class="chart-title">متوسط زمن الاستجابة (ms)</div>
    </div>

    <div class="chart">
        <div class="bar" style="left:45px;height:43px;"></div>
        <div class="bar" style="left:76px;height:28px;"></div>
        <div class="bar" style="left:107px;height:70px;"></div>
        <div class="bar" style="left:138px;height:31px;"></div>
        <div style="position:absolute;left:18px;top:25px;font-size:12px;">10</div>
        <div style="position:absolute;left:18px;top:66px;font-size:12px;">5</div>
        <div style="position:absolute;left:18px;top:101px;font-size:12px;">0</div>
        <div class="chart-title">فقدان الحزم (%)</div>
        <div class="chart-stars">★ ★ ★</div>
    </div>
</div>

<div class="section">إعلان موظف الشهر</div>

<div class="employee">
    <div class="avatar">👨‍💼</div>
    <div>
        <div class="emp-name">أحمد علي</div>
        <div class="emp-text">
            تقديرًا لجهودك المميزة وأدائك الاستثنائي في تحسين استقرار الشبكة وخدمة العملاء هذا الشهر.
            تهانينا على هذا التكريم المستحق.
        </div>
    </div>
</div>
<form action="/" method="get" target="_top">
    <input type="hidden" name="page" value="logout">
    <button type="submit"><span>⇥</span>خروج</button>
</form>

<form action="/" method="get" target="_top">
    <input type="hidden" name="page" value="todo">
    <button type="submit"><span>☑</span>المهام</button>
</form>
=========================
تحليل رسائل العملاء - بدون تغيير الواجهة
=========================

st.markdown("---")
st.subheader("📊 تحليل رسائل العملاء")

BASE_DIR = os.path.dirname(os.path.abspath(file))
CHAT_LOG_PATH = os.path.join(BASE_DIR, "..", "data", "chat_logs.csv")

if os.path.exists(CHAT_LOG_PATH):
logs = pd.read_csv(CHAT_LOG_PATH, encoding="utf-8-sig")

if logs.empty:
    st.info("لا توجد رسائل عملاء حتى الآن.")
else:
    latest = logs.tail(1).iloc[0]

    channel = str(latest.get("display_channel", "none"))
    notification_type = str(latest.get("notification_type", "none"))
    escalation = str(latest.get("escalation", "False")).lower() in ["true", "1", "yes"]
    network_problem = str(latest.get("network_problem", "False")).lower() in ["true", "1", "yes"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Intent", latest.get("intent", ""))
        st.metric("Sentiment", latest.get("sentiment", ""))

    with col2:
        st.metric("Problem", latest.get("issue_type", ""))
        st.metric("Network", str(latest.get("network_problem", "")))

    with col3:
        st.metric("Notification", notification_type)
        st.metric("Channel", channel)

    st.markdown("### 🚦 حالة التصعيد")

    if channel == "monitoring_log":
        st.info("🟢 متابعة عادية: تم تسجيل المشكلة بدون إرسال إشعار داخلي أو خارجي.")

    elif channel == "customer_app":
        st.warning("🟡 External Notification: تم إرسال إشعار للعميل بسبب تكرار المشكلة من نفس العميل.")

    elif channel == "employee_dashboard":
        st.error("🔴 Internal Escalation: المشكلة تكررت في نفس المنطقة وتحتاج متابعة من الموظف.")

    elif not network_problem:
        st.success("✅ لا توجد مشكلة شبكة في آخر رسالة.")

    else:
        st.info("لا توجد مرحلة تصعيد محددة حاليًا.")

    st.markdown("### 🚨 Problem / Alert")
    if network_problem:
        st.error(f"نوع المشكلة: {latest.get('issue_type', '')}")
        st.write("السبب:", latest.get("reason", ""))
        st.write("الإجراء المقترح:", latest.get("suggested_action", ""))
        st.write("عدد تكرار المشكلة للعميل:", latest.get("repeat_count", ""))
        st.write("عدد مشاكل المنطقة:", latest.get("area_issue_count", ""))
    else:
        st.success("لا توجد مشكلة شبكة حالية.")

    st.markdown("### 🏢 Internal Notification")
    if channel == "employee_dashboard":
        st.warning("تنبيه داخلي للموظف: يرجى متابعة الحالة من لوحة الموظف.")
    else:
        st.info("لا يوجد تنبيه داخلي حاليًا.")

    st.markdown("### 📱 External Notification")
    if channel == "customer_app":
        st.warning("تنبيه خارجي للعميل: سيتم إشعار العميل بمتابعة المشكلة.")
    elif channel == "employee_dashboard" and str(latest.get("show_to_customer", "0")) in ["1", "True", "true"]:
        st.warning("تنبيه خارجي للعميل + تصعيد داخلي للموظف.")
    else:
        st.info("لا يوجد تنبيه خارجي حاليًا.")

    st.markdown("### 👤 آخر رسالة")
    st.write("رسالة العميل:", latest.get("message", ""))
    st.write("رد البوت:", latest.get("bot_response", ""))
    st.write("المنطقة:", latest.get("region", ""))
    st.write("العميل:", latest.get("user_id", ""))
    st.write("Decision Rule:", latest.get("decision_rule", ""))

    st.markdown("### 📋 آخر 20 سجل")
    st.dataframe(logs.tail(20), use_container_width=True)

else:
st.info("لا يوجد ملف سجلات بعد. أرسلي رسالة من شات العميل أولاً.")

إغلاق
