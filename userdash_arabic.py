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

robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS المطور (تنسيق الواجهة)
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

/* تأثير النقر والحركة (Animation) */
.clickable {{ 
    cursor: pointer; 
    transition: transform 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
}}
.clickable:active {{ 
    transform: scale(0.92); /* تأثير الضغط */
}}
.nav-item.clickable:active {{
    transform: scale(1.2); /* تكبير أيقونات الشريط السفلي عند النقر */
}}

/* نظام النجوم */
.star-rating {{
display: flex;
justify-content: center;
gap: 4px;
margin-top: 5px;
}}
.star-rating label {{
font-size: 32px;
color: #ddd;
cursor: pointer;
}}

/* تعديل المسافة بين قسم الرصيد والأيقونات */
.grid4 {{ 
    display:grid; 
    grid-template-columns:repeat(4,1fr); 
    gap:8px; 
    margin-top: 25px; /* مسافة لمنع الالتصاق */
    margin-bottom: 12px; 
}}

.mini {{
background:white; border-radius:20px; min-height:105px;
padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);
}}
.icon {{ font-size:24px; margin-bottom:5px; }}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; }}

/* تعديل الشريط السفلي والأيقونات */
.nav {{
margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; color:#6b6b6b; align-items: end;
}}
.nav-item {{
    font-size: 22px; /* تكبير حجم الأيقونة */
    font-weight: 800;
}}
.nav-text {{
    font-size: 11px;
    display: block;
    margin-top: 2px;
}}

.bot-bg {{
width:52px; height:52px; background:white; border-radius:14px;
margin: 0 auto 5px; display:flex; align-items:center; justify-content:center;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}}
.active {{ color:#0d69dd; }}

#MainMenu, header, footer {{ visibility:hidden; }}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. قسم الملف الشخصي
# =====================================
user_name = st.text_input("أدخل اسم المستخدم", value="فرح")

st.markdown(f"""
<div class="card clickable">
<div style="display:flex; gap:10px; align-items:flex-start; text-align: right;">
<img src="data:image/png;base64,{robot_full}" style="width:55px; height:70px; object-fit:contain;">
<div>
<div style="font-size:17px; font-weight:900;">أهلاً بك: {user_name}</div>
<div style="font-size:13px; color:#555; direction: ltr;">+962 79 123 4567</div>
<div style="font-size:13px; color:#555;">صالح لغاية: 25 مايو، 2026</div>
</div>
</div>
<div style="margin-top:10px; background:#eef5ff; padding:10px 14px; border-radius:18px; font-size:14px; font-weight:700; text-align: right;">
📍 الموقع: عمان
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. معلومات الرصيد
# =====================================
st.markdown(f"""
<div class="title">معلومات رقمك</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center; direction: ltr;">
<div style="flex: 1; text-align: left;">
<div style="position: relative; width: 70px; height: 35px; margin-right: auto;">
<div style="width: 70px; height: 35px; border-radius: 70px 70px 0 0; background: linear-gradient(90deg, #0d69dd 60%, #e0e0e0 60%); position: relative; overflow: hidden;">
<div style="position: absolute; bottom: 0; left: 7px; width: 56px; height: 28px; background: white; border-radius: 56px 56px 0 0;"></div>
<div style="position: absolute; bottom: 0; left: 50%; width: 2px; height: 28px; background: #083d8c; transform-origin: bottom; transform: rotate(45deg);"></div>
</div>
</div>
<div style="font-size:14px; font-weight:900; color:#102646; margin-top:2px; text-align: center; width:70px;">6 جيجا</div>
</div>
<div style="flex: 2; text-align: right;">
<div style="font-size:13px; font-weight:700; color:#666;">الرصيد المتبقي</div>
<div style="font-size:40px; font-weight:900; color:#102646; direction: rtl;">4.7 <span style="font-size:18px;">جيجابايت</span></div>
</div>
</div>
<div style="margin-top:10px; height:8px; border-radius:20px; background:#dce8f7; overflow:hidden;">
<div style="width:78%; height:100%; background:linear-gradient(90deg,#083d8c,#1567e0); float: right;"></div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. أيقونات الخدمات (مفصولة بمسافة الآن)
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini clickable"><div class="icon">📡</div><div class="mini-text">حزم<br>الإنترنت</div></div>
<div class="mini clickable"><div class="icon">🌍</div><div class="mini-text">التجديد +<br>التغيير</div></div>
<div class="mini clickable"><div class="icon">💰</div><div class="mini-text">اتصالات<br>دولية</div></div>
<div class="mini clickable"><div class="icon">🔔</div><div class="mini-text">تنبيهات<br>الشبكة</div></div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. قسم التقييم
# =====================================
st.markdown("""
<div class="title">تقييم الخدمة</div>
<div class="card">
<div style="font-weight:900; font-size:14px; color:#102646; text-align: right;">⭐ مستوى أمان الخدمة</div>
<div style="margin-top:10px; height:20px; border-radius:18px; background:linear-gradient(90deg,#0047ba,#27a4ff,#ff8c00,#df4126);"></div>
<div style="text-align:center; margin-top:12px; font-weight:700; font-size:13px; color:#102646;">قيم خدمتنا</div>
<div class="star-rating">
<label>★</label><label>★</label><label>★</label><label>★</label><label>★</label>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 5. قوة الشبكة
# =====================================
st.markdown("""
<div class="title">قوة الشبكة في منطقتك</div>
<div class="card clickable">
<div style="display: flex; justify-content: space-between; align-items: center; direction: rtl;">
<div style="flex: 1.2; text-align: right;">
<div style="font-size:16px; font-weight:900; color:#102646;">📍 عمان</div>
<div style="font-size:13px;
