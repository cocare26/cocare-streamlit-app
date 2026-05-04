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
# CSS المطور (تنسيق مدمج وحقول شفافة)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}}

/* إزالة هوامش الأعمدة لتقريب العناصر */
[data-testid="column"] {{
    display: flex;
    align-items: center;
}}

/* جعل حقل الاسم مدمجاً */
div[data-testid="stTextInput"] > div > div > input {{
    background: transparent !important;
    border: none !important;
    color: #102646 !important;
    font-weight: 900 !important;
    font-size: 17px !important;
    padding: 0 !important;
    height: auto !important;
}}

/* جعل حقل الموقع مدمجاً */
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

.nav {{
    margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
    text-align:center; font-size:11px; font-weight:800; color:#6b6b6b;
}}
.bot-bg {{ width:45px; height:45px; background:white; border-radius:12px; margin: 0 auto 5px; display:flex; align-items:center; justify-content:center; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

locations_list = ["Amman", "Zarqa", "Irbid", "Balqa", "Mafraq", "Jerash", "Ajloun", "Madaba", "Karak", "Tafilah", "Ma'an", "Aqaba"]

# =====================================
# 1. قسم الملف الشخصي (الموقع المعدل)
# =====================================
st.write('<div class="card">', unsafe_allow_html=True)
col_img, col_info = st.columns([1, 4])

with col_img:
    st.markdown(f'<img src="data:image/png;base64,{robot_full}" style="width:55px; height:70px; object-fit:contain;">', unsafe_allow_html=True)

with col_info:
    # السطر الأول: Welcome + الاسم
    c_w, c_n = st.columns([1.2, 2])
    with c_w:
        st.markdown('<div style="font-size:17px; font-weight:900; color:#102646; padding-top:4px;">Welcome:</div>', unsafe_allow_html=True)
    with c_n:
        user_name = st.text_input("name_input", value="Farah", label_visibility="collapsed")
    
    st.markdown('<div style="font-size:13px; color:#555; margin-top:-5px;">+962 79 123 4567</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size:13px; color:#555; margin-top:-2px;">Valid until: May 25, 2026</div>', unsafe_allow_html=True)

# سطر الموقع (داخل نفس البطاقة)
st.write('<div style="margin-top:10px; background:#eef5ff; padding:5px 14px; border-radius:18px; display:flex; align-items:center;">', unsafe_allow_html=True)
cl1, cl2 = st.columns([1.2, 3])
with cl1:
    st.markdown('<span style="font-size:15px; font-weight:700;">📍 Location:</span>', unsafe_allow_html=True)
with cl2:
    selected_loc = st.selectbox("loc_select", options=locations_list, index=0, label_visibility="collapsed")
st.write('</div></div>', unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد (العداد المضاف)
# =====================================
st.markdown(f"""
<div class="title">Your Number Info</div>
<div class="card">
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
<div class="grid4" style="display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:12px;">
<div class="mini" style="background:white; border-radius:20px; padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);">
    <div style="font-size:24px;">📡</div><div style="font-size:11px; font-weight:800;">Internet</div>
</div>
<div class="mini" style="background:white; border-radius:20px; padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);">
    <div style="font-size:24px;">🌍</div><div style="font-size:11px; font-weight:800;">Renewals</div>
</div>
<div class="mini" style="background:white; border-radius:20px; padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);">
    <div style="font-size:24px;">💰</div><div style="font-size:11px; font-weight:800;">Int. Calls</div>
</div>
<div class="mini" style="background:white; border-radius:20px; padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);">
    <div style="font-size:24px;">🔔</div><div style="font-size:11px; font-weight:800;">Notifications</div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. قوة الشبكة (محدثة تلقائياً بالموقع المختار)
# =====================================
st.markdown(f"""
<div class="title">Network Strength in your area</div>
<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="flex: 1.2;">
            <div style="font-size:16px; font-weight:900; color:#102646;">📍 {selected_loc}</div>
            <div style="font-size:13px; font-weight:700; color:#003366;">Very Strong Signal</div>
        </div>
        <div style="flex: 1; text-align: center;">
             <div style="font-size: 10px; font-weight: 900; color: #102646;">-68dBm (Excellent)</div>
             <div style="display: flex; justify-content: center; align-items: flex-end; gap: 2px; margin-top: 4px;">
                <div style="width: 4px; height: 6px; background: #0056b3;"></div>
                <div style="width: 4px; height: 10px; background: #0056b3;"></div>
                <div style="width: 4px; height: 14px; background: #0056b3;"></div>
                <div style="width: 4px; height: 18px; background: #ccc;"></div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
    <div class="nav-item">⚙️<br>Settings</div>
    <div class="nav-item">🎡<br>Spin</div>
    <div class="nav-item">
        <div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:32px;"></div>
        Chatbot
    </div>
    <div class="nav-item" style="color:#0d69dd;">🏠<br>Home</div>
    <div class="nav-item">🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
