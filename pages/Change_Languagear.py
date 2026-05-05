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

div.stButton > button:hover {
    transform:translateY(-2px);
}
</style>

<div class="title">تغيير اللغة</div>
""", unsafe_allow_html=True)

# ===== زر رجوع =====
if st.button("› رجوع"):
    st.switch_page("pages/settingar.py")

# ===== الأزرار =====

# عربي
if st.button("🌐 العربية ✔"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

# إنجليزي
if st.button("🌐 English ‹"):
    st.session_state.lang = "en"
    st.switch_page("pages/Settings.py")
