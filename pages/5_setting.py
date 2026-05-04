import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
[data-testid="stAppViewContainer"] { background:#f0f7ff; }
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100% );
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
    direction: ltr;
}
#MainMenu, header, footer { visibility:hidden; }

.main-wrapper { width:100%; display:flex; flex-direction:column; height:550px; }
.header-container { display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; padding-top:10px; }
.back-icon { position:absolute; left:0; font-size:28px; font-weight:bold; color:#102646; text-decoration:none; }
.title { margin:0; font-weight:900; font-size:20px; color:#102646; }

.setting-item { 
    background:white; border-radius:100px; padding:14px 22px; margin-bottom:15px; 
    display:flex; align-items:center; justify-content:space-between; 
    box-shadow:0 4px 12px rgba(0,0,0,0.08); text-decoration:none; transition:0.3s; 
}
.setting-item:hover { transform:translateY(-2px); box-shadow:0 6px 15px rgba(0,0,0,0.12); }
.item-left { display:flex; align-items:center; gap:12px; }
.item-left i { color:#102646; font-size:16px; width:20px; text-align:center; }
.item-text { color:#102646; font-weight:800; font-size:14px; text-decoration:none; }
.arrow { color:#102646; font-weight:bold; font-size:18px; text-decoration:none; }

.bottom-row { display:flex; gap:10px; margin-top:auto; padding-bottom:10px; }
.bottom-item { 
    flex:1; background:white; border-radius:100px; padding:12px; 
    display:flex; align-items:center; justify-content:center; gap:8px; 
    box-shadow:0 4px 12px rgba(0,0,0,0.08); text-decoration:none; 
}
.bottom-item span { color:#102646; font-weight:800; font-size:12px; text-decoration:none; }
.bottom-item i { color:#102646; font-size:14px; }
</style>

<div class="main-wrapper">
    <div class="header-container">
        <a href="/?page=customer" target="_self" class="back-icon">‹</a>
        <h2 class="title">Settings</h2>
    </div>
    
    <a href="/?page=Change_password" target="_self" class="setting-item">
        <div class="item-left"><i class="fas fa-lock"></i><span class="item-text">Change Password</span></div>
        <span class="arrow">›</span>
    </a>
    
    <a href="/?page=Change_language" target="_self" class="setting-item">
        <div class="item-left"><i class="fas fa-globe"></i><span class="item-text">Change Language</span></div>
        <span class="arrow">›</span>
    </a>
    
    <a href="/?page=Rate_app" target="_self" class="setting-item">
        <div class="item-left"><i class="fas fa-star"></i><span class="item-text">Rate App</span></div>
        <span class="arrow">›</span>
    </a>
    
    <a href="/" target="_self" class="setting-item">
        <div class="item-left"><i class="fas fa-sign-out-alt"></i><span class="item-text">Log Out</span></div>
        <span class="arrow">›</span>
    </a>
    
    <div class="bottom-row">
        <a href="/?page=Report_Problem" target="_self" class="bottom-item">
            <i class="fas fa-exclamation-triangle"></i><span>Report Problem</span>
        </a>
        <a href="/?page=Contact_Us" target="_self" class="bottom-item">
            <i class="fas fa-envelope"></i><span>Contact Us</span>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)
