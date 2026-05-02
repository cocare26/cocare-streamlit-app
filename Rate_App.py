import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Rate App", layout="centered")

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

.store-item {
    background: white;
    border-radius: 25px;
    padding: 12px 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}
.store-item:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0,0,0,.15);
}
.store-item-left {
    display: flex;
    align-items: center;
    gap: 15px;
}
.store-item-icon {
    font-size: 20px;
    color: var(--navy);
}
.store-item-text {
    font-weight: bold;
    color: var(--navy);
}
.store-item-arrow {
    font-size: 20px;
    color: #ccc;
}
</style>
""", unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html>
<head>
    <title>Rate App</title>
</head>
<body>
    <div class="block-container">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <a href="/?page=settings" style="text-decoration: none; color: var(--navy); font-size: 24px; margin-right: 10px;">←</a>
            <h3 style="margin: 0;">Rate App</h3>
        </div>

        <div class="store-item" onclick="window.open(\'https://play.google.com/store/apps/details?id=com.cocare.app\', \'_blank\')">
            <div class="store-item-left">
                <span class="store-item-icon">▶️</span>
                <span class="store-item-text">Google Play Store</span>
            </div>
            <span class="store-item-arrow">›</span>
        </div>

        <div class="store-item" onclick="window.open(\'https://apps.apple.com/us/app/cocare/id1234567890\', \'_blank\')">
            <div class="store-item-left">
                <span class="store-item-icon"></span>
                <span class="store-item-text">Apple App Store</span>
            </div>
            <span class="store-item-arrow">›</span>
        </div>

        <div class="store-item" onclick="window.open(\'https://appgallery.huawei.com/app/C101234567\', \'_blank\')">
            <div class="store-item-left">
                <span class="store-item-icon">H</span>
                <span class="store-item-text">Huawei AppGallery</span>
            </div>
            <span class="store-item-arrow">›</span>
        </div>
    </div>
</body>
</html>
""", height=700)
