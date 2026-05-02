import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Contact Us", layout="centered")

# 2. التنسيق العام (CSS)
st.markdown("""
<style>
/* 🎯 ألوان أساسية */
:root {
    --navy: #0f2446;
    --bg1: #d6ecff;
    --bg2: #bfe3ff;
    --bg3: #eaf6ff;
}

/* 📱 جعل الخلفية تمتد لتغطية الشاشة بالكامل وتوسيط المحتوى */
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 الكارد الرئيسي مع توسيطه في منتصف الشاشة */
.block-container {
    max-width: 450px !important;
    margin: auto !important;
    padding: 30px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    
    /* توسيط المحتوى داخلياً */
    display: flex;
    flex-direction: column;
    justify-content: center;
}

/* تحسين شكل النصوص داخل المكون */
h2 {
    color: var(--navy);
    font-weight: 900;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة (HTML/JS) داخل كبسولة متوسطة
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: transparent;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100%;
        }
        
        .main-wrapper {
            width: 100%;
            max-width: 380px;
            text-align: center;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center; /* توسيط الهيدر */
            margin-bottom: 40px;
            position: relative;
        }

        .back-icon {
            position: absolute;
            left: 0;
            font-size: 24px;
            color: #0f2446;
            text-decoration: none;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 28px;
            color: #0f2446;
        }

        /* 💊 تصميم الكبسولة البيضاء الطويلة */
        .capsule {
            background: white;
            border-radius: 100px;
            padding: 18px 25px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            box-shadow: 0 6px 15px rgba(0,0,0,0.08);
            transition: 0.3s;
        }

        .capsule:hover {
            transform: translateY(-3px);
        }

        .icon {
            margin-right: 15px;
            color: #0f2446;
            font-size: 20px;
            display: flex;
            align-items: center;
        }

        .text {
            color: #0f2446;
            font-weight: 700;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الهيدر مع السهم على اليسار والعنوان في المنتصف -->
        <div class="header-container">
            <a href="#" class="back-icon"><i class="fas fa-arrow-left"></i></a>
            <h2 class="title">Contact Us</h2>
        </div>

        <!-- كبسولة الإيميل -->
        <div class="capsule">
            <div class="icon"><i class="fas fa-envelope"></i></div>
            <div class="text">Email: CoCare26@gmail.com</div>
        </div>

        <!-- كبسولة الهاتف -->
        <div class="capsule">
            <div class="icon"><i class="fas fa-phone"></i></div>
            <div class="text">Phone: +962 79 123 4567</div>
        </div>
    </div>
</body>
</html>
""", height=500)
