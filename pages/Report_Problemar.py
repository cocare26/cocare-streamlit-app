import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تبليغ عن مشكلة", layout="centered")

st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}
* { direction: rtl; }

.block-container{
    max-width:350px !important;    
    margin:auto !important;
    padding:30px !important;            
    background:linear-gradient(160deg, var(--bg1), var(--bg2), var(--bg3));
    border-radius:42px;            
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}

[data-testid="stAppViewContainer"]{ background:#eef2f7; }

/* ===== HEADER ===== */
.header-wrapper {
    position: relative;
    height: 50px;
    margin-bottom: 40px;
}

.back-style {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:#0f2446 !important;
    font-size:28px !important;
    border:none !important;
}

/* العنوان */
.title-text {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -70%);
    font-size:20px;
    font-weight:900;
    color:#0f2446;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)

st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تبليغ عن مشكلة</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== UI =====
components.html("""
<!DOCTYPE html>
<html dir="rtl">
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
    padding: 18px; 
    background: white; 
    font-size: 16px; 
    box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
}

/* زر الإرسال */
.send-btn { 
    background: white; 
    border-radius: 100px; 
    width: 100%; 
    padding: 14px 22px; 
    display: flex; 
    align-items: center; 
    justify-content: space-between; 
    border: none; 
    cursor: pointer; 
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    transition: all 0.3s ease;
}

/* hover */
.send-btn:hover {
    transform: translateY(-6px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* النص */
.send-btn span { 
    color: #0f2446; 
    font-weight: 700; 
}

/* الأيقونة */
.main-icon { 
    color: #808080; 
    font-size: 18px;
    margin-left: 10px;
}

/* 👇 رفع الزر لفوق */
.btn-container {
    margin-top: 90px;
}
</style>
</head>

<body>
<div class="main-wrapper">

    <textarea class="report-textarea" placeholder="أنا بحاجة للمساعدة..."></textarea>

    <div class="btn-container">
        <button class="send-btn" onclick="showPopup()">
            <span>إرسال التقرير</span>
            <i class="fas fa-paper-plane main-icon"></i>
        </button>
    </div>

</div>

<script>
function showPopup(){
    alert("تم إرسال التقرير بنجاح ✅");
    window.parent.history.back();
}
</script>

</body>
</html>
""", height=500)
