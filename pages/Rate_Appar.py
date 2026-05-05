import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تقييم التطبيق", layout="centered")

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

/* إخفاء الهيدر الافتراضي */
[data-testid="stHeader"] {display: none !important;}

/* ضبط الاتجاه للعربية */
* { direction: rtl; }

[data-testid="stAppViewContainer"]{ background:#eef2f7; }

.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

/* ===== HEADER ===== */
.header-wrapper {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 40px;
    min-height: 40px;
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
    width:auto !important;
    padding:0 !important;
    border: none !important; /* إزالة الحدود الافتراضية */
}

.title-text {
    font-size:20px;
    font-weight:900;
    color:#0f2446;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header-wrapper">', unsafe_allow_html=True)

st.markdown('<div class="back-style">', unsafe_allow_html=True)
# التعديل الرئيسي هنا
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تقييم التطبيق</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ... (باقي كود components.html يظل كما هو)
