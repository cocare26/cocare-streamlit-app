import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="تغيير اللغة", layout="centered")

# تأكد من عدم وجود فراغات غريبة في الـ CSS
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:rtl; }
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff) !important;
    font-family:'Segoe UI';
}
#MainMenu, header, footer { visibility:hidden; }
.block-container {
    max-width:420px;
    margin:auto;
    padding:30px 20px;
    background: white;
    border-radius:50px;
    box-shadow:0 15px 45px rgba(0,0,0,.1);
    min-height:620px;
    margin-top: 60px;
}
.header { position:relative; text-align:center; margin-bottom:40px; }
.back-style { position:absolute; right:0; top:0; }
.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:black !important;
    font-size:30px !important;
    border:none !important;
}
.title-text { font-size:22px; font-weight:900; color:#102646; }
</style>
""", unsafe_allow_html=True)

# الهيدر
st.markdown('<div class="header">', unsafe_allow_html=True)
st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("›"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# المكونات
components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<style>
body { margin:0; font-family:'Segoe UI'; display:flex; justify-content:center; background: transparent; }
.wrapper { width:100%; max-width:380px; }
.item {
    display:flex; justify-content:space-between; align-items:center;
    background:white; border-radius:100px; padding:14px 22px;
    margin-bottom:15px; box-shadow:0 4px 12px rgba(0,0,0,0.08);
    color:#102646; font-weight:800; cursor: pointer; border: 1px solid #f0f0f0;
}
.item:hover { transform:translateY(-2px); border-color: #2f80ed; }
</style>
</head>
<body>
<div class="wrapper">
    <div class="item" onclick="window.parent.history.back();">
        <span>🌐 العربية</span>
        <span>✔</span>
    </div>
    <div class="item" onclick="window.open('/Settings', '_top');">
        <span>🌐 English</span>
        <span>‹</span>
    </div>
</div>
</body>
</html>
""", height=400)
