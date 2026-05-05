import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ✅ تخزين اللغة (افتراضي عربي)
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

# ===== CSS الأساسي =====
st.markdown("""
<style>
/* ضبط الاتجاه للعربية */
* { margin:0; padding:0; box-sizing:border-box; direction:rtl; }

html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff) !important;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* إخفاء الهيدر والفوتر */
#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:420px; /* العرض الذي تفضله */
    margin:auto;
    padding:30px 20px;
    background: white; /* الكبسولة بيضاء والخلفية متدرجة كما طلبت سابقاً */
    border-radius:50px;
    box-shadow:0 15px 45px rgba(0,0,0,.1);
    min-height:620px;
    margin-top: 60px;
}

/* ===== HEADER ===== */
.header {
    position:relative;
    text-align:center;
    margin-bottom:40px;
}

/* سهم الرجوع جهة اليمين في العربية */
.back-style {
    position:absolute;
    right:0;
    top:0;
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:black !important;
    font-size:30px !important;
    width:auto !important;
    padding:0 !important;
    border:none !important;
}

/* العنوان */
.title-text {
    font-size:22px;
    font-weight:900;
    color:#102646;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header">', unsafe_allow_html=True)

# سهم الرجوع
st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("›"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

# عنوان الصفحة
st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== UI (المكونات بلغة HTML) =====
result = components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<style>
body {
    margin:0;
    font-family:'Segoe UI';
    display:flex;
    justify-content:center;
    background: transparent;
}

.wrapper {
    width:100%;
    max-width:380px;
}

/* تصميم الخيارات (Items) */
.item {
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-decoration:none;
    color:#102646;
    font-weight:800;
    transition:0.2s;
    cursor: pointer;
    border: 1px solid #f0f0f0;
}

.item:hover {
    transform:translateY(-2px);
    border-color: #2f80ed;
}

.check-mark {
    color: #102646;
    font-size: 18px;
}
</style>
</head>

<body>

<div class="wrapper">

<!-- خيار اللغة العربية (محدد بـ ✔) -->
<div class="item" onclick="window.parent.history.back();">
    <span>🌐 العربية</span>
    <span class="check-mark">✔</span>
</div>

<!-- خيار اللغة الإنجليزية -->
<div class="item" onclick="window.open('/Settings', '_top');">
    <span>🌐 English</span>
    <span>‹</span>
</div>

</div>

</body>
</html>
""", height=400)
