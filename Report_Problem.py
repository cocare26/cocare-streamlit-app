import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS)
st.markdown("""
<style>
/* 🎯 الألوان الأساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
    --gray-color: #808080; /* اللون الرمادي المطلوب */
}

[data-testid="stHeader"] {display: none !important;}

/* 📦 1. الكارد الرئيسي (Main Container) */
.block-container{
    max-width:350px !important;    
    margin:auto !important;
    padding:30px !important;       
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;            
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

[data-testid="stAppViewContainer"]{ background:#eef2f7; }
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
        body { font-family: 'Segoe UI', sans-serif; background: transparent; margin: 0; display: flex; justify-content: center; }
        
        .main-wrapper {
            width: 100%;
            max-width: 290px;      
            height: 480px;         
            display: flex;
            flex-direction: column;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;
            position: relative;
        }

        .back-icon {
            position: absolute; left: 0;
            font-size: 28px;
            font-weight: bold; color: #0f2446;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px;
            color: #0f2446;
        }

        /* 📝 صندوق النص مع تعديل لون الـ Placeholder للرمادي */
        .report-textarea {
            width: 100%;
            height: 220px;
            border-radius: 25px;
            border: none;
            outline: none;
            padding: 18px;
            background: white;
            font-size: 16px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-family: inherit;
        }

        /* 🎨 جعل لون "I need help" رمادي */
        .report-textarea::placeholder {
            color: #808080;
        }

        /* 🔘 زر الإرسال */
        .send-btn {
            background: white;
            border-radius: 100px;
            width: 100%;
            padding: 14px 22px;
            display: flex;
            align-items: center;
            justify-content: space-between; 
            border: none;
            margin-top: auto;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            box-sizing: border-box;
        }

        /* نص السيند ريبورت - جهة اليمين */
        .send-btn span { 
            color: #0f2446; 
            font-weight: 700; 
            font-size: 14px; 
            order: 2; 
        }

        /* أيقونة الطيارة - جهة الشمال بلون رمادي */
        .main-icon { 
            color: #808080; /* تم تغيير اللون للرمادي */
            font-size: 18px; 
            order: 1; 
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Report a Problem</h2>
        </div>

        <textarea class="report-textarea" placeholder="I need help"></textarea>

        <div style="margin-top: auto; padding-bottom: 10px;">
            <button class="send-btn" onclick="alert('Sent!')">
                <i class="fas fa-paper-plane main-icon"></i>
                <span>Send Report</span>
            </button>
        </div>
    </div>
</body>
</html>
""", height=500)
