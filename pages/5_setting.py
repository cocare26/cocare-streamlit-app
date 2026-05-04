import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS (اختياري للتنسيق) =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

.block-container {
    max-width:430px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff);
    border-radius:30px;
    min-height:600px;
}

.title {
    text-align:center;
    font-size:26px;
    font-weight:900;
    color:#102646;
    margin-bottom:25px;
}
</style>
""", unsafe_allow_html=True)

# ===== Title =====
st.markdown("<div class='title'>Settings ⚙️</div>", unsafe_allow_html=True)

# ===== Navigation (IMPORTANT FIX) =====
st.page_link("6_Change_Password", label="🔒 Change Password")
st.page_link("7_Change_Language", label="🌐 Change Language")
st.page_link("8_Rate_App", label="⭐ Rate App")
st.page_link("9_Report_Problem", label="🐞 Report Problem")
st.page_link("10_Contact_Us", label="📞 Contact Us")

st.write("---")

# ===== Logout =====
if st.button("🚪 Log Out"):
    st.session_state.clear()
    st.switch_page("0_arabic_app")
