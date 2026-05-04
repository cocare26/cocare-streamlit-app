import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

.block-container {
    max-width:420px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff);
    border-radius:25px;
    min-height:600px;
}

.title {
    text-align:center;
    font-size:26px;
    font-weight:900;
    color:#102646;
    margin-bottom:30px;
}
</style>
""", unsafe_allow_html=True)


import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

st.title("Settings")

st.page_link("pages/6_Change_Password.py", label="🔒 Change Password")
st.page_link("pages/7_Change_Language.py", label="🌐 Change Language")
st.page_link("pages/8_Rate_App.py", label="⭐ Rate App")
st.page_link("pages/9_Report_Problem.py", label="🐞 Report Problem")
st.page_link("pages/10_Contact_Us.py", label="📞 Contact Us")
st.write("---")

if st.button("🚪 Log Out"):
    st.session_state.clear()
    st.switch_page("pages/0_arabic_app.py")
