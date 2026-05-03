import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)


components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body{
    font-family:Arial;
    margin:0;
    display:flex;
    justify-content:center;
    background:transparent;
}

.wrapper{
    width:290px;
    display:flex;
    flex-direction:column;
    height:480px;
}

.header{
    display:flex;
    justify-content:center;
    align-items:center;
    margin-bottom:30px;
    position:relative;
}

.back{
    position:absolute;
    left:0;
    font-size:26px;
    cursor:pointer;
}

.title{
    font-size:20px;
    font-weight:bold;
}

/* buttons */
.item{
    background:white;
    border-radius:100px;
    padding:14px;
    margin-bottom:12px;
    display:flex;
    align-items:center;
    cursor:pointer;
}

.item i{
    margin-right:auto;
    color:#0f2446;
}

.text{
    font-weight:600;
    color:#0f2446;
    margin-right:10px;
}

.arrow{
    font-weight:bold;
}
</style>
</head>

<body>

<div class="wrapper">

    <div class="header">
        <div class="back" onclick="go('customer')">&lt;</div>
        <div class="title">Settings</div>
    </div>

    <div class="item" onclick="go('change_password')">
        <i class="fas fa-lock"></i>
        <div class="text">Change Password</div>
        <div class="arrow">›</div>
    </div>

    <div class="item" onclick="go('change_language')">
        <i class="fas fa-globe"></i>
        <div class="text">Change Language</div>
        <div class="arrow">›</div>
    </div>

    <div class="item" onclick="go('rate_app')">
        <i class="fas fa-star"></i>
        <div class="text">Rate App</div>
        <div class="arrow">›</div>
    </div>

    <div class="item" onclick="go('report_problem')">
        <i class="fas fa-exclamation-triangle"></i>
        <div class="text">Report Problem</div>
        <div class="arrow">›</div>
    </div>

    <div class="item" onclick="go('contact_us')">
        <i class="fas fa-envelope"></i>
        <div class="text">Contact Us</div>
        <div class="arrow">›</div>
    </div>

</div>

<script>
function go(p){
    window.top.location.href = "/?page=" + p;
}
</script>

</body>
</html>
""", height=500)
