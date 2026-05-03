import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Rate App", layout="centered")

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

/* 📦 الكارد الرئيسي - تم تقليل العرض ليكون أنحف (350px) */
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
        
        .main-wrapper {
            width: 100%;
            max-width: 290px; /* تقليل عرض المحتوى الداخلي */
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 30px;
            position: relative;
        }

        /* 🔙 سهم الرجوع العلوي < */
        .back-icon {
            position: absolute;
            left: 0;
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

        /* ⚪ بوكس مستطيل أبيض بحواف دائرية */
        .store-item {
            background: white;
            border-radius: 100px;
            padding: 12px 20px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }

        .store-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }

        .store-item-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .store-item-icon {
            font-size: 18px;
            color: #0f2446;
            width: 25px;
            text-align: center;
        }

        .store-item-text {
            font-weight: bold;
            color: #0f2446;
            font-size: 14px;
        }

        /* ⬅️ الرمز < بدل السهم في الأزرار */
        .store-item-arrow {
            font-size: 18px;
            font-weight: bold;
            color: #0f2446; /* تغيير اللون ليكون متناسقاً مع التصميم */
            transform: rotate(180deg); /* تدوير الرمز ليشير لليمين */
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الرأس -->
        <div class="header-container">
            <a href="#" class="back-icon">&lt;</a>
            <h2 class="title">Rate App</h2>
        </div>

        <!-- Google Play -->
        <div class="store-item" onclick="window.open('https://play.google.com/store/apps', '_blank')">
            <div class="store-item-left">
                <span class="store-item-icon"><i class="fab fa-google-play"></i></span>
                <span class="store-item-text">Google Play Store</span>
            </div>
            <span class="store-item-arrow">&lt;</span>
        </div>

        <!-- App Store -->
        <div class="store-item" onclick="window.open('https://apps.apple.com', '_blank')">
            <div class="store-item-left">
                <span class="store-item-icon"><i class="fab fa-apple"></i></span>
                <span class="store-item-text">Apple App Store</span>
            </div>
            <span class="store-item-arrow">&lt;</span>
        </div>

        <!-- Huawei -->
        <div class="store-item" onclick="window.open('https://appgallery.huawei.com', '_blank')">
            <div class="store-item-left">
                <span class="store-item-icon"><i class="fas fa-mobile-alt"></i></span>
                <span class="store-item-text">Huawei AppGallery</span>
            </div>
            <span class="store-item-arrow">&lt;</span>
        </div>
    </div>
</body>
</html>
""", height=400)import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Rate App", layout="centered")

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

/* 📦 الكارد الرئيسي - تم تقليل العرض ليكون أنحف (350px) */
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
        
        .main-wrapper {
            width: 100%;
            max-width: 290px; /* تقليل عرض المحتوى الداخلي */
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 30px;
            position: relative;
        }

        /* 🔙 سهم الرجوع العلوي < */
        .back-icon {
            position: absolute;
            left: 0;
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

        /* ⚪ بوكس مستطيل أبيض بحواف دائرية */
        .store-item {
            background: white;
            border-radius: 100px;
            padding: 12px 20px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }

        .store-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }

        .store-item-left {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .store-item-icon {
            font-size: 18px;
            color: #0f2446;
            width: 25px;
            text-align: center;
        }

        .store-item-text {
            font-weight: bold;
            color: #0f2446;
            font-size: 14px;
        }

        /* ⬅️ الرمز < بدل السهم في الأزرار */
        .store-item-arrow {
            font-size: 18px;
            font-weight: bold;
            color: #0f2446; /* تغيير اللون ليكون متناسقاً مع التصميم */
            transform: rotate(180deg); /* تدوير الرمز ليشير لليمين */
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الرأس -->
        <div class="header-container">
            <a href="#" class="back-icon">&lt;</a>
            <h2 class="title">Rate App</h2>
        </div>

        <!-- Google Play -->
        <div class="store-item" onclick="window.open('https://play.google.com/store/apps', '_blank')">
            <div class="store-item-left">
                <span class="store-item-icon"><i class="fab fa-google-play"></i></span>
                <span class="store-item-text">Google Play Store</span>
            </div>
            <span class="store-item-arrow">&lt;</span>
        </div>

        <!-- App Store -->
        <div class="store-item" onclick="window.open('https://apps.apple.com', '_blank')">
            <div class="store-item-left">
                <span class="store-item-icon"><i class="fab fa-apple"></i></span>
                <span class="store-item-text">Apple App Store</span>
            </div>
            <span class="store-item-arrow">&lt;</span>
        </div>

        <!-- Huawei -->
        <div class="store-item" onclick="window.open('https://appgallery.huawei.com', '_blank')">
            <div class="store-item-left">
                <span class="store-item-icon"><i class="fas fa-mobile-alt"></i></span>
                <span class="store-item-text">Huawei AppGallery</span>
            </div>
            <span class="store-item-arrow">&lt;</span>
        </div>
    </div>
</body>
</html>
""", height=400)
