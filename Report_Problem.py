import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Report a Problem", layout="centered")

# 2. التنسيق العام (CSS) - المقاسات الموحدة 350px
st.markdown("""
<style>
/* 🎯 الألوان المعتمدة */
:root {
    --navy: #0f2446;
    --accent-blue: #2f80ed;
    --bg-grad: linear-gradient(160deg, #d6ecff 0%, #eaf6ff 100%);
}

/* تصفير المسافات العلوية الافتراضية لـ Streamlit */
[data-testid="stHeader"] {display: none !important;}
.block-container {
    padding-top: 2rem !important;
    max-width: 350px !important; /* 1. العرض الموحد */
    margin: auto !important;
}

[data-testid="stAppViewContainer"] {
    background: #eef2f7;
}

/* 📦 الكارد الرئيسي (Main Container) */
.main .block-container {
    background: var(--bg-grad); /* 5. الخلفية المتدرجة */
    border-radius: 42px;         /* 1. الحواف الدائرية */
    padding: 30px !important;    /* 1. المسافات الداخلية */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15); /* 1. الظل المعتمد */
}

header {visibility: hidden;}
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
        
        /* 📏 الحاوية الداخلية (Main Wrapper) */
        .main-wrapper {
            width: 100%;
            max-width: 290px; /* 2. العرض الأقصى الداخلي */
            display: flex;
            flex-direction: column;
            height: 480px;    /* 2. الارتفاع المخصص */
        }

        /* 🔝 الرأس (Header Section) */
        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px; /* 3. المسافة السفلية */
            position: relative;
        }

        /* 🔙 أيقونة الرجوع */
        .back-icon {
            position: absolute;
            left: 0;
            font-size: 28px; /* 3. حجم الأيقونة */
            font-weight: bold;
            color: #0f2446;
            text-decoration: none;
            line-height: 1;
        }

        /* 🏷️ العنوان */
        .title {
            margin: 0;
            font-weight: 900; /* 3. وزن الخط */
            font-size: 20px;   /* 3. حجم الخط */
            color: #0f2446;    /* 5. لون Navy */
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
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-family: inherit;
        }

        /* 🔘 زر الإرسال (على نمط كبسولة الخيارات) */
        .btn-container {
            margin-top: auto;
            padding-bottom: 10px;
        }

        .send-btn {
            background: white;       /* 4. خلفية بيضاء صريحة */
            border-radius: 100px;    /* 4. حواف دائرية تماماً */
            width: 100%;
            padding: 14px 22px;      /* 4. المسافات الداخلية المعتمدة */
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
            color: #0f2446;     /* 5. لون Navy */
            font-weight: 700;
            font-size: 14px;    /* 4. حجم الخط الداخلي */
        }

        .send-btn i {
            color: #2f80ed;     /* 5. لون Accent Blue للأيقونة */
            font-size: 18px;    /* 4. حجم الأيقونة */
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <!-- الهيدر الموحد -->
        <div class="header-container">
            <div class="back-icon">&lt;</div>
            <h2 class="title">Report a Problem</h2>
        </div>

        <!-- صندوق النص -->
        <textarea class="report-textarea" placeholder="Describe your problem here..."></textarea>

        <!-- زر الإرسال (كبسولة) -->
        <div class="btn-container">
            <button class="send-btn" onclick="alert('Report Sent!')">
                <span>Send Report</span>
                <i class="fas fa-paper-plane"></i>
            </button>
        </div>
    </div>
</body>
</html>
""", height=500) # 2. الارتفاع المخصص لستريمليت
