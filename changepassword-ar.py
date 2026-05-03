import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="تغيير كلمة المرور", layout="centered")

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

/* 📦 الكارد الرئيسي - مقاس موحد (350px) */
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
<html dir="rtl">
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
            margin-bottom: 35px;
            position: relative;
        }

        /* 🔙 سهم الرجوع الموحد > للعربية */
        .back-icon {
            position: absolute;
            right: 0;
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

        /* ⚪ بوكس الإدخال */
        .input-capsule {
            background: white;
            border-radius: 100px;
            padding: 10px 18px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        .input-capsule i.field-icon {
            color: #0f2446;
            margin-left: 12px;
            font-size: 16px;
        }

        .input-capsule input {
            border: none;
            outline: none;
            flex-grow: 1;
            font-size: 14px;
            color: #0f2446;
            background: transparent;
            text-align: right;
        }

        .input-capsule i.toggle-eye {
            color: #ccc;
            cursor: pointer;
            margin-right: 10px;
        }

        /* 🔘 زر الحفظ الأبيض */
        .save-btn-container {
            margin-top: auto;
            display: flex;
            justify-content: center;
            padding-bottom: 10px;
        }

        .save-box {
            background: white;
            border-radius: 100px;
            width: 100%;
            padding: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
            border: none;
        }

        .save-box span {
            color: #0f2446;
            font-weight: bold;
            font-size: 16px;
        }

        .save-box:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon" onclick="goPage('settings-ar')">&gt;</div>
            <h2 class="title">تغيير كلمة المرور</h2>
        </div>

        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="كلمة المرور الحالية">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="كلمة المرور الجديدة">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="تأكيد كلمة المرور">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <div class="save-btn-container">
            <button class="save-box" onclick="alert('تم حفظ كلمة المرور!')">
                <span>حفظ</span>
            </button>
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
