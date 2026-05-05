import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تغيير اللغة", layout="centered")

st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
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

components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
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

.header-container{
    display:flex;
    align-items:center;
    justify-content:center;
    margin-bottom:40px;
    position:relative;
}

/* 🔙 السهم صار يمين */
.back-icon{
    position:absolute;
    right:0;
    font-size:28px;
    font-weight:bold;
    color:#0f2446;
    cursor:pointer;
}

.title{
    margin:0;
    font-weight:900;
    font-size:20px;
    color:#0f2446;
}

/* ⚪ كبسولة اللغة */
.language-capsule{
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.3s;
}

.language-capsule:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
}

.left-content{
    display:flex;
    align-items:center;
    gap:12px;
}

.icon{
    color:#0f2446;
    font-size:16px;
}

.label{
    color:#0f2446;
    font-weight:700;
    font-size:14px;
}

/* ✔ و > */
.status-mark{
    font-size:18px;
    font-weight:bold;
}

.check{ color:#2f80ed; }

.arrow-icon{
    color:#0f2446;
    font-size:18px;
}

</style>
</head>

<body>

<div class="main-wrapper">

    <div class="header-container">
        <div class="back-icon" onclick="goPage('settings-ar')">&gt;</div>
        <h2 class="title">تغيير اللغة</h2>
    </div>

    <!-- الإنجليزية -->
    <div class="language-capsule" onclick="goPage('Settings')">
        <div class="left-content">
            <div class="icon"><i class="fas fa-globe"></i></div>
            <div class="label">English</div>
        </div>
        <div class="status-mark">
            <span class="arrow-icon">&lt;</span>
        </div>
    </div>

    <!-- العربية -->
    <div class="language-capsule">
        <div class="left-content">
            <div class="icon"><i class="fas fa-globe"></i></div>
            <div class="label">العربية</div>
        </div>
        <div class="status-mark check">
            <i class="fas fa-check"></i>
        </div>
    </div>

</div>

<script>
function goPage(p){
     window.parent.location.href = "/" + p;
}
</script>

</body>
</html>
""", height=500)
