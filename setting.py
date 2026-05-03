import streamlit as st
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="Settings", layout="centered")

# CSS الخارجي (الكارد)
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# HTML UI
components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>

body{
    font-family:'Segoe UI', sans-serif;
    margin:0;
    display:flex;
    justify-content:center;
    background:transparent;
}

.main-wrapper{
    width:100%;
    max-width:290px;
    display:flex;
    flex-direction:column;
    height:480px;
}

/* Header */
.header-container{
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:35px;
    position:relative;
}

.back-icon{
    position:absolute;
    left:0;
    font-size:28px;
    font-weight:bold;
    color:#0f2446;
    text-decoration:none;
}

.title{
    margin:0;
    font-weight:900;
    font-size:20px;
    color:#0f2446;
}

/* 🔥 عناصر الإعدادات */
.setting-item{
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.3s;
}

.setting-item i{
    color:#0f2446;
    font-size:16px;
}

/* النص */
.setting-text{
    flex:1;
    text-align:right;
    margin-right:10px;
    font-size:14px;
    font-weight:600;
    color:#0f2446;
}

/* السهم */
.setting-item .arrow{
    margin-left:10px;
    color:#0f2446;
    font-weight:bold;
}

/* hover */
.setting-item:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* أزرار تحت */
.bottom-row{
    margin-top:auto;
    display:flex;
    gap:10px;
}

.small-btn{
    flex:1;
    background:white;
    border-radius:100px;
    padding:12px;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    font-size:13px;
    font-weight:700;
    color:#0f2446;
    cursor:pointer;
    transition:0.3s;
}

.small-btn:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

</style>
</head>

<body>

<div class="main-wrapper">

    <div class="header-container">
        <a href="#" class="back-icon">&lt;</a>
        <h2 class="title">Settings</h2>
    </div>

    <div class="setting-item">
        <i class="fas fa-lock"></i>
        <span class="setting-text">Change Password</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item">
        <i class="fas fa-globe"></i>
        <span class="setting-text">Change Language</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item">
        <i class="fas fa-star"></i>
        <span class="setting-text">Rate App</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item">
        <i class="fas fa-sign-out-alt"></i>
        <span class="setting-text">Log Out</span>
        <span class="arrow">›</span>
    </div>

    <div class="bottom-row">
        <div class="small-btn">⚠️ Report Problem</div>
        <div class="small-btn">✉️ Contact Us</div>
    </div>

</div>

</body>
</html>
""", height=500)
