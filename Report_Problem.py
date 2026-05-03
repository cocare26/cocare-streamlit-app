import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - بناءً على المواصفات المذكورة
st.markdown("""
<style>
/* 🎯 5. ألوان التنسيق (Color Palette) */
:root {
    --navy: #0f2446;
    --accent-blue: #2f80ed;
    --bg1: #d6ecff;
    --bg2: #bfe3ff;
    --bg3: #eaf6ff;
}

/* إخفاء عناصر ستريمليت الافتراضية */
[data-testid="stHeader"] {display: none !important;}
header {visibility: hidden;}
footer {visibility: hidden;}

/* 📱 خلفية التطبيق */
[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 1. الكارد الرئيسي (Main Container) */
.block-container {
    max-width: 350px !important;    /* العرض الموحد 350px */
    margin: auto !important;
    padding: 30px !important;       /* المسافات الداخلية 30px */
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%); /* التدرج المعتمد */
    border-radius: 42px;            /* الحواف 42px */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15); /* الظل المعتمد */
    margin-top: 40px !important;
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
            max-width: 290px;      /* العرض الأقصى 290px */
            display: flex;
            flex-direction: column;
            height: 480px;         /* الارتفاع المخصص 480px */
        }

        /* 🔝 3. الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;   /* المسافة السفلية 40px */
            position: relative;
        }

        /* 🔙 أيقونة الرجوع */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 28px;       /* الحجم المعتمد 28px */
            font-weight: bold;
            color: #0f2446;        /* لون Navy */
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        /* 🏷️ العنوان */
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
            font-size: 14px;
            color: #0f2446;
            resize: none;
            box-sizing: border-box;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-family: inherit;
        }

        /* 🔘 4. كبسولة الإرسال (Language Capsules Style) */
        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;             /* خلفية بيضاء صريحة */
            border-radius: 100px;          /* دائرية تماماً 100px */
            width: 100%;
            padding: 14px 22px;            /* 14px عمودياً و 22px أفقياً */
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            box-sizing: border-box;
            transition: 0.3s;
        }

        .btn-content {
            display: flex;
            align-items: center;
            gap: 12px;                     /* الفراغ بين الأيقونة والنص 12px */
        }

        .send-btn span {
            color: #0f2446;                /* لون Navy */
            font-weight: 700;
            font-size: 14px;               /* حجم الخط 14px */
        }

        .send-btn i.main-icon {
            color: #0f2446;
            font-size: 18px;               /* حجم الأيقونة 18px */
        }

        .send-btn i.arrow-icon {
            color: #2f80ed;                /* لون السهم Accent Blue */
            font-size: 18px;               /* حجم الأيقونة 18px */
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
""", height=500) # 500px لضمان عدم ظهور شريط تمرير
