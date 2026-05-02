import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Password", layout="centered")

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

        /* 💊 تصميم بوكس الإدخال الأبيض (الكبسولة) */
        .input-capsule {
            background: white;
            border-radius: 100px;
            padding: 12px 20px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }

        .input-capsule i.field-icon {
            color: #0f2446;
            margin-right: 12px;
            font-size: 18px;
        }

        .input-capsule input {
            border: none;
            outline: none;
            flex-grow: 1;
            font-size: 15px;
            color: #0f2446;
            background: transparent;
        }

        .input-capsule i.toggle-eye {
            color: #ccc;
            cursor: pointer;
            margin-left: 10px;
        }

        /* 🔘 زر الحفظ */
        .save-btn-container {
            display: flex;
            justify-content: center;
            margin-top: 25px;
        }

        .save-btn {
            background: linear-gradient(90deg, #2f80ed, #1c6fa4);
            color: white;
            border: none;
            padding: 12px 50px;
            border-radius: 100px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 0 6px 15px rgba(47, 128, 237, 0.3);
            transition: 0.3s;
        }

        .save-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(47, 128, 237, 0.4);
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <a href="#" class="back-icon"><i class="fas fa-arrow-left"></i></a>
            <h2 class="title">Change Password</h2>
        </div>

        <!-- كلمة السر الحالية -->
        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="Current Password">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <!-- كلمة السر الجديدة -->
        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="New Password">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <!-- إعادة كتابة كلمة السر الجديدة -->
        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="Re-write Password">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <!-- زر الحفظ في المنتصف -->
        <div class="save-btn-container">
            <button class="save-btn">Save</button>
        </div>
    </div>
</body>
</html>
""", height=500)
