import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Change Language", layout="centered")

# 2. التنسيق العام (CSS) - بناءً على "المسطرة" المعتمدة
st.markdown("""
<style>
/* 🎨 الألوان المعتمدة */
:root {
    --navy: #0f2446;
    --accent: #2f80ed;
    --bg-grad: linear-gradient(160deg, #d6ecff 0%, #eaf6ff 100%);
}

/* 📱 خلفية التطبيق */
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 الكارد الرئيسي (Main Container) */
.block-container {
    max-width: 350px !important; /* العرض الموحد */
    margin: auto !important;
    padding: 30px !important;    /* المسافة الداخلية الموحدة */
    background: var(--bg-grad);
    border-radius: 42px;         /* الحواف الدائرية */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15); /* الظل المعتمد */
    margin-top: 50px !important;
}

/* إخفاء عناصر ستريمليت الزائدة */
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
        
        /* 📏 الحاوية الداخلية (Main Wrapper) */
        .main-wrapper {
            width: 100%;
            max-width: 290px;
            display: flex;
            flex-direction: column;
            height: 480px; /* الارتفاع المعتمد */
        }

        /* 🔝 الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px; /* المسافة السفلية الموحدة */
            position: relative;
        }

        /* 🔙 أيقونة الرجوع الموحدة < */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 28px; /* الحجم المعتمد */
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        /* 🏷️ العنوان (Title) */
        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px; /* الحجم المعتمد */
            color: #0f2446;
        }

        /* 💊 كبسولات الخيارات (Language Capsules) */
        .capsule {
            background: white;
            border-radius: 100px; /* دائرية تماماً */
            padding: 14px 22px;   /* البادينج المعتمد */
            margin-bottom: 15px;  /* المسافة بين الكبسولات */
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
        }

        .capsule:hover {
            transform: translateY(-2px);
        }

        .left-content {
            display: flex;
            align-items: center;
            gap: 12px; /* الفراغ المعتمد (Gap) */
        }

        /* أيقونة الكرة الأرضية */
        .globe-icon {
            font-size: 16px; /* الحجم المعتمد */
            color: #0f2446;
            width: 20px;
            text-align: center;
        }

        .lang-text {
            color: #0f2446;
            font-weight: 700;
            font-size: 14px; /* الحجم المعتمد */
        }

        /* أيقونة الصح */
        .check-icon {
            color: #2f80ed; /* اللون الأزرق المعتمد (Accent) */
            font-size: 18px; /* الحجم المعتمد */
            visibility: hidden; /* مخفية افتراضياً وتظهر للمختار */
        }

        .active .check-icon {
            visibility: visible;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الهيدر -->
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Change Language</h2>
        </div>

        <!-- الخيارات -->
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
                <span class="lang-text">English (US)</span>
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
    </div>
</body>
</html>
""", height=500)
