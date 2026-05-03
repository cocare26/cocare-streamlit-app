import streamlit as st
import base64
import os

# =====================================
# 1. إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="Telecom Dashboard",
    page_icon="📱",
    layout="centered"
)

# =====================================
# 2. قراءة الصور وتحويلها لـ Base64
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# 3. واجهة المستخدم (CSS) - مطابقة للتصميم الأصلي
# =====================================
st.markdown(f"""
<style>
/* إخفاء القوائم الافتراضية لـ Streamlit */
#MainMenu, header, footer {{visibility: hidden;}}

/* تنسيق الخلفية العامة */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: #f0f7ff;
    font-family: 'Segoe UI', sans-serif;
}}

/* حاوية الموبايل */
.block-container {{
    max-width: 430px;
    margin: auto;
    padding: 20px 15px;
    background: linear-gradient(180deg, #e1f1ff 0%, #ffffff 100%);
    border-radius: 40px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}}

/* تصميم الكروت */
.card {{
    background: white;
    border-radius: 20px;
    padding: 15px;
    margin-bottom: 15px;
    box-shadow: 0 4px 15px rgba(0, 102, 204, 0.05);
}}

.section-title {{
    font-size: 17px;
    font-weight: 700;
    color: #000;
    margin: 10px 0;
}}

/* الملف الشخصي */
.profile-info {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.avatar-img {{
    width: 55px;
    height: 55px;
    object-fit: contain;
}}

.user-details {{
    font-size: 13px;
    color: #555;
    line-height: 1.4;
}}

.location-box {{
    background: #eef5ff;
    padding: 8px 12px;
    border-radius: 12px;
    font-size: 14px;
    font-weight: 600;
    margin-top: 10px;
}}

/* شريط البيانات GB */
.gb-val {{
    font-size: 36px;
    font-weight: 800;
    color: #003366;
}}

.progress-bg {{
    background: #e0eefc;
    height: 10px;
    border-radius: 10px;
    margin: 10px 0;
}}

.progress-fill {{
    background: linear-gradient(90deg, #0052cc, #4ca1ff);
    width: 78%;
    height: 100%;
    border-radius: 10px;
}}

/* شبكة الأيقونات */
.icon-grid {{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
    margin-bottom: 15px;
}}

.icon-item {{
    background: white;
    border-radius: 18px;
    padding: 10px 5px;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
}}

/* شريط القوة Ratings */
.rating-bar {{
    height: 12px;
    background: linear-gradient(90deg, #0047ba 0%, #27a4ff 40%, #ff8c00 70%, #df4126 100%);
    border-radius: 6px;
    margin: 10px 0;
}}

/* النافبار السفلي */
.bottom-nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 10px;
    border-top: 1px solid #eee;
}}

.nav-btn {{
    text-align: center;
    font-size: 11px;
    color: #888;
}}

.active-nav {{ color: #0066cc; font-weight: 700; }}

.bot-icon-bg {{
    width: 45px;
    height: 45px;
    background: white;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin: auto auto 4px auto;
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# 4. بناء هيكل الصفحة (HTML)
# =====================================

# الملف الشخصي
st.markdown(f"""
<div class="card">
    <div class="profile-info">
        <img src="data:image/png;base64,{robot_full}" class="avatar-img">
        <div>
            <div style="font-size: 18px; font-weight: 800;">Welcome: User Name</div>
            <div class="user-details">+962 79 123 4567<br>Valid until: May 25, 2024</div>
        </div>
    </div>
    <div class="location-box">📍 Location: Amman</div>
</div>
""", unsafe_allow_html=True)

# معلومات البيانات
st.markdown("""
<div class="section-title">Your Number Info</div>
<div class="card">
    <div style="font-size: 14px; color: #666;">Remaining GB</div>
    <div class="gb-val">4.7 <span style="font-size: 18px;">GB</span></div>
    <div class="progress-bg"><div class="progress-fill"></div></div>
    <div style="text-align: right; font-weight: 700;">6 GB</div>
</div>
""", unsafe_allow_html=True)

# الأيقونات الأربعة
st.markdown("""
<div class="icon-grid">
    <div class="icon-item">📡<br><span style="font-size: 10px; font-weight: 700;">Internet</span></div>
    <div class="icon-item">🔄<br><span style="font-size: 10px; font-weight: 700;">Renewals</span></div>
    <div class="icon-item">💰<br><span style="font-size: 10px; font-weight: 700;">Intl Calls</span></div>
    <div class="icon-item">🔔<br><span style="font-size: 10px; font-weight: 700;">Network</span></div>
</div>
""", unsafe_allow_html=True)

# التقييمات وقوة الشبكة
st.markdown("""
<div class="section-title">Service Ratings</div>
<div class="card">
    <div style="font-size: 13px; font-weight: 700;">⭐ Service Security Rate</div>
    <div class="rating-bar"></div>
    <div style="text-align:center; color:#ffcc00; font-size:20px;">★ ★ ★ ★ ☆</div>
</div>

<div class="section-title">Network Strength</div>
<div class="card">
    <div style="font-weight: 800;">📍 Amman</div>
    <div style="color: #003366; font-size: 14px; font-weight: 700;">Very Strong Signal</div>
    <div style="text-align: center; font-size: 20px; font-weight: 900; color: #003366; margin-top: 10px;">📶 -68dBm</div>
</div>
""", unsafe_allow_html=True)

# النافبار السفلي
st.markdown(f"""
<div class="bottom-nav">
    <div class="nav-btn">⚙️<br>Settings</div>
    <div class="nav-btn">🎡<br>Spin</div>
    <div class="nav-btn">
        <div class="bot-icon-bg"><img src="data:image/png;base64,{robot_head}" style="width:30px;"></div>
        Chatbot
    </div>
    <div class="nav-btn active-nav">🏠<br>Home</div>
    <div class="nav-btn">🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
