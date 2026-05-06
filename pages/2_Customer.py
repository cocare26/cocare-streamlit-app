import streamlit as st
import base64
import os

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="Telecom Dashboard",
    page_icon="📱",
    layout="centered"
)

# =====================================
# دالة معالجة الصور (Base64)
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

# تحميل صور الروبوت الأساسية (تأكد من وجود هذه الملفات أو تعليق الأسطر)
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# تحميل صور الأيقونات الأربعة الجديدة
# تأكد من وجود هذه الملفات في نفس المجلد
img_internet = get_base64("icon_internet.png")
img_renewals = get_base64("icon_renewals.png")
img_calls = get_base64("icon_calls.png")
img_notifications = get_base64("icon_notifications.png")

# =====================================
# CSS المطور (تعديلات لتغطية الصورة للإطار وإخفاء النص)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
background:#f0f7ff;
font-family:'Segoe UI', sans-serif;
}}
section.main > div {{ padding-top:4px; }}
div[data-testid="stVerticalBlock"] {{ gap:0.4rem; }}

#MainMenu, header, footer {{ visibility:hidden; }}

.block-container {{
max-width:430px;
margin:auto;
padding:12px 16px;
background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%);
border-radius:42px;
box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card {{
background: white;
border-radius: 20px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 4px 15px rgba(0,0,0,.05);
transition: all 0.3s ease;
}}

.balance-card {{
    padding: 6px 14px !important;
    margin-bottom: 4px !important;
}}

.card:hover, .nav-item:hover, .bot-bg:hover, .mini-icon-cover:hover {{
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}}

.title {{
font-size:15px;
font-weight:900;
color:#102646;
margin: 4px 0 4px 4px;
}}

.clickable {{ 
    cursor: pointer; 
    transition: all 0.3s ease; 
}}
.clickable:active {{ transform: scale(0.95); }}

.welcome-card {{
    background: white;
    border-radius: 20px;
    padding: 8px 12px;
    margin-bottom: 8px;
    box-shadow: 0 6px 15px rgba(0,0,0,.06);
    display: flex;
    align-items: center;
    position: relative;
    height: 100px;
    transition: all 0.3s ease;
}}

.robot-img-welcome {{
    width: 95px; 
    height: 95px;
    background: transparent !important;
    border-radius: 14px;
    margin-right: 12px;
    object-fit: contain;
    padding: 4px;
    transition: transform 0.4s ease;
}}

.welcome-text-container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
}}

.needle {{
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 2px;
    height: 30px;
    background: #333;
    transform-origin: bottom center;
    z-index: 5;
}}

/* تنسيقات قسم قوة الشبكة - تم الحفاظ عليها */
.signal-icon {{
    display: flex;
    align-items: flex-end;
    gap: 2px;
    justify-content: center;
    margin-top: 5px;
}}
.signal-bar {{
    width: 4px;
    border-radius: 1px;
}}

/* تنسيقات شبكة الأيقونات المحدثة */
.grid4 {{ 
    display:grid; 
    grid-template-columns:repeat(4,1fr); 
    gap:6px; 
    margin: 8px 0 6px; 
}}

/* تصميم مربع الأيقونة المغطاة بالكامل */
.mini-icon-cover {{
    background:white; /* خلفية بيضاء احتياطية */
    border-radius:18px; /* نفس حواف الإطار الأبيض القديم */
    min-height:90px;
    padding: 0; /* إلغاء البادينج للسماح للصورة بالتغطية الكاملة */
    text-align:center;
    box-shadow:0 6px 15px rgba(0,0,0,.06);
    transition: all 0.3s ease;
    overflow: hidden; /* يضمن أن الصورة المربعة لا تخرج عن حواف الإطار المنحنية */
    display: flex;
    align-items: center;
    justify-content: center;
}}

/* تنسيق الصورة الموحدة لتغطية الإطار */
.mini-cover-img {{
    width: 100%; /* تملأ كل عرض المربع */
    height: 100%; /* تملأ كل ارتفاع المربع */
    object-fit: cover; /* الأهم: تجعل الصورة تغطي المساحة بالكامل وتقص الزوائد */
    object-position: center; /* تضمن توسيط الصورة المقصوصة */
}}

/* تنسيقات الشريط السفلي - تم الحفاظ عليها */
.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 22px; font-weight: 800; transition: all 0.3s ease; }}
.nav-text {{ font-size: 10px; display: block; }}
.bot-bg {{
width:50px; height:50px; background:white; border-radius:12px;
margin: 0 auto 4px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
transition: all 0.3s ease;
}}
.active {{ color:inherit; }} 
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الملف الشخصي
# =====================================
st.markdown(f"""
<div class="welcome-card clickable">
    <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
    <div class="welcome-text-container">
        <div style="font-size:20px; font-weight:900; color:#102646; line-height:1.1;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555; margin-top:2px;">+962 79 123 4567</div>
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
        <div style="font-size:11px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0;">
        📍 Location: Amman</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">Your Number Info</div>
<div class="card balance-card clickable">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
<div style="font-size:32px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
</div>
<div style="flex: 1; text-align: right;">
<div style="position: relative; width: 60px; height: 30px; margin-left: auto;">
    <div style="width: 50px; height: 25px; border-radius: 50px 50px 0 0; background: linear-gradient(90deg, #1A4FA0 60%, #E0E0E0 60%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 5px; width: 40px; height: 20px; background: white; border-radius: 40px 40px 0 0;"></div>
        <div class="needle" style="height:20px; transform: rotate(45deg);"></div>
    </div>
</div>
<div style="font-size:10px; font-weight:900; color:#102646;">6 GB</div>
</div>
</div>
<div style="margin-top:4px; height:6px; border-radius:10px; background:#E0E0E0; overflow:hidden;">
<div style="width:78%; height:100%; background:#1A4FA0;"></div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات (المعدلة للتغطية وإزالة النص)
# =====================================
# تم استبدال الرموز بالنصوص المرفقة كـ `src` للصور المعدلة، وتم حذف النصوص تماماً
st.markdown(f"""
<div class="grid4">
<div class="mini-icon-cover clickable">
    <img src="data:image/png;base64,{img_internet}" class="mini-cover-img">
</div>
<div class="mini-icon-cover clickable">
    <img src="data:image/png;base64,{img_renewals}" class="mini-cover-img">
</div>
<div class="mini-icon-cover clickable">
    <img src="data:image/png;base64,{img_calls}" class="mini-cover-img">
</div>
<div class="mini-icon-cover clickable">
    <img src="data:image/png;base64,{img_notifications}" class="mini-cover-img">
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card clickable" style="padding-top: 10px;">
<div style="font-weight:900; font-size:12px; color:#102646; margin-bottom: 5px;">⭐ Service Security Rate</div>
<div style="display: flex; gap: 8px; margin-bottom: 8px;">
<div style="background: linear-gradient(90deg, #4caf50 60%, #ffeb3b 60%, #ffeb3b 85%, #f44336 85%); height: 20px; border-radius: 4px; flex: 2; display: flex; align-items: center; justify-content: space-between; padding: 0 10px; color: white; font-size: 11px; font-weight: bold;">
<span>★ 4.5</span>
<span>4.5%</span>
</div>
<div style="background: #E0E0E0; height: 20px; border-radius: 4px; padding: 0 10px; color: white; font-size: 11px; font-weight: bold; display: flex; align-items: center;">24%</div>
</div>
<div style="text-align:center; font-weight:700; font-size:11px; color:#666;">Rate our service</div>
<div style="display: flex; justify-content: center; gap: 5px; font-size: 20px; color: #ffcc00; margin-top: 2px;">
★ ★ ★ ★ ☆
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. قوة الشبكة
# =====================================
st.markdown("""
<div class="title">Network Strength in your area</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 1.2;">
<div style="font-size:14px; font-weight:900; color:#102646;">📍 Amman</div>
<div style="font-size:12px; font-weight:700; color:#1A4FA0; margin-bottom:6px;">Very Strong Signal</div>
<div style="display: flex; gap: 4px;">
<div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
<div style="font-size: 7px; color: #666; font-weight:bold;">Packet Loss (%)</div>
<div style="font-size: 16px; font-weight: 900; color: #000;">0</div>
</div>
<div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
<div style="font-size: 7px; color: #666; font-weight:bold;">Avg Jitter (ms)</div>
<div style="font-size: 16px; font-weight: 900; color: #000;">19</div>
</div>
</div>
</div>
<div style="flex: 1; text-align: center;">
<div style="position: relative; width: 80px; margin: 0 auto;">
    <div style="width: 80px; height: 40px; border-radius: 80px 80px 0 0; background: linear-gradient(90deg, #4caf50 20%, #ffeb3b 50%, #f44336 100%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 8px; width: 64px; height: 32px; background: white; border-radius: 64px 64px 0 0;"></div>
        <div class="needle" style="height: 35px; transform: rotate(-60deg);"></div>
    </div>
<div style="font-size: 9px; font-weight: 900; color: #102646; margin-top: 4px;">-68dBm (Excellent)</div>
<div class="signal-icon">
    <div class="signal-bar" style="height:4px; background:#1A4FA0;"></div>
    <div class="signal-bar" style="height:7px; background:#1A4FA0;"></div>
    <div class="signal-bar" style="height:10px; background:#1A4FA0;"></div>
    <div style="width:1px; height:12px; background:#DDD; margin:0 2px;"></div>
    <div class="signal-bar" style="height:4px; background:#4CAF50;"></div>
    <div class="signal-bar" style="height:7px; background:#4CAF50;"></div>
    <div class="signal-bar" style="height:10px; background:#4CAF50;"></div>
</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 6. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item clickable">⚙️<span class="nav-text">Settings</span></div>
<div class="nav-item clickable">🎡<span class="nav-text">Spin</span></div>
<div class="nav-item clickable">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:34px;"></div>
<span class="nav-text">Chatbot</span>
</div>
<div class="nav-item active clickable">🏠<span class="nav-text">Home</span></div>
<div class="nav-item clickable">🎁<span class="nav-text">Game</span></div>
</div>
""", unsafe_allow_html=True)
