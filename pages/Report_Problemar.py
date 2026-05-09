import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تبليغ عن مشكلة", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* إخفاء الهيدر الافتراضي */
[data-testid="stHeader"] {
    display: none !important;
}


* {
    direction: rtl;
}

/* الحاوية الرئيسية - نفس تصميم النسخة الإنجليزية */
.block-container{
    max-width: 430px !important;
    height: 820px !important;
    margin: auto !important;
    padding: 30px !important;
    background: linear-gradient(160deg, var(--bg1), var(--bg2), var(--bg3));
    border-radius: 42px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

/* خلفية التطبيق */
[data-testid="stAppViewContainer"]{
    background: #eef2f7;
}

/* إخفاء الفوتر */
footer {
    visibility: hidden;
}

/* ===== HEADER ===== */
.header {
    position: relative;
    height: 110px;
    margin-bottom: 40px;
}

/* زر الرجوع على اليمين */
.back-style {
    position: absolute;
    right: 0;
    top: 50%;
    transform: translateY(-50%);
}

.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    color: #0f2446 !important;
    font-size: 28px !important;
    border: none !important;
    padding: 0 !important;
    min-width: auto !important;
}

/* العنوان في المنتصف */
.title-text {
    position: absolute;
    transform: translate(-50%, -150%);
    font-size: 20px;
    font-weight: 900;
    color: #0f2446;
    white-space: nowrap;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====

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
    direction: rtl;
}

.main-wrapper {
    width: 100%;
    max-width: 100%;
    height: 480px;
    display: flex;
    flex-direction: column;
}

/* مربع الكتابة - نفس حجم النسخة الإنجليزية */
.report-textarea {
    height: 300px;
    border-radius: 25px;
    border: none;
    outline: none;
    padding: 18px;
    background: white;
    font-size: 16px;
    color: #0f2446;
    resize: none;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    font-family: 'Segoe UI';
    direction: rtl;
    text-align: right;
    box-sizing: border-box;
}

.report-textarea::placeholder {
    color: #808080;
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
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* النص */
.send-btn span {
    color: #0f2446;
    font-weight: 700;
    font-size: 14px;
}

/* الأيقونة */
.main-icon {
    color: #808080;
    font-size: 18px;
}

/* hover */
.send-btn:hover {
    transform: translateY(-8px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

/* نفس المسافات الموجودة بالنسخة الإنجليزية */
.btn-container {
    margin-top: 20px;
    margin-bottom: 40px;
}
</style>
</head>

<body>

<div class="main-wrapper">

<textarea class="report-textarea" placeholder="أنا بحاجة للمساعدة"></textarea>

<div class="btn-container">
    <button class="send-btn" onclick="showPopup()">
        <i class="fas fa-paper-plane main-icon"></i>
        <span>إرسال التقرير</span>
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
