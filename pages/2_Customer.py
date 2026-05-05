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

# تحميل الصور (تأكد من وجود الملفات في نفس المجلد)
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

/* تصميم الحاوية الرئيسية */
.block-container {{
max-width:430px;
margin:auto;
padding:12px 16px;
background: linear-gradient(180deg, #FFFFFF 0%, #E3F2FD 30%, #BBDEFB 100%);
border-radius:42px;
box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

/* تخصيص الـ Popover ليشبه الـ Mini Card */
div[data-testid="stPopover"] {{
    width: 100%;
}}
div[data-testid="stPopover"] > button {{
    background: white !important;
    border-radius: 18px !important;
    border: none !important;
    box-shadow: 0 6px 15px rgba(0,0,0,.06) !important;
    padding: 8px 4px !important;
    min-height: 90px !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
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

.mini-text {{ font-size:10px; font-weight:800; line-height:1.1; color:#102646; margin-top:5px; }}

.title {{
font-size:15px;
font-weight:900;
color:#102646;
margin: 4px 0 4px 4px;
}}

.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 22px; font-weight: 800; transition: all 0.3s ease; cursor:pointer; }}
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
<div class="card" style="display: flex; align-items: center; height: 100px;">
    <img src="data:image/png;base64,{robot_full}" style="width: 95px; height: 95px; object-fit: contain; margin-right:12px;">
    <div>
        <div style="font-size:18px; font-weight:900; color:#102646;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555;">+962 79 123 4567</div>
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown("""
<div class="title">Your Number Info</div>
<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
            <div style="font-size:32px; font-weight:900; color:#102646;">4.7 <span style="font-size:14px;">GB</span></div>
        </div>
        <div style="text-align: right;">
            <div style="font-size:10px; font-weight:900; color:#102646;">Total: 6 GB</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات (Popovers)
# =====================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.popover("📡\nInternet"):
        st.markdown("**Available Bundles**")
        st.button("Buy 10GB - 5 JOD")
        st.button("Buy 50GB - 12 JOD")

with col2:
    with st.popover("🌍\nRenew"):
        st.markdown("**Subscription**")
        st.info("Your plan expires in 5 days.")
        st.button("Renew Now")

with col3:
    with st.popover("💰\nIntl"):
        st.markdown("**International**")
        st.text_input("Enter Country Code")
        st.button("Check Rates")

with col4:
    with st.popover("🔔\nAlerts"):
        st.markdown("**Notifications**")
        st.write("✅ System is running smoothly.")
        st.write("⚠️ Maintenance at 2:00 AM.")

# =====================================
# 4. قسم التقييم 
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card">
    <div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
    <div style="background: linear-gradient(90deg, #1A4FA0, #46A1E2); height: 20px; border-radius: 5px; margin-top:5px; color:white; font-size:11px; display:flex; align-items:center; padding-left:10px;">
    Excellent 4.5/5
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. قوة الشبكة
# =====================================
st.markdown("""
<div class="title">Network Strength</div>
<div class="card">
    <div style="font-size:14px; font-weight:900; color:#102646;">📍 Amman - Center</div>
    <div style="font-size:12px; color:green; font-weight:bold;">Excellent Signal</div>
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
        <div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:34px;"></div>
        <span class="nav-text">Chatbot</span>
    </div>
    <div class="nav-item">🏠<span class="nav-text">Home</span></div>
    <div class="nav-item">🎁<span class="nav-text">Game</span></div>
</div>
""", unsafe_allow_html=True)
