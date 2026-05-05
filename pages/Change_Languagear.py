import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث =====
st.markdown("""
<style>
* { direction:rtl; }

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكبسولة */
.block-container {
    max-width:430px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    position: relative; /* ضروري لضبط موقع السهم داخلياً */
    margin-top: 50px;
}

/* العنوان */
.title {
    text-align:center;
    font-size:22px;
    font-weight:900;
    color:#102646;
    margin-top: 20px; /* مسافة بسيطة من الأعلى */
    margin-bottom:30px;
}

/* ===== تنسيق زر الرجوع (المربع الأسود في أول الصفحة) ===== */
.back-style {
    position: absolute; /* يجعله مرتبطاً بأعلى الكبسولة */
    top: 20px;
    right: 20px;
    z-index: 999;
}

.back-style .stButton > button {
    background-color: #000000 !important;
    color: #ffffff !important;
    width: 45px !important;
    height: 45px !important;
    border-radius: 0px !important; /* مربع حاد */
    font-size: 24px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: none !important;
    padding: 0 !important;
    line-height: 0 !important;
}

/* الأزرار العامة */
div.stButton > button {
    width:100%;
    height:65px;
    border-radius:100px;
    background:white;
    border:none;
    color:#102646;
    font-weight:800;
    font-size:18px;
    margin-bottom:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

div.stButton > button:hover {
    transform:translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الصفحة =====

# زر الرجوع في أول الكبسولة
st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("‹"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title">تغيير اللغة</div>', unsafe_allow_html=True)

# الأزرار
if st.button("🌐 العربية ✔️"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English ‹"):
    st.switch_page("pages/Settings.py")
