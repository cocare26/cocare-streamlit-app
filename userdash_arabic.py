import streamlit as st
import base64
import os

# =====================================
# إعداد الصفحة
# =====================================
st.set_page_config(
    page_title="لوحة تحكم الاتصالات",
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

# تحميل الصور (تأكدي من وجود الملفات في نفس المجلد بنفس هذه الأسماء)
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (اللغة العربية والتأثيرات الحركية)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; direction: rtl; }}
html, body, [data-testid="stAppViewContainer"] {{
background:#f0f7ff;
font-family:'Segoe UI', sans-serif;
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
transition: transform 0.3s ease;
}}

.title {{
font-size:17px;
font-weight:900;
color:#102646;
margin: 8px 4px 8px 0;
text-align: right;
}}

.clickable {{ 
    cursor: pointer; 
    transition: all 0.3s ease; 
}}
.clickable:active {{ transform: scale(0.95); }}

/* تأثير حركة المؤشر على الأيقونات */
.mini:hover, .nav-item:hover, .bot-bg:hover {{
    transform: translateY(-5px) scale(1.05);
}}

/* نظام النجوم التفاعلي */
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
transition: all 0.3s ease;
}}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; }}

.robot-img-welcome {{
    width: 130px; 
    height: auto;
    background: transparent !important;
    filter: drop-shadow(0 8px 15px rgba(0,0,0,0.1));
    margin-left: 10px;
    object-fit: contain;
    transition: transform 0.4s ease;
}}
.robot-img-welcome:hover {{ transform: scale(1.05); }}

.welcome-text-container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: right;
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

/* الشريط السفلي */
.nav {{
margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{ font-size: 24px; font-weight: 800; transition: all 0.3s ease; }}
.nav-text {{ font-size: 11px; display: block; margin-top: 2px; }}
.bot-bg {{
width:55px; height:55px; background:white; border-radius:14px;
margin: 0 auto 5px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
transition: all 0.3s ease;
}}
.active {{ color:#0d69dd; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الملف الشخصي
# =====================================
st.markdown(f"""
<div class="card clickable">
<div style="display:flex; align-items:center; flex-direction: row-reverse;">
    <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
    <div class="welcome-text-container" style="flex:1;">
        <div style="font-size:26px; font-weight:900; color:#102646; line-height:1.2;">أهلاً بك</div>
        <div style="font-size:14px; color:#555; margin-top:4px;">+962 79 123 4567</div>
        <div style="font-size:14px; color:#555;">صالح لغاية: 25 مايو 2026</div>
    </div>
</div>
<div style="margin-top:15px; background:#eef5ff; padding:10px 14px; border-radius:18px; font-size:14px; font-weight:700; text-align:right;">
📍 الموقع الحالي: عمان
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">معلومات اشتراكك</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center; flex-direction: row-reverse;">
<div style="flex: 2; text-align: right;">
<div style="font-size:13px; font-weight:700; color:#666;">الإنترنت المتبقي</div>
<div style="font-size:40px; font-weight:900; color:#102646;">4.7 <span style="font-size:18px;">GB</span></div>
</div>
<div style="flex: 1; text-align: left;">
<div style="position: relative; width: 70px; height: 35px; margin-right: auto;">
    <div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #0d69dd 60%, #e0e0e0 60%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
        <div class="needle" style="transform: rotate(45deg);"></div>
    </div>
</div>
<div style="font-size:14px; font-weight:900; color:#102646; margin-top:2px;">السعة 6 GB</div>
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
<div class="mini clickable"><div style="font-size:28px;">📡</div><div class="mini-text">حزم<br>الإنترنت</div></div>
<div class="mini clickable"><div style="font-size:28px;">🌍</div><div class="mini-text">تجديد<br>الاشتراك</div></div>
<div class="mini clickable"><div style="font-size:28px;">💰</div><div class="mini-text">اتصال<br>دولي</div></div>
<div class="mini clickable"><div style="font-size:28px;">🔔</div><div class="mini-text">إشعارات<br>الشبكة</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">تقييم الخدمة</div>
<div class="card">
<div style="font-weight:900; font-size:14px; color:#102646; text-align:right;">⭐ مستوى أمان الخدمة</div>
<div style="margin-top:10px; height:20px; border-radius:18px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
<div style="text-align:center; margin-top:12px; font-weight:700; font-size:14px; color:#102646; margin-bottom:5px;">شاركنا رأيك</div>
<div class="star-rating">
    <input type="radio" id="5" name="rate"><label for="5">★</label>
    <input type="radio" id="4" name="rate"><label for="4">★</label>
    <input type="radio" id="3" name="rate"><label for="3">★</label>
    <input type="radio" id="2" name="rate"><label for="2">★</label>
    <input type="radio" id="1" name="rate"><label for="1">★</label>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. قوة الشبكة
# =====================================
st.markdown("""
<div class="title">قوة الشبكة في منطقتك</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center; flex-direction: row-reverse;">
<div style="flex: 1.2; text-align: right;">
<div style="font-size:16px; font-weight:900; color:#102646;">📍 عمان</div>
<div style="font-size:13px; font-weight:700; color:#003366; margin-bottom:8px;">إشارة ممتازة</div>
<div style="display: flex; gap: 6px; flex-direction: row-reverse;">
<div style="background: #f1f7ff; border-radius: 12px; padding: 8px; text-align: center; flex: 1;">
<div style="font-size: 8px; font-weight: 700; color: #666; line-height:1;">فقد البيانات (%)</div>
<div style="font-size: 18px; font-weight: 900; color: #000; margin-top: 2px;">0</div>
</div>
<div style="background: #f1f7ff; border-radius: 12px; padding: 8px; text-align: center; flex: 1;">
<div style="font-size: 8px; font-weight: 700; color: #666; line-height:1;">التذبذب (ms)</div>
<div style="font-size: 18px; font-weight: 900; color: #000; margin-top: 2px;">19</div>
</div>
</div>
</div>
<div style="flex: 1; text-align: center;">
<div style="position: relative; width: 100px; margin: 0 auto;">
    <div style="width: 100px; height: 50px; border-radius: 100px 100px 0 0; background: linear-gradient(90deg, #4caf50 20%, #ffeb3b 50%, #f44336 100%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 10px; width: 80px; height: 40px; background: white; border-radius: 80px 80px 0 0;"></div>
        <div class="needle" style="height: 40px; transform: rotate(-60deg);"></div>
    </div>
<div style="font-size: 10px; font-weight: 900; color: #102646; margin-top: 5px;">-68dBm (ممتاز)</div>
</div>
</div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 6. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item clickable">⚙️<span class="nav-text">الإعدادات</span></div>
<div class="nav-item clickable">🎡<span class="nav-text">اربح</span></div>
<div class="nav-item clickable">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:38px;"></div>
<span class="nav-text">المساعد</span>
</div>
<div class="nav-item active clickable">🏠<span class="nav-text">الرئيسية</span></div>
<div class="nav-item clickable">🎁<span class="nav-text">الألعاب</span></div>
</div>
""", unsafe_allow_html=True)
