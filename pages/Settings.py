import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="App", layout="centered")

components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body{
    margin:0;
    background:#f0f7ff;
    font-family:Arial;
    display:flex;
    justify-content:center;
}

/* phone frame */
.app {
    width:390px;
    height:700px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    padding:20px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    overflow:hidden;
    position:relative;
}

/* pages */
.page {
    position:absolute;
    width:100%;
    top:0;
    left:0;
    transition:0.4s;
}

.hidden {
    transform:translateX(100%);
    opacity:0;
}

.active {
    transform:translateX(0);
    opacity:1;
}

/* header */
.header {
    text-align:center;
    position:relative;
    margin-bottom:25px;
}

.back {
    position:absolute;
    left:0;
    font-size:26px;
    cursor:pointer;
}

.title {
    font-weight:900;
}

/* cards */
.item {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.2s;
}

.item:hover {
    transform:scale(0.97);
}

/* bottom */
.bottom {
    display:flex;
    gap:10px;
    margin-top:40px;
}

.bottom div {
    flex:1;
    background:white;
    padding:12px;
    border-radius:100px;
    text-align:center;
    cursor:pointer;
}
</style>
</head>

<body>

<div class="app">

<!-- SETTINGS -->
<div id="settings" class="page active">
    <div class="header">
        <h2 class="title">Settings</h2>
    </div>

    <div class="item" onclick="go('password')">
        <span><i class="fas fa-lock"></i> Change Password</span>
        <span>›</span>
    </div>

    <div class="item" onclick="go('language')">
        <span><i class="fas fa-globe"></i> Change Language</span>
        <span>›</span>
    </div>

    <div class="item" onclick="go('rate')">
        <span><i class="fas fa-star"></i> Rate App</span>
        <span>›</span>
    </div>

    <div class="item" onclick="go('logout')">
        <span><i class="fas fa-sign-out-alt"></i> Log Out</span>
        <span>›</span>
    </div>

    <div class="bottom">
        <div onclick="go('report')">Report</div>
        <div onclick="go('contact')">Contact</div>
    </div>
</div>

<!-- PASSWORD -->
<div id="password" class="page hidden">
    <div class="header">
        <div class="back" onclick="go('settings')">‹</div>
        <h2>Change Password</h2>
    </div>
</div>

<!-- LANGUAGE -->
<div id="language" class="page hidden">
    <div class="header">
        <div class="back" onclick="go('settings')">‹</div>
        <h2>Change Language</h2>
    </div>
</div>

<!-- RATE -->
<div id="rate" class="page hidden">
    <div class="header">
        <div class="back" onclick="go('settings')">‹</div>
        <h2>Rate App ⭐</h2>
    </div>
</div>

<!-- CONTACT -->
<div id="contact" class="page hidden">
    <div class="header">
        <div class="back" onclick="go('settings')">‹</div>
        <h2>Contact Us</h2>
    </div>
</div>

<!-- REPORT -->
<div id="report" class="page hidden">
    <div class="header">
        <div class="back" onclick="go('settings')">‹</div>
        <h2>Report Problem</h2>
    </div>
</div>

</div>

<script>
function go(id){
    document.querySelectorAll('.page').forEach(p=>{
        p.classList.remove('active');
        p.classList.add('hidden');
    });

    document.getElementById(id).classList.remove('hidden');
    document.getElementById(id).classList.add('active');
}
</script>

</body>
</html>
""", height=720)
