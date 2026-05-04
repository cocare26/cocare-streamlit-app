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

robot_full = get_base64("robot_full.png")
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

.clickable {{ cursor: pointer; transition: transform 0.2s, opacity 0.2s; }}
.clickable:active {{ transform: scale(0.96); opacity: 0.8; }}

/* نظام النجوم */
.star-rating {{
display: flex;
justify-content: center;
gap: 4px;
margin-top: 5px;
}}
.star-rating input {{ display: none; }}
.star-rating label {{
font-size: 32px;
color: #ddd;
cursor: pointer;
transition: color 0.2s;
}}
.star-rating label:hover,
.star-rating label:hover ~ label,
.star-rating input:checked ~ label {{
color: #f4b400;
}}

.grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-bottom:12px; }}
.mini {{
background:white; border-radius:20px; min-height:105px;
padding:12px 5px; text-align:center; box-shadow:0 6px 18px rgba(0,0,0,.08);
}}
.icon {{ font-size:24px; margin-bottom:5px; }}
.mini-text {{ font-size:11px; font-weight:800; line-height:1.2; }}

.nav {{
margin-top:12px; display:grid; grid-template-columns:repeat(5,1fr);
text-align:center; font-size:11px; font-weight:800; color:#6b6b6b;
}}
.bot-bg {{
width:45px; height:45px; background:white; border-radius:12px;
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
# 3. أيقونات الخدمات
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
<div style="font-size:13px; font-weight:700; color:#003366; margin-bottom:8px;">إشارة قوية جداً</div>
<div style="display: flex; gap: 6px; direction: ltr;">
<div style="background: #f1f7ff; border-radius: 12px; padding: 8px; text-align: center; flex: 1;">
<div style="font-size: 8px; font-weight: 700; color: #666; line-height:1;">Packet Loss (%)</div>
<div style="font-size: 18px; font-weight: 900; color: #000; margin-top: 2px;">0</div>
</div>
<div style="background: #f1f7ff; border-radius: 12px; padding: 8px; text-align: center; flex: 1;">
<div style="font-size: 8px; font-weight: 700; color: #666; line-height:1;">Avg Jitter (ms)</div>
<div style="font-size: 18px; font-weight: 900; color: #000; margin-top: 2px;">19</div>
</div>
</div>
</div>
<div style="flex: 1; text-align: center;">
<div style="position: relative; width: 100px; margin: 0 auto;">
<div style="width: 100px; height: 50px; border-radius: 100px 100px 0 0; background: linear-gradient(90deg, #4caf50 20%, #ffeb3b 50%, #f44336 100%); position: relative; overflow: hidden;">
<div style="position: absolute; bottom: 0; left: 10px; width: 80px; height: 40px; background: white; border-radius: 80px 80px 0 0;"></div>
<div style="position: absolute; bottom: 0; left: 50%; width: 2px; height: 40px; background: #333; transform-origin: bottom; transform: rotate(-60deg);"></div>
</div>
<div style="font-size: 10px; font-weight: 900; color: #102646; margin-top: 5px; direction: ltr;">-68dBm (ممتاز)</div>
<div style="display: flex; justify-content: center; align-items: flex-end; gap: 2px; margin-top: 4px;">
<div style="width: 4px; height: 6px; background: #0056b3;"></div>
<div style="width: 4px; height: 10px; background: #0056b3;"></div>
<div style="width: 4px; height: 14px; background: #0056b3;"></div>
<div style="width: 4px; height: 18px; background: #ccc;"></div>
</div>
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
<div class="nav-item clickable">⚙️<br>الإعدادات</div>
<div class="nav-item clickable">🎡<br>العجلة</div>
<div class="nav-item clickable">
<div class="bot-bg"><img src="data:image/png;base64,{robot_head}" style="width:32px;"></div>
المساعد
</div>
<div class="nav-item active clickable">🏠<br>الرئيسية</div>
<div class="nav-item clickable">🎁<br>الألعاب</div>
</div>
""", unsafe_allow_html=True)
