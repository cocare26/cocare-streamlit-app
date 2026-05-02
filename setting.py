import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 
st.set_page_config(page_title="Settings", layout="centered")

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS
st.markdown("""
<style>
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
}

[data-testid="stAppViewContainer"] { 
    background: #eef2f7; 
}

/* البوكس الرئيسي */
.block-container {
    max-width: 80% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 30px 40px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* تصميم الأزرار النحيفة */
div.stButton > button {
    width: 100% !important;
    height: 55px !important; 
    border-radius: 100px !important; 
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 35px !important;
    padding-right: 35px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    transition: 0.3s;

/* 🎯 ألوان أساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* --- تصغير كلمة Settings لتصل لـ 50 بكسل --- */
.settings-header {
    color: #000000 !important; 
    font-weight: 900 !important;
    font-size: 50px !important; /* الحجم الجديد المطلوب */
    margin: 0 !important;
    flex-grow: 1;
    text-align: center;
    padding-left: 50px; 
    line-height: 1.2;
/* 📦 الكارد الرئيسي */
.block-container{
    max-width:420px;
    margin:auto;
    padding:25px 30px;

    background:linear-gradient(160deg,
        var(--bg1) 0%,
        var(--bg2) 45%,
        var(--bg3) 100%
    );

    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

/* 🧠 العناوين */
h1, h2, h3{
    color:var(--navy);
    text-align:center;
    font-weight:900;
}

/* 🧾 Inputs */
div[data-testid="stTextInput"] input{
    border-radius:25px;
    height:44px;
    border:none !important;
    outline:none !important;
    padding-left:16px;
    background:rgba(255,255,255,0.95);
}

/* سهم الرجوع متناسب مع العنوان الجديد */
.back-arrow {
    font-size: 40px !important; 
    font-weight: 900 !important; 
    color: #000000 !important; 
/* 📍 Select */
div[data-testid="stSelectbox"] div{
    border-radius:25px;
}

/* 🔘 الأزرار الأساسية */
div.stButton > button{
    width:100%;
    height:46px;
    border-radius:25px;
    border:none;

    background:linear-gradient(90deg,
        var(--accent),
        var(--accent2)
    );

    color:white;
    font-weight:bold;

    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

/* ✨ hover */
div.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 18px rgba(0,0,0,.2);
}

/* 🤍 زر ثانوي */
div.stButton:nth-of-type(1) > button{
    background:white;
    color:var(--navy);
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

.settings-item {
    background: white;
    border-radius: 25px;
    padding: 12px 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}
.settings-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,.15);
}
.settings-item-left {
    display: flex;
    align-items: center;
    gap: 15px;
}
.settings-item-icon {
    font-size: 20px;
    color: var(--navy);
}
.settings-item-text {
    font-weight: bold;
    color: var(--navy);
}
.settings-item-arrow {
    font-size: 20px;
    color: #ccc;
}
.settings-group {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin-top: 20px;
}
.settings-group-item {
    flex: 1;
    background: white;
    border-radius: 25px;
    padding: 12px 0;
    text-align: center;
    font-weight: bold;
    color: var(--navy);
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}
.settings-group-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,.15);
}
.settings-group-item-icon {
    font-size: 20px;
    margin-bottom: 5px;
    color: var(--navy);
}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    # هيدر الصفحة
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 30px; padding-left: 20px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
components.html("""
<!DOCTYPE html>
<html>
<head>
    <title>Settings</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <div class="block-container">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <a href="/?page=employee" style="text-decoration: none; color: var(--navy); font-size: 24px; margin-right: 10px;"><i class="fas fa-arrow-left"></i></a>
            <h3 style="margin: 0;">Settings</h3>
        </div>

        <div class="settings-item" onclick="window.location.href=\'/?page=change_password\'" >
            <div class="settings-item-left">
                <span class="settings-item-icon"><i class="fas fa-lock"></i></span>
                <span class="settings-item-text">Change Password</span>
            </div>
            <span class="settings-item-arrow"><i class="fas fa-chevron-right"></i></span>
        </div>

        <div class="settings-item" onclick="window.location.href=\'/?page=change_language\'" >
            <div class="settings-item-left">
                <span class="settings-item-icon"><i class="fas fa-globe"></i></span>
                <span class="settings-item-text">Change Language</span>
            </div>
            <span class="settings-item-arrow"><i class="fas fa-chevron-right"></i></span>
        </div>

        <div class="settings-item" onclick="window.location.href=\'/?page=rate_app\'" >
            <div class="settings-item-left">
                <span class="settings-item-icon"><i class="fas fa-star"></i></span>
                <span class="settings-item-text">Rate App</span>
            </div>
            <span class="settings-item-arrow"><i class="fas fa-chevron-right"></i></span>
        </div>

        <div class="settings-item" onclick="window.location.href=\'/?page=logout\'" >
            <div class="settings-item-left">
                <span class="settings-item-icon"><i class="fas fa-sign-out-alt"></i></span>
                <span class="settings-item-text">Log Out</span>
            </div>
            <span class="settings-item-arrow"><i class="fas fa-chevron-right"></i></span>
        </div>

        <div class="settings-group">
            <div class="settings-group-item" onclick="window.location.href=\'/?page=report_problem\'" >
                <span class="settings-group-item-icon"><i class="fas fa-exclamation-triangle"></i></span>
                <span>Report a Problem</span>
            </div>
            <div class="settings-group-item" onclick="window.location.href=\'/?page=contact_us\'" >
                <span class="settings-group-item-icon"><i class="fas fa-envelope"></i></span>
                <span>Contact Us</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار
    def make_btn(emoji, label, page, gap_size):
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # الأزرار بالمسافات الأصلية
    make_btn("🔒", "Change Password", "password", gap_size=130)
    make_btn("🌐", "Change Language", "language", gap_size=130)
    make_btn("⭐", "Rate App", "rate", gap_size=145)
    make_btn("🚪", "Log Out", "main", gap_size=145)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# الشاشات الفرعية
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black;'>Change Password</h1>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black;'>Change Language</h1>", unsafe_allow_html=True)
    </div>
</body>
</html>
""", height=700)
