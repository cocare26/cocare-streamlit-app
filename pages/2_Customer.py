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

# إدارة الحالة لعرض الواجهات (Interfaces)
if "current_page" not in st.session_state:
    st.session_state.current_page = "main"

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
# CSS المطور (نفس الكود مع إضافة تنسيق للـ Interface)
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

/* تنسيق الواجهة الجديدة (Interface) */
.interface-container {{
    text-align: center;
    padding: 40px 20px;
    background: white;
    border-radius: 30px;
    margin-top: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}}
.link-style {{
    color: #1A4FA0;
    text-decoration: none;
    font-size: 14px;
    word-break: break-all;
    display: block;
    margin-bottom: 15px;
}}

.card {{
background: white;
border-radius: 20px;
padding: 10px 14px;
margin-bottom: 8px;
box-shadow: 0 4px 15px rgba(0,0,0,.05);
transition: all 0.3s ease;
}}

.balance-card {{
    padding: 6px 14px !important;
    margin-bottom: 4px !important;
}}

.rating-card {{
    padding: 4px 14px 6px !important;
    margin-bottom: 4px !important;
}}

.card:hover, .mini:hover, .nav-item:hover, .bot-bg:hover {{
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}}

.title {{
font-size:15px;
font-weight:900;
color:#102646;
margin: 4px 0 4px 4px;
}}

.clickable {{ cursor: pointer; }}

.rating-bar-container {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    background: linear-gradient(90deg, #1A4FA0, #46A1E2, #D47E2E, #C63F2A);
    height: 22px;
    border-radius: 4px;
    margin-top: 6px;
    padding: 0 10px;
    color: white;
    font-size: 11px;
    font-weight: bold;
}}

.welcome-card {{
    background: white;
    border-radius: 20px;
    padding: 8px 12px;
    margin-bottom: 8px;
    display: flex;
    align-items: center;
    height: 100px;
}}

.robot-img-welcome {{
    width: 95px; height: 95px;
    object-fit: contain;
    margin-right: 12px;
}}

.needle {{
    position: absolute; bottom: 0; left: 50%;
    width: 2px; height: 30px; background: #333;
    transform-origin: bottom center;
}}

.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:6px; margin: 8px 0 6px; }}

.mini {{
background:white; border-radius:18px; min-height:90px;
padding:8px 4px; text-align:center; box-shadow:0 6px 15px rgba(0,0,0,.06);
}}
.mini-text {{ font-size:10px; font-weight:800; line-height:1.1; color:#102646; }}

.nav {{
margin-top:8px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 22px; font-weight: 800; }}
.nav-text {{ font-size: 10px; display: block; }}
.bot-bg {{
width:50px; height:50px; background:white; border-radius:12px;
margin: 0 auto 4px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}

/* إخفاء أزرار Streamlit وجعلها تغطي الأيقونات */
div.stButton > button {{
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0;
    cursor: pointer;
    border: none;
}}
.button-container {{ position: relative; }}
</style>
""", unsafe_allow_html=True)

# دالة للعودة للرئيسية
def go_home():
    st.session_state.current_page = "main"

# =====================================
# منطق التنقل (Navigation Logic)
# =====================================
if st.session_state.current_page != "main":
    # واجهة الـ Interface التي تظهر عند النقر
    st.markdown(f"""
    <div class="interface-container">
        <div style="font-size: 40px; margin-bottom: 20px;">📱</div>
        <a class="link-style" href="#">https://telecom.app/services/{st.session_state.current_page.lower().replace(' ', '_')}</a>
        <h2 style="color: #102646; font-weight: 900;">{st.session_state.current_page}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("Back to Home"):
        go_home()
        st.rerun()

else:
    # 1. قسم الملف الشخصي
    st.markdown(f"""
    <div class="welcome-card">
        <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
        <div class="welcome-text-container">
            <div style="font-size:20px; font-weight:900; color:#102646; line-height:1.1;">Welcome: User Name</div>
            <div style="font-size:12px; color:#555; margin-top:2px;">+962 79 123 4567</div>
            <div style="font-size:10px; color:#777;">Valid until: May 25, 2024</div>
            <div style="font-size:11px; background:#F0F7FF; border-radius:20px; padding:2px 10px; color:#102646; font-weight:700; margin-top:5px; border:1px solid #D0E0F0;">📍 Location: Amman</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. معلومات الرصيد
    st.markdown(f"""
    <div class="title">Your Number Info</div>
    <div class="card balance-card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 2;">
    <div style="font-size:10px; font-weight:700; color:#666;">Remaining GB</div>
    <div style="font-size:32px; font-weight:900; color:#102646; line-height:0.9;">4.7 <span style="font-size:14px;">GB</span></div>
    </div>
    <div style="flex: 1; text-align: right;">
    <div style="position: relative; width: 60px; height: 30px; margin-left: auto;">
        <div style="width: 50px; height: 25px; border-radius: 50px 50px 0 0; background: linear-gradient(90deg, #1A4FA0 60%, #E0E0E0 60%); position: relative; overflow: hidden;">
            <div style="position: absolute; bottom: 0; left: 5px; width: 40px; height: 20px; background: white; border-radius: 40px 40px 0 0;"></div>
            <div class="needle" style="height:20px; transform: rotate(45deg);"></div>
        </div>
    </div>
    <div style="font-size:10px; font-weight:900; color:#102646;">6 GB</div>
    </div>
    </div>
    <div style="margin-top:4px; height:6px; border-radius:10px; background:#E0E0E0; overflow:hidden;">
    <div style="width:78%; height:100%; background:#1A4FA0;"></div>
    </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. أيقونات الخدمات (مع تفعيل النقر)
    cols = st.columns(4)
    items = [
        ("📡", "Internet Packages"),
        ("🌍", "Renewals + Changes"),
        ("💰", "International Calls"),
        ("🔔", "Network Notifications")
    ]
    
    st.markdown('<div class="grid4">', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="button-container"><div class="mini"><div style="font-size:24px;">📡</div><div class="mini-text">Internet<br>Packages</div></div>', unsafe_allow_html=True)
        if st.button("btn1"): st.session_state.current_page = "Internet Packages"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="button-container"><div class="mini"><div style="font-size:24px;">🌍</div><div class="mini-text">Renewals +<br>Changes</div></div>', unsafe_allow_html=True)
        if st.button("btn2"): st.session_state.current_page = "Renewals + Changes"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="button-container"><div class="mini"><div style="font-size:24px;">💰</div><div class="mini-text">International<br>Calls</div></div>', unsafe_allow_html=True)
        if st.button("btn3"): st.session_state.current_page = "International Calls"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="button-container"><div class="mini"><div style="font-size:24px;">🔔</div><div class="mini-text">Network<br>Notifications</div></div>', unsafe_allow_html=True)
        if st.button("btn4"): st.session_state.current_page = "Network Notifications"; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. قسم التقييم
    st.markdown("""
    <div class="title">Service Ratings</div>
    <div class="card rating-card">
    <div style="font-weight:900; font-size:12px; color:#102646;">⭐ Service Security Rate</div>
    <div class="rating-bar-container">
        <span>★ 4.5</span><span>4.5%</span><span style="background:rgba(255,255,255,0.3); padding:0 5px; border-radius:2px;">24%</span>
    </div>
    <div style="text-align:center; margin-top:8px; font-weight:700; font-size:11px; color:#666; margin-bottom:2px;">Rate our service</div>
    <div style="display:flex; justify-content:center; gap:5px; font-size:24px; color:#ffcc00;">★★★★☆</div>
    </div>
    """, unsafe_allow_html=True)

    # 5. قوة الشبكة
    st.markdown("""
    <div class="title">Network Strength in your area</div>
    <div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center;">
    <div style="flex: 1.2;">
    <div style="font-size:14px; font-weight:900; color:#102646;">📍 Amman</div>
    <div style="font-size:12px; font-weight:700; color:#1A4FA0; margin-bottom:6px;">Very Strong Signal</div>
    <div style="display: flex; gap: 4px;">
    <div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
    <div style="font-size: 7px; color: #666; font-weight:bold;">Packet Loss (%)</div><div style="font-size: 16px; font-weight: 900; color: #000;">0</div>
    </div>
    <div style="background: #F1F7FF; border-radius: 10px; padding: 6px; text-align: center; flex: 1; border: 1px solid #E0E0E0;">
    <div style="font-size: 7px; color: #666; font-weight:bold;">Avg Jitter (ms)</div><div style="font-size: 16px; font-weight: 900; color: #000;">19</div>
    </div>
    </div>
    </div>
    <div style="flex: 1; text-align: center;">
    <div style="position: relative; width: 80px; margin: 0 auto;">
        <div style="width: 80px; height: 40px; border-radius: 80px 80px 0 0; background: linear-gradient(90deg, #4caf50 20%, #ffeb3b 50%, #f44336 100%); position: relative; overflow: hidden;">
            <div style="position: absolute; bottom: 0; left: 8px; width: 64px; height: 32px; background: white; border-radius: 64px 64px 0 0;"></div>
            <div class="needle" style="height: 35px; transform: rotate(-60deg);"></div>
        </div>
    <div style="font-size: 9px; font-weight: 900; color: #102646; margin-top: 4px;">-68dBm (Excellent)</div>
    </div>
    </div>
    </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================
# 6. الشريط السفلي (مع تفعيل النقر)
# =====================================
st.markdown('<div class="nav">', unsafe_allow_html=True)
b1, b2, b3, b4, b5 = st.columns(5)
with b1:
    st.markdown('<div class="button-container"><div class="nav-item">⚙️<span class="nav-text">Settings</span></div>', unsafe_allow_html=True)
    if st.button("s1"): st.session_state.current_page = "Settings"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with b2:
    st.markdown('<div class="button-container"><div class="nav-item">🎡<span class="nav-text">Spin</span></div>', unsafe_allow_html=True)
    if st.button("s2"): st.session_state.current_page = "Spin"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with b3:
    st.markdown(f'<div class="button-container"><div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:34px;"></div><span class="nav-text">Chatbot</span>', unsafe_allow_html=True)
    if st.button("s3"): st.session_state.current_page = "Chatbot"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with b4:
    st.markdown('<div class="button-container"><div class="nav-item">🏠<span class="nav-text">Home</span></div>', unsafe_allow_html=True)
    if st.button("s4"): go_home(); st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
with b5:
    st.markdown('<div class="button-container"><div class="nav-item">🎁<span class="nav-text">Game</span></div>', unsafe_allow_html=True)
    if st.button("s5"): st.session_state.current_page = "Game"; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
