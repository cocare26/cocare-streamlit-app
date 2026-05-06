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
# CSS المطور (لضمان تماثل أحجام الأيقونات)
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

/* إجبار الأيقونات على نفس الحجم بالضبط */
div[data-testid="stPopover"] {{
    width: 100% !important;
}}

div[data-testid="stPopover"] > button {{
    background: white !important;
    border: none !important;
    padding: 0 !important; 
    width: 100% !important;
    height: 95px !important; /* طول ثابت وموحد */
    min-height: 95px !important;
    max-height: 95px !important;
    border-radius: 18px !important;
    box-shadow: 0 6px 15px rgba(0,0,0,.06) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    transition: all 0.3s ease !important;
}}

/* تنسيق النص داخل الأيقونة ليكون موحداً */
div[data-testid="stPopover"] p {{
    font-size: 10px !important;
    font-weight: 800 !important;
    color: #102646 !important;
    line-height: 1.2 !important;
    text-align: center !important;
    margin: 0 !important;
    white-space: pre-line !important; /* للحفاظ على تنسيق الأسطر */
}}

.card {{
background: white;
border-radius: 20px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 4px 15px rgba(0,0,0,.05);
}}

.title {{
font-size:15px;
font-weight:900;
color:#102646;
margin: 4px 0 4px 4px;
}}

.clickable {{ cursor: pointer; }}

.welcome-card {{
    background: white;
    border-radius: 20px;
    padding: 8px 12px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    height: 100px;
}}

.robot-img-welcome {{
    width: 95px; height: 95px;
    object-fit: contain;
    margin-right: 12px;
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
        <div style="font-size:20px; font-weight:900; color:#102646;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555;">+962 79 123 4567</div>
        <div style="font-size:11px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0; display:inline-block;">
        📍 Location: Amman</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">Your Number Info</div>
<div class="card clickable" style="padding: 10px 14px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
<div style="font-size:32px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
</div>
<div style="flex: 1; text-align: right; font-size:10px; font-weight:900;">6 GB</div>
</div>
<div style="margin-top:8px; height:6px; border-radius:10px; background:#E0E0E0; overflow:hidden;">
<div style="width:78%; height:100%; background:#1A4FA0;"></div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات (الآن بحجم موحد إجباري)
# =====================================
cols = st.columns(4)

with cols[0]:
    pop1 = st.popover("📡\nInternet\nPackages")
    pop1.info("Select data bundles.")

with cols[1]:
    pop2 = st.popover("🌍\nRenewals +\nChanges")
    pop2.success("Manage your plan.")

with cols[2]:
    pop3 = st.popover("💰\nInternational\nCalls")
    pop3.warning("Global call rates.")

with cols[3]:
    pop4 = st.popover("🔔\nNetwork\nNotifications")
    pop4.error("No network issues.")

# =====================================
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card" style="padding: 10px 14px;">
<div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
<div style="display: flex; align-items: center; justify-content: space-between; background: linear-gradient(90deg, #1A4FA0, #46A1E2, #D47E2E); height: 22px; border-radius: 4px; margin-top: 6px; padding: 0 10px; color: white; font-size: 11px; font-weight: bold;">
    <span>★ 4.5</span>
    <span>24%</span>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item">⚙️<span class="nav-text">Settings</span></div>
<div class="nav-item">🎡<span class="nav-text">Spin</span></div>
<div class="nav-item">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:34px;"></div>
<span class="nav-text">Chatbot</span>
</div>
<div class="nav-item" style="color:#102646;">🏠<span class="nav-text">Home</span></div>
<div class="nav-item">🎁<span class="nav-text">Game</span></div>
</div>
""", unsafe_allow_html=True)
