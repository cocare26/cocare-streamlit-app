import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS شكل الصفحة =====
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

.card {
    background:white;
    padding:14px;
    margin-bottom:12px;
    border-radius:100px;
    text-align:center;
    font-weight:700;
    color:#102646;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ===== Title =====
st.markdown("<div class='title'>Settings ⚙️</div>", unsafe_allow_html=True)

# ===== Navigation (الأهم) =====

st.page_link("pages/6_Change_Password.py", label="🔒 Change Password")

st.page_link("pages/7_Change_Language.py", label="🌐 Change Language")

st.page_link("pages/8_Rate_App.py", label="⭐ Rate App")

st.page_link("pages/9_Report_Problem.py", label="🐞 Report Problem")

st.page_link("pages/10_Contact_Us.py", label="📞 Contact Us")

st.write("---")

# ===== Logout =====
if st.button("🚪 Log Out"):
    st.session_state.clear()
    st.switch_page("pages/0_arabic_app.py")
