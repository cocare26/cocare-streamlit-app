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

# تحميل صور الأيقونات
icon_internet = get_base64("internet.png")
icon_renewals = get_base64("renewals.png")
icon_calls = get_base64("calls.png")
icon_notifications = get_base64("notifications.png")

# تحميل صور الشريط السفلي
icon_sitting = get_base64("sitting.png")
icon_spin = get_base64("spin.png")
icon_home = get_base64("home.png")
icon_game = get_base64("game.png")

# تعريف المتغير page
page = "2_Customer_EN"

# =====================================
# CSS المطور (تم تعديله لإجبار العرض الأفقي)
# =====================================
st.markdown("""
<style>
*{ margin:0; padding:0; box-sizing:border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}
section.main > div { padding-top:4px; }
div[data-testid="stVerticalBlock"] { gap:0.4rem; }

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px; 
    min-height:820px; 
    margin:auto;
    padding:12px 16px;
    background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

/* --- الحل النهائي لإجبار الأعمدة على البقاء في صف واحد على الموبايل --- */
[data-testid="stHorizontalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: flex-start !important;
    justify-content: space-between !important;
}

[data-testid="column"] {
    width: auto !important;
    flex: 1 1 0% !important;
    min-width: 0px !important;
}
/* ------------------------------------------------------------------- */

.card {
    background: white;
    border-radius: 20px;
    padding: 10px 14px;
    margin-bottom: 8px;
    box-shadow: 0 4px 15px rgba(0,0,0,.05);
    transition: all 0.3s ease;
}
.rating-card {
    padding: 4px 14px 6px !important;
    margin-bottom: 4px !important;
}

.title {
    font-size:15px;
    font-weight:900;
    color:#102646;
    margin: 4px 0 4px 4px;
}

.clickable {
    cursor: pointer; 
    transition: all 0.3s ease; 
    position: relative; 
}
.clickable:active { transform: scale(0.95); }

.service-icon-img {
    width: 60px;
    height: 60px;
    object-fit: contain;
    margin-bottom: 2px;
}

.service-label {
    font-size: 8px;
    font-weight: 800;
    color: #102646;
    line-height: 1.1;
    text-align: center;
}

.nav-item {
    display: flex; 
    flex-direction: column; 
    align-items: center; 
    color:#6b6b6b; 
    font-size: 9px;
    font-weight: 700;
}

.nav-img-footer {
    width: 32px;
    height: 32px;
    object-fit: contain;
    margin-bottom: 2px;
}

.bot-bg {
    width:42px; height:42px; background:white; border-radius:12px;
    margin: 0 auto 2px; display:flex; align-items:center; justify-content:center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

.stButton > button {
    position: relative;
    width: 100%;
    height: 95px;
    opacity: 0;
    margin-top: -95px;
    border: none;
    background: transparent;
    cursor: pointer;
    z-index: 10;
}

.star-rating { display: flex; flex-direction: row-reverse; justify-content: center; gap: 4px; }
.star-rating input { display: none; }
.star-rating label { font-size: 24px; color: #ddd; cursor: pointer; }
.star-rating input:checked ~ label { color: #ffcc00; }

.rating-bar-container {
    display: flex; align-items: center; justify-content: space-between;
    background: linear-gradient(90deg, #1A4FA0, #46A1E2, #D47E2E, #C63F2A);
    height: 22px; border-radius: 4px; margin-top: 6px; padding: 0 10px;
    color: white; font-size: 11px; font-weight: bold;
}

.welcome-card {
    background: white; border-radius: 20px; padding: 8px 12px; margin-bottom: 8px;
    display: flex; align-items: center; height: 100px;
}
.robot-img-welcome { width: 90px; height: 90px; object-fit: contain; margin-right: 12px; }

.needle {
    position: absolute; bottom: 0; left: 50%; width: 2px; height: 30px;
    background: #333; transform-origin: bottom center; z-index: 5;
}
</style>
""", unsafe_allow_html=True)

# 1. قسم الملف الشخصي
st.markdown(f"""
<div class="welcome-card clickable">
    <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
    <div class="welcome-text-container">
        <div style="font-size:18px; font-weight:900; color:#102646; line-height:1.1;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555; margin-top:2px;">+962 79 123 4567</div>
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
        <div style="font-size:10px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0; display:inline-block;">
        📍 Location: Amman</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. معلومات الرصيد
st.markdown("""
<div class="title">Your Number Info</div>
<div class="card balance-card clickable">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
<div style="font-size:30px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
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

st.markdown("<div style='height:15px'></div>", unsafe_allow_html=True)

# 3. أيقونات الخدمات (تم استبدال extra_small بـ small لتجنب الأخطاء)
cols = st.columns(4, gap="small")

services = [
    {"key": "internet", "icon": icon_internet, "label": "Internet<br>Packages", "page": "pages/InternetPackages.py"},
    {"key": "renewals", "icon": icon_renewals, "label": "Renewals +<br>Tariff", "page": "pages/RenewalsTariff.py"},
    {"key": "calls", "icon": icon_calls, "label": "Int.<br>Calls", "page": "pages/InternationalCalls.py"},
    {"key": "notifications", "icon": icon_notifications, "label": "Network<br>Alerts", "page": "pages/NetworkNotifications.py"}
]

for col, service in zip(cols, services):
    with col:
        clicked = st.button(label="", key=service["key"], use_container_width=True)
        st.markdown(f"""
        <div style="margin-top:-90px; text-align:center; pointer-events:none;">
            <img src="data:image/png;base64,{service['icon']}" class="service-icon-img">
            <div class="service-label">{service['label']}</div>
        </div>
        """, unsafe_allow_html=True)
        if clicked:
            st.switch_page(service["page"])

# 4. قسم التقييم
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

# 5. قوة الشبكة
st.markdown("""
<div class="title">Network Strength in your area</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 1.2;">
<div style="font-size:14px; font-weight:900; color:#102646;">📍 Amman</div>
<div style="font-size:11px; font-weight:700; color:#1A4FA0; margin-bottom:6px;">Very Strong Signal</div>
<div style="display: flex; gap: 4px;">
<div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
<div style="font-size: 7px; color: #666; font-weight:bold;">Packet Loss</div>
<div style="font-size: 14px; font-weight: 900; color: #000;">0</div>
</div>
<div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
<div style="font-size: 7px; color: #666; font-weight:bold;">Avg Jitter</div>
<div style="font-size: 14px; font-weight: 900; color: #000;">19</div>
</div>
</div>
</div>
<div style="flex: 1; text-align: center;">
<div style="position: relative; width: 70px; margin: 0 auto;">
    <div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #4caf50 20%, #ffeb3b 50%, #f44336 100%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
        <div class="needle" style="height: 30px; transform: rotate(-60deg);"></div>
    </div>
<div style="font-size: 8px; font-weight: 900; color: #102646; margin-top: 4px;">Excellent</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:25px'></div>", unsafe_allow_html=True)

# 6. الشريط السفلي (تم إجبار الترتيب الأفقي بـ CSS)
n_cols = st.columns(5, gap="small")

with n_cols[0]:
    st.markdown(f"""
    <div class="nav-item">
        <img src="data:image/png;base64,{icon_sitting}" class="nav-img-footer">
        <span>Settings</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("set", key="nav_set"): st.switch_page("pages/Settings.py")

with n_cols[1]:
    st.markdown(f"""
    <div class="nav-item">
        <img src="data:image/png;base64,{icon_spin}" class="nav-img-footer">
        <span>Spin</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("spi", key="nav_spin"): st.switch_page("pages/_Game_E.py")

with n_cols[2]:
    st.markdown(f"""
    <div class="nav-item">
        <div class="bot-bg">
            <img src="data:image/png;base64,{robot_head}" style="width:30px; height:30px; object-fit:contain;">
        </div>
        <span>Chatbot</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("bot", key="nav_bot"): st.switch_page("cocare-streamlit-app/pages/Chatbot_EN.py")

with n_cols[3]:
    st.markdown(f"""
    <div class="nav-item">
        <img src="data:image/png;base64,{icon_home}" class="nav-img-footer">
        <span>Home</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("hom", key="nav_home"): st.switch_page("pages/2_Customer_EN.py")

with n_cols[4]:
    st.markdown(f"""
    <div class="nav-item">
        <img src="data:image/png;base64,{icon_game}" class="nav-img-footer">
        <span>Game On</span>
    </div>
    """, unsafe_allow_html=True)
    if st.button("gam", key="nav_game"): st.switch_page("pages/_Game_E.py")
