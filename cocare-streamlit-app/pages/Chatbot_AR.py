import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="المساعد الذكي", layout="centered")

with open("robot_head.png", "rb") as f:
    robot = base64.b64encode(f.read()).decode()

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
}}

.menu div {{
    padding:8px 12px;
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
    font-size:20px;
    cursor:pointer;
}}

.chat-input {{
    flex:1;
    height:34px;
    border-radius:22px;
    border:none;
    padding-right:10px;
}}

.send {{
    width:40px;
    height:40px;
    border-radius:50%;
    background:#1c6fa4;
    color:white;
    text-align:center;
    line-height:40px;
    cursor:pointer;
}}
</style>
</head>

<body>
<div class="phone">

    <div class="topbar">
        <a href="/Customer" target="_self" style="text-decoration:none;">
            <div class="back">›</div>
        </a>
        <img class="avatar" src="data:image/png;base64,{robot}">
        <div class="dot"></div>
        <div class="status">جاهز للمساعدة</div>
    </div>

    <div id="chatBox" class="chat-box">
        <div class="msg bot">مرحبًا 👋 كيف أقدر أساعدك؟</div>
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
    let m = document.getElementById("menu");
    m.style.display = m.style.display === "block" ? "none" : "block";
}}

function addMessage(text,type){{
    let box = document.getElementById("chatBox");
    let msg = document.createElement("div");
    msg.className = "msg " + type;
    msg.innerText = text;
    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}}

function botReply(text){{
    let r = "تم استلام طلبك";

    if(text=="فحص الشبكة") r="الشبكة عندك ممتازة 👍";
    else if(text=="استهلاك الإنترنت") r="تقدر تشوف استهلاكك من التطبيق";
    else if(text=="تجديد الباقة") r="تقدر تجدد الباقة من قسم الباقات";
    else if(text=="المكالمات الدولية") r="الخدمة متاحة عندك";
    else if(text=="العروض") r="في عروض جديدة حالياً 🎁";
    else if(text=="الدعم") r="تم تحويلك للدعم الفني 👨‍💻";

    setTimeout(()=>addMessage(r,"bot"),500);
}}

function sendMessage(){{
    let input=document.getElementById("chatInput");
    let text=input.value.trim();
    if(!text) return;

    addMessage(text,"user");
    input.value="";
    botReply(text);
}}

function quickMsg(text){{
    document.getElementById("menu").style.display="none";
    addMessage(text,"user");
    botReply(text);
}}

function checkEnter(event){{
    if(event.key==="Enter"){{
        sendMessage();
    }}
}}
</script>

</body>
</html>
"""

components.html(html, height=730)
