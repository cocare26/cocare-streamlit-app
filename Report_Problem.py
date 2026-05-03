import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Change Language", layout="centered")

# 2. التنسيق العام (CSS) - المقاس الموحد الجديد 290px
st.markdown("""
<style>
/* 🎯 الألوان المعتمدة */
:root {
    --navy: #0f2446;
    --accent: #2f80ed;
    --bg-grad: linear-gradient(160deg, #d6ecff 0%, #eaf6ff 100%);
}

/* 📱 خلفية التطبيق */
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 الكارد الرئيسي - العرض المحدث (290px) */
.block-container {
    max-width: 290px !important; 
    margin: auto !important;
    padding: 20px !important;    /* تقليل المسافات الجانبية لتناسب نحافة الكارد */
    background: var(--bg-grad);
    border-radius: 42px;         
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-top: 50px !important;
}

/* إخفاء عناصر ستريمليت */
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة (HTML/JS)
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
        }
        
        /* 📏 الحاوية الداخلية (تم تصغيرها لتناسب الـ 290px) */
        .main-wrapper {
            width: 100%;
            max-width: 240px; 
            display: flex;
            flex-direction: column;
            height: 480px;
        }

        /* 🔝 الرأس */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 35px; 
            position: relative;
        }

        /* 🔙 أيقونة الرجوع < */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 24px; 
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
        }

        /* 🏷️ العنوان */
        .title {
            margin: 0;
            font-weight: 900;
            font-size: 17px; /* خط أصغر قليلاً ليناسب العرض النحيف */
            color: #0f2446;
        }

        /* 💊 الكبسولات */
        .capsule {
            background: white;
            border-radius: 100px;
            padding: 12px 16px; 
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06);
            cursor: pointer;
        }

        .left-content {
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .globe-icon {
            font-size: 14px;
            color: #0f2446;
            width: 16px;
        }

        .lang-text {
            color: #0f2446;
            font-weight: 700;
            font-size: 12.5px;
        }

        .check-icon {
            color: #2f80ed;
            font-size: 16px;
            visibility: hidden;
        }

        .active .check-icon {
            visibility: visible;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Change Language</h2>
        </div>

        <!-- خيارات اللغات -->
        <div class="capsule active">
            <div class="left-content">
                <i class="fas fa-globe globe-icon"></i>
                <span class="lang-text">English (UK)</span>
            </div>
            <i class="fas fa-check-circle check-icon"></i>
        </div>

        <div class="capsule">
            <div class="left-content">
                <i class="fas fa-globe globe-icon"></i>
                <span class="lang-text">Arabic (Jordan)</span>
            </div>
            <i class="fas fa-check-circle check-icon"></i>
        </div>
        
        <div class="capsule">
            <div class="left-content">
                <i class="fas fa-globe globe-icon"></i>
                <span class="lang-text">French (France)</span>
            </div>
            <i class="fas fa-check-circle check-icon"></i>
        </div>
    </div>
</body>
</html>
""", height=500)
