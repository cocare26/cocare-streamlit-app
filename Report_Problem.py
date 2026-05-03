import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - دمج مقاسات الكود الأول مع تصميم الكارد
st.markdown("""
<style>
/* 🎯 ألوان أساسية من الكود الأول */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* إخفاء الهيدر تماماً لرفع الكارد */
[data-testid="stHeader"] {display: none !important;}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 الكارد الرئيسي - مقاسات الكود الأول */
.block-container{
    max-width:420px !important; /* اعتماد 420px كما في طلبك الأول */
    margin:auto !important;
    padding:25px 30px !important; /* حواف داخلية 25px فوق-تحت و 30px يمين-يسار */

    background:linear-gradient(160deg, 
        var(--bg1) 0%, 
        var(--bg2) 45%, 
        var(--bg3) 100%
    );

    border-radius:42px; /* الحواف الدائرية المعتمدة */
    box-shadow:0 10px 30px rgba(0,0,0,.15); /* الظل من الكود الأول */
    margin-top: 20px !important;
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
        body { font-family: 'Segoe UI', sans-serif; background: transparent; margin: 0; display: flex; justify-content: center; }
        
        /* 📏 الحاوية الداخلية (Main Wrapper) */
        .main-wrapper {
            width: 100%;
            max-width: 340px; /* توسيع المحتوى الداخلي قليلاً ليتناسب مع كارد 420px */
            height: 480px;
            display: flex;
            flex-direction: column;
        }

        /* 🔝 الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 30px;
            position: relative;
        }

        .back-icon {
            position: absolute; left: 0;
            font-size: 28px;
            font-weight: 900; 
            color: #0f2446;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900; /* Extra Bold كما في h1 من الكود الأول */
            font-size: 22px; 
            color: #0f2446;
        }

        /* 🧾 Inputs - ستايل الكود الأول */
        .report-textarea {
            width: 100%;
            height: 220px;
            border-radius: 25px;
            border: none !important;
            outline: none !important;
            padding: 20px;
            background: rgba(255,255,255,0.95); /* شفافية بسيطة كما في الكود الأول */
            font-size: 16px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
            font-family: inherit;
        }

        /* 🔘 الأزرار الأساسية - ستايل الكود الأول */
        .send-btn {
            width: 100%;
            height: 46px;
            border-radius: 25px;
            border: none;
            background: linear-gradient(90deg, #2f80ed, #1c6fa4); /* تدرج الأزرار من الكود الأول */
            color: white;
            font-weight: bold;
            font-size: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 25px;
            cursor: pointer;
            box-shadow: 0 6px 14px rgba(47,128,237,.25);
            transition: 0.3s ease;
            margin-top: auto;
        }

        /* ✨ hover من الكود الأول */
        .send-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 18px rgba(0,0,0,.2);
        }

        .btn-content { display: flex; align-items: center; gap: 12px; }

        .main-icon { color: white; font-size: 18px; }
        .arrow-icon { color: white; font-size: 18px; }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Report a Problem</h2>
        </div>
        
        <textarea class="report-textarea" placeholder="Describe your problem here..."></textarea>
        
        <button class="send-btn" onclick="alert('Sent!')">
            <div class="btn-content">
                <i class="fas fa-paper-plane main-icon"></i>
                <span>Send Report</span>
            </div>
            <i class="fas fa-chevron-right arrow-icon"></i>
        </button>
    </div>
</body>
</html>
""", height=500)
