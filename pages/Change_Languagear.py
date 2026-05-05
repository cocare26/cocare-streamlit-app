import streamlit as st
import os

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== DEBUG (عشان نتأكد من أسماء الملفات) =====

# ===== CSS =====
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

/* العنوان */
.title {
    text-align:center;
    font-size:22px;
    font-weight:900;
    color:#102646;
    margin-bottom:30px;
}

/* الأزرار */
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
    text-align:right;
}


.back-style {
    position: fixed;
    top: 58px;
    right: 25px;
    z-index:999;
}

.back-style .stButton > button {
    background:#111827 !important;   /* لون أسود */
    color:white !important;          /* سهم أبيض */
    
    width:50px !important;           /* عرض مربع */
    height:50px !important;          /* طول مربع */

    border-radius:12px !important;   /* زوايا ناعمة زي الصورة */

    font-size:26px !important;       /* حجم السهم */
    font-weight:900 !important;

    display:flex !important;
    align-items:center !important;
    justify-content:center !important;

    padding:0 !important;
    border:none !important;
}

div.stButton > button:hover {
    transform:translateY(-2px);
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

# عربي
if st.button("🌐 العربية ✔️"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

# إنجليزي
if st.button("🌐 English ‹"):
    st.session_state.lang = "en"
    st.switch_page("pages/Settings.py")
