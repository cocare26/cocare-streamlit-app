import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS الموحد والنحيف =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكونتينر النحيف */
.block-container {
    max-width: 390px; 
    margin: auto;
    padding: 35px 20px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

/* تنسيق البوكسات الموحد */
div.stButton > button {
    width: 100% !important;
    min-height: 60px !important; 
    border-radius: 35px !important;
    margin-bottom: 20px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 5px 12px rgba(0,0,0,0.06) !important;
    
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 16px !important;
    
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important; 
    
    padding: 0px 25px !important;
    transition: 0.3s;
}

/* السهم الصغير في النهاية */
div.stButton > button::after {
    content: "›";
    font-size: 26px;
    color: #102646;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #fcfcfc !important;
}

</style>

<div style="text-align:center; font-weight:900; color:#102646; font-size:22px; margin-bottom:25px;">Settings</div>
""", unsafe_allow_html=True)

# ===== الأزرار مع زيادة المسافات لضبط الاستقامة مية بالمية =====

# 1. مسافة للأزرار اللي نصها طويل أصلاً
normal_gap = "&nbsp;" * 10 

if st.button(f"🔒{normal_gap}Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button(f"🌐{normal_gap}Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

# 2. مسافة "إضافية وجبارة" للكلمات القصيرة (Rate و Log) عشان يلحقوا اللي فوقهم
# زدنا الفراغات لـ 55 عشان تندفع الكلمة لأقصى اليمين
extreme_gap = "&nbsp;" * 55

if st.button(f"⭐{extreme_gap}Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button(f"🚪{extreme_gap}Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")
