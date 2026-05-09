import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تقييم التطبيق", layout="centered")

st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}

* { direction: rtl; }

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
 max-width: 430px !important;
   height: 820px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

/* ===== HEADER ===== */
.header-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 40px;
    gap: 10px;
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:#0f2446 !important;
    font-size:28px !important;
    width:auto !important;
    padding:0 !important;
    border: none !important;
}

/* العنوان نزلناه */
.title-text {
    font-size:20px;
    font-weight:900;
    color:#0f2446;
    text-align: center;
    margin-top: 20px;  /* 👈 نزلناه أكثر */
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)

col1, col2 = st.columns([1,4])

with col1:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("›"):
        st.switch_page("pages/settingar.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="title-text">تقييم التطبيق</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== CONTENT =====
components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: transparent;
    margin: 0;
    display: flex;
    justify-content: center;
}
.main-wrapper { width: 100%; max-width: 290px; }
.store-item {
    background: white;
    border-radius: 100px;
    padding: 14px 22px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    cursor: pointer;
    transition: 0.3s ease;
}
.store-item:hover { 
    transform: translateY(-2px); 
    box-shadow: 0 6px 15px rgba(0,0,0,0.12); 
}
.store-item-right { 
    display: flex; 
    align-items: center; 
    gap: 12px; 
}
.store-item-icon { 
    font-size: 16px; 
    color: #0f2446; 
    width: 20px; 
    text-align: center; 
}
.store-item-text { 
    font-weight: 700; 
    color: #0f2446; 
    font-size: 14px; 
}
.store-item-arrow { 
    font-size: 18px; 
    font-weight: bold; 
    color: #0f2446; 
}
</style>
</head>
<body>
<div class="main-wrapper">

    <div class="store-item" onclick="window.open('https://play.google.com/store/apps', '_blank')">
        <div class="store-item-right">
            <span class="store-item-icon"><i class="fab fa-google-play"></i></span>
            <span class="store-item-text">متجر جوجل بلاي</span>
        </div>
        <span class="store-item-arrow">‹</span>
    </div>

    <div class="store-item" onclick="window.open('https://apps.apple.com', '_blank')">
        <div class="store-item-right">
            <span class="store-item-icon"><i class="fab fa-apple"></i></span>
            <span class="store-item-text">متجر آبل</span>
        </div>
        <span class="store-item-arrow">‹</span>
    </div>

    <div class="store-item" onclick="window.open('https://appgallery.huawei.com', '_blank')">
        <div class="store-item-right">
            <span class="store-item-icon"><i class="fas fa-mobile-alt"></i></span>
            <span class="store-item-text">متجر هواوي</span>
        </div>
        <span class="store-item-arrow">‹</span>
    </div>

</div>
</body>
</html>
""", height=350)
