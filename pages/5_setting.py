import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

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
.setting-item {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    text-decoration:none;
}
.item-left {
    display:flex;
    align-items:center;
    gap:12px;
}
.item-text {
    font-weight:800;
    color:#102646;
}
.arrow {
    font-size:18px;
}
.bottom-row {
    display:flex;
    gap:10px;
    margin-top:40px;
}
.bottom-item {
    flex:1;
    background:white;
    padding:12px;
    border-radius:100px;
    text-align:center;
    text-decoration:none;
}
</style>
""", unsafe_allow_html=True)

st.title("Settings")

# 🔥 بدل JS → استخدم page_link (الأصح)
st.page_link("pages/6_Change_Password.py", label="🔒 Change Password")
st.page_link("pages/7_Change_Language.py", label="🌐 Change Language")
st.page_link("pages/8_Rate_App.py", label="⭐ Rate App")

st.page_link("pages/9_Report_Problem.py", label="🐞 Report Problem")
st.page_link("pages/10_Contact_Us.py", label="📞 Contact Us")

st.page_link("pages/0_arabic_app.py", label="🚪 Log Out")
