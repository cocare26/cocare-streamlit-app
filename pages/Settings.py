import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS المحدث: عرض أقل ومسافة أكبر =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* 1. تقليل عرض الكونتينر ليصبح أنحف */
.block-container {
    max-width: 380px; /* صغرنا العرض من 500 لـ 380 */
    margin: auto;
    padding: 40px 20px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
}

/* 2. تنسيق البوكسات */
div.stButton > button {
    width: 100% !important;
    min-height: 95px !important; 
    border-radius: 45px !important;
    margin-bottom: 20px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 8px 15px rgba(0,0,0,0.08) !important;
    
    font-weight: 800 !important;
    color: #102646 !important;
    font-size: 18px !important;
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    
    /* 3. زيادة المسافة بين الإيموجي والنص أكثر (زدناها لـ 90) */
    gap: 90px !important; 
    
    padding: 0px 30px !important;
    transition: 0.3s;
}

/* السهم في النهاية */
div.stButton > button::after {
    content: "›";
    font-size: 28px;
    color: #102646;
    margin-left: auto;
}

div.stButton > button:hover {
    transform: scale(1.02);
    background-color: #fff !important;
}

</style>
<div style="text-align:center; font-weight:900; color:#102646; font-size:24px; margin-bottom:30px;">Settings</div>
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
