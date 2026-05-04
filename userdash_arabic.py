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

# تحميل الصور (تأكدي من وجود الملفات في مستودع GitHub الخاص بك)
robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (دعم العربية والواجهة المودرن)
# =====================================
st.markdown(f"""
<style>
* {{ margin:0; padding:0; box-sizing:border-box; direction: rtl; }}
html, body, [data-testid="stAppViewContainer"] {{
    background:#f0f7ff;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
    margin: 8px 4px 8px 0;
    text-align: right;
}}

.robot-img-welcome {{
    width: 140px;
    height: auto;
    background: transparent !important;
    margin-left: 5px;
    object-fit: contain;
    mix-blend-mode: multiply; 
    filter: contrast(110%);
}}

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

.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin: 20px 0 12px; }}
.mini {{ background:white; border-radius:20px; min-height:105px; padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08); }}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; }}

.star-rating {{ display: flex; flex-direction: row; justify-content: center; gap: 4px; }}
.star-rating input {{ display: none; }}
.star-rating label {{ font-size: 35px; color: #ddd; cursor: pointer; }}
.star-rating input:checked ~ label {{ color: #ffcc00; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الترحيب (Welcome)
# =====================================
st.markdown(f"""
<div class="card">
<div style="display:flex; align-items:center;">
    <img src="data:image/png;base64,{robot_full}" class="robot-img-welcome">
    <div class="welcome-text-container">
        <div style="font-size:26px; font-weight:900; color:#102646; line-height:1.2;">أهلاً بك</div>
        <div style="font-size:14px; color:#555; margin-top:4px; direction: ltr;">+962 79 123 4567</div>
        <div style="font-size:14px; color:#555;">صالح لغاية: 25 مايو 2026</div>
    </div>
</div>
<div style="margin-top:10px; background:#eef5ff; padding:10px 14px; border-radius:18px; font-size:14px; font-weight:700; text-align: right;">
📍 الموقع: عمان
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد (Number Info)
# =====================================
st.markdown(f"""
<div class="title">معلومات رقمك</div>
<div class="card">
<div style="display: flex; justify-content: space-between; align-items: center;">
<div style="flex: 2; text-align: right;">
<div style="font-size:13px; font-weight:700; color:#666;">الإنترنت المتبقي</div>
<div style="font-size:40px; font-weight:900; color:#102646;">4.7 <span style="font-size:18px;">جيجابايت</span></div>
</div>
<div style="flex: 1; text-align: left;">
<div style="position: relative; width: 70px; height: 35px; margin-right: auto;">
    <div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #0d69dd 60%, #e0e0e0 60%); position: relative; overflow: hidden;">
        <div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
        <div class="needle" style="transform: rotate(45deg);"></div>
    </div>
</div>
<div style="font-size:14px; font-weight:900; color:#102646; margin-top:2px; text-align:center;">6 جيجابايت</div>
</div>
</div>
<div style="margin-top:10px; height:8px; border-radius:20px; background:#dce8f7; overflow:hidden;">
<div style="width:78%; height:100%; background:linear-gradient(90deg,#083d8c,#1567e0); float: right;"></div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات (Grid)
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini"><div style="font-size:28px;">📡</div><div class="mini-text">حزم<br>الإنترنت</div></div>
<div class="mini"><div style="font-size:28px;">🌍</div><div class="mini-text">تجديد +<br>تغيير</div></div>
<div class="mini"><div style="font-size:28px;">💰</div><div class="mini-text">اتصالات<br>دولية</div></div>
<div class="mini"><div style="font-size:28px;">🔔</div><div class="mini-text">تنبيهات<br>الشبكة</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. التقييم وقوة الشبكة
# =====================================
st.markdown("""
<div class="title">تقييم الخدمة وقوة الشبكة</div>
<div class="card">
    <div style="font-weight:900; font-size:14px; color:#102646; text-align: right;">⭐ مستوى الأمان</div>
    <div style="margin-top:10px; height:15px; border-radius:18px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
    <div style="display: flex; justify-content: space-around; margin-top:15px; border-top: 1px solid #eee; padding-top:10px;">
        <div style="text-align:center;"><div style="font-size:10px; color:#666;">فقدان البيانات</div><div style="font-weight:900;">0%</div></div>
        <div style="text-align:center;"><div style="font-size:10px; color:#666;">التذبذب</div><div style="font-weight:900;">19ms</div></div>
        <div style="text-align:center;"><div style="font-size:10px; color:#666;">الإشارة</div><div style="font-weight:900; color:#28a745;">ممتازة</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. الشريط السفلي (Navigation)
# =====================================
st.markdown(f"""
<div class="nav">
<div class="nav-item">⚙️<span class="nav-text">الإعدادات</span></div>
<div class="nav-item">🎡<span class="nav-text">اربح</span></div>
<div class="nav-item">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:38px;"></div>
<span class="nav-text">المساعد</span>
</div>
<div class="nav-item active">🏠<span class="nav-text">الرئيسية</span></div>
<div class="nav-item">🎁<span class="nav-text">ألعاب</span></div>
</div>
""", unsafe_allow_html=True)
