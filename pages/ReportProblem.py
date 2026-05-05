import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Report a Problem", layout="centered")

# ===== CSS =====
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

.block-container{
    max-width:350px !important;    
    margin:auto !important;
    padding:30px !important;       
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;            
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* ===== HEADER ===== */
.header {
    position:relative;
    text-align:center;
    margin-bottom:40px;
}

.back-style {
    position:absolute;
    left:0;
    top:0;
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:#0f2446 !important;
    font-size:28px !important;
    width:auto !important;
    padding:0 !important;
}

/* 👇 رفع الكلمة + منع سطرين */
.title-text {
    font-size:20px;
    font-weight:900;
    color:#0f2446;
    margin-top: -15px;     /* 🔥 رفع */
    white-space: nowrap;   /* 🔥 سطر واحد */
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
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body {
    font-family: 'Segoe UI';
    background: transparent;
    margin: 0;
    display: flex;
    justify-content: center;
}

.main-wrapper {
    width: 100%;
    max-width: 290px;
    height: 480px;
    display: flex;
    flex-direction: column;
}

.report-textarea {
    width: 100%;
    height: 220px;
    border-radius: 25px;
    border: none;
    outline: none;
    padding: 18px;
    background: white;
    font-size: 16px;
    color: #0f2446;
    resize: none;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}

.report-textarea::placeholder {
    color: #808080;
}

.send-btn {
    background: white;
    border-radius: 100px;
    width: 100%;
    padding: 14px 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: none;
    margin-top: auto;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.send-btn span {
    color: #0f2446;
    font-weight: 700;
    font-size: 14px;
}

.main-icon {
    color: #808080;
    font-size: 18px;
}

.send-btn:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}
</style>
</head>

<body>

<div class="main-wrapper">

<textarea class="report-textarea" placeholder="I need help"></textarea>

<div style="margin-top:auto;">
    <button class="send-btn" onclick="showPopup()">
        <i class="fas fa-paper-plane main-icon"></i>
        <span>Send Report</span>
    </button>
</div>

</div>

<script>
function showPopup(){
    alert("Report sent successfully ✅");
    window.parent.history.back();
}
</script>

</body>
</html>
""", height=500)
