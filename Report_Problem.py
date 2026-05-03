import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - بناءً على المسطرة (350px)
st.markdown("""
<style>
/* 🎯 الألوان المعتمدة */
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
    border-radius: 42px;         /* الحواف الدائرية المعتمدة */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15); /* الظل المعتمد */
    margin-top: 50px !important;
}

/* إخفاء عناصر ستريمليت الزائدة */
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stHeader"] {background: rgba(0,0,0,0);}
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
        }

        /* 🏷️ العنوان (Title) */
        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px; /* الحجم المعتمد */
            color: #0f2446;
        }

        /* 📝 صندوق النص */
        .report-textarea {
            width: 100%;
            height: 240px;
            border-radius: 25px;
            border: none;
            outline: none;
            padding: 18px;
            background: white;
            font-size: 14px; /* الحجم المعتمد للنصوص الداخلية */
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-family: inherit;
        }

        /* 🔘 زر الإرسال بنمط الكبسولة الموحد */
        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;
            border-radius: 100px; /* دائرية تماماً */
            width: 100%;
            padding: 14px 22px;   /* بادينج الكبسولة المعتمد */
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
        }

        .send-btn span {
            color: #0f2446;
            font-weight: 700;
            font-size: 14px; /* الحجم المعتمد */
        }

        .send-btn i {
            color: #0f2446;
            font-size: 16px; /* حجم الأيقونة المعتمد */
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
        <textarea class="report-textarea" placeholder="Describe your problem here..."></textarea>

        <!-- زر الإرسال -->
        <div class="btn-container">
            <button class="send-btn" onclick="alert('Report Sent!')">
                <i class="fas fa-paper-plane"></i>
                <span>Send Report</span>
            </button>
        </div>
    </div>
</body>
</html>
""", height=500) # الارتفاع المعتمد لـ Streamlit
