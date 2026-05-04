import streamlit as st
import streamlit.components.v1 as components

# 1. إعداد الصفحة
st.set_page_config(page_title="الإعدادات", layout="centered")

# 2. التنسيق العام (CSS) ليتناسب مع ديزاين المشروع
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction: rtl; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
section.main > div { padding-top:8px; }
div[data-testid="stVerticalBlock"] { gap:0rem; }

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة (HTML/JS)
components.html("""
<!DOCTYPE html>
<html dir="rtl">
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
            max-width: 380px;
            display: flex;
            flex-direction: column;
            height: 520px;
        }

        .header-container {
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 35px;
            position: relative;
            padding-top: 10px;
        }

        .back-icon {
            position: absolute;
            right: 0;
            font-size: 28px;
            font-weight: bold;
            color: #102646;
            text-decoration: none;
            line-height: 1;
            cursor: pointer;
        }

        .title {
            margin: 0;
            font-weight: 900;
            font-size: 20px;
            color: #102646;
        }

        .setting-item {
            background: white;
            border-radius: 100px;
            padding: 14px 22px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
            text-decoration: none;
        }

        .setting-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }

        .item-right {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .item-right i {
            color: #102646;
            font-size: 16px;
            width: 20px;
            text-align: center;
        }

        .item-text {
            color: #102646;
            font-weight: 800;
            font-size: 14px;
        }

        .arrow {
            color: #102646;
            font-weight: bold;
            font-size: 18px;
        }

        .bottom-row {
            display: flex;
            gap: 10px;
            margin-top: auto;
            padding-bottom: 10px;
        }

        .bottom-item {
            flex: 1;
            background: white;
            border-radius: 100px;
            padding: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            cursor: pointer;
            transition: 0.3s;
        }

        .bottom-item i {
            color: #102646;
            font-size: 14px;
        }

        .bottom-item span {
            color: #102646;
            font-weight: 800;
            font-size: 12px;
        }

        .bottom-item:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 15px rgba(0,0,0,0.12);
        }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon" onclick="goPage('customer')">›</div>
            <h2 class="title">الإعدادات</h2>
        </div>

        <!-- Change Password -->
        <div class="setting-item" onclick="goPage('Change_password-ar')">
            <div class="item-right">
                <i class="fas fa-lock"></i>
                <span class="item-text">تغيير كلمة المرور</span>
            </div>
            <span class="arrow">‹</span>
        </div>

        <!-- Change Language -->
        <div class="setting-item" onclick="goPage('Change_language-ar')">
            <div class="item-right">
                <i class="fas fa-globe"></i>
                <span class="item-text">تغيير اللغة</span>
            </div>
            <span class="arrow">‹</span>
        </div>

        <!-- Rate App -->
        <div class="setting-item" onclick="goPage('Rate_app-ar')">
            <div class="item-right">
                <i class="fas fa-star"></i>
                <span class="item-text">تقييم التطبيق</span>
            </div>
            <span class="arrow">‹</span>
        </div>

        <!-- Logout -->
        <div class="setting-item" onclick="goPage('logout')">
            <div class="item-right">
                <i class="fas fa-sign-out-alt"></i>
                <span class="item-text">تسجيل الخروج</span>
            </div>
            <span class="arrow">‹</span>
        </div>

        <!-- Bottom Row -->
        <div class="bottom-row">
            <div class="bottom-item" onclick="goPage('Report_Problem-ar')">
                <i class="fas fa-exclamation-triangle"></i>
                <span>الإبلاغ عن مشكلة</span>
            </div>
            <div class="bottom-item" onclick="goPage('Contact_Us-ar')">
                <i class="fas fa-envelope"></i>
                <span>تواصل معنا</span>
            </div>
        </div>
    </div>

    <script>
    function goPage(p){
        if(p === 'logout'){
            window.top.location.href = "/";
        } else {
            window.top.location.href = "/?page=" + p;
        }
    }
    </script>
</body>
</html>
""", height=600)
