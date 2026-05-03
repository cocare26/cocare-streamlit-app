import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - تصفير الـ Padding الافتراضي لـ Streamlit
st.markdown("""
<style>
/* تصفير المسافات الإضافية التي يضعها ستريمليت في الأعلى */
.block-container {
    padding-top: 2rem !important; /* مسافة بسيطة جداً ليتنفس الكارد */
    padding-bottom: 0rem !important;
}

/* إخفاء الهيدر تماماً */
[data-testid="stHeader"] {
    display: none !important;
}

/* 📱 خلفية التطبيق */
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 الكارد الرئيسي (350px) كما طلبت */
.main .block-container {
    max-width: 350px !important;
    margin: auto !important;
    background: linear-gradient(160deg, #d6ecff 0%, #eaf6ff 100%);
    border-radius: 42px;
    padding: 30px !important; /* المسافة الداخلية المعتمدة */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

/* إخفاء الفوتر */
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
            max-width: 290px; 
            display: flex;
            flex-direction: column;
            height: 480px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px; /* المسافة المعتمدة */
            position: relative;
        }

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

        .report-textarea {
            width: 100%;
            height: 240px;
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

        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;
            border-radius: 100px;
            width: 100%;
            padding: 14px 22px;
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
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Report a Problem</h2>
        </div>

        <textarea class="report-textarea" placeholder="How can we help?"></textarea>

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
