import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="تغيير اللغة", layout="centered")

# 2. التنسيق العام (CSS)
st.markdown("""
<style>
/* 🎯 ألوان أساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 الكارد الرئيسي - العرض الموحد 350px */
.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة (HTML/JS) باللغة العربية
components.html("""
<!DOCTYPE html>
<html dir="rtl"> <!-- تفعيل الاتجاه من اليمين لليسار -->
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: transparent;
            margin: 0;
            display: flex;
            justify-content: center;
        }
        
        .main-wrapper {
            width: 100%;
            max-width: 290px;
            display: flex;
            flex-direction: column;
            height: 480px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;
            position: relative;
        }

        /* 🔙 رمز الرجوع الموحد > للعربية على اليمين */
        .back-icon {
            position: absolute;
            right: 0;
            font-size: 28px;
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px;
            color: #0f2446;
        }

        /* ⚪ كبسولة اللغة */
        .language-capsule {
            background: white;
            border-radius: 100px;
            padding: 14px 22px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }

        .language-capsule:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        }

        .right-content {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .icon {
            color: #0f2446;
            font-size: 16px;
        }

        .label {
            color: #0f2446;
            font-weight: 700;
            font-size: 14px;
        }

        /* علامة الصح والرمز الجديد < */
        .status-mark {
            font-size: 18px;
            font-weight: bold;
            display: flex;
            align-items: center;
        }
        
        .check { color: #2f80ed; } 
        
        .arrow-icon { 
            color: #0f2446; 
            font-size: 22px; 
            line-height: 1;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <a href="#" class="back-icon">&gt;</a>
            <h2 class="title">تغيير اللغة</h2>
        </div>

        <!-- العربية (مختارة) -->
        <a href="#" class="language-capsule">
            <div class="right-content">
                <div class="icon"><i class="fas fa-globe"></i></div>
                <div class="label">العربية</div>
            </div>
            <div class="status-mark check"><i class="fas fa-check"></i></div>
        </a>

        <!-- English -->
        <a href="#" class="language-capsule">
            <div class="right-content">
                <div class="icon"><i class="fas fa-globe"></i></div>
                <div class="label">English</div>
            </div>
            <div class="status-mark">
                <span class="arrow-icon">&lt;</span>
            </div>
        </a>
    </div>
</body>
</html>
""", height=500)
