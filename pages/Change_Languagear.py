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
    margin-top:50px;   /* 👈 نزّلناها كثير */
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
    top: 20px;   /* 👈 كان 58، هسا ارتفع */
    right: 25px;
    z-index:999;
}

.back-style .stButton > button {
    background:#111827 !important;
    color:white !important;
    width:45px !important;
    height:60px !important;
    border-radius:10px !important;
    font-size:28px !important;
    padding:0 !important;
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
col_gap_ar = "&nbsp;" * 40
col_gap_en = "&nbsp;" * 40
# عربي
if st.button(f"🌐  العربية  {col_gap_ar} {col_gap_ar}✔️"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

# إنجليزي
if st.button(f"🌐  English {col_gap_en} {col_gap_en} ‹"):
    st.session_state.lang = "en"
    st.switch_page("pages/Settings.py")







