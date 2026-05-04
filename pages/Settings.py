import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer { visibility:hidden; }
[data-testid="stAppViewContainer"] { background:#f0f7ff; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:30px;
}

.btn {
    width:100%;
    padding:14px;
    margin-bottom:12px;
    border-radius:30px;
    border:none;
    background:white;
    font-weight:bold;
    cursor:pointer;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center'>Settings</h2>", unsafe_allow_html=True)

# ========= BUTTONS =========

if st.button("🔒 Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐 Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("✉️ Contact Us"):
    st.switch_page("pages/ContactUs.py")

if st.button("🐞 Report Problem"):
    st.switch_page("pages/ReportProblem.py")
