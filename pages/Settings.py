import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}
#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}
</style>
""", unsafe_allow_html=True)

components.html("""
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>

body { margin:0; font-family:Arial; }

.main-wrapper { max-width:380px; margin:auto; }

.header-container {
    text-align:center;
    margin-bottom:30px;
    position:relative;
}

.back-icon {
    position:absolute;
    left:0;
    font-size:28px;
    color:#102646;
    text-decoration:none;
}

.title { font-weight:900; color:#102646; }

.setting-item {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-decoration:none;
    color:#102646;
}

.item-left {
    display:flex;
    gap:12px;
    align-items:center;
    font-weight:800;
    font-size:14px;
}

.arrow { font-size:18px; }

.bottom-row {
    display:flex;
    gap:10px;
    margin-top:40px;
}

.bottom-item {
    flex:1;
    background:white;
    border-radius:100px;
    padding:12px;
    text-align:center;
    text-decoration:none;
    color:#102646;
    font-weight:800;
    font-size:12px;
}
</style>
</head>

<body>

<div class="main-wrapper">

<div class="header-container">
<a href="?page=settings" class="back-icon">‹</a>
<h2 class="title">Settings</h2>
</div>

<a href="?page=change_password" class="setting-item">
<div class="item-left">
<i class="fas fa-lock"></i> Change Password
</div>
<span class="arrow">›</span>
</a>

<a href="?page=change_language" class="setting-item">
<div class="item-left">
<i class="fas fa-globe"></i> Change Language
</div>
<span class="arrow">›</span>
</a>

<a href="?page=rate_app" class="setting-item">
<div class="item-left">
<i class="fas fa-star"></i> Rate App
</div>
<span class="arrow">›</span>
</a>

<a href="?page=logout" class="setting-item">
<div class="item-left">
<i class="fas fa-sign-out-alt"></i> Log Out
</div>
<span class="arrow">›</span>
</a>

<div class="bottom-row">
<a href="?page=report" class="bottom-item">Report Problem</a>
<a href="?page=contact" class="bottom-item">Contact Us</a>
</div>

</div>

</body>
</html>
""", height=600)
