import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - العرض الجديد 290px
st.markdown("""
<style>
/* 🎯 ألوان أساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --bg-grad: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
}

/* تصفير المسافات العلوية لستريمليت */
[data-testid="stHeader"] {display: none !important;}
.block-container {
    padding-top: 2rem !important;
    max-width: 290px !important; /* 📏 العرض الذي طلبته */
    margin: auto !important;
}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 الكارد الرئيسي */
.main .block-container {
    background: var(--bg-grad);
    border-radius: 42px;
    padding: 25px !important; /* تقليل المسافة الداخلية لتناسب العرض الصغير */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

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
        
        .main-wrapper {
            width: 100%;
            max-width: 240px; /* تناسق المحتوى الداخلي */
            display: flex;
            flex-direction: column;
            height: 460px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 25px;
            position: relative;
        }

        .back-icon {
            position: absolute;
            left: 0;
            font-size: 24px;
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 18px; /* تصغير الخط ليناسب العرض */
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
            font-size: 14px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06);
            font-family: inherit;
        }

        .report-textarea::placeholder {
            color: #888888;
        }

        .btn-container {
            margin-top: auto;
            padding-bottom: 5px;
        }

        /* 🔘 زر الإرسال الكبسولة */
        .send-btn {
            background: white;
            border-radius: 100px;
            width: 100%;
            padding: 12px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            box-sizing: border-box;
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
            <h2 class="title">Report Problem</h2>
        </div>

        <textarea class="report-textarea" placeholder="I need help..."></textarea>

        <div class="btn-container">
            <button class="send-btn" onclick="alert('Report Sent!')">
                <i class="fas fa-paper-plane"></i>
                <span>Send Report</span>
            </button>
        </div>
    </div>
</body>
</html>
""", height=500)
