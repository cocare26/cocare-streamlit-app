import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="الإبلاغ عن مشكلة", layout="centered")

st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
    --gray-color: #808080;
}

[data-testid="stHeader"] {display: none !important;}

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

components.html("""
<!DOCTYPE html>
<html dir="rtl"> <!-- تفعيل الاتجاه من اليمين لليسار -->
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

        /* سهم الرجوع الموحد > للعربية على اليمين */
        .back-icon {
            position: absolute; 
            right: 0;
            font-size: 28px;
            font-weight: bold; 
            color: #0f2446;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px;
            color: #0f2446;
        }

        /* 📝 صندوق النص */
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
            transition: 0.3s;
        }

        .send-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }

        /* نص الإرسال - جهة اليمين */
        .send-btn span { 
            color: #0f2446; 
            font-weight: 700; 
            font-size: 14px; 
        }

        /* أيقونة الطيارة - جهة اليسار */
        .main-icon { 
            color: #808080; 
            font-size: 18px; 
            transform: scaleX(-1); /* عكس اتجاه الطيارة لتناسب العربي */
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon" onclick="goPage('settings-ar')">&gt;</div>
            <h2 class="title">الإبلاغ عن مشكلة</h2>
        </div>

        <textarea class="report-textarea" placeholder="أنا بحاجة للمساعدة..."></textarea>

        <div style="margin-top: auto; padding-bottom: 10px;">
            <button class="send-btn" onclick="alert('تم الإرسال!')">
                <span>إرسال البلاغ</span>
                <i class="fas fa-paper-plane main-icon"></i>
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
