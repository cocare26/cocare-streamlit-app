import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS الموحد والنحيف =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* حاوية السهم */
.back-btn-container {
    position: absolute;
    right: 10px; 
    top: 5px;   
    z-index: 1001;
}

.back-btn-container .stButton > button {
    background-color: white !important;
    color: #102646 !important;
    width: 45px !important;
    height: 45px !important;
    border-radius: 50% !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-size: 24px !important;
    padding: 0 !important;
}

/* الكونتينر النحيف - تم تقليل البادينج العلوي */
.block-container {
    max-width: 390px; 
    margin: auto;
    /* الرقم الأول (0px) هو المسؤول عن المسافة فوق */
    padding: 0px 20px 35px 20px !important; 
}

/* تنسيق البوكسات */
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

div.stButton > button::after {
    content: "›";
    font-size: 26px;
    color: #102646;
}
</style>

<!-- تم إضافة margin-top:40px هنا لنزول الكلمة -->
<div style="text-align:center; font-weight:900; color:#102646; font-size:22px; margin-top:200px; margin-bottom:25px;">Settings</div>
""", unsafe_allow_html=True)

st.markdown('<div class="back-btn-container">', unsafe_allow_html=True)
if st.button("›", key="top_right_back"):
    st.switch_page("app.py") 
st.markdown('</div>', unsafe_allow_html=True)

# ===== الأزرار مع زيادة المسافات لضبط الاستقامة مية بالمية =====

# 1. مسافة للأزرار اللي نصها طويل أصلاً
normal_gap1 = "&nbsp;" * 45

if st.button(f"🔒{normal_gap1}Change Password"):
    st.switch_page("pages/ChangePassword.py")

normal_gap2 = "&nbsp;" * 43
if st.button(f"🌐{normal_gap2}Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

# 2. مسافة "إضافية وجبارة" للكلمات القصيرة (Rate و Log) عشان يلحقوا اللي فوقهم
# زدنا الفراغات لـ 55 عشان تندفع الكلمة لأقصى اليمين
extreme_gap1 = "&nbsp;" * 63

if st.button(f"⭐{extreme_gap1}Rate App"):
    st.switch_page("pages/RateApp.py")
extreme_gap2 = "&nbsp;" * 64
if st.button(f"🚪{extreme_gap2}Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")


col_gap = "&nbsp;" * 5

col1, col2 = st.columns(2)

with col1:
    if st.button(f"⚠️{col_gap}Report a problem"):
        st.switch_page("pages/ReportProblem.py")

with col2:
    if st.button(f"✉️{col_gap}Contact us"):
        st.switch_page("pages/ContactUs.py")
