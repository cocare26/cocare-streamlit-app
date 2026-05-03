import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Report a Problem", layout="centered")

# 🛠️ كود CSS لإجبار البوكس على النحافة القصوى
st.markdown("""
<style>
/* إزالة المسافات الجانبية من الحاوية الأساسية لستريمليت */
.main .block-container {
    max-width: 300px !important; 
    padding-left: 0px !important;
    padding-right: 0px !important;
    margin: auto !important;
}

/* 📦 الكارد الرئيسي - نحيف جداً (300px) */
[data-testid="stAppViewContainer"] .block-container {
    max-width: 300px !important;
    background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
    border-radius: 42px;
    padding: 20px !important;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-top: 50px !important;
}

/* إخفاء شريط التنقل العلوي لزيادة الجمالية */
header {visibility: hidden;}
footer {visibility: hidden;}

/* خلفية الصفحة العامة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
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
            max-width: 250px; /* المحتوى الداخلي نحيف جداً */
            display: flex;
            flex-direction: column;
            height: 450px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 30px;
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
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 18px;
            color: #0f2446;
        }

        /* 📝 صندوق النص */
        .report-textarea {
            width: 100%;
            height: 200px;
            border-radius: 25px;
            border: none;
            outline: none;
            padding: 15px;
            background: white;
            font-size: 14px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            font-family: inherit;
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
            padding: 12px 15px;
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
""", height=470)
