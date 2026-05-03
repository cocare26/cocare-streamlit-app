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
# CSS المطور (تنسيق الواجهة)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}}
section.main > div {{ padding-top:8px; }}
div[data-testid="stVerticalBlock"] {{ gap:0rem; }}

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

/* نظام النجوم */
.star-rating {{
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    gap: 4px;
    margin-top: 8px;
}}
.star-rating input {{ display: none; }}
.star-rating label {{
    font-size: 30px;
    color: #ddd;
    cursor: pointer;
    transition: color 0.2s;
}}
.star-rating label:hover,
.star-rating label:hover ~ label,
.star-rating input:checked ~ label {{
    color: #f4b400;
}}

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
.bot-bg {{
    width:45px; height:45px; background:white; border-radius:12px;
    margin: 0 auto 5px; display:flex; align-items:center; justify-content:center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}
.active {{ color:#0d69dd; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الملف الشخصي
# =====================================
user_name = st.text_input("Enter User Name", value="User Name")

st.markdown(f"""
<div class="card clickable">
    <div style="display:flex; gap:10px; align-items:flex-start;">
        <img src="data:image/png;base64,{robot_full}" style="width:55px; height:70px; object-fit:contain;">
        <div>
            <div style="font-size:17px; font-weight:900;">Welcome: {user_name}</div>
            <div style="font-size:13px; color:#555;">+962 79 123 4567</div>
            <div style="font-size:13px; color:#555;">Valid until: May 25, 2024</div>
        </div>
    </div>
    <div style="margin-top:10px; background:#eef5ff; padding:10px 14px; border-radius:18px; font-size:14px; font-weight:700;">
        📍 Location: Amman
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown("""
<div class="title">Your Number Info</div>
<div class="card clickable">
    <div style="font-size:13px; font-weight:700; color:#666;">Remaining GB</div>
    <div style="font-size:40px; font-weight:900; color:#102646;">4.7 <span style="font-size:18px;">GB</span></div>
    <div style="margin-top:10px; height:8px; border-radius:20px; background:#dce8f7; overflow:hidden;">
        <div style="width:78%; height:100%; background:linear-gradient(90deg,#083d8c,#1567e0);"></div>
    </div>
    <div style="text-align:right; font-size:22px; font-weight:900; color:#102646; margin-top:5px;">6 GB</div>
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
    <div style="font-weight:900; font-size:14px; color:#102646;">⭐ Service Security Rate</div>
    <div style="margin-top:10px; height:20px; border-radius:18px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
    <div style="text-align:center; margin-top:12px; font-weight:700; font-size:13px; color:#102646;">Rate our service</div>
    <div class="star-rating">
        <input type="radio" id="s5" name="rate" value="5"><label for="s5">★</label>
        <input type="radio" id="s4" name="rate" value="4"><label for="s4">★</label>
        <input type="radio" id="s3" name="rate" value="3"><label for="s3">★</label>
        <input type="radio" id="s2" name="rate" value="2"><label for="s2">★</label>
        <input type="radio" id="s1" name="rate" value="1"><label for="s1">★</label>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. قوة الشبكة (تم الضبط ليتطابق مع الصورة الأصلية)
# =====================================
st.markdown("""
<div class="title">Network Strength in your area</div>
<div class="card clickable">
    <div style="font-size:17px; font-weight:900;">📍 Amman</div>
    <div style="font-size:14px; font-weight:700; color:#003366;">Very Strong Signal</div>
    
    <div style="display: flex; justify-content: center; gap: 8px; margin-top: 15px;">
        <div style="flex: 1; background: #f1f7ff; border-radius: 15px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; font-weight: 700; color: #555;">Packet Loss (%)</div>
            <div style="font-size: 22px; font-weight: 900; color: #000; margin-top: 4px;">0</div>
        </div>
        <div style="flex: 1; background: #f1f7ff; border-radius: 15px; padding: 10px; text-align: center;">
            <div style="font-size: 11px; font-weight: 700; color: #555;">Avg Jitter (ms)</div>
            <div style="font-size: 22px; font-weight: 900; color: #000; margin-top: 4px;">19</div>
        </div>
    </div>

    <div style="text-align:center; margin-top:15px; font-size:18px; font-weight:900; color:#003366;">📶 -68 dBm (Excellent)</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 6. الشريط السفلي (Navbar)
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
