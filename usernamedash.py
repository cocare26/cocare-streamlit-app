import streamlit as st
import base64

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="Telecom Dashboard",
    page_icon="📱",
    layout="centered"
)

# =====================================
# دالة تحويل الصورة Base64
# =====================================
def get_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =====================================
# ضع أسماء الصور هنا
# robot_full.png   = صورة الروبوت الكامل
# robot_head.png   = صورة رأس الروبوت السفلي
# =====================================
robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# إدخال اسم المستخدم
# =====================================
user_name = st.text_input("Enter User Name", value="User Name")

# =====================================
# CSS كامل
# =====================================
st.markdown(f"""
<style>

/* Reset */
*{{
margin:0;
padding:0;
box-sizing:border-box;
}}

html, body, [data-testid="stAppViewContainer"]{{
background:#e9edf3;
font-family:'Segoe UI', sans-serif;
}}

section.main > div{{
padding-top:8px;
}}

div[data-testid="stVerticalBlock"]{{
gap:0rem;
}}

.block-container{{
max-width:430px;
margin:auto;
padding:18px 16px 22px 16px;

background:linear-gradient(
180deg,
#dff2ff 0%,
#c7e7ff 55%,
#f4fbff 100%
);

border-radius:42px;
box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card{{
background:white;
border-radius:24px;
padding:14px;
margin-bottom:12px;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.title{{
font-size:17px;
font-weight:900;
color:#102646;
margin-bottom:8px;
margin-top:4px;
}}

.profile{{
display:flex;
gap:10px;
align-items:flex-start;
}}

.avatar{{
width:55px;
height:70px;
object-fit:contain;
}}

.name{{
font-size:17px;
font-weight:900;
margin-bottom:4px;
}}

.sub{{
font-size:13px;
margin-bottom:3px;
}}

.location{{
margin-top:10px;
background:#eef5ff;
padding:10px 14px;
border-radius:18px;
font-size:14px;
font-weight:700;
}}

.small{{
font-size:15px;
font-weight:700;
}}

.big-number{{
font-size:42px;
font-weight:900;
color:#102646;
line-height:1;
margin-top:5px;
}}

.gb{{
font-size:18px;
font-weight:700;
}}

.progress{{
margin-top:12px;
height:10px;
border-radius:20px;
background:#dce8f7;
overflow:hidden;
}}

.fill{{
width:78%;
height:100%;
background:linear-gradient(90deg,#083d8c,#1567e0);
}}

.bottom-right{{
text-align:right;
font-size:26px;
font-weight:900;
margin-top:8px;
color:#102646;
}}

.grid4{{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:8px;
margin-bottom:12px;
}}

.mini{{
background:white;
border-radius:20px;
min-height:112px;
padding:10px 6px;
text-align:center;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.icon{{
font-size:28px;
margin-bottom:8px;
}}

.mini-text{{
font-size:12px;
font-weight:800;
line-height:1.2;
}}

.bar{{
margin-top:10px;
height:28px;
border-radius:18px;
background:linear-gradient(
90deg,
#0047ba 0%,
#27a4ff 40%,
#ff8c00 70%,
#df4126 100%
);
}}

.center{{
text-align:center;
}}

.star{{
font-size:28px;
color:#f4b400;
letter-spacing:2px;
margin-top:8px;
}}

.city{{
font-size:18px;
font-weight:900;
}}

.signal{{
font-size:28px;
font-weight:900;
margin-top:4px;
}}

.row2{{
display:grid;
grid-template-columns:1fr 1fr;
gap:10px;
margin-top:12px;
}}

.smallbox{{
background:#edf4ff;
border-radius:18px;
padding:12px;
text-align:center;
font-size:14px;
font-weight:700;
}}

.num{{
font-size:28px;
font-weight:900;
margin-top:4px;
}}

.meter{{
text-align:center;
margin-top:14px;
font-size:22px;
font-weight:900;
color:#102646;
}}

.nav{{
margin-top:12px;
display:grid;
grid-template-columns:repeat(5,1fr);
text-align:center;
font-size:12px;
font-weight:800;
color:#6b6b6b;
}}

.nav div{{
padding-top:8px;
}}

.active{{
color:#0d69dd;
}}

.bottom-robot{{
width:42px;
height:42px;
border-radius:50%;
object-fit:cover;
box-shadow:0 4px 10px rgba(0,0,0,.2);
}}

#MainMenu, header, footer{{
visibility:hidden;
}}

</style>
""", unsafe_allow_html=True)

# =====================================
# PROFILE
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
# NUMBER INFO
# =====================================
st.markdown("""
<div class="title">Your Number Info</div>

<div class="card">

<div class="small">Remaining GB</div>

<div class="big-number">
4.7 <span class="gb">GB</span>
</div>

<div class="progress">
<div class="fill"></div>
</div>

<div class="bottom-right">6 GB</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# ICONS
# =====================================
st.markdown("""
<div class="grid4">

<div class="mini">
<div class="icon">📡</div>
<div class="mini-text">Internet<br>Packages</div>
</div>

<div class="mini">
<div class="icon">🌍</div>
<div class="mini-text">Renewals +<br>Tariff Changes</div>
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
# RATINGS
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>

<div class="card">

<div style="font-weight:900;">⭐ Service Security Rate</div>

<div class="bar"></div>

<div class="center" style="margin-top:10px;font-weight:700;">
Rate our service
</div>

<div class="center star">
★ ★ ★ ★ ☆
</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# NETWORK
# =====================================
st.markdown("""
<div class="title">Network Strength in your area</div>

<div class="card">

<div class="city">📍 Amman</div>

<div class="signal">Very Strong Signal</div>

<div class="row2">

<div class="smallbox">
Packet Loss (%)
<div class="num">0</div>
</div>

<div class="smallbox">
Avg Jitter (ms)
<div class="num">19</div>
</div>

</div>

<div class="meter">
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
<img class="bottom-robot" src="data:image/png;base64,{robot_head}">
<br>Chatbot
</div>

<div class="active">🏠<br>Home</div>

<div>🎁<br>Game</div>

</div>


# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="Telecom Dashboard",
    page_icon="📱",
    layout="centered"
)

# =====================================
# دالة تحويل الصورة Base64
# =====================================
def get_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =====================================
# ضع أسماء الصور هنا
# robot_full.png   = صورة الروبوت الكامل
# robot_head.png   = صورة رأس الروبوت السفلي
# =====================================
robot_full = get_base64("robot_full.png")
robot_head = get_base64("robot_head.png")

# =====================================
# إدخال اسم المستخدم
# =====================================
user_name = st.text_input("Enter User Name", value="User Name")

# =====================================
# CSS كامل
# =====================================
st.markdown(f"""
<style>

/* Reset */
*{{
margin:0;
padding:0;
box-sizing:border-box;
}}

html, body, [data-testid="stAppViewContainer"]{{
background:#e9edf3;
font-family:'Segoe UI', sans-serif;
}}

section.main > div{{
padding-top:8px;
}}

div[data-testid="stVerticalBlock"]{{
gap:0rem;
}}

.block-container{{
max-width:430px;
margin:auto;
padding:18px 16px 22px 16px;

background:linear-gradient(
180deg,
#dff2ff 0%,
#c7e7ff 55%,
#f4fbff 100%
);

border-radius:42px;
box-shadow:0 14px 35px rgba(0,0,0,.15);
}}

.card{{
background:white;
border-radius:24px;
padding:14px;
margin-bottom:12px;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.title{{
font-size:17px;
font-weight:900;
color:#102646;
margin-bottom:8px;
margin-top:4px;
}}

.profile{{
display:flex;
gap:10px;
align-items:flex-start;
}}

.avatar{{
width:55px;
height:70px;
object-fit:contain;
}}

.name{{
font-size:17px;
font-weight:900;
margin-bottom:4px;
}}

.sub{{
font-size:13px;
margin-bottom:3px;
}}

.location{{
margin-top:10px;
background:#eef5ff;
padding:10px 14px;
border-radius:18px;
font-size:14px;
font-weight:700;
}}

.small{{
font-size:15px;
font-weight:700;
}}

.big-number{{
font-size:42px;
font-weight:900;
color:#102646;
line-height:1;
margin-top:5px;
}}

.gb{{
font-size:18px;
font-weight:700;
}}

.progress{{
margin-top:12px;
height:10px;
border-radius:20px;
background:#dce8f7;
overflow:hidden;
}}

.fill{{
width:78%;
height:100%;
background:linear-gradient(90deg,#083d8c,#1567e0);
}}

.bottom-right{{
text-align:right;
font-size:26px;
font-weight:900;
margin-top:8px;
color:#102646;
}}

.grid4{{
display:grid;
grid-template-columns:repeat(4,1fr);
gap:8px;
margin-bottom:12px;
}}

.mini{{
background:white;
border-radius:20px;
min-height:112px;
padding:10px 6px;
text-align:center;
box-shadow:0 6px 18px rgba(0,0,0,.08);
}}

.icon{{
font-size:28px;
margin-bottom:8px;
}}

.mini-text{{
font-size:12px;
font-weight:800;
line-height:1.2;
}}

.bar{{
margin-top:10px;
height:28px;
border-radius:18px;
background:linear-gradient(
90deg,
#0047ba 0%,
#27a4ff 40%,
#ff8c00 70%,
#df4126 100%
);
}}

.center{{
text-align:center;
}}

.star{{
font-size:28px;
color:#f4b400;
letter-spacing:2px;
margin-top:8px;
}}

.city{{
font-size:18px;
font-weight:900;
}}

.signal{{
font-size:28px;
font-weight:900;
margin-top:4px;
}}

.row2{{
display:grid;
grid-template-columns:1fr 1fr;
gap:10px;
margin-top:12px;
}}

.smallbox{{
background:#edf4ff;
border-radius:18px;
padding:12px;
text-align:center;
font-size:14px;
font-weight:700;
}}

.num{{
font-size:28px;
font-weight:900;
margin-top:4px;
}}

.meter{{
text-align:center;
margin-top:14px;
font-size:22px;
font-weight:900;
color:#102646;
}}

.nav{{
margin-top:12px;
display:grid;
grid-template-columns:repeat(5,1fr);
text-align:center;
font-size:12px;
font-weight:800;
color:#6b6b6b;
}}

.nav div{{
padding-top:8px;
}}

.active{{
color:#0d69dd;
}}

.bottom-robot{{
width:42px;
height:42px;
border-radius:50%;
object-fit:cover;
box-shadow:0 4px 10px rgba(0,0,0,.2);
}}

#MainMenu, header, footer{{
visibility:hidden;
}}

</style>
""", unsafe_allow_html=True)

# =====================================
# PROFILE
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
# NUMBER INFO
# =====================================
st.markdown("""
<div class="title">Your Number Info</div>

<div class="card">

<div class="small">Remaining GB</div>

<div class="big-number">
4.7 <span class="gb">GB</span>
</div>

<div class="progress">
<div class="fill"></div>
</div>

<div class="bottom-right">6 GB</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# ICONS
# =====================================
st.markdown("""
<div class="grid4">

<div class="mini">
<div class="icon">📡</div>
<div class="mini-text">Internet<br>Packages</div>
</div>

<div class="mini">
<div class="icon">🌍</div>
<div class="mini-text">Renewals +<br>Tariff Changes</div>
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
# RATINGS
# =====================================
st.markdown("""
<div class="title">Service Ratings</div>

<div class="card">

<div style="font-weight:900;">⭐ Service Security Rate</div>

<div class="bar"></div>

<div class="center" style="margin-top:10px;font-weight:700;">
Rate our service
</div>

<div class="center star">
★ ★ ★ ★ ☆
</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# NETWORK
# =====================================
st.markdown("""
<div class="title">Network Strength in your area</div>

<div class="card">

<div class="city">📍 Amman</div>

<div class="signal">Very Strong Signal</div>

<div class="row2">

<div class="smallbox">
Packet Loss (%)
<div class="num">0</div>
</div>

<div class="smallbox">
Avg Jitter (ms)
<div class="num">19</div>
</div>

</div>

<div class="meter">
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
<img class="bottom-robot" src="data:image/png;base64,{robot_head}">
<br>Chatbot
</div>

<div class="active">🏠<br>Home</div>

<div>🎁<br>Game</div>

</div>
""", unsafe_allow_html=True)
