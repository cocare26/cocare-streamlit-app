import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Employee Dashboard", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background:#eef2f7; }
.block-container { padding-top:10px; max-width:520px; }
header, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<style>
body{font-family:Arial}
</style>
</head>

<body>

<h2>مشاكل الشبكة</h2>

<p>نسبة المشاكل: 4.5%</p>

<h3>سجل التنبيهات والمشاكل</h3>

<p>❗ مشكلة - بطء إنترنت</p>
<p>⚠️ داخلي - مشكلة بالشبكة</p>
<p>🌐 خارجي - من مزود الخدمة</p>

<h3>مؤشرات الأداء</h3>
<p>متوسط التأخير</p>
<p>فقدان الحزم</p>

<h3>موظف الشهر</h3>
<p>أحمد علي</p>

</body>
</html>
""", height=820)
