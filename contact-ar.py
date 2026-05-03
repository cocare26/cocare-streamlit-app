import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="تواصل معنا", layout="centered")

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

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 الكارد الرئيسي - المقاس الموحد (350px) */
.block-container {
    max-width: 350px !important;
    margin: auto !important;
    padding: 30px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة (HTML/JS) مع دعم العربية
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

        /* الرأس */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;
            position: relative;
        }

        /* 🔙 رمز الرجوع الموحد > (عكسته ليناسب العربية) */
        .back-icon {
            position: absolute;
            right: 0; /* أصبح على اليمين في العربية */
            font-size: 28px;
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px;
            color: #0f2446;
        }

        /* 💊 كبسولة الخيارات */
        .capsule {
            background: white;
            border-radius: 100px;
            padding: 14px 22px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            transition: 0.3s;
            cursor: pointer;
        }

        .capsule:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }

        .icon {
            margin-left: 12px; /* المسافة أصبحت لليسار لأن الأيقونة يمين النص */
            color: #0f2446;
            font-size: 16px;
            display: flex;
            align-items: center;
            width: 20px;
            justify-content: center;
        }

        .text {
            color: #0f2446;
            font-weight: 700;
            font-size: 14px;
            direction: ltr; /* لضمان بقاء الأرقام والإيميل بشكل صحيح من اليسار لليمين */
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الهيدر -->
        <div class="header-container">
            <div class="back-icon" onclick="goPage('settings-ar')">&gt;</div>
            <h2 class="title">تواصل معنا</h2>
        </div>

        <!-- كبسولة البريد الإلكتروني -->
        <div class="capsule" onclick="window.location.href='mailto:CoCare26@gmail.com'">
            <div class="icon"><i class="fas fa-envelope"></i></div>
            <div class="text">CoCare26@gmail.com</div>
        </div>

        <!-- كبسولة الهاتف -->
        <div class="capsule" onclick="window.location.href='tel:+962791234567'">
            <div class="icon"><i class="fas fa-phone"></i></div>
            <div class="text">+962 79 123 4567</div>
        </div>
    </div>

    <script>
    function goPage(p){
        window.top.location.href = "/?page=" + p;
    }
    </script>
</body>
</html>
""", height=500)
