import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS المحدث: سماكة أقل (أنحف) ومسافة كبيرة =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكونتينر النحيف */
.block-container {
    max-width: 380px; 
    margin: auto;
    padding: 35px 20px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

/* تنسيق البوكسات (الأزرار) */
div.stButton > button {
    width: 100% !important;
    
    /* 👇 تخفيف السماكة: قللنا الارتفاع من 95 لـ 60 👇 */
    min-height: 60px !important; 
    
    border-radius: 30px !important; /* تقليل الانحناء ليناسب السماكة الجديدة */
    margin-bottom: 18px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 5px 12px rgba(0,0,0,0.06) !important;
    
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 16px !important;
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    
    /* المسافة بين الإيموجي والنص */
    gap: 75px !important; 
    
    padding: 0px 25px !important;
}

/* السهم الصغير */
div.stButton > button::after {
    content: "›";
    font-size: 24px;
    color: #102646;
    margin-left: auto;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #fcfcfc !important;
}

</style>
<div style="text-align:center; font-weight:900; color:#102646; font-size:22px; margin-bottom:25px;">Settings</div>
""", unsafe_allow_html=True)

# ===== الأزرار =====

if st.button("🔒 Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐 Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("⭐ Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button("🚪 Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")
