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
# CSS المطور (لجعل الحقول مدمجة)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}}
/* إخفاء إطار حقول إدخال streamlit الافتراضية لجعلها تبدو مدمجة */
div[data-testid="stTextInput"] > div > div > input,
div[data-testid="stSelectbox"] > div > div > div {{
    background-color: transparent !important;
    border: none !important;
    padding: 0 !important;
    font-weight: 900 !important;
    color: #102646 !important;
}}
div[data-testid="stTextInput"] label, div[data-testid="stSelectbox"] label {{
    display: none !important; /* إخفاء العناوين التوضيحية فوق الحقول */
}}

.block-container {{
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card {{
    background:white;
    border-radius:24px;
    padding:14px;
    margin-bottom:12px;
    box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.title {{
    font-size:17px;
    font-weight:900;
    color:#102646;
    margin: 8px 0 8px 4px;
}}

.clickable {{ cursor: pointer; transition: transform 0.2s; }}
.clickable:active {{ transform: scale(0.98); }}

.star-rating {{ display: flex; flex-direction: row-reverse; justify-content: center; gap: 4px; margin-top: 5px; }}
.star-rating label {{ font-size: 32px; color: #ddd; cursor: pointer; }}

.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:12px; }}
.mini {{
    background:white; border-radius:20px; min-height:105px;
    padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);
}}
.icon {{ font-size:24px; margin-bottom:5px; }}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; }}

.nav {{
    margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
    text-align:center; font-size:11px; font-weight:800; color:#6b6b6b;
}}
.bot-bg {{ width:45px; height:45px; background:white; border-radius:12px; margin: 0 auto 5px; display:flex; align-items:center; justify-content:center; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

# القائمة المنسدلة من الصورة
locations_list = ["Amman", "Zarqa", "Irbid", "Balqa", "Mafraq", "Jerash", "Ajloun", "Madaba", "Karak", "Tafilah", "Ma'an", "Aqaba"]

# =====================================
# 1. بطاقة الترحيب المدمجة
# =====================================
with st.container():
    st.write('<div class="card clickable">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 4])
    with c1:
        st.markdown(f'<img src="data:image/png;base64,{robot_full}" style="width:55px; height:70px; object-fit:contain;">', unsafe_allow_html=True)
    with c2:
        st.write('<div style="font-size:17px; font-weight:900; margin-bottom:-10px;">Welcome:</div>', unsafe_allow_html=True)
        user_name = st.text_input("", value="User Name", placeholder="Type name...")
        st.write('<div style="font-size:13px; color:#555; margin-top:-5px;">+962 79 123 4567</div>', unsafe_allow_html=True)
        st.write('<div style="font-size:13px; color:#555;">Valid until: May 25, 2024</div>', unsafe_allow_html=True)
    
    # قسم الموقع المدمج
    st.write('<div style="margin-top:10px; background:#eef5ff; padding:5px 14px; border-radius:18px; display:flex; align-items:center; gap:5px;">', unsafe_allow_html=True)
    st.write('📍', unsafe_allow_html=True)
    selected_loc = st.selectbox("", options=locations_list, index=0)
    st.write('</div></div>', unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
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
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card">
<div style="font-weight:900; font-size:14px; color:#10264
