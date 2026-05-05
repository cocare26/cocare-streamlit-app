import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS =====
==== CSS =====
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI';
}

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

/* ===== HEADER ===== */
.header {
    position:relative;
    text-align:center;
    margin-bottom:30px;
}

/* السهم */
.back-style {
    position:absolute;
    left:0;
    top:0;
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:black !important;
    font-size:26px !important;
    width:auto !important;
    padding:0 !important;
}

/* العنوان */
.title-text {
    font-size:20px;
    font-weight:900;
    color:#102646;
}
.item {
    cursor: pointer;
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
