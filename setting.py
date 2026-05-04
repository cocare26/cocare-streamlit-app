import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

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
    cursor:pointer;
}

.title{
    margin:0;
    font-weight:900;
    font-size:20px;
    color:#0f2446;
}

/* الأزرار العلوية: أيقونة يسار | نص وسهم يمين */
.setting-item{
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.3s;
}

.setting-item i.left-icon{
    color:#0f2446;
    font-size:16px;
    margin-right: auto; /* دفع النص والسهم لليمين */
}

.setting-text-right{
    font-size:14px;
    font-weight:600;
    color:#0f2446;
    margin-right: 10px;
}

.setting-item .arrow{
    color:#0f2446;
    font-weight:bold;
    font-size: 18px;
}

/* تصميم أزرار Bottom Row (كما كانت في الكود الأصلي) */
.bottom-row{
    margin-top:auto;
    display:flex;
    gap:10px;
}

.bottom-row .setting-item{
    flex:1;
    padding:12px 14px;
    justify-content: space-between; /* توزيع الأيقونة والنص والسهم */
}

.bottom-row .setting-text{
    flex:1;
    text-align:left;
    margin-left:15px;
    font-size:13px;
    font-weight:600;
    color:#0f2446;
}

.setting-item:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

</style>
</head>

<body>

<div class="main-wrapper">

    <div class="header-container">
        <div class="back-icon" onclick="goPage('customer')">&lt;</div>
        <h2 class="title">Settings</h2>
    </div>

    <!-- الأزرار المعدلة: الأيقونة على اليسار -->
    <div class="setting-item" onclick="goPage('Change_password')">
        <i class="fas fa-lock left-icon"></i>
        <span class="setting-text-right">Change Password</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="goPage('Change_language')">
        <i class="fas fa-globe left-icon"></i>
        <span class="setting-text-right">Change Language</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="goPage('Rate_app')">
        <i class="fas fa-star left-icon"></i>
        <span class="setting-text-right">Rate App</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="goPage('logout')">
        <i class="fas fa-sign-out-alt left-icon"></i>
        <span class="setting-text-right">Log Out</span>
        <span class="arrow">›</span>
    </div>

    <!-- الأزرار السفلية: رجعت كما كانت في كودك الأساسي -->
    <div class="bottom-row">
        <div class="setting-item" onclick="goPage('Report_Problem')">
            <i class="fas fa-exclamation-triangle"></i>
            <span class="setting-text">Report Problem</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="goPage('Contact_Us')">
            <i class="fas fa-envelope"></i>
            <span class="setting-text">Contact Us</span>
            <span class="arrow">›</span>
        </div>
    </div>

</div>

<script>
function goPage(p){
    window.top.location.href = "/?page=" + p;
}
</script>

</body>
</html>
""", height=500)
