import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Password", layout="centered")

st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

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
            max-width: 290px; /* عرض المحتوى الداخلي ليتناسق مع الحجم الجديد */
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

        /* 🔙 تبديل السهم لرمز < */
        .back-icon {
            position: absolute;
            left: 0;
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
            margin-right: 12px;
            font-size: 16px;
        }

        .input-capsule input {
            border: none;
            outline: none;
            flex-grow: 1;
            font-size: 14px;
            color: #0f2446;
            background: transparent;
        }

        .input-capsule i.toggle-eye {
            color: #ccc;
            cursor: pointer;
            margin-left: 10px;
        }

        /* 📝 نص ريبورت باسورد */
        .report-text {
            text-align: center;
            color: white;
            font-size: 13px;
            margin-top: 5px;
            margin-bottom: 20px;
            cursor: pointer;
            font-weight: bold;
            text-shadow: 0px 1px 2px rgba(0,0,0,0.1);
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
            <div class="back-icon" onclick="goPage('settings')">&lt;</div>
            <h2 class="title">Change Password</h2>
        </div>

        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="Current Password">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="New Password">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <div class="input-capsule">
            <i class="fas fa-lock field-icon"></i>
            <input type="password" placeholder="Re-write New Password">
            <i class="fas fa-eye-slash toggle-eye"></i>
        </div>

        <div class="report-text">
            Report Password
        </div>

        <div class="save-btn-container">
            <button class="save-box" onclick="alert('Password Saved!')">
                <span>Save</span>
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
