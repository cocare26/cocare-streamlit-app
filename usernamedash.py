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
# قراءة الصور
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (تعديل مواقع النجوم والأحجام)
# =====================================
st.markdown(f"""
<style>
/* الأساسيات */
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}}
section.main > div {{ padding-top:8px; }}
div[data-testid="stVerticalBlock"] {{ gap:0rem; }}

/* حاوية الموبايل */
.block-container {{
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.1);
}}

/* الكروت */
.card, .mini, .nav-item {{
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}}

.card {{
    background:white;
    border-radius:24px;
    padding:14px;
    margin-bottom:12px;
    box-shadow:0 6px 18px rgba(0,0,0,.05);
}}

.title {{
    font-size:17px;
    font-weight:900;
    color:#102646;
    margin: 12px 0 8px 4px;
}}

/* --- تعديل النجوم لتبدو بنفس حجم وموقع التصميم الأصلي --- */
.star-rating-container {{
    text-align: center;
    margin-top: 8px;
    padding-bottom: 5px;
}}
.stars {{
    display: inline-flex;
    flex-direction: row-reverse;
    gap: 3px;
}}
.stars input {{ display: none; }}
.stars label {{
    font-size: 22px; /* الحجم المطابق للصورة */
    color: #ddd;
    cursor: pointer;
    transition: color 0.2s;
}}
.stars input:checked ~ label,
.stars label:hover,
.stars label:hover ~ label {{
    color: #f4b400;
}}

/* الملف الشخصي */
.profile {{ display:flex; gap:10px; align-items:flex-start; }}
.avatar {{ width:55px; height:70px; object-fit:contain; }}
.name {{ font-size:17px; font-weight:900; color:#102646; }}
.sub {{ font-size:13px; color: #6b7280; }}
.location {{
    margin-top:10px; background:#f0f7ff; padding:10px 14px;
    border-radius:18px; font-size:14px; font-weight:700; color:#102646;
}}

/* البيانات GB */
.big-number {{ font-size:42px; font-weight:900; color:#102646; line-height:1; }}
.progress {{ margin-top:12px; height:10px; border-radius:20px; background:#e5efff; overflow:hidden; }}
.fill {{ width:78%; height:100%; background:linear-gradient(90deg,#083d8c,#1567e0); }}

/* شبكة الأيقونات */
.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:12px; }}
.mini {{
    background:white; border-radius:20px; min-height:110px;
    padding:12px 5px; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,.05);
}}
.icon {{ font-size:28px; margin-bottom:8px; }}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; color:#102646; }}

/* Network Strength */
.network-card {{ background: white; border-radius: 24px; padding: 18px; margin-bottom: 12px; }}
.net-city {{ font-size: 18px; font-weight: 900; color: #000; margin-bottom: 2px; }}
.net-status {{ font-size: 15px; font-weight: 700; color: #0047ba; margin-bottom: 15px; }}
.stat-box-container {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
.stat-box {{
    background: #f8f9fa; border: 1px solid #f0f0f0; border-radius: 18px; padding: 12px; text-align: center;
}}
.stat-label {{ font-size: 12px; font-weight: 700; color: #6b7280; margin-bottom: 4px; }}
.stat-value {{ font-size: 28px; font-weight: 900; color: #000; }}
.dbm-meter {{
    text-align: center; margin-top: 18px; font-size: 20px;
    font-weight: 900; color: #102646;
}}

/* النافبار السفلي */
.nav {{
    margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
    text-align:center; font-size:12px; font-weight:800; color:#9ca3af;
}}
.bot-bg {{
    width:48px; height:48px; background:white; border-radius:16px;
    margin: 0 auto 5px; display:flex; align-items:center; justify-content:center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08); border: 1px solid #f0f0f0;
}}
.active {{ color:#0d69dd; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# اسم المستخدم
# =====================================
user_name = st.text_input("Enter User Name", value="User Name")

# =====================================
# 1. PROFILE
# =====================================
st.markdown(f"""
<div class="card">
    <div class="profile">
        <img class="avatar" src="data:image/png;base64,{robot_full}">
        <div>
            <div class="name">Welcome: {user_name}</div>
            <div class="sub">+962 79 123 4567</div>
            <div class="sub">Valid until: May 25, 2024</div>
        </div>
    </div>
    <div class="location">📍 Location: Amman</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. NUMBER INFO
# =====================================
st.markdown("""
<div class="title">Your Number Info</div>
<div class="card">
    <div style="font-size:14px; font-weight:700; color:#6b7280;">Remaining GB</div>
    <div class="big-number">4.7 <span style="font-size:18px;">GB</span></div>
    <div class="progress"><div class="fill"></div></div>
    <div style="text-align:right; font-size:24px; font-weight:900; color:#102646; margin-top:8px;">6 GB</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. ICONS
# =====================================
st.markdown("""
<div class="grid4">
    <div class="mini">
        <div class="icon">📡</div>
        <div class="mini-text">Internet<br>Packages</div>
    </div>
    <div class="mini">
        <div class="icon">🌍</div>
        <div class="mini-text">Renewals +<br>Changes</div>
    </div>
    <div class="mini">
        <div class="icon">💰</div>
        <div class="mini-text">International<br>Calls</div>
    </div>
    <div class="mini">
        <div class="icon">🔔</div>
        <div class="mini-text">Network<br>Notifications</div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. RATINGS (تم تعديل الموقع والحجم يدوياً)
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card">
    <div style="font-weight:900; font-size:14px; color:#102646;">⭐ Service Security Rate</div>
    <div style="margin-top:10px; height:18px; border-radius:18px; background:linear-gradient(90deg,#0047ba 0%,#27a4ff 40%,#ff8c00 70%,#df4126 100%);"></div>
    <div style="text-align:center; margin-top:15px; font-weight:800; font-size:13px; color:#102646;">Rate our service</div>
    
    <div class="star-rating-container">
        <div class="stars">
            <input type="radio" id="s5" name="star_rating"><label for="s5">★</label>
            <input type="radio" id="s4" name="star_rating"><label for="s4">★</label>
            <input type="radio" id="s3" name="star_rating"><label for="s3">★</label>
            <input type="radio" id="s2" name="star_rating"><label for="s2">★</label>
            <input type="radio" id="s1" name="star_rating"><label for="s1">★</label>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. NETWORK STRENGTH
# =====================================
st.markdown(f"""
<div class="title">Network Strength in your area</div>
<div class="network-card">
    <div class="net-city">📍 Amman</div>
    <div class="net-status">Very Strong Signal</div>
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
    <div class="dbm-meter">📶 -68 dBm (Excellent)</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 6. NAVBAR
# =====================================
st.markdown(f"""
<div class="nav">
    <div class="nav-item">⚙️<br>Settings</div>
    <div class="nav-item">🎡<br>Spin</div>
    <div class="nav-item">
        <div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:34px;"></div>
        Chatbot
    </div>
    <div class="nav-item active">🏠<br>Home</div>
    <div class="nav-item">🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
