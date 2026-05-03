import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Report a Problem", layout="centered")

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

/* 📦 الكارد الرئيسي - تم تنحيف العرض إلى 310px */
.block-container{
    max-width:310px !important; 
    margin:auto !important;
    padding:25px !important;
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
            max-width: 260px; /* تنحيف المحتوى الداخلي */
            display: flex;
            flex-direction: column;
            height: 460px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 35px;
            position: relative;
        }

        /* 🔙 سهم الرجوع < */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 26px;
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 18px; /* تصغير الخط قليلاً ليتناسب مع النحافة */
            color: #0f2446;
        }

        /* 📝 صندوق النص */
        .report-textarea {
            width: 100%;
            height: 220px;
            border-radius: 25px;
            border: none;
            outline: none;
            padding: 15px;
            background: white;
            font-size: 13px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-family: inherit;
        }

        .report-textarea::placeholder {
            color: #888888;
        }

        /* 🔘 زر الإرسال */
        .btn-container {
            margin-top: auto;
            padding-bottom: 5px;
        }

        .send-btn {
            background: white;
            border-radius: 100px;
            width: 100%;
            padding: 10px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            transition: 0.3s;
            box-sizing: border-box;
        }

        .send-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }

        .send-btn span {
            color: #0f2446;
            font-weight: bold;
            font-size: 14px;
        }

        .send-btn i {
            color: #0f2446;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <a href="#" class="back-icon">&lt;</a>
            <h2 class="title">Report a Problem</h2>
        </div>

        <textarea class="report-textarea" placeholder="I need help"></textarea>

        <div class="btn-container">
            <button class="send-btn" onclick="alert('Report Sent!')">
                <i class="fas fa-paper-plane"></i>
                <span>Send Report</span>
            </button>
        </div>
    </div>
</body>
</html>
""", height=480)
