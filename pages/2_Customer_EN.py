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


st.markdown("""
<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
    overflow-x:hidden !important;
    width:100%;
}

section.main > div {
    padding-top:4px;
}

div[data-testid="stVerticalBlock"] {
    gap:0.4rem;
}

#MainMenu, header, footer {
    visibility:hidden;
}

/* الحاوية الرئيسية */
.block-container {
    max-width:430px;
    margin:auto;
    padding:12px 10px;
    background:linear-gradient(180deg,#FFFFFF 0%,#E3F2FD 30%,#BBDEFB 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

/* الكروت */
.card {
    background:white;
    border-radius:20px;
    padding:10px 14px;
    margin-bottom:8px;
    box-shadow:0 4px 15px rgba(0,0,0,.05);
}

/* ===================== */
/* SERVICES GRID (الوسط) */
/* ===================== */

.services-grid {
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:8px;
}

.service-item {
    flex:1;
    text-align:center;
}

.service-img-custom {
    width:40px;
    height:40px;
    object-fit:contain;
    display:block;
    margin:auto;
}

.service-label-custom {
    font-size:8px;
    font-weight:800;
    color:#102646;
    line-height:1.1;
    margin-top:4px;
}

/* ===================== */
/* GENERAL UI */
/* ===================== */

.title {
    font-size:15px;
    font-weight:900;
    color:#102646;
    margin:4px 0 4px 4px;
}

.clickable {
    cursor:pointer;
    transition:all 0.3s ease;
    position:relative;
}

/* زر شفاف */
.stButton > button {
    width:100%;
    height:70px;
    opacity:0;
    border:none;
    background:transparent;
    cursor:pointer;
    position:relative;
    z-index:10;
}

/* ===================== */
/* WELCOME CARD */
/* ===================== */

.welcome-card {
    background:white;
    border-radius:20px;
    padding:8px 12px;
    margin-bottom:8px;
    display:flex;
    align-items:center;
    height:100px;
}

.robot-img-welcome {
    width:90px;
    height:90px;
    object-fit:contain;
    margin-right:12px;
}

/* ===================== */
/* NAV ITEMS (TEXT ONLY) */
/* ===================== */

.nav-item {
    display:flex;
    flex-direction:column;
    align-items:center;
    font-size:8px;
    font-weight:700;
    color:#6b6b6b;
    text-align:center;
}

.nav-item span {
    font-size:7px !important;
    line-height:1 !important;
}

/* ===================== */
/* BOTTOM NAV (IMPORTANT) */
/* ===================== */

.bottom-nav {
    position:fixed;
    bottom:0;
    left:0;
    width:100%;
    max-width:430px;
    margin:auto;
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:white;
    padding:8px 10px;
    box-shadow:0 -2px 10px rgba(0,0,0,0.1);
    z-index:999;
}

.bottom-nav .nav-item {
    flex:1;
    text-align:center;
}

.bottom-nav img {
    width:22px;
    height:22px;
    object-fit:contain;
}

/* ===================== */
/* RATING */
/* ===================== */

.rating-bar-container {
    display:flex;
    align-items:center;
    justify-content:space-between;
    background:linear-gradient(90deg,#1A4FA0,#46A1E2,#D47E2E,#C63F2A);
    height:22px;
    border-radius:4px;
    margin-top:6px;
    padding:0 10px;
    color:white;
    font-size:11px;
    font-weight:bold;
}

.star-rating {
    display:flex;
    flex-direction:row-reverse;
    justify-content:center;
    gap:4px;
}

.star-rating input { display:none; }

.star-rating label {
    font-size:24px;
    color:#ddd;
    cursor:pointer;
}

.star-rating input:checked ~ label {
    color:#ffcc00;
}

/* ===================== */
/* MOBILE ONLY (JUST SIZE) */
/* ===================== */

@media (max-width:480px) {

    .service-img-custom {
        width:30px;
        height:30px;
    }

    .service-label-custom {
        font-size:6px;
    }

    .nav-item span {
        font-size:5.5px !important;
    }

    .bottom-nav img {
        width:18px;
        height:18px;
    }

    .block-container {
        padding:10px 6px;
    }
}

</style>
""", unsafe_allow_html=True)
# 1. قسم الملف الشخصي
st.markdown(f"""
<div class="welcome-card clickable">
    <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
    <div class="welcome-text-container">
        <div style="font-size:18px; font-weight:900; color:#102646; line-height:1.1;">Welcome: Farah</div>
        <div style="font-size:12px; color:#555; margin-top:2px;">+962 79 123 4567</div>
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
        <div style="font-size:11px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0;">
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

st.markdown("<div style='height:5px'></div>", unsafe_allow_html=True)

# 3. أيقونات الخدمات (تم تصحيح المسافات هنا)
st.markdown(f"""
<div class="services-grid">

    <div class="service-item">
        <img src="data:image/png;base64,{icon_internet}" class="service-img-custom">
        <div class="service-label-custom">Internet<br>Packages</div>
    </div>

    <div class="service-item">
        <img src="data:image/png;base64,{icon_renewals}" class="service-img-custom">
        <div class="service-label-custom">Renewals +<br>Changes</div>
    </div>

    <div class="service-item">
        <img src="data:image/png;base64,{icon_calls}" class="service-img-custom">
        <div class="service-label-custom">Int.<br>Calls</div>
    </div>

    <div class="service-item">
        <img src="data:image/png;base64,{icon_notifications}" class="service-img-custom">
        <div class="service-label-custom">Network<br>Notif.</div>
    </div>

</div>
""", unsafe_allow_html=True)

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
<div style="font-size:12px; font-weight:700; color:#1A4FA0; margin-bottom:6px;">Very Strong Signal</div>
<div style="display: flex; gap: 4px;">
<div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
<div style="font-size: 7px; color: #666; font-weight:bold;">Packet Loss</div>
<div style="font-size: 14px; font-weight: 900; color: #000;">0%</div>
</div>
<div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
<div style="font-size: 7px; color: #666; font-weight:bold;">Avg Jitter</div>
<div style="font-size: 14px; font-weight: 900; color: #000;">19ms</div>
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
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)

# 6. الشريط السفلي
st.markdown(f"""
<div class="bottom-nav">

    <div class="nav-item" onclick="window.location.href='pages/Settings.py'">
        <img src="data:image/png;base64,{icon_sitting}" class="nav-img-footer">
        <span>Settings</span>
    </div>

    <div class="nav-item" onclick="window.location.href='pages/_Game_E.py'">
        <img src="data:image/png;base64,{icon_spin}" class="nav-img-footer">
        <span>Spin</span>
    </div>

    <div class="nav-item">
        <div class="bot-bg">
            <img src="data:image/png;base64,{robot_head}" style="width:26px;height:26px;">
        </div>
        <span>Chatbot</span>
    </div>

    <div class="nav-item" onclick="window.location.href='pages/2_Customer_EN.py'">
        <img src="data:image/png;base64,{icon_home}" class="nav-img-footer">
        <span>Home</span>
    </div>

    <div class="nav-item" onclick="window.location.href='pages/_Game_E.py'">
        <img src="data:image/png;base64,{icon_game}" class="nav-img-footer">
        <span>Game</span>
    </div>

</div>
""", unsafe_allow_html=True)
