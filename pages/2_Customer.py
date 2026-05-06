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
# CSS المطور (تثبيت الحجم وتفعيل الحركة)
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

/* إجبار الأيقونات الأربعة على نفس الحجم تماماً */
div[data-testid="stPopover"] {{
    width: 100% !important;
}}
div[data-testid="stPopover"] > button {{
    background: white !important;
    border-radius: 18px !important;
    border: none !important;
    box-shadow: 0 6px 15px rgba(0,0,0,.06) !important;
    padding: 5px !important;
    height: 105px !important; /* ارتفاع ثابت وموحد للكل */
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    overflow: hidden !important; /* لمنع خروج النص عن الحجم */
    text-overflow: ellipsis !important;
}}

/* تأثير الحركة عند مرور الماوس */
div[data-testid="stPopover"] > button:hover {{
    transform: translateY(-10px) !important; /* حركة واضحة للأعلى */
    box-shadow: 0 15px 25px rgba(0,0,0,0.1) !important;
    background-color: #ffffff !important;
}}

.card {{
background: white;
border-radius: 20px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 4px 15px rgba(0,0,0,.05);
}}

.title {{ font-size:15px; font-weight:900; color:#102646; margin: 4px 0 4px 4px; }}
.clickable {{ cursor: pointer; }}

/* نجوم التقييم التفاعلية */
.star-rating {{ display: flex; flex-direction: row-reverse; justify-content: center; gap: 4px; }}
.star-rating label {{ font-size: 24px; color: #ddd; cursor: pointer; transition: 0.2s; }}
.star-rating label:hover, .star-rating label:hover ~ label {{ color: #FFD700; }}

.rating-bar-container {{
    display: flex; align-items: center; justify-content: space-between;
    background: linear-gradient(90deg, #1A4FA0, #46A1E2, #D47E2E, #C63F2A);
    height: 22px; border-radius: 4px; margin-top: 6px; padding: 0 10px;
    color: white; font-size: 11px; font-weight: bold;
}}
.needle {{ position: absolute; bottom: 0; left: 50%; width: 2px; height: 30px; background: #333; transform-origin: bottom center; z-index: 5; }}
.signal-icon {{ display: flex; align-items: flex-end; gap: 2px; justify-content: center; margin-top: 5px; }}
.signal-bar {{ width: 4px; border-radius: 1px; }}

.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 22px; font-weight: 800; cursor: pointer; }}
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
    <div style="background: white; border-radius: 20px; padding: 8px 12px; margin-bottom: 8px; box-shadow: 0 6px 15px rgba(0,0,0,.06); display: flex; align-items: center; height: 100px;">
    <img src="data:image/png;base64,{robot_full}" style="width: 95px; height: 95px; border-radius: 14px; margin-right: 12px; object-fit: contain;">
    <div class="welcome-text-container">
        <div style="font-size:20px; font-weight:900; color:#102646; line-height:1.1;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555; margin-top:2px;">+962 79 123 4567</div>
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
        <div style="font-size:11px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0; width: fit-content;">📍 Amman</div>
    </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">Your Number Info</div>
<div class="card clickable" style="padding: 6px 14px !important; margin-bottom: 4px !important;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
<div style="font-size:32px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
</div>
<div style="flex: 1; text-align: right;">
<div style="position: relative; width: 60px; height: 30px; margin-left: auto;">
    <div style="width: 50px; height: 25px; border-radius: 50px 50px 0 0; background: linear-gradient(90deg, #1A4FA0 60%, #E0E0E0 60%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 5px; width: 40px; height: 20px; background: white; border-radius: 40px 40px 0 0;"></div>
        <div class="needle" style="height:20px; transform: rotate(45deg); left:48%;"></div>
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
# 3. أيقونات الخدمات (Popovers) - الآن بأحجام ثابتة وحركة
# =====================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.popover("📡\nInternet\nPackages"):
        st.button("Buy 1GB", key="b1")

with col2:
    with st.popover("🌍\nRenewals +\nChanges"):
        st.button("Renew Now", key="b3")

with col3:
    with st.popover("💰\nInternational\nCalls"):
        st.button("Activate", key="b4")

with col4:
    with st.popover("🔔\nNetwork\nNotifications"):
        st.write("• Network update at 12AM")

# =====================================
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card" style="padding: 4px 14px 6px !important; margin-bottom: 4px !important;">
<div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
<div class="rating-bar-container">
    <span>★ 4.5</span>
    <span>4.5%</span>
    <span style="background:rgba(255,255,255,0.3); padding:0 5px; border-radius:2px;">24%</span>
</div>
<div style="text-align:center; margin-top:8px; font-weight:700; font-size:11px; color:#666; margin-bottom:2px;">Rate our service</div>
<div class="star-rating">
    <label>★</label><label>★</label><label>★</label><label>★</label><label>★</label>
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
        <div class="needle" style="height: 35px; transform: rotate(-60deg); left:48%;"></div>
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
<div class="nav-item">⚙️<span class="nav-text">Settings</span></div>
<div class="nav-item">🎡<span class="nav-text">Spin</span></div>
<div class="nav-item">
<div class="bot-bg
