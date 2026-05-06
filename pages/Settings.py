import streamlit as st


from language_guard import check_language

check_language(__file__.split("\\")[-1])



st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS الموحد والنحيف =====
st.markdown("""
<style>

.title {
    text-align: center;
    font-weight: 900;
    color: #102646;
    font-size: 22px;
}

div.stButton > button {
    width: 100% !important;
    min-height: 65px !important;

    border-radius: 35px !important;
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
}

#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* شكل زر السهم */
.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 28px !important;
    padding: 0 !important;
}

.back-style {
    position: absolute;
    top: 0px;
    right: 0px;
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

/* الكونتينر النحيف */
.block-container {
    max-width: 390px; 
    margin: auto;
    padding-top: 80px !important;
    padding-left: 20px !important;
    padding-right: 20px !important;
    padding-bottom: 35px !important;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
}

/* تنسيق البوكسات */
div.stButton > button {
    width: 100% !important;
    min-height: 65px !important;

    border-radius: 35px !important;
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
}

div.stButton > button::after {
    content: "›";
    font-size: 26px;
    color: #102646;
}

/* الهيدر الجديد */
.header-title {
    text-align:center;
    font-weight:900;
    color:#102646;
    font-size:22px;
    margin-top:8px;
    margin-bottom:25px;
}

</style>

<div style="display:none;">Settings</div>
""", unsafe_allow_html=True)

# ===== الهيدر: السهم مع Settings بنفس السطر =====
col_back, col_title, col_empty = st.columns([1, 6, 1])

with col_back:
    if st.button("›", key="top_right_back"):
        st.switch_page("pages/2_Customer.py")

with col_title:
    st.markdown('<div class="header-title">Settings</div>', unsafe_allow_html=True)

# ===== الأزرار مع زيادة المسافات لضبط الاستقامة مية بالمية =====

normal_gap1 = "&nbsp;" * 45

if st.button(f"🔒{normal_gap1}Change Password"):
    st.switch_page("pages/ChangePassword.py")

normal_gap2 = "&nbsp;" * 43
if st.button(f"🌐{normal_gap2}Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

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
