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

# تحميل الصور
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

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

/* تنسيق الـ Popover ليعود لحجم الـ mini الأصلي */
div[data-testid="stPopover"] {{
    width: 100%;
}}

div[data-testid="stPopover"] > button {{
    background: white !important;
    border: none !important;
    padding: 8px 2px !important;
    width: 100% !important;
    min-height: 90px !important; /* الحجم الأصلي */
    border-radius: 18px !important;
    box-shadow: 0 6px 15px rgba(0,0,0,.06) !important;
    transition: all 0.3s ease !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
}}

/* تنسيق النص داخل زر البوب أوفر ليطابق mini-text */
div[data-testid="stPopover"] p {{
    font-size: 10px !important;
    font-weight: 800 !important;
    color: #102646 !important;
    line-height: 1.1 !important;
    margin: 0 !important;
    text-align: center !important;
}}

div[data-testid="stPopover"] > button:hover {{
    transform: translateY(-5px) !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
}}

.card {{
background: white;
border-radius: 20px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 4px 15px rgba(0,0,0,.05);
transition: all 0.3s ease;
}}

.balance-card {{ padding: 6px 14px !important; margin-bottom: 4px !important; }}
.rating-card {{ padding: 4px 14px 6px !important; margin-bottom: 4px !important; }}

.title {{
font-size:15px;
font-weight:900;
color:#102646;
margin: 4px 0 4px 4px;
}}

.clickable {{ cursor: pointer; transition: all 0.3s ease; }}
.clickable:active {{ transform: scale(0.95); }}

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
}}

.robot-img-welcome {{
    width: 95px; height: 95px;
    object-fit: contain;
    margin-right: 12px;
}}

.needle {{
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 2px;
    height: 30px;
    background: #333;
    transform-origin: bottom center;
}}

.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 22px; font-weight: 800; }}
.nav-text {{ font-size: 10px; display: block; }}
.bot-bg {{
width:50px; height:50px; background:white; border-radius:12px;
margin: 0 auto 4px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}
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
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2026</div>
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
# 3. أيقونات الخدمات (Popovers)
# =====================================
cols = st.columns(4)

with cols[0]:
    pop1 = st.popover("📡\nInternet\nPackages")
    pop1.info("Internet bundles available for your plan.")

with cols[1]:
    pop2 = st.popover("🌍\nRenewals +\nChanges")
    pop2.success("Switch to a new monthly plan.")

with cols[2]:
    pop3 = st.popover("💰\nInternational\nCalls")
    pop3.warning("Global calling rates.")

with cols[3]:
    pop4 = st.popover("🔔\nNetwork\nNotifications")
    pop4.error("Check network status.")

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
<div style="font-size:12px; font-weight:700; color:#1A4FA0;">Very Strong Signal</div>
<div style="display: flex; gap: 4px; margin-top:5px;">
<div style="background: #F1F7FF; border: 1px solid #E0E0E0; border-radius: 8px; flex: 1; text-align: center; padding: 4px;">
<div style="font-size: 7px; font-weight:bold;">Packet Loss</div><div style="font-size: 14px; font-weight:900;">0</div></div>
<div style="background: #F1F7FF; border: 1px solid #E0E0E0; border-radius: 8px; flex: 1; text-align: center; padding: 4px;">
<div style="font-size: 7px; font-weight:bold;">Avg Jitter</div><div style="font-size: 14px; font-weight:900;">19</div></div>
</div>
</div>
<div style="flex: 1; text-align: center;">
<div style="position: relative; width: 70px; margin: 0 auto;">
    <div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #4caf50, #ffeb3b, #f44336); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
        <div class="needle" style="height: 30px; transform: rotate(-60deg); left:48%;"></div>
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
<div class="nav-item clickable">🏠<span class="nav-text">Home</span></div>
<div class="nav-item clickable">🎁<span class="nav-text">Game</span></div>
</div>
""", unsafe_allow_html=True)
