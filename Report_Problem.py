import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - المقاسات الموحدة 350px
st.markdown("""
<style>
/* 🎯 5. ألوان التنسيق (Color Palette) */
:root {
    --navy: #0f2446;
    --accent-blue: #2f80ed;
    --bg-grad: linear-gradient(160deg, #d6ecff 0%, #eaf6ff 100%);
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
    max-width: 350px !important;    /* العرض الموحد */
    margin: auto !important;
    padding: 30px !important;       /* المسافات الداخلية من جميع الجهات */
    background: var(--bg-grad);     /* الخلفية المتدرجة بزاوية 160 */
    border-radius: 42px;            /* الحواف الدائرية العصرية */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15); /* الظل المعتمد */
    margin-top: 20px !important;
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
            max-width: 290px;      /* العرض الداخلي للمحتوى */
            display: flex;
            flex-direction: column;
            height: 480px;         /* الارتفاع المخصص داخل CSS */
        }

        /* 🔝 3. الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;   /* المسافة السفلية لفصل العنوان */
            position: relative;
        }

        /* أيقونة الرجوع */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 28px;       /* الحجم المعتمد 28px */
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        /* عنوان الصفحة */
        .title {
            margin: 0;
            font-weight: 900;      /* وزن الخط Extra Bold */
            font-size: 20px;       /* حجم الخط 20px */
            color: #0f2446;        /* لون Navy */
        }

        /* 📝 صندوق النص */
        .report-textarea {
            width: 100%;
            height: 220px;
            border-radius: 25px;   /* حواف متناسقة */
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
            color: #888;
        }

        /* 🔘 4. كبسولة الإرسال (على نمط كبسولات الخيارات) */
        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;             /* خلفية بيضاء صريحة */
            border-radius: 100px;          /* دائرية تماماً */
            width: 100%;
            padding: 14px 22px;            /* 14px عمودي و 22px أفقي */
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            border: none;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            box-sizing: border-box;
            transition: 0.3s;
        }

        .send-btn:hover {
            transform: translateY(-2px);
        }

        .send-btn span {
            color: #0f2446;                /* لون Navy */
            font-weight: 700;
            font-size: 14px;               /* حجم الخط الداخلي 14px */
        }

        .send-btn i {
            color: #2f80ed;                /* لون الأيقونة Accent Blue */
            font-size: 18px;               /* حجم الأيقونة 18px */
        }

        /* الفراغ بين الأيقونة والنص */
        .btn-content {
            display: flex;
            align-items: center;
            gap: 12px;                     /* Gap المعتمد 12px */
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

        <!-- صندوق النص -->
        <textarea class="report-textarea" placeholder="Describe your problem here..."></textarea>

        <!-- زر الإرسال (الكبسولة) -->
        <div class="btn-container">
            <button class="send-btn" onclick="alert('Report Sent!')">
                <div class="btn-content">
                    <i class="fas fa-paper-plane"></i>
                    <span>Send Report</span>
                </div>
                <i class="fas fa-chevron-right" style="color: #0f2446; font-size: 16px;"></i>
            </button>
        </div>
    </div>
</body>
</html>
""", height=500) # 2. الارتفاع المخصص لـ Streamlit لضمان عدم ظهور سكرول
