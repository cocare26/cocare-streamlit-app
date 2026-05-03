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
# 2. قراءة الصور
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# 3. CSS المعدل (ضبط مواقع النجوم والأحجام)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#e9edf3;
    font-family:'Segoe UI', sans-serif;
}}
section.main > div {{ padding-top:5px; }}
div[data-testid="stVerticalBlock"] {{ gap:0rem; }}

.block-container {{
    max-width:430px;
    margin:auto;
    padding:12px 12px 25px 12px;
    background:linear-gradient(180deg,#dff2ff 0%,#f4fbff 100%);
    border-radius:40px;
    box-shadow:0 10px 30px rgba(0,0,0,.1);
}}

/* الكروت */
.card {{
    background:white;
    border-radius:22px;
    padding:14px;
    margin-bottom:10px;
    box-shadow:0 4px 12px rgba(0,0,0,.05);
}}

.title {{
    font-size:16px;
    font-weight:900;
    color:#102646;
    margin: 10px 0 6px 5px;
}}

/* الملف الشخصي */
.profile {{ display:flex; gap:10px; align-items:center; }}
.avatar {{ width:50px; height:60px; object-fit:contain; }}
.name {{ font-size:16px; font-weight:900; color:#102646; }}
.sub {{ font-size:12px; color: #6b7280; line-height:1.2; }}
.location {{
    margin-top:8px; background:#eef5ff; padding:8px 12px;
    border-radius:14px; font-size:13px; font-weight:700; color:#102646;
}}

/* البيانات GB */
.big-number {{ font-size:38px; font-weight:900; color:#102646; line-height:1; }}
.progress {{ margin-top:10px; height:10px; border-radius:20px; background:#dce8f7; overflow:hidden; }}
.fill {{ width:78%; height:100%; background:linear-gradient(90deg,#083d8c,#1567e0); }}

/* الأيقونات الأربعة */
.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin-bottom:10px; }}
.mini {{
    background:white; border-radius:18px; padding:12px 2px;
    text-align:center; box-shadow:0 4px 10px rgba(0,0,0,.04);
    cursor: pointer;
}}
.icon {{ font-size:24px; margin-bottom:5px; }}
.mini-text {{ font-size:10px; font-weight:800; line-height:1.1; color:#102646; }}

/* --- تعديل النجوم لتبدو أصلية وفي موقعها --- */
.star-container {{
    text-align: center;
    margin-top: 10px;
}}
.star-rating {{
    display: inline-flex;
    flex-direction: row-reverse;
    gap: 2px;
}}
.star-rating input {{ display: none; }}
.star-rating label {{
    font-size: 22px; /* تصغير الحجم ليناسب الكرت */
    color: #ddd;
    cursor: pointer;
    transition: 0.2s;
}}
.star-rating label:hover,
.star-rating label:hover ~ label,
.star-rating input:checked ~ label {{
    color: #f4b400;
}}

/* قسم الشبكة */
.stat-box-container {{ display: flex; gap: 8px; margin-top: 10px; }}
.stat-box {{
    flex: 1; background: #f1f4f9; border-radius: 15px; padding: 10px 5px; text-align: center;
}}
.stat-label {{ font-size: 10px; font-weight: 700; color: #666; margin-bottom: 2px; }}
.stat-value {{ font-size: 24px; font-weight: 900; color: #000; }}

/* النافبار السفلي */
.nav {{
    margin-top:15px; display:flex; justify-content:space-between; align-items:center;
    text-align:center; font-size:10px; font-weight:800; color:#9ca3af;
    padding: 0 10px;
}}
.nav-item {{ cursor: pointer; }}
.bot-bg {{
    width:42px; height:42px; background:white; border-radius:14px;
    margin: 0 auto 4px; display:flex; align-items:center; justify-content:center;
    box-shadow: 0 4px 8px rgba(0,0,0,0.06); border: 1px solid #eee;
}}
.active {{ color:#0d69dd; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# محتوى الصفحة
# =====================================

# 1. PROFILE
st.markdown(f"""
<div class="card">
    <div class="profile">
        <img class="avatar" src="data:image/png;base64,{robot_full}">
        <div>
            <div class="name">Welcome: Farah</div>
            <div class="sub">+962 79 123 4567<br>Valid until: May 25, 2024</div>
        </div>
    </div>
    <div class="location">📍 Location: Amman</div>
</div>
""", unsafe_allow_html=True)

# 2. NUMBER INFO
st.markdown("""
<div class="title">Your Number Info</div>
<div class="card">
    <div style="font-size:12px; font-weight:700; color:#6b7280;">Remaining GB</div>
    <div class="big-number">4.7 <span style="font-size:18px;">GB</span></div>
    <div class="progress"><div class="fill"></div></div>
    <div style="text-align:right; font-size:20px; font-weight:900; color:#102646; margin-top:5px;">6 GB</div>
</div>
""", unsafe_allow_html=True)

# 3. ICONS
st.markdown("""
<div class="grid4">
    <div class="mini"><div class="icon">📡</div><div class="mini-text">Internet<br>Packages</div></div>
    <div class="mini"><div class="icon">🔄</div><div class="mini-text">Renewals +<br>Changes</div></div>
    <div class="mini"><div class="icon">💰</div><div class="mini-text">International<br>Calls</div></div>
    <div class="mini"><div class="icon">🔔</div><div class="mini-text">Network<br>Notifications</div></div>
</div>
""", unsafe_allow_html=True)

# 4. RATINGS (تم تعديل الموقع والحجم)
st.markdown(f"""
<div class="title">Service Ratings</div>
<div class="card">
    <div style="font-weight:900; font-size:13px; color:#102646;">⭐ Service Security Rate</div>
    <div style="margin-top:8px; height:12px; border-radius:10px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
    <div style="text-align:center; margin-top:12px; font-weight:800; font-size:12px; color:#102646;">Rate our service</div>
    
    <div class="star-container">
        <div class="star-rating">
            <input type="radio" id="star5" name="rating" value="5"><label for="star5">★</label>
            <input type="radio" id="star4" name="rating" value="4"><label for="star4">★</label>
            <input type="radio" id="star3" name="rating" value="3"><label for="star3">★</label>
            <input type="radio" id="star2" name="rating" value="2"><label for="star2">★</label>
            <input type="radio" id="star1" name="rating" value="1"><label for="star1">★</label>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 5. NETWORK STRENGTH
st.markdown("""
<div class="title">Network Strength in your area</div>
<div class="card">
    <div style="font-size:16px; font-weight:900; color:#000;">📍 Amman</div>
    <div style="font-size:14px; font-weight:700; color:#0047ba; margin-bottom:10px;">Very Strong Signal</div>
    <div class="stat-box-container">
        <div class="stat-box">
            <div class="stat-label">Packet Loss (%)</div>
            <div class="stat-value">0</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Avg Jitter (ms)</div>
            <div class="stat-value">19</div>
        </div>
    </div>
    <div style="text-align: center; margin-top:12px; font-size:18px; font-weight:900; color:#102646;">📶 -68 dBm (Excellent)</div>
</div>
""", unsafe_allow_html=True)

# 6. NAVBAR
st.markdown(f"""
<div class="nav">
    <div class="nav-item">⚙️<br>Settings</div>
    <div class="nav-item">🎡<br>Spin</div>
    <div class="nav-item">
        <div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:30px;"></div>
        Chatbot
    </div>
    <div class="nav-item active">🏠<br>Home</div>
    <div class="nav-item">🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
