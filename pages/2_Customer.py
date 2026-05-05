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
# ✅ حالة الـ Popup (إضافة فقط)
# =====================================
if "popup" not in st.session_state:
    st.session_state.popup = None

def open_popup(name):
    st.session_state.popup = name

def close_popup():
    st.session_state.popup = None

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
# CSS المطور + popup
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

.balance-card {{ padding: 6px 14px !important; margin-bottom: 4px !important; }}
.rating-card {{ padding: 4px 14px 6px !important; margin-bottom: 4px !important; }}

.card:hover, .mini:hover, .nav-item:hover, .bot-bg:hover {{
transform: translateY(-5px);
box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}}

.title {{ font-size:15px; font-weight:900; color:#102646; margin: 4px 0 4px 4px; }}

.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin: 8px 0 6px; }}

.mini {{
background:white; border-radius:18px; min-height:90px;
padding:8px 4px; text-align:center;
box-shadow:0 6px 15px rgba(0,0,0,.06);
}}

.mini-text {{ font-size:10px; font-weight:800; color:#102646; }}

.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center;
}}

.nav-item {{ font-size: 22px; }}

.bot-bg {{
width:50px; height:50px; background:white;
border-radius:12px; margin:auto;
display:flex; align-items:center; justify-content:center;
}}

.popup {{
position: fixed;
bottom: 80px;
left: 50%;
transform: translateX(-50%);
width: 330px;
background: white;
border-radius: 20px;
padding: 15px;
box-shadow: 0 10px 40px rgba(0,0,0,0.2);
z-index: 9999;
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. الملف الشخصي
# =====================================
st.markdown(f"""
<div class="card">
Welcome User<br>📍 Amman
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. الرصيد
# =====================================
st.markdown("""
<div class="card">
Remaining: 4.7 GB
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. الأيقونات
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini">📡<div class="mini-text">Internet</div></div>
<div class="mini">🌍<div class="mini-text">Renew</div></div>
<div class="mini">💰<div class="mini-text">Calls</div></div>
<div class="mini">🔔<div class="mini-text">Notify</div></div>
</div>
""", unsafe_allow_html=True)

# ✅ أزرار شفافة فوق الأيقونات
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button(" ", key="i1"):
        open_popup("internet")

with col2:
    if st.button(" ", key="i2"):
        open_popup("renew")

with col3:
    if st.button(" ", key="i3"):
        open_popup("calls")

with col4:
    if st.button(" ", key="i4"):
        open_popup("notif")

# =====================================
# 4. popup
# =====================================
if st.session_state.popup:
    st.markdown('<div class="popup">', unsafe_allow_html=True)

    if st.session_state.popup == "internet":
        st.markdown("### 📡 Internet Packages")
        st.write("Manage your internet")

    elif st.session_state.popup == "renew":
        st.markdown("### 🌍 Renewals")
        st.write("Change your plan")

    elif st.session_state.popup == "calls":
        st.markdown("### 💰 Calls")
        st.write("International calls")

    elif st.session_state.popup == "notif":
        st.markdown("### 🔔 Notifications")
        st.write("Latest alerts")

    if st.button("Close"):
        close_popup()

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================
# 5. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item">⚙️</div>
<div class="nav-item">🎡</div>
<div class="nav-item"><img src="data:image/png;base64,{robot_head}" width="30"></div>
<div class="nav-item">🏠</div>
<div class="nav-item">🎁</div>
</div>
""", unsafe_allow_html=True)
