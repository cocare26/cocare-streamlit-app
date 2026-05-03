import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - الألوان المستوحاة من الصورة
st.markdown("""
<style>
/* 🎯 5. ألوان التنسيق (Color Palette) المعدلة */
:root {
    --navy: #0f2446;
    --accent-blue: #2f80ed;
    /* التدرج اللوني المحدث ليكون مثل الصورة */
    --bg-grad: linear-gradient(180deg, #d8efff 0%, #ebf7ff 100%);
}

/* تصفير المسافات العلوية لستريمليت */
[data-testid="stHeader"] {display: none !important;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* 📱 خلفية الصفحة الخارجية */
[data-testid="stAppViewContainer"] {
    background: #f4f7f9;
}

/* 📦 1. الكارد الرئيسي (Main Container) */
.block-container {
    max-width: 350px !important;    /* العرض الموحد 350px */
    margin: auto !important;
    padding: 30px !important;       /* المسافات الداخلية 30px */
    background: var(--bg-grad);     /* لون الصورة المرفقة */
    border-radius: 42px;            /* الحواف 42px */
    box-shadow: 0 15px 35px rgba(0,0,0,0.1); 
    margin-top: 30px !important;
}
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
        
        /* 📏 2. الحاوية الداخلية (Main Wrapper) */
        .main-wrapper {
            width: 100%;
            max-width: 290px; 
            display: flex;
            flex-direction: column;
            height: 480px;
        }

        /* 🔝 3. الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px; /* المسافة 40px */
            position: relative;
        }

        /* 🔙 أيقونة الرجوع الموحدة < */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 28px; /* حجم 28px */
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
        }

        /* 🏷️ العنوان الموحد */
        .title {
            margin: 0;
            font-weight: 900; /* Extra Bold */
            font-size: 20px;   /* حجم 20px */
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
            font-size: 14px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            font-family: inherit;
        }

        .report-textarea::placeholder {
            color: #aaa;
        }

        /* 🔘 4. كبسولة الإرسال (زر أبيض صريح) */
        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;
            border-radius: 100px; /* دائرية تماماً */
            width: 100%;
            padding: 14px 22px;   /* 14px عمودي و 22px أفقي */
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            box-sizing: border-box;
            transition: 0.3s;
        }

        .send-btn span {
            color: #0f2446;
            font-weight: 700;
            font-size: 14px; /* حجم 14px */
        }

        /* الفراغ والأيقونات */
        .btn-content {
            display: flex;
            align-items: center;
            gap: 12px; /* فجوة 12px */
        }

        .send-btn i.main-icon {
            color: #0f2446;
            font-size: 18px; /* حجم 18px */
        }
        
        .send-btn i.arrow-icon {
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

        <textarea class="report-textarea" placeholder="I need help"></textarea>

        <div class="btn-container">
            <button class="send-btn" onclick="alert('Report Sent!')">
                <div class="btn-content">
                    <i class="fas fa-paper-plane main-icon"></i>
                    <span>Send Report</span>
                </div>
                <i class="fas fa-chevron-right arrow-icon"></i>
            </button>
        </div>
    </div>
</body>
</html>
""", height=500)
