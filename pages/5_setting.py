import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

.title {
    text-align:center;
    color:#102646;
    font-weight:900;
    margin-bottom:30px;
}

.btn {
    background:white;
    padding:14px 20px;
    border-radius:100px;
    margin-bottom:12px;
    text-align:center;
    font-weight:700;
    color:#102646;
    text-decoration:none;
    display:block;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}

.btn:hover {
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 class='title'>Settings</h2>", unsafe_allow_html=True)

# 🔥 التنقل الصحيح (بدون JS)

if st.button("🔒 Change Password"):
    st.query_params["page"] = "Change_password-ar"
    st.rerun()

if st.button("🌐 Change Language"):
    st.query_params["page"] = "Change_language-ar"
    st.rerun()

if st.button("⭐ Rate App"):
    st.query_params["page"] = "Rate_app-ar"
    st.rerun()

if st.button("🐞 Report Problem"):
    st.query_params["page"] = "Report_Problem-ar"
    st.rerun()

if st.button("📞 Contact Us"):
    st.query_params["page"] = "Contact_Us-ar"
    st.rerun()

if st.button("🚪 Log Out"):
    st.session_state.clear()
    st.query_params.clear()
    st.switch_page("pages/0_arabic_app.py")
