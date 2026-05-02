import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Language", layout="centered")

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

/* 📦 الكارد الرئيسي */
.block-container{
    max-width:450px !important;
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
            max-width: 380px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
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
            font-size: 24px;
            color: #0f2446;
        }

        /* 💊 تصميم الكبسولة البيضاء الطويلة */
        .language-capsule {
            background: white;
            border-radius: 100px;
            padding: 15px 25px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between; /* توزيع العناصر (الاسم يسار والعلامة يمين) */
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }

        .language-capsule:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.1);
        }

        .left-content {
            display: flex;
            align-items: center;
            gap: 15px;
        }

        .icon {
            color: #0f2446;
            font-size: 18px;
        }

        .label {
            color: #0f2446;
            font-weight: 700;
            font-size: 16px;
        }

        /* علامة الصح والسهم في أقصى اليمين */
        .status-mark {
            font-size: 18px;
            font-weight: bold;
        }
        
        .check { color: #2f80ed; } /* لون الصح */
        .arrow { color: #0f2446; font-size: 22px; } /* لون وحجم السهم */
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <a href="#" class="back-icon"><i class="fas fa-arrow-left"></i></a>
            <h2 class="title">Change Language</h2>
        </div>

        <!-- كبسولة الإنجليزية مع علامة صح -->
        <a href="#" class="language-capsule">
            <div class="left-content">
                <div class="icon"><i class="fas fa-globe"></i></div>
                <div class="label">English</div>
            </div>
            <div class="status-mark check"><i class="fas fa-check"></i></div>
        </a>

        <!-- كبسولة العربية مع سهم -->
        <a href="#" class="language-capsule">
            <div class="left-content">
                <div class="icon"><i class="fas fa-globe"></i></div>
                <div class="label">العربية</div>
            </div>
            <div class="status-mark arrow">›</div>
        </a>
    </div>
</body>
</html>
""", height=500)
