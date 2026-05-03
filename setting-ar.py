import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="الإعدادات", layout="centered")

# CSS الخارجي (تنسيق الكارد الرئيسي)
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* الكارد الرئيسي الموحد بمقاس 350px */
.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    direction: rtl; /* اتجاه المحتوى للعربية */
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>

body{
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin:0;
    display:flex;
    justify-content:center;
    background:transparent;
}

.main-wrapper{
    width:100%;
    max-width:290px;
    display:flex;
    flex-direction:column;
    height:480px;
}

/* الرأس (Header) */
.header-container{
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:35px;
    position:relative;
}

.back-icon{
    position:absolute;
    right:0; /* وضع السهم على اليمين في العربي */
    font-size:28px;
    font-weight:bold;
    color:#0f2446;
    text-decoration:none;
}

.title{
    margin:0;
    font-weight:900;
    font-size:22px;
    color:#0f2446;
}

/* عناصر الإعدادات (الأزرار) */
.setting-item{
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.3s;
    text-decoration:none;
}

.setting-item i{
    color:#0f2446;
    font-size:16px;
    margin-left: 15px; /* مسافة بين الأيقونة والنص */
}

.setting-text{
    flex:1;
    text-align:right;
    font-size:14px;
    font-weight:700;
    color:#0f2446;
}

.setting-item .arrow{
    margin-right:10px;
    color:#0f2446;
    font-weight:bold;
    font-size: 18px;
}

.setting-item:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* الصف السفلي (أزرار التواصل) */
.bottom-row{
    margin-top:auto;
    display:flex;
    gap:10px;
}

.bottom-row .setting-item{
    flex:1;
    padding:12px 10px;
    flex-direction: column; /* جعل الأيقونة فوق النص لضمان المساحة */
    border-radius: 20px;
    text-align: center;
}

.bottom-row .setting-text{
    text-align: center;
    margin: 5px 0 0 0;
    font-size: 12px;
}

.bottom-row i{
    margin: 0;
}

</style>
</head>

<body>

<div class="main-wrapper">

    <div class="header-container">
        <a href="#" class="back-icon">&gt;</a>
        <h2 class="title">الإعدادات</h2>
    </div>

    <!-- تغيير كلمة المرور -->
    <div class="setting-item">
        <i class="fas fa-lock"></i>
        <span class="setting-text">تغيير كلمة المرور</span>
        <span class="arrow">‹</span>
    </div>

    <!-- تغيير اللغة -->
    <div class="setting-item">
        <i class="fas fa-globe"></i>
        <span class="setting-text">تغيير اللغة</span>
        <span class="arrow">‹</span>
    </div>

    <!-- تقييم التطبيق -->
    <div class="setting-item">
        <i class="fas fa-star"></i>
        <span class="setting-text">تقييم التطبيق</span>
        <span class="arrow">‹</span>
    </div>

    <!-- تسجيل الخروج -->
    <div class="setting-item">
        <i class="fas fa-sign-out-alt"></i>
        <span class="setting-text">تسجيل الخروج</span>
        <span class="arrow">‹</span>
    </div>

    <div class="bottom-row">
        <!-- الإبلاغ عن مشكلة -->
        <div class="setting-item">
            <i class="fas fa-exclamation-triangle"></i>
            <span class="setting-text">بلاغ عن مشكلة</span>
        </div>

        <!-- تواصل معنا -->
        <div class="setting-item">
            <i class="fas fa-envelope"></i>
            <span class="setting-text">تواصل معنا</span>
        </div>
    </div>

</div>

</body>
</html>
""", height=500)
