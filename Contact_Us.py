import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
/* 🎯 ألوان أساسية */
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 الكارد الرئيسي */
.block-container{
    max-width:420px;
    margin:auto;
    padding:25px 30px;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

/* 💊 تصميم الكبسولة (المستطيل الأبيض الطويل) */
.capsule-box {
    background: white;
    border-radius: 100px; /* تجعل الحواف دائرية تماماً كالكبسولة */
    padding: 18px 25px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    width: 100%;
}

.icon-style {
    font-size: 20px;
    color: var(--navy);
}

.text-style {
    font-weight: bold;
    color: var(--navy);
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# دمج الـ HTML مع الـ CSS الجديد لضمان الشكل
components.html("""
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: transparent; }
        .wrapper { max-width: 380px; margin: auto; }
        
        .header {
            display: flex;
            align-items: center;
            margin-bottom: 30px;
            color: #0f2446;
        }

        .capsule {
            background: white;
            border-radius: 100px; /* سر شكل الكبسولة */
            padding: 15px 25px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .icon {
            margin-right: 15px;
            color: #0f2446;
            font-size: 18px;
            display: flex;
            align-items: center;
        }

        .text {
            color: #0f2446;
            font-weight: 700;
            font-size: 15px;
        }
        
        a { text-decoration: none; color: inherit; }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="header">
            <a href="#" style="font-size: 24px; margin-right: 15px;"><i class="fas fa-arrow-left"></i></a>
            <h2 style="margin: 0; font-weight: 900;">Contact Us</h2>
        </div>

        <!-- كبسولة الإيميل -->
        <div class="capsule">
            <div class="icon"><i class="fas fa-envelope"></i></div>
            <div class="text">Email: CoCare26@gmail.com</div>
        </div>

        <!-- كبسولة الهاتف -->
        <div class="capsule">
            <div class="icon"><i class="fas fa-phone"></i></div>
            <div class="text">Phone: +962 79 123 4567</div>
        </div>
    </div>
</body>
</html>
""", height=400)
