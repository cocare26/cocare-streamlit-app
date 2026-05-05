import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث =====
st.markdown("""
<style>
* { direction:rtl; }

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width:430px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

.title {
    text-align:center;
    font-size:22px;
    font-weight:900;
    color:#102646;
    margin-bottom:30px;
}

/* تنسيق الأزرار العامة */
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

/* ===== تنسيق زر الرجوع (الأسود المربع) ===== */
.back-style {
    position: fixed;
    top: 58px;
    right: 25px;
    z-index:999;
}

.back-style .stButton > button {
    background-color: #000000 !important;  /* بوكس أسود سادة */
    color: #ffffff !important;           /* رمز أبيض */
    width: 50px !important;              /* عرض ثابت */
    height: 50px !important;             /* طول ثابت */
    border-radius: 0px !important;       /* شكل مربع تماماً (بدون حواف دائرية) */
    font-size: 30px !important;          /* حجم الرمز */
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border: none !important;
    padding-bottom: 8px !important;      /* لوزن مكان السهم بالمنتصف */
}

div.stButton > button:hover {
    transform:translateY(-2px);
    opacity: 0.9;
}
</style>

<div class="title">تغيير اللغة</div>
""", unsafe_allow_html=True)

# ===== زر رجوع =====
st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("‹"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

# ===== الأزرار =====
if st.button("🌐 العربية ✔️"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

if st.button("🌐 English ‹"):
    st.session_state.lang = "en"
    st.switch_page("pages/Settings.py")
