import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Settings", layout="centered")

# ======= CSS الخارجي =======
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

# ======= HTML كامل =======
components.html("""
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body {
    margin:0;
    font-family:Arial;
}

.main-wrapper {
    max-width:380px;
    margin:auto;
}

/* HEADER */
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

.title {
    font-weight:900;
    color:#102646;
}

/* SETTINGS ITEMS */
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
    transition:0.3s;
}

.setting-item:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

.item-left {
    display:flex;
    gap:12px;
    align-items:center;
    font-weight:800;
    font-size:14px;
}

.arrow {
    font-size:18px;
}

/* BOTTOM ROW */
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
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.3s;
}

.bottom-item:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}
</style>
</head>

<body>

<div class="main-wrapper">

<!-- HEADER -->
<div class="header-container">
<a href="?page=settings" target="_top" class="back-icon">‹</a>
<h2 class="title">Settings</h2>
</div>

<!-- CHANGE PASSWORD -->
<a href="?page=change_password" target="_top" class="setting-item">
<div class="item-left">
<i class="fas fa-lock"></i> Change Password
</div>
<span class="arrow">›</span>
</a>

<!-- CHANGE LANGUAGE -->
<a href="?page=change_language" target="_top" class="setting-item">
<div class="item-left">
<i class="fas fa-globe"></i> Change Language
</div>
<span class="arrow">›</span>
</a>

<!-- RATE APP -->
<a href="?page=rate_app" target="_top" class="setting-item">
<div class="item-left">
<i class="fas fa-star"></i> Rate App
</div>
<span class="arrow">›</span>
</a>

<!-- LOGOUT -->
<a href="?page=logout" target="_top" class="setting-item">
<div class="item-left">
<i class="fas fa-sign-out-alt"></i> Log Out
</div>
<span class="arrow">›</span>
</a>

<!-- BOTTOM -->
<div class="bottom-row">
<a href="?page=report" target="_top" class="bottom-item">Report Problem</a>
<a href="?page=contact" target="_top" class="bottom-item">Contact Us</a>
</div>

</div>

</body>
</html>
""", height=600)
