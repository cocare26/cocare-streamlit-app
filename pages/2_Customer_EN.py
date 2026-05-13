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
icon_internet = get_base64("internet.png")
icon_renewals = get_base64("renewals.png")
icon_calls = get_base64("calls.png")
icon_notifications = get_base64("notifications.png")
icon_sitting = get_base64("sitting.png")
icon_spin = get_base64("spin.png")
icon_home = get_base64("home.png")
icon_game = get_base64("game.png")

page = "2_Customer_EN"

# =====================================
# CSS المطور والمعدل (إصلاح التباعد)
# =====================================
st.markdown("""
<style>
*{ margin:0; padding:0; box-sizing:border-box; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}
section.main > div { padding-top:4px; }

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px; 
    margin:auto;
    padding:12px 16px;
    background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%);
    border-radius:42px;
}

/* --- تعديل جذري لمنع تباعد الأيقونات --- */
[data-testid="stHorizontalBlock"] {
    gap: 0px !important; /* إلغاء الفراغ التلقائي بين الأعمدة */
    display: flex !important;
    flex-direction: row !important;
    align-items: flex-start !important;
    justify-content: space-between !important;
}

[data-testid="column"] {
    flex: 1 1 0% !important;
    min-width: 0px !important;
    padding: 0 2px !important; /* مسافة بسيطة جداً يميناً ويساراً */
}

.card {
    background: white; border-radius: 20px; padding: 10px 14px;
    margin-bottom: 8px; box-shadow: 0 4px 15px rgba(0,0,0,.05);
}

.title { font-size:15px; font-weight:900; color:#102646; margin: 4px 0 4px 4px; }

/* تنسيق أيقونات الخدمات */
.service-wrapper {
    display: flex; flex-direction: column; align-items: center;
    text-align: center; pointer-events: none;
}
.service-icon-img { width: 72px; height: 72px; object-fit: contain; }
.service-label { font-size: 10px; font-weight: 800; color: #102646; line-height: 1.2; margin-top: 2px; }

/* تنسيق الشريط السفلي */
.nav-item {
    display: flex; flex-direction: column; align-items: center;
    color:#6b6b6b; font-size: 10px; font-weight: 700; pointer-events: none;
}
.nav-img-footer { width: 34px; height: 34px; object-fit: contain; }
.bot-bg {
    width:50px; height:50px; background:white; border-radius:12px;
    display:flex; align-items:center; justify-content:center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 2px;
}

/* أزرار شفافة فوق التصميم */
.stButton > button {
    position: relative; width: 100% !important; height: 95px !important;
    opacity: 0 !important; margin-top: -95px !important;
    border: none !important; background: transparent !important;
    z-index: 10; cursor: pointer;
}

/* النجوم وقوة الشبكة */
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

.needle {
    position: absolute; bottom: 0; left: 50%; width: 2px; height: 30px;
    background: #333; transform-origin: bottom center; z-index: 5;
}
</style>
""", unsafe_allow_html=True)

# 1. قسم الملف الشخصي
st.markdown(f"""
<div class="card" style="display: flex; align-items: center; height: 100px;">
    <img src="data:image/png;base64,{robot_full}" style="width: 90px; height: 90px; object-fit: contain; margin-right: 12px;">
    <div>
        <div style="font-size:18px; font-weight:900; color:#102646;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555;">+962 79 123 4567</div>
        <div style="font-size:10px; background:#F0F7FF; border-radius:10px; padding:2px 8px; display:inline-block; margin-top:4px; border:1px solid #D0E0F0;">📍 Amman</div>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. معلومات الرصيد
st.markdown("""
<div class="title">Your Number Info</div>
<div class="card">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
<div style="font-size:32px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
</div>
<div style="flex: 1; text-align: right;">
<div style="position: relative; width: 50px; height: 25px; margin-left: auto;">
    <div style="width: 50px; height: 25px; border-radius: 50px 50px 0 0; background: linear-gradient(90deg, #1A4FA0 60%, #E0E0E0 60%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 5px; width: 40px; height: 20px; background: white; border-radius: 40px 40px 0 0;"></div>
        <div class="needle" style="height:18px; transform: rotate(45deg);"></div>
    </div>
</div>
<div style="font-size:10px; font-weight:900;">6 GB</div>
</div>
</div>
<div style="margin-top:6px; height:6px; border-radius:10px; background:#E0E0E0; overflow:hidden;">
<div style="width:78%; height:100%; background:#1A4FA0;"></div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

# 3. أيقونات الخدمات (إصلاح مشكلة التباعد)
cols = st.columns(4)
services = [
    {"key": "internet", "icon": icon_internet, "label": "Internet<br>Packages", "page": "pages/InternetPackages.py"},
    {"key": "renewals", "icon": icon_renewals, "label": "Renewals +<br>Tariff", "page": "pages/RenewalsTariff.py"},
    {"key": "calls", "icon": icon_calls, "label": "International<br>Calls", "page": "pages/InternationalCalls.py"},
    {"key": "notifications", "icon": icon_notifications, "label": "Network<br>Alerts", "page": "pages/NetworkNotifications.py"}
]

for col, s in zip(cols, services):
    with col:
        st.markdown(f"""
        <div class="service-wrapper">
            <img src="data:image/png;base64,{s['icon']}" class="service-icon-img">
            <div class="service-label">{s['label']}</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("", key=s["key"]):
            st.switch_page(s["page"])

# 4. قسم التقييم
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card">
<div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
<div class="rating-bar-container">
    <span>★ 4.5</span><span>4.5%</span><span style="background:rgba(255,255,255,0.3); padding:0 5px; border-radius:2px;">24%</span>
</div>
<div style="text-align:center; margin-top:8px; font-size:11px; color:#666;">Rate our service</div>
<div class="star-rating">
    <input type="radio" id="5" name="r"><label for="5">★</label>
    <input type="radio" id="4" name="r"><label for="4">★</label>
    <input type="radio" id="3" name="r"><label for="3">★</label>
    <input type="radio" id="2" name="r"><label for="2">★</label>
    <input type="radio" id="1" name="r"><label for="1">★</label>
</div>
</div>
""", unsafe_allow_html=True)

# 5. قوة الشبكة
st.markdown("""
<div class="title">Network Strength</div>
<div class="card">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 1.3;">
    <div style="font-size:14px; font-weight:900; color:#102646;">📍 Amman</div>
    <div style="font-size:11px; font-weight:700; color:#1A4FA0; margin-bottom:6px;">Very Strong Signal</div>
    <div style="display: flex; gap: 4px;">
        <div style="background: #F1F7FF; border-radius: 8px; padding: 4px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
            <div style="font-size: 7px; color: #666;">Packet Loss</div>
            <div style="font-size: 14px; font-weight: 900;">0</div>
        </div>
        <div style="background: #F1F7FF; border-radius: 8px; padding: 4px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
            <div style="font-size: 7px; color: #666;">Avg Jitter</div>
            <div style="font-size: 14px; font-weight: 900;">19</div>
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

st.markdown("<div style='height:35px'></div>", unsafe_allow_html=True)

# 6. الشريط السفلي (إصلاح مشكلة التباعد)
n_cols = st.columns(5)
navs = [
    {"k": "set", "i": icon_sitting, "l": "Settings", "p": "pages/Settings.py"},
    {"k": "spi", "i": icon_spin, "l": "Spin", "p": "pages/_Game_E.py"},
    {"k": "bot", "i": robot_head, "l": "Chatbot", "p": "cocare-streamlit-app/pages/Chatbot_EN.py", "is_bot": True},
    {"k": "hom", "i": icon_home, "l": "Home", "p": "pages/2_Customer_EN.py"},
    {"k": "gam", "i": icon_game, "l": "Game On", "p": "pages/_Game_E.py"}
]

for col, n in zip(n_cols, navs):
    with col:
        if n.get("is_bot"):
            st.markdown(f'<div class="nav-item"><div class="bot-bg"><img src="data:image/png;base64,{n["i"]}" style="width:38px;"></div><span>{n["l"]}</span></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="nav-item"><img src="data:image/png;base64,{n["i"]}" class="nav-img-footer"><span>{n["l"]}</span></div>', unsafe_allow_html=True)
        
        if st.button("", key=f"btn_{n['k']}"):
            st.switch_page(n["p"])
