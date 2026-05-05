import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Report a Problem", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}

.block-container{
    max-width:350px !important;    
    margin:auto !important;
    padding:30px !important;       
    background:linear-gradient(160deg, var(--bg1), var(--bg2), var(--bg3));
    border-radius:42px;            
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* ===== HEADER ===== */
.header {
    position: relative;
    height: 110px;  /* 👈 كبرناه */
    margin-bottom: 40px;
}

.back-style {
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:#0f2446 !important;
    font-size:28px !important;
    border: none !important;
}

/* 🔥 العنوان مرفوع أكثر */
.title-text {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -160%);
    font-size:20px;
    font-weight:900;
    color:#0f2446;
    white-space: nowrap;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header">', unsafe_allow_html=True)

st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("‹"):
    st.switch_page("pages/Settings.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">Report a Problem</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== UI =====
components.html("""
<!DOCTYPE html>
<html>
<body style="font-family:Segoe UI; display:flex; justify-content:center;">

<div style="width:290px; display:flex; flex-direction:column; height:480px;">

<textarea style="
width:100%;
height:220px;
border-radius:25px;
border:none;
padding:18px;
font-size:16px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
" placeholder="I need help"></textarea>

<div style="margin-top:auto;">
<button onclick="alert('Report sent successfully ✅')" style="
width:100%;
padding:14px 22px;
border:none;
border-radius:100px;
background:white;
display:flex;
justify-content:space-between;
align-items:center;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
cursor:pointer;
">
<i>✈️</i>
<span style="font-weight:700;">Send Report</span>
</button>
</div>

</div>

</body>
</html>
""", height=500)
