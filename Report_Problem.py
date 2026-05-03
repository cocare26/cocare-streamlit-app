import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - المقاسات الموحدة 350px
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

/* إخفاء الزوائد لجمالية التصميم */
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
        
        /* الحاوية الداخلية الموحدة (290px x 480px) */
        .main-wrapper {
            width: 100%;
            max-width: 290px;
            display: flex;
            flex-direction: column;
            height: 480px;
        }

        /* الرأس الموحد */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px; /* المسافة الموحدة 40px */
            position: relative;
        }

        /* 🔙 رمز الرجوع الموحد < */
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

        /* العنوان الموحد */
        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px;
            color: #0f2446;
        }

        /* 📝 صندوق النص (التعديل ليناسب المساحة الموحدة) */
        .report-textarea {
            width: 100%;
            height: 240px; /* زيادة الارتفاع قليلاً لملء الفراغ بشكل متناسق */
            border-radius: 25px;
            border: none;
            outline: none;
            padding: 18px;
            background: white;
            font-size: 14px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-family: inherit;
        }

        .report-textarea::placeholder {
            color: #888888;
        }

        /* 🔘 زر الإرسال الموحد (نفس نمط الكبسولة) */
        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;
            border-radius: 100px;
            width: 100%;
            padding: 14px 22px; /* بادينج موحد مثل الكبسولات */
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
            font-weight: 700;
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
        <!-- الهيدر الموحد -->
        <div class="header-container">
            <a href="#" class="back-icon">&lt;</a>
            <h2 class="title">Report a Problem</h2>
        </div>

        <!-- صندوق النص -->
        <textarea class="report-textarea" placeholder="I need help"></textarea>

        <!-- زر الإرسال بنمط الكبسولة -->
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
