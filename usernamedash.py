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
# CSS
# =====================================
st.markdown("""
<style>

*{margin:0;padding:0;box-sizing:border-box;}

html, body, [data-testid="stAppViewContainer"]{
background:#f0f7ff;
font-family:'Segoe UI', sans-serif;
}

section.main > div{padding-top:8px;}
div[data-testid="stVerticalBlock"]{gap:0rem;}

.block-container{
max-width:430px;
margin:auto;
padding:18px 16px;
background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
border-radius:42px;
box-shadow:0 14px 35px rgba(0,0,0,.15);
}

.card{
background:white;
border-radius:24px;
padding:14px;
margin-bottom:12px;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}

.title{
font-size:17px;
font-weight:900;
color:#102646;
margin: 8px 0 8px 4px;
}

.grid4{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:8px;
margin-bottom:12px;
}

.mini{
background:white;
border-radius:20px;
min-height:105px;
padding:12px 5px;
text-align:center;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}

.icon{font-size:24px;margin-bottom:5px;}
.mini-text{font-size:11px;font-weight:800;}

.nav{
margin-top:12px;
display:grid;
grid-template-columns:repeat(5,1fr);
text-align:center;
font-size:11px;
font-weight:800;
color:#6b6b6b;
}

.bot-bg{
width:45px;height:45px;
background:white;
border-radius:12px;
margin:auto;
display:flex;
align-items:center;
justify-content:center;
box-shadow:0 4px 10px rgba(0,0,0,0.1);
}

.active{color:#0d69dd;}

#MainMenu, header, footer{visibility:hidden;}

</style>
""", unsafe_allow_html=True)

# =====================================
# USER INPUT
# =====================================
user_name = st.text_input("Enter User Name", value="User Name")

# =====================================
# PROFILE
# =====================================
st.markdown(f"""
<div class="card">
<div style="display:flex;gap:10px;">
<img src="data:image/png;base64,{robot_full}" style="width:55px;">
<div>
<div style="font-size:17px;font-weight:900;">Welcome: {user_name}</div>
<div style="font-size:13px;">+962 79 123 4567</div>
<div style="font-size:13px;">Valid until: May 25, 2024</div>
</div>
</div>

<div style="margin-top:10px;background:#eef5ff;padding:10px;border-radius:18px;">
📍 Location: Amman
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# DATA
# =====================================
st.markdown("""
<div class="title">Your Number Info</div>

<div class="card">
<div style="font-size:13px;">Remaining GB</div>
<div style="font-size:40px;font-weight:900;">4.7 GB</div>

<div style="margin-top:10px;height:8px;background:#dce8f7;border-radius:20px;">
<div style="width:78%;height:100%;background:#1567e0;"></div>
</div>

<div style="text-align:right;font-weight:900;">6 GB</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# ICONS
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini"><div class="icon">📡</div><div class="mini-text">Internet<br>Packages</div></div>
<div class="mini"><div class="icon">🌍</div><div class="mini-text">Renewals</div></div>
<div class="mini"><div class="icon">💰</div><div class="mini-text">Calls</div></div>
<div class="mini"><div class="icon">🔔</div><div class="mini-text">Notifications</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# RATINGS
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>

<div class="card">
<div style="font-weight:900;">⭐ Service Security Rate</div>

<div style="height:20px;margin-top:10px;border-radius:18px;
background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);">
</div>

<div style="text-align:center;margin-top:10px;">Rate our service</div>

<div style="text-align:center;font-size:26px;color:#f4b400;">
★ ★ ★ ★ ☆
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# NETWORK (المعدل)
# =====================================
st.markdown("""
<div class="title">Network Strength in your area</div>

<div class="card">

<div style="display:flex;justify-content:space-between;align-items:flex-start;">

<div>
<div style="font-weight:900;">📍 Amman</div>
<div style="font-size:13px;color:#003366;">Very Strong Signal</div>
</div>

<div style="display:flex;gap:6px;">

<div style="background:#f1f7ff;border-radius:12px;padding:8px;text-align:center;">
<div style="font-size:10px;">Packet Loss</div>
<div style="font-weight:900;">0</div>
</div>

<div style="background:#f1f7ff;border-radius:12px;padding:8px;text-align:center;">
<div style="font-size:10px;">Jitter</div>
<div style="font-weight:900;">19</div>
</div>

</div>

</div>

<div style="text-align:center;margin-top:12px;font-weight:900;">
📶 -68 dBm (Excellent)
</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# NAVBAR
# =====================================
st.markdown(f"""
<div class="nav">
<div>⚙️<br>Settings</div>
<div>🎡<br>Spin</div>
<div>
<div class="bot-bg">
<img src="data:image/png;base64,{robot_head}" width="30">
</div>
Chatbot
</div>
<div class="active">🏠<br>Home</div>
<div>🎁<br>Game</div>
</div>
""", unsafe_allow_html=True)
