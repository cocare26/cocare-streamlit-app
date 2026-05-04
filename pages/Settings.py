import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="الإعدادات", layout="centered")

st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction: rtl; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}
#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
}
</style>
""", unsafe_allow_html=True)

components.html("""
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body { margin:0; font-family:Arial; }

.main-wrapper {
    max-width:380px;
    margin:auto;
}

.header-container {
    text-align:center;
    margin-bottom:30px;
    position:relative;
}

.back-icon {
    position:absolute;
    right:0;
    font-size:28px;
    cursor:pointer;
}

.setting-item {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    cursor:pointer;
}

.item-right { display:flex; gap:12px; }

.bottom-row {
    display:flex;
    gap:10px;
    margin-top:40px;
}
.bottom-item {
    flex:1;
    background:white;
    border-radius:100px;
    padding:12px;
    text-align:center;
    cursor:pointer;
}
</style>
</head>

<body>
<div class="main-wrapper">

<div class="header-container">
<div class="back-icon" onclick="goPage('customer')">›</div>
<h2>الإعدادات</h2>
</div>

<div class="setting-item" onclick="goPage('Change_password-ar')">
<div class="item-right"><i class="fas fa-lock"></i> تغيير كلمة المرور</div>
<span>‹</span>
</div>

<div class="setting-item" onclick="goPage('Change_language-ar')">
<div class="item-right"><i class="fas fa-globe"></i> تغيير اللغة</div>
<span>‹</span>
</div>

<div class="setting-item" onclick="goPage('logout')">
<div class="item-right"><i class="fas fa-sign-out-alt"></i> تسجيل الخروج</div>
<span>‹</span>
</div>

<div class="bottom-row">
<div class="bottom-item" onclick="goPage('Report_Problem-ar')">الإبلاغ عن مشكلة</div>
<div class="bottom-item" onclick="goPage('Contact_Us-ar')">تواصل معنا</div>
</div>

</div>

<script>
function goPage(p){
    window.parent.location.search = "?page=" + p;
}
</script>

</body>
</html>
""", height=600)
