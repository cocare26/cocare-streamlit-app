import streamlit as st
import base64
import os

# =====================================
# 1. إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="CoCare Dashboard",
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
# 3. واجهة المستخدم المتقدمة (CSS المطابق 100%)
# =====================================
st.markdown(f"""
<style>
/* إخفاء عناصر ستريمليت */
#MainMenu, header, footer {{visibility: hidden;}}
div[data-testid="stVerticalBlock"] {{gap: 0rem;}}

/* الخلفية العامة */
html, body, [data-testid="stAppViewContainer"] {{
    background-color: #f1f6fb;
    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
}}

/* حاوية الموبايل الرئيسية */
.block-container {{
    max-width: 430px;
    margin: auto;
    padding: 15px 15px 25px 15px;
    background: linear-gradient(180deg, #d2e9ff 0%, #ffffff 40%);
    border-radius: 45px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}}

/* تصميم الكروت */
.card {{
    background: white;
    border-radius: 22px;
    padding: 15px;
    margin-bottom: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    cursor: pointer;
    transition: 0.2s;
}}
.card:active {{ transform: scale(0.98); }}

.title-text {{
    font-size: 16px;
    font-weight: 800;
    color: #102646;
    margin: 10px 0 8px 5px;
}}

/* الملف الشخصي */
.profile-flex {{
    display: flex;
    align-items: center;
    gap: 12px;
}}
.avatar-img {{ width: 55px; height: 60px; object-fit: contain; }}
.welcome-msg {{ font-size: 18px; font-weight: 800; color: #102646; }}
.user-sub {{ font-size: 12px; color: #666; font-weight: 600; line-height: 1.4; }}
.loc-tag {{
    background: #eef5ff; color: #102646; padding: 8px 12px;
    border-radius: 15px; font-size: 13px; font-weight: 700;
    margin-top: 10px; display: inline-block;
}}

/* شريط البيانات */
.gb-rem {{ font-size: 13px; font-weight: 700; color: #555; }}
.gb-main {{ font-size: 38px; font-weight: 900; color: #102646; margin: 4px 0; }}
.progress-container {{
    background: #e1eefc; height: 10px; border-radius: 10px;
    margin: 8px 0; overflow: hidden;
}}
.progress-fill {{
    background: linear-gradient(90deg, #0b47a1, #1e88e5);
    width: 78%; height: 100%; border-radius: 10px;
}}

/* شبكة الأيقونات الـ 4 */
.icon-grid {{
    display: grid; grid-template-columns: repeat(4, 1fr);
    gap: 8px; margin-bottom: 15px;
}}
.icon-box {{
    background: white; border-radius: 20px; padding: 12px 2px;
    text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.04);
    cursor: pointer;
}}
.icon-emoji {{ font-size: 26px; margin-bottom: 5px; }}
.icon-label {{ font-size: 10.5px; font-weight: 800; color: #102646; line-height: 1.2; }}

/* قسم الشبكة (المعدل ليتطابق 100%) */
.net-title {{ font-size: 17px; font-weight: 800; color: #000; }}
.net-signal {{ font-size: 14px; font-weight: 700; color: #003366; margin-bottom: 12px; }}
.stat-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }}
.stat-box {{
    background: #f1f4f9; border-radius: 15px; padding: 10px; text-align: center;
}}
.stat-label {{ font-size: 11px; font-weight: 700; color: #666; margin-bottom: 4px; }}
.stat-number {{ font-size: 26px; font-weight: 900; color: #000; }}
.dbm-text {{
    text-align: center; margin-top: 12px; font-size: 20px;
    font-weight: 900; color: #003366;
}}

/* النافبار السفلي */
.bottom-navbar {{
    display: flex; justify-content: space-between; align-items: center;
    padding-top: 10px; margin-top: 5px; border-top: 1px solid #eee;
}}
.nav-btn {{ text-align: center; font-size: 11px; font-weight: 800; color: #888; cursor: pointer; }}
.nav-btn.active {{ color: #0066cc; }}
.bot-container {{
    width: 48px; height: 48px; background: white; border-radius: 15px;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin: 0 auto 4px auto;
    border: 1px solid #eee;
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# 4. محتوى الصفحة (HTML)
# =====================================

# الملف الشخصي
st.markdown(f"""
<div class="card">
    <div class="profile-flex">
        <img src="data:image/png;base64,{robot_full}" class="avatar-img">
        <div>
            <div class="welcome-msg">Welcome: User Name</div>
            <div class="user-sub">+962 79 123 4567<br>Valid until: May 25, 2024</div>
        </div>
    </div>
    <div class="loc-tag">📍 Location: Amman</div>
</div>
""", unsafe_allow_html=True)

# شريط البيانات
st.markdown("""
<div class="title-text">Your Number Info</div>
<div class="card">
    <div class="gb-rem">Remaining GB</div>
    <div class="gb-main">4.7 <span style="font-size: 20px; font-weight: 700;">GB</span></div>
    <div class="progress-container"><div class="progress-fill"></div></div>
    <div style="text-align: right; font-size: 24px; font-weight: 900; color: #102646;">6 GB</div>
</div>
""", unsafe_allow_html=True)

# شبكة الأيقونات
st.markdown("""
<div class="icon-grid">
    <div class="icon-box">
        <div class="icon-emoji">📡</div>
        <div class="icon-label">Internet<br>Packages</div>
    </div>
    <div class="icon-box">
        <div class="icon-emoji">🔄</div>
        <div class="icon-label">Renewals +<br>Changes</div>
    </div>
    <div class="icon-box">
        <div class="icon-emoji">💰</div>
        <div class="icon-label">International<br>Calls</div>
    </div>
    <div class="icon-box">
        <div class="icon-emoji">🔔</div>
        <div class="icon-label">Network<br>Notifications</div>
    </div>
</div>
""", unsafe_allow_html=True)

# التقييمات
st.markdown("""
<div class="title-text">Service Ratings</div>
<div class="card">
    <div style="font-weight: 800; font-size: 14px; margin-bottom: 8px;">⭐ Service Security Rate</div>
    <div style="height: 14px; border-radius: 10px; background: linear-gradient(90deg, #0047ba, #27a4ff, #ff8c00, #df4126);"></div>
    <div style="text-align: center; margin-top: 10px; font-weight: 800; font-size: 13px; color: #444;">Rate our service</div>
    <div style="text-align: center; font-size: 24px; color: #f4b400; letter-spacing: 2px;">★ ★ ★ ★ ☆</div>
</div>
""", unsafe_allow_html=True)

# قوة الشبكة (المعدل 100%)
st.markdown("""
<div class="title-text">Network Strength in your area</div>
<div class="card">
    <div class="net-title">📍 Amman</div>
    <div class="net-signal">Very Strong Signal</div>
    <div class="stat-row">
        <div class="stat-box">
            <div class="stat-label">Packet Loss (%)</div>
            <div class="stat-number">0</div>
        </div>
        <div class="stat-box">
            <div class="stat-label">Avg Jitter (ms)</div>
            <div class="stat-number">19</div>
        </div>
    </div>
    <div class="dbm-text">📶 -68 dBm (Excellent)</div>
</div>
""", unsafe_allow_html=True)

# النافبار السفلي
st.markdown(f"""
<div class="bottom-navbar">
    <div class="nav-btn">⚙️<br>Settings</div>
    <div class="nav-btn">🎡<br>Spin</div>
    <div class="nav-btn">
        <div class="bot-container">
            <img src="data:image/png;base64,{robot_head}" style="width: 32px; height: 32px; object-fit: contain;">
        </div>
        Chatbot
    </div>
    <div class="nav-btn active">🏠<br>Home</div>
    <div class="nav-btn">🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
