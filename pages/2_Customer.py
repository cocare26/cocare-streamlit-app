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

# تحميل الصور الأساسية
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# تحميل صور الأيقونات الأربعة الجديدة
icon_internet = get_base64("pages/internet.png")
icon_renewals = get_base64("pages/renewals.png")
icon_calls = get_base64("pages/calls.png")
icon_notifications = get_base64("pages/notifications.png")

# --- تحميل صور الشريط السفلي ---
icon_sitting = get_base64("pages/sitting.png")
icon_spin = get_base64("pages/spin.png")
icon_home = get_base64("pages/home.png")
icon_game = get_base64("pages/game.png")

# =====================================
# CSS المطور
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

.rating-card {{
    padding: 4px 14px 6px !important;
    margin-bottom: 4px !important;
}}

.card:hover, .nav-item:hover, .bot-bg:hover {{
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

.star-rating {{
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    gap: 4px;
}}
.star-rating input {{ display: none; }}
.star-rating label {{
    font-size: 24px;
    color: #ddd;
    cursor: pointer;
    transition: color 0.2s, transform 0.2s;
}}
.star-rating label:hover {{ transform: scale(1.2); }}
.star-rating input:checked ~ label,
.star-rating label:hover,
.star-rating label:hover ~ label {{
    color: #ffcc00;
}}

.rating-bar-container {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(90deg, #1A4FA0, #46A1E2, #D47E2E, #C63F2A);
    height: 22px;
    border-radius: 4px;
    margin-top: 6px;
    padding: 0 10px;
    color: white;
    font-size: 11px;
    font-weight: bold;
}}

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

.grid4 {{ 
    display:grid; 
    grid-template-columns:repeat(4,1fr); 
    gap:6px; 
    margin: 8px 0 6px; 
    }}

    div.stButton > button {{
    width: 100%;
    height: 90px;
    opacity: 0;
    margin-top: -90px;
    cursor: pointer;
    border: none;
}}
/* تعديل الأيقونات بالوسط: إزالة الإطار والظل والنص */
.mini-no-border {{
    background: transparent; 
    border-radius: 0; 
    min-height: 85px;
    padding: 0; 
    text-align: center;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.mini-img-large {{
    width: 85px; /* تكبير الصورة لتأخذ مساحة الإطار السابق */
    height: 85px;
    object-fit: contain;
}}

/* استايل صور الشريط السفلي */
.nav-img-footer {{
    width: 35px;
    height: 35px;
    object-fit: contain;
}}

.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: center;
}}
.nav-item {{ transition: all 0.3s ease; display: flex; flex-direction: column; align-items: center; }}
.bot-bg {{
width:50px; height:50px; background:white; border-radius:12px;
margin: 0 auto 4px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
transition: all 0.3s ease;
}}
.active {{ color:inherit; transform: scale(1.1); }} 
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
# 3. أيقونات الخدمات + التنقل بالصور
# =====================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("internet.png", use_container_width=True)
    if st.button(" ", key="internet_btn"):
        st.switch_page("InternetPackages.py")

with col2:
    st.image("renewals.png", use_container_width=True)
    if st.button(" ", key="renewals_btn"):
        st.switch_page("RenewalsTariff.py")

with col3:
    st.image("calls.png", use_container_width=True)
    if st.button(" ", key="calls_btn"):
        st.switch_page("InternationalCalls.py")

with col4:
    st.image("notifications.png", use_container_width=True)
    if st.button(" ", key="notif_btn"):
        st.switch_page("NetworkNotifications.py")
        
# =====================================
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card rating-card">
<div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
<div class="rating-bar-container">
    <span>★ 4.5</span>
    <span>4.5%</span>
    <span style="background:rgba(255,255,255,0.3); padding:0 5px; border-radius:2px;">24%</span>
</div>
<div style="text-align:center; margin-top:8px; font-weight:700; font-size:11px; color:#666; margin-bottom:2px;">Rate our service</div>
<div class="star-rating">
    <input type="radio" id="5" name="rate"><label for="5">★</label>
    <input type="radio" id="4" name="rate"><label for="4">★</label>
    <input type="radio" id="3" name="rate"><label for="3">★</label>
    <input type="radio" id="2" name="rate"><label for="2">★</label>
    <input type="radio" id="1" name="rate"><label for="1">★</label>
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
# 6. الشريط السفلي (معدل: صور فقط)
# =====================================
st.markdown(f""" 
<div class="nav">
<div class="nav-item clickable">
<img src="data:image/png;base64,{icon_sitting}"
class="nav-img-footer">
</div> 
<div class="nav-item clickable">
<img src="data:image/png;base64,{icon_spin}" 
class="nav-img-footer"> 
</div> 
<div class="nav-item clickable"> 
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" 
style="width:34px;"></div>
</div> 
<div class="nav-item active clickable">
<img src="data:image/png;base64,{icon_home}"
class="nav-img-footer"> 
</div> 
<div class="nav-item clickable"> 
<img src="data:image/png;base64,{icon_game}" 
class="nav-img-footer"> 
</div> 
</div>
""", unsafe_allow_html=True)
