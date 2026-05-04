import streamlit as st
import base64
import os

# 1. إعدادات الصفحة
st.set_page_config(page_title="CoCare Dashboard", page_icon="📱", layout="centered")

# 2. دالة التحويل (تأكدي من وجود الصور في GitHub بنفس الأسماء)
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

img_robot = get_base64("robot_full.png.jpeg")
img_head = get_base64("robot_head.png")

# 3. الـ CSS (تم فصله لضمان عدم حدوث Syntax Error)
style_code = f"""
<style>
    * {{ margin:0; padding:0; box-sizing:border-box; direction: rtl; text-align: right; }}
    html, body, [data-testid="stAppViewContainer"] {{ background:#f0f7ff; font-family:'Segoe UI', sans-serif; }}
    .block-container {{ max-width:430px; margin:auto; padding:20px; background:linear-gradient(180deg,#dff2ff 0%,#f4fbff 100%); border-radius:40px; }}
    .card {{ background:white; border-radius:24px; padding:15px; margin-bottom:12px; box-shadow:0 4px 12px rgba(0,0,0,0.05); }}
    .title {{ font-size:18px; font-weight:bold; color:#102646; margin:10px 0; }}
    .robot-img {{ width:100px; height:auto; margin-left:15px; filter: drop-shadow(0 5px 10px rgba(0,0,0,0.1)); }}
    .grid4 {{ display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin:15px 0; }}
    .mini {{ background:white; border-radius:18px; padding:10px; text-align:center; box-shadow:0 4px 10px rgba(0,0,0,0.05); font-size:11px; font-weight:bold; }}
    .nav {{ display:grid; grid-template-columns:repeat(5,1fr); text-align:center; margin-top:20px; color:#666; }}
    .bot-bg {{ width:50px; height:50px; background:white; border-radius:15px; margin:0 auto 5px; display:flex; align-items:center; justify-content:center; box-shadow:0 4px 8px rgba(0,0,0,0.1); }}
    .active {{ color:#0d69dd; font-weight:bold; }}
</style>
"""
st.markdown(style_code, unsafe_allow_html=True)

# 4. محتوى الصفحة (بناء العناصر تدريجياً لتجنب الأخطاء)
# القسم الأول: الترحيب
st.markdown(f"""
<div class="card">
    <div style="display:flex; align-items:center;">
        <img src="data:image/png;base64,{img_robot}" class="robot-img">
        <div>
            <div style="font-size:22px; font-weight:900; color:#102646;">أهلاً بك</div>
            <div style="font-size:14px; color:#555; direction:ltr;">+962 79 123 4567</div>
            <div style="font-size:13px; color:#777;">صلاحية الاشتراك: 25 مايو 2026</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# القسم الثاني: الرصيد
st.markdown("""
<div class="title">استهلاك البيانات</div>
<div class="card">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <div style="font-size:12px; color:#666;">المتبقي</div>
            <div style="font-size:32px; font-weight:900; color:#102646;">4.7 <span style="font-size:15px;">GB</span></div>
        </div>
        <div style="text-align:center; font-weight:bold; font-size:12px;">إجمالي: 6 GB</div>
    </div>
    <div style="background:#eee; height:8px; border-radius:10px; margin-top:10px; position:relative;">
        <div style="background:#1567e0; width:78%; height:100%; border-radius:10px; position:absolute; right:0;"></div>
    </div>
</div>
""", unsafe_allow_html=True)

# القسم الثالث: الأيقونات
st.markdown("""
<div class="grid4">
    <div class="mini">📡<br>الحزم</div>
    <div class="mini">🌍<br>التجديد</div>
    <div class="mini">💰<br>رصيد</div>
    <div class="mini">🔔<br>تنبيهات</div>
</div>
""", unsafe_allow_html=True)

# القسم الرابع: حالة الشبكة
st.markdown("""
<div class="title">حالة الشبكة</div>
<div class="card">
    <div style="display:flex; justify-content:space-between;">
        <div>
            <div style="font-weight:bold;">📍 عمان</div>
            <div style="color:green; font-size:13px;">التغطية متميزة</div>
        </div>
        <div style="font-size:12px; text-align:left;">-68 dBm</div>
    </div>
</div>
""", unsafe_allow_html=True)

# القسم الخامس: التنقل
st.markdown(f"""
<div class="nav">
    <div>⚙️<br><span style="font-size:10px;">الإعدادات</span></div>
    <div>🎡<br><span style="font-size:10px;">اربح</span></div>
    <div>
        <div class="bot-bg"><img src="data:image/png;base64,{img_head}" style="width:30px;"></div>
        <span style="font-size:10px;">المساعد</span>
    </div>
    <div class="active">🏠<br><span style="font-size:10px;">الرئيسية</span></div>
    <div>🎁<span style="font-size:10px;"><br>هدايا</span></div>
</div>
""", unsafe_allow_html=True)
