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
# دالة الصور
# =====================================
def get_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

robot_full = get_base64("robot_full.png.jpeg")
robot_head = get_base64("robot_head.png")

# =====================================
# CSS (RTL + إصلاحات)
# =====================================
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

.card {
    background:white;
    border-radius:24px;
    padding:14px;
    margin-bottom:12px;
    box-shadow:0 6px 18px rgba(0,0,0,.08);
}

.title {
    font-size:17px;
    font-weight:900;
    margin: 8px 0;
    color:#102646;
}

.grid4 { 
    display:grid; 
    grid-template-columns:repeat(4,1fr); 
    gap:8px; 
    margin:20px 0;
}

.mini {
    background:white;
    border-radius:20px;
    padding:12px 5px;
    text-align:center;
}

.nav {
    margin-top:12px;
    display:grid;
    grid-template-columns:repeat(5,1fr);
    text-align:center;
}

.bot-bg {
    width:55px;
    height:55px;
    background:white;
    border-radius:14px;
    margin:auto;
    display:flex;
    align-items:center;
    justify-content:center;
}
</style>
""", unsafe_allow_html=True)

# =====================================
# 1. الملف الشخصي
# =====================================
st.markdown(f"""
<div class="card">
<div style="display:flex; align-items:center;">
    <img src="data:image/png;base64,{robot_full}" width="110">
    <div>
        <div style="font-size:24px; font-weight:900;">مرحباً</div>
        <div>+962 79 123 4567</div>
        <div>صالح حتى: 25 مايو 2026</div>
    </div>
</div>

<div style="margin-top:12px; background:#eef5ff; padding:10px; border-radius:18px;">
📍 الموقع: عمّان
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 2. الرصيد
# =====================================
st.markdown("""
<div class="title">معلومات رقمك</div>
<div class="card">
<div>البيانات المتبقية</div>
<div style="font-size:40px; font-weight:900;">4.7 جيجابايت</div>
<div>من 6 جيجابايت</div>

<div style="margin-top:10px; height:8px; background:#dce8f7; border-radius:20px;">
<div style="width:78%; height:100%; background:#1567e0;"></div>
</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 3. الخدمات
# =====================================
st.markdown("""
<div class="grid4">
<div class="mini">📡<br>باقات الإنترنت</div>
<div class="mini">🌍<br>تجديد</div>
<div class="mini">💰<br>دولي</div>
<div class="mini">🔔<br>إشعارات</div>
</div>
""", unsafe_allow_html=True)

# =====================================
# 4. التقييم (بدون HTML خطير)
# =====================================
st.markdown('<div class="title">تقييم الخدمة</div>', unsafe_allow_html=True)

rating = st.radio(
    "قيّم الخدمة",
    ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"],
    horizontal=True
)

# =====================================
# 5. الشبكة
# =====================================
st.markdown("""
<div class="title">قوة الشبكة في منطقتك</div>
<div class="card">
📍 عمّان<br>
إشارة قوية جداً<br><br>

فقدان الحزم: 0%<br>
التذبذب: 19 ms
</div>
""", unsafe_allow_html=True)

# =====================================
# 6. الشريط السفلي
# =====================================
st.markdown(f"""
<div class="nav">
<div>⚙️<br>الإعدادات</div>
<div>🎡<br>حظك</div>
<div>
    <div class="bot-bg">
        <img src="data:image/png;base64,{robot_head}" width="35">
    </div>
    مساعد
</div>
<div>🏠<br>الرئيسية</div>
<div>🎁<br>ألعاب</div>
</div>
""", unsafe_allow_html=True)
