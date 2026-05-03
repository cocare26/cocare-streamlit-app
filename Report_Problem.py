import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - بناءً على المقاسات والمعلومات التي اعتمدتها
st.markdown("""
<style>
/* 🎯 ألوان أساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* إخفاء الهيدر لرفع الكارد */
[data-testid="stHeader"] {display: none !important;}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 1. الكارد الرئيسي (Main Container) */
.block-container{
    max-width:350px !important;    /* العرض النحيف المعتمد */
    margin:auto !important;
    padding:30px !important;       /* المسافات الداخلية 30px */
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;            /* الحواف الدائرية 42px */
    box-shadow:0 15px 35px rgba(0,0,0,0.15); /* الظل المعتمد */
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
        
        /* 📏 2. الحاوية الداخلية (Main Wrapper) */
        .main-wrapper {
            width: 100%;
            max-width: 290px;      /* العرض الأقصى الداخلي 290px */
            height: 480px;         /* الارتفاع المخصص 480px */
            display: flex;
            flex-direction: column;
        }

        /* 🔝 3. الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;   /* المسافة السفلية 40px */
            position: relative;
        }

        .back-icon {
            position: absolute; left: 0;
            font-size: 28px;       /* حجم أيقونة الرجوع 28px */
            font-weight: bold; color: #0f2446;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900;      /* وزن الخط 900 */
            font-size: 20px;       /* حجم الخط 20px */
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

        /* 🔘 4. كبسولة الإرسال (زر أبيض صريح بمواصفاتك) */
        .send-btn {
            background: white;
            border-radius: 100px;  /* الحواف 100px */
            width: 100%;
            padding: 14px 22px;    /* المسافات: 14px عمودي و 22px أفقي */
            display: flex;
            align-items: center;
            justify-content: space-between; /* ✅ لضمان توزيع العناصر على الأطراف */
            border: none;
            margin-top: auto;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            box-sizing: border-box;
        }

        .send-btn span { 
            color: #0f2446; 
            font-weight: 700; 
            font-size: 14px; 
            order: 2; /* ✅ النص يروح لجهة اليمين */
        }

        .main-icon { 
            color: #0f2446; 
            font-size: 18px; 
            order: 1; /* ✅ الأيقونة تروح لجهة الشمال */
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الرأس -->
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Report a Problem</h2>
        </div>

        <!-- صندوق النص معPlaceholder المطلوب -->
        <textarea class="report-textarea" placeholder="I need help"></textarea>

        <!-- زر الإرسال مع توزيع العناصر على الأطراف -->
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
