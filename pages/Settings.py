import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS لتوسيع المسافة بين الإيموجي والنص =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width:450px;
    margin:auto;
    padding:40px 25px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 20px 40px rgba(0,0,0,0.15);
}

/* تنسيق الزر ليسمح بمسافات كبيرة */
div.stButton > button {
    width: 100% !important;
    min-height: 90px !important;
    border-radius: 45px !important;
    margin-bottom: 25px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.08) !important;
    
    font-weight: 800 !important;
    color: #102646 !important;
    font-size: 18px !important;
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important; 
    
    /* 👇 زدنا المسافة (gap) بشكل كبير كما طلبت 👇 */
    gap: 60px !important; 
    
    padding: 0px 40px !important;
    transition: 0.3s;
}

/* السهم الصغير في نهاية البوكس */
div.stButton > button::after {
    content: "›";
    font-size: 28px;
    color: #ccc; /* لون خفيف للسهم عشان يبرز النص */
    margin-left: auto; 
}

div.stButton > button:hover {
    background-color: #fcfcfc !important;
    transform: translateY(-2px);
}

</style>
<div class="title" style="text-align:center; font-weight:900; color:#102646; font-size:26px; margin-bottom:30px;">Settings</div>
""", unsafe_allow_html=True)

# ===== البوكسات بالمسافات المطلوبة =====

if st.button("🔒 Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐 Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("⭐ Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button("🚪 Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")
