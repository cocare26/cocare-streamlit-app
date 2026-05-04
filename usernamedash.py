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

robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (تنسيق مدمج)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}}
/* تنسيق حقول الإدخال لتبدو كجزء من التصميم */
div[data-testid="stTextInput"] > div > div > input {{
    background: transparent !important;
    border: none !important;
    color: #102646 !important;
    font-weight: 900 !important;
    font-size: 17px !important;
    padding: 0 !important;
}}
div[data-testid="stSelectbox"] > div > div > div {{
    background: transparent !important;
    border: none !important;
    color: #102646 !important;
    font-weight: 700 !important;
    padding: 0 !important;
}}
.block-container {{
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
}}
.card {{
    background:white;
    border-radius:24px;
    padding:14px;
    margin-bottom:12px;
    box-shadow:0 6px 18px rgba(0,0,0,.08);
}}
.title {{ font-size:17px; font-weight:900; color:#102646; margin: 8px 0 8px 4px; }}
.clickable {{ cursor: pointer; transition: transform 0.2s; }}
.clickable:active {{ transform: scale(0.98); }}

.nav {{
    margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
    text-align:center; font-size:11px; font-weight:800; color:#6b6b6b;
}}
.bot-bg {{ width:45px; height:45px; background:white; border-radius:12px; margin: 0 auto 5px; display:flex; align-items:center; justify-content:center; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

# قائمة المحافظات
locations_list = ["Amman", "Zarqa", "Irbid", "Balqa", "Mafraq", "Jerash", "Ajloun", "Madaba", "Karak", "Tafilah", "Ma'an", "Aqaba"]

# =====================================
# 1. قسم الملف الشخصي (مدمج)
# =====================================
with st.container():
    # الجزء العلوي من البطاقة
    st.markdown(f"""
    <div class="card">
    <div style="display:flex; gap:10px; align-items:flex-start;">
        <img src="data:image/png;base64,{robot_full}" style="width:55px; height:70px; object-fit:contain;">
        <div style="flex-grow:1;">
            <div style="font-size:17px; font-weight:900; color:#102646;">Welcome:</div>
    """, unsafe_allow_html=True)
    
    # حقل الاسم مدمج
    user_name = st.text_input("name_input", value="Farah", label_visibility="collapsed")
    
    st.markdown("""
            <div style="font-size:13px; color:#555; margin-top:2px;">+962 79 123 4567</div>
            <div style="font-size:13px; color:#555;">Valid until: May 25, 2026</div>
        </div>
    </div>
    <div style="margin-top:10px; background:#eef5ff; padding:8px 14px; border-radius:18px; display:flex; align-items:center; gap:8px;">
        <span style="font-size:16px;">📍 Location:</span>
    """, unsafe_allow_html=True)
    
    # حقل اختيار الموقع مدمج
    selected_loc = st.selectbox("loc_select", options=locations_list, index=0, label_visibility="collapsed")
    
    st.markdown("</div></div>", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد (مع العداد المضاف)
# =====================================
st.markdown(f"""
<div class="title">Your Number Info</div>
<div class="card clickable">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="flex: 2;">
            <div style="font-size:13px; font-weight:700; color:#666;">Remaining GB</div>
            <div style="font-size:40px; font-weight:900; color:#102646;">4.7 <span style="font-size:18px;">GB</span></div>
        </div>
        <div style="flex: 1; text-align: right;">
            <div style="position: relative; width: 70px; height: 35px; margin-left: auto;">
                <div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #0d69dd 60%, #e0e0e0 60%); position: relative; overflow: hidden;">
                    <div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
                    <div style="position: absolute; bottom: 0; left: 50%; width: 2px; height: 28px; background: #083d8c; transform-origin: bottom; transform: rotate(45deg);"></div>
                </div>
            </div>
            <div style="font-size:14px; font-weight:900; color:#102646; margin-top:2px;">6 GB</div>
        </div>
    </div>
    <div style="margin-top:10px; height:8px; border-radius:20px; background:#dce8f7; overflow:hidden;">
        <div style="width:78%; height:100%; background:linear-gradient(90deg,#083d8c,#1567e0);"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini clickable"><div class="icon">📡</div><div class="mini-text">Internet<br>Packages</div></div>
<div class="mini clickable"><div class="icon">🌍</div><div class="mini-text">Renewals +<br>Changes</div></div>
<div class="mini clickable"><div class="icon">💰</div><div class="mini-text">International<br>Calls</div></div>
<div class="mini clickable"><div class="icon">🔔</div><div class="mini-text">Network<br>Notifications</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. قسم التقييم و قوة الشبكة
# =====================================
st.markdown(f"""
<div class="title">Service Ratings</div>
<div class="card">
    <div style="font-weight:900; font-size:14px; color:#102646;">⭐ Service Security Rate</div>
    <div style="margin-top:10px; height:20px; border-radius:18px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
</div>

<div class="title">Network Strength in your area</div>
<div class="card clickable">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="flex: 1.2;">
            <div style="font-size:16px; font-weight:900; color:#102646;">📍 {selected_loc}</div>
            <div style="font-size:13px; font-weight:700; color:#003366;">Very Strong Signal</div>
        </div>
        <div style="flex: 1; text-align: center;">
            <div style="position: relative; width: 100px; margin: 0 auto;">
                <div style="width: 80px; height: 40px; border-radius: 80px 80px 0 0; background: linear-gradient(90deg, #4caf50 20%, #ffeb3b 50%, #f44336 100%); position: relative; margin:auto;">
                    <div style="position: absolute; bottom: 0; left: 10px; width: 60px; height: 30px; background: white; border-radius: 60px 60px 0 0;"></div>
                </div>
                <div style="font-size: 10px; font-weight: 900; color: #102646; margin-top: 5px;">-68dBm</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. الشريط السفلي (Navbar)
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item clickable">⚙️<br>Settings</div>
<div class="nav-item clickable">🎡<br>Spin</div>
<div class="nav-item clickable">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:32px;"></div>
Chatbot
</div>
<div class="nav-item active clickable">🏠<br>Home</div>
<div class="nav-item clickable">🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
