import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Contact Us", layout="centered")

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

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 الكارد الرئيسي */
.block-container{
    max-width:420px;
    margin:auto;
    padding:25px 30px;

    background:linear-gradient(160deg,
        var(--bg1) 0%,
        var(--bg2) 45%,
        var(--bg3) 100%
    );

    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}

/* 🧠 العناوين */
h1, h2, h3{
    color:var(--navy);
    text-align:center;
    font-weight:900;
}

/* 🧾 Inputs */
div[data-testid="stTextInput"] input{
    border-radius:25px;
    height:44px;
    border:none !important;
    outline:none !important;
    padding-left:16px;
    background:rgba(255,255,255,0.95);
}

/* 📍 Select */
div[data-testid="stSelectbox"] div{
    border-radius:25px;
}

/* 🔘 الأزرار الأساسية */
div.stButton > button{
    width:100%;
    height:46px;
    border-radius:25px;
    border:none;

    background:linear-gradient(90deg,
        var(--accent),
        var(--accent2)
    );

    color:white;
    font-weight:bold;

    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

/* ✨ hover */
div.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 18px rgba(0,0,0,.2);
}

/* 🤍 زر ثانوي */
div.stButton:nth-of-type(1) > button{
    background:white;
    color:var(--navy);
    box-shadow:0 2px 8px rgba(0,0,0,.1);
}

.contact-item {
    background: white;
    border-radius: 25px;
    padding: 12px 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 15px;
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
}
.contact-item-icon {
    font-size: 20px;
    color: var(--navy);
}
.contact-item-text {
    font-weight: bold;
    color: var(--navy);
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <div class="block-container">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <a href="/?page=settings" style="text-decoration: none; color: var(--navy); font-size: 24px; margin-right: 10px;"><i class="fas fa-arrow-left"></i></a>
            <h3 style="margin: 0;">Contact Us</h3>
        </div>

        <div class="contact-item">
            <span class="contact-item-icon"><i class="fas fa-envelope"></i></span>
            <span class="contact-item-text">Email: CoCare26@gmail.com</span>
        </div>

        <div class="contact-item">
            <span class="contact-item-icon"><i class="fas fa-phone"></i></span>
            <span class="contact-item-text">Phone: +962 79 123 4567</span>
        </div>
    </div>
</body>
</html>
""", height=700)
