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
# CSS المطور (التعديلات المطلوبة)
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

/* توحيد حجم وتناسق الـ Popovers الوسطى */
div[data-testid="stPopover"] {{
    width: 100% !important;
}}
div[data-testid="stPopover"] > button {{
    background: white !important;
    border-radius: 18px !important;
    border: none !important;
    box-shadow: 0 6px 15px rgba(0,0,0,.06) !important;
    padding: 8px 4px !important;
    height: 95px !important; /* طول ثابت وموحد */
    width: 100% !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1.1 !important;
    white-space: pre-line !important;
}}

/* تأثير الحركة عند التأشير بالماوس */
div[data-testid="stPopover"] > button:hover {{
    transform: translateY(-5px) scale(1.05) !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.12) !important;
    background: #fdfdfd !important;
}}

.card {{
background: white;
border-radius: 20px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 4px 15px rgba(0,0,0,.05);
transition: all 0.3s ease;
}}

.card:hover {{
    transform: translateY(-3px);
    box-shadow: 0 8px 18px rgba(0,0,0,0.08);
}}

.title {{ font-size:15px; font-weight:900; color:#102646; margin: 4px 0 4px 4px; }}
.clickable {{ cursor: pointer; }}

/* نجوم تقييم تفاعلية */
.star-rating {{
    display: flex;
    flex-direction: row-reverse;
    justify-content: center;
    gap: 4px;
}}
.star-rating input {{ display: none; }}
.star-rating label {{
    font-size: 26px;
    color: #ddd;
    cursor: pointer;
    transition: color 0.2s, transform 0.2s;
}}
.star-rating label:hover {{ transform: scale(1.2); }}
.star-rating input:checked ~ label,
.star-rating label:hover,
.star-rating label:hover ~ label {{
    color: #ffcc00;
}}

.rating-bar-container {{
    display: flex; align-items: center; justify-content: space-between;
    background: linear-gradient(90deg, #1A4FA0, #46A1E2, #D47E2E, #C63F2A);
    height: 22px; border-radius: 4px; margin-top: 6px; padding: 0 10px;
    color: white; font-size: 11px; font-weight: bold;
}}

.nav-item:hover, .bot-bg:hover {{
    transform: translateY(-5px);
}}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الملف الشخصي
# =====================================
st.markdown(f"""
<div class="welcome-card clickable">
    <div style="background: white; border-radius: 20px; padding: 8px 12px; margin-bottom: 8px; box-shadow: 0 6px 15px rgba(0,0,0,.06); display: flex; align-items: center; height: 100px;">
    <img src="data:image/png;base64,{robot_full}" style="width: 95px; height: 95px; border-radius: 14px; margin-right: 12px; object-fit: contain;">
    <div class="welcome-text-container">
        <div style="font-size:20px; font-weight:900; color:#102646; line-height:1.1;">Welcome: User Name</div>
        <div style="font-size:12px; color:#555; margin-top:2px;">+962 79 123 4567</div>
        <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
        <div style="font-size:11px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0; width: fit-content;">📍 Amman</div>
    </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">Your Number Info</div>
<div class="card clickable" style="padding: 10px 14px; margin-bottom: 8px;">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
<div style="font-size:32px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
</div>
<div style="flex: 1; text-align: right; font-size:10px; font-weight:900; color:#102646;">6 GB</div>
</div>
<div style="margin-top:8px; height:6px; border-radius:10px; background:#E0E0E0; overflow:hidden;">
<div style="width:78%; height:100%; background:#1A4FA0;"></div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات (Popovers) - حجم موحد وتفاعل
# =====================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.popover("📡\nInternet\nPackages"):
        st.markdown("<p style='color:#102646; font-weight:bold;'>Available Bundles</p>", unsafe_allow_html=True)
        st.button("Buy 1GB", key="b1")

with col2:
    with st.popover("🌍\nRenewals +\nChanges"):
        st.markdown("<p style='color:#102646; font-weight:bold;'>Subscription</p>", unsafe_allow_html=True)
        st.info("Plan ends in 4 days")

with col3:
    with st.popover("💰\nInternational\nCalls"):
        st.markdown("<p style='color:#102646; font-weight:bold;'>Intl Calls</p>", unsafe_allow_html=True)
        st.button("Activate", key="b4")

with col4:
    with st.popover("🔔\nNetwork\nNotifications"):
        st.markdown("<p style='color:#102646; font-weight:bold;'>Notifications</p>", unsafe_allow_html=True)
        st.write("• Network update at 12AM")

# =====================================
# 4. قسم التقييم التفاعلي
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>
<div class="card">
<div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
<div class="rating-bar-container">
    <span>★ 4.5</span>
    <span>4.5%</span>
    <span style="background:rgba(255,255,255,0.3); padding:0 5px; border-radius:2px;">24%</span>
</div>
<div style="text-align:center; margin-top:8px; font-weight:700; font-size:11px; color:#666; margin-bottom:2px;">Rate our service</div>
<div class="star-rating">
    <input type="radio" id="s5" name="star_rate"><label for="s5" title="5 stars">★</label>
    <input type="radio" id="s4" name="star_rate"><label for="s4" title="4 stars">★</label>
    <input type="radio" id="s3" name="star_rate"><label for="s3" title="3 stars">★</label>
    <input type="radio" id="s2" name="star_rate"><label for="s2" title="2 stars">★</label>
    <input type="radio" id="s1" name="star_rate"><label for="s1" title="1 star">★</label>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. قوة الشبكة
# =====================================
st.markdown("""
<div class="title">Network Strength in your area</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 1.2;">
<div style="font-size:14px; font-weight:900; color:#102646;">📍 Amman</div>
<div style="font-size:12px; font-weight:700; color:#1A4FA0;">Very Strong Signal</div>
</div>
<div style="flex: 1; text-align: center; font-size: 9px; font-weight: 900; color: #102646;">-68dBm (Excellent)</div>
</div>
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
<div class="nav-item active">🏠<span class="nav-text">Home</span></div>
<div class="nav-item">🎁<span class="nav-text">Game</span></div>
</div>
""", unsafe_allow_html=True)
