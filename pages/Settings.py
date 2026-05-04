import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS =====
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
#MainMenu, header, footer { visibility:hidden; }

[data-testid="stAppViewContainer"] { background:#f0f7ff; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

/* 🎯 نخلي الزر شكله زي الكارد */
div.stButton > button {
    width:100%;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    background:white;
    color:#102646;
    font-weight:800;
    font-size:14px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:none;
}

/* hover effect */
div.stButton > button:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* نخلي النص يسار */
div.stButton > button p {
    margin:0;
}
</style>

<h2 style="text-align:center; color:#102646;">Settings</h2>
""", unsafe_allow_html=True)

# ===== BUTTONS =====

if st.button("🔒   Change Password      ›"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐   Change Language      ›"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("✉️   Contact Us      ›"):
    st.switch_page("pages/ContactUs.py")

if st.button("🐞   Report Problem      ›"):
    st.switch_page("pages/ReportProblem.py")
