import streamlit as st
import base64
import os

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="لوحة الاتصالات",
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

robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS (تمت إضافة اتجاه RTL)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body, [data-testid="stAppViewContainer"] {{
background:#f0f7ff;
font-family:'Segoe UI', sans-serif;
direction: rtl;
text-align: right;
}}

section.main > div {{ padding-top:8px; }}
div[data-testid="stVerticalBlock"] {{ gap:0rem; }}

#MainMenu, header, footer {{ visibility:hidden; }}

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

.clickable {{ cursor: pointer; transition: transform 0.2s ease; }}
.clickable:active {{ transform: scale(0.95); }}

.star-rating {{
display: flex;
flex-direction: row-reverse;
justify-content: center;
gap: 4px;
}}
.star-rating input {{ display: none; }}
.star-rating label {{
font-size: 35px;
color: #ddd;
cursor: pointer;
transition: color 0.2s;
}}
.star-rating input:checked ~ label,
.star-rating label:hover,
.star-rating label:hover ~ label {{
color: #ffcc00;
}}

.grid4 {{ 
display:grid; 
grid-template-columns:repeat(4,1fr); 
gap:8px; 
margin: 20px 0 12px; 
}}

.mini {{
background:white; border-radius:20px; min-height:105px;
padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);
}}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; }}

.robot-img-welcome {{
width:130px;
height:auto;
background: transparent !important;
filter: drop-shadow(0 8px 15px rgba(0,0,0,0.1));
margin-left: 10px;
object-fit: contain;
}}

.welcome-text-container {{
display: flex;
flex-direction: column;
justify-content: center;
}}

.needle {{
position: absolute;
bottom: 0;
left: 50%;
width: 2px;
height: 30px;
background: #333;
transform-origin: bottom center;
z-index: 5;
}}

.nav {{
margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 24px; font-weight: 800; }}
.nav-text {{ font-size: 11px; display: block; margin-top: 2px; }}

.bot-bg {{
width:55px; height:55px; background:white; border-radius:14px;
margin: 0 auto 5px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}

.active {{ color:#0d69dd; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. الملف الشخصي
# =====================================
st.markdown(f"""
<div class="card clickable">
<div style="display:flex; align-items:center;">
    <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
    <div class="welcome-text-container">
        <div style="font-size:26px; font-weight:900; color:#102646;">مرحباً</div>
        <div style="font-size:14px; color:#555; margin-top:4px;">+962 79 123 4567</div>
        <div style="font-size:14px; color:#555;">صالح حتى: 25 مايو 2026</div>
    </div>
</div>
<div style="margin-top:15px; background:#eef5ff; padding:10px 14px; border-radius:18px; font-size:14px; font-weight:700;">
📍 الموقع: عمّان
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. الرصيد
# =====================================
st.markdown(f"""
<div class="title">معلومات رقمك</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2;">
<div style="font-size:13px; font-weight:700; color:#666;">البيانات المتبقية</div>
<div style="font-size:40px; font-weight:900; color:#102646;">4.7 <span style="font-size:18px;">جيجابايت</span></div>
</div>
<div style="flex: 1; text-align: left;">
<div style="font-size:14px; font-weight:900; color:#102646;">6 جيجابايت</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. الخدمات
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini clickable"><div style="font-size:28px;">📡</div><div class="mini-text">باقات<br>الإنترنت</div></div>
<div class="mini clickable"><div style="font-size:28px;">🌍</div><div class="mini-text">تجديد +<br>تعديل</div></div>
<div class="mini clickable"><div style="font-size:28px;">💰</div><div class="mini-text">مكالمات<br>دولية</div></div>
<div class="mini clickable"><div style="font-size:28px;">🔔</div><div class="mini-text">إشعارات<br>الشبكة</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. التقييم
# =====================================
st.markdown("""
<div class="title">تقييم الخدمة</div>
<div class="card">
<div style="font-weight:900; font-size:14px;">⭐ تقييم أمان الخدمة</div>
<div style="text-align:center; margin-top:12px;">قيّم الخدمة</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. الشبكة
# =====================================
st.markdown("""
<div class="title">قوة الشبكة في منطقتك</div>
<div class="card clickable">
<div>📍 عمّان</div>
<div>إشارة قوية جداً</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 6. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item clickable">⚙️<span class="nav-text">الإعدادات</span></div>
<div class="nav-item clickable">🎡<span class="nav-text">حظك</span></div>
<div class="nav-item clickable">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:38px;"></div>
<span class="nav-text">المساعد</span>
</div>
<div class="nav-item active clickable">🏠<span class="nav-text">الرئيسية</span></div>
<div class="nav-item clickable">🎁<span class="nav-text">الألعاب</span></div>
</div>
""", unsafe_allow_html=True)
