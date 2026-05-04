import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
#MainMenu, header, footer { visibility:hidden; }

[data-testid="stAppViewContainer"] { background:#f0f7ff; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

.setting-item { 
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-decoration:none !important;
    transition:0.3s;
}

.setting-item:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

.item-left {
    display:flex;
    align-items:center;
    gap:12px;
}

.item-text {
    color:#102646;
    font-weight:800;
    font-size:14px;
}

.arrow {
    color:#102646;
    font-weight:bold;
    font-size:18px;
}

.bottom-row {
    display:flex;
    gap:10px;
    margin-top:50px;
}

.bottom-item { 
    flex:1;
    background:white;
    border-radius:100px;
    padding:12px;
    display:flex;
    align-items:center;
    justify-content:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-decoration:none !important;
}

.bottom-item span {
    color:#102646;
    font-weight:800;
    font-size:12px;
}
</style>

<div style="text-align:center; margin-bottom:30px;">
    <h2 style="color:#102646; font-weight:900;">Settings</h2>
</div>

<a href="?page=change_password" target="_self" class="setting-item">
    <div class="item-left">
        <i class="fas fa-lock"></i>
        <span class="item-text">Change Password</span>
    </div>
    <span class="arrow">›</span>
</a>

<a href="?page=change_language" target="_self" class="setting-item">
    <div class="item-left">
        <i class="fas fa-globe"></i>
        <span class="item-text">Change Language</span>
    </div>
    <span class="arrow">›</span>
</a>

<a href="?page=contact" target="_self" class="setting-item">
    <div class="item-left">
        <i class="fas fa-envelope"></i>
        <span class="item-text">Contact Us</span>
    </div>
    <span class="arrow">›</span>
</a>

<a href="?page=report" target="_self" class="setting-item">
    <div class="item-left">
        <i class="fas fa-bug"></i>
        <span class="item-text">Report Problem</span>
    </div>
    <span class="arrow">›</span>
</a>

<div class="bottom-row">
    <a href="?page=settings" target="_self" class="bottom-item">
        <span>Back</span>
    </a>
</div>

""", unsafe_allow_html=True)
