import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS =====
st.markdown("""
<style>

/* اتجاه عربي */
* { direction:rtl; }

/* الخلفية */
[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكونتينر */
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
    height:85px !important; 
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

/* ===== زر السهم ===== */
.back-style {
    position: fixed;
    top: 60px;
    right: 25px;
    z-index:999;
}

/* كسر ستايل Streamlit */
.back-style .stButton button {
    all: unset !important;

    background:#111827 !important;
    color:white !important;

    width:50px !important;
    height:50px !important;

    border-radius:12px !important;

    display:flex !important;
    align-items:center !important;
    justify-content:center !important;

    font-size:28px !important;
    font-weight:900 !important;

    cursor:pointer !important;

    box-shadow:0 6px 15px rgba(0,0,0,0.25);
}

/* Hover */
.back-style button:hover {
    transform:scale(1.05);
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
