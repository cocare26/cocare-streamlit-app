import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS =====
st.markdown("""
<style>

div.stButton > button {
    width:100%;
    border-radius:100px;
    padding:18px;

#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكونتينر */
.block-container {
    max-width:420px;
    margin:auto;
    padding:30px 20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 20px 40px rgba(0,0,0,.15);
}

/* العنوان */
.title {
    text-align:center;
    font-size:22px;
    font-weight:900;
    color:#102646;
    margin-bottom:30px;
}

/* الأزرار الرئيسية */
div.stButton > button {
    width:100%;
    border-radius:100px;
    padding:18px;
    margin-bottom:18px;
    background:white;
    border:none;
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
    font-weight:800;
    color:#102646;
    text-align:left;
    font-size:15px;
    transition:0.25s;
}

div.stButton:nth-of-type(-n+4) > button {
    padding-left: 50px !important;
}

/* hover */
div.stButton > button:hover {
    transform:translateY(-4px);
    box-shadow:0 10px 20px rgba(0,0,0,0.15);
}

/* السهم */
div.stButton > button::after {
    content: "›";
    float:right;
    font-size:18px;
}

/* الصف السفلي */
.bottom-row {
    display:flex;
    gap:15px;
    margin-top:30px;
}

/* أزرار تحت */
.bottom-row div.stButton > button {
    width:100%;
    text-align:center;
}

</style>

<div class="title">Settings</div>
""", unsafe_allow_html=True)
# ===== buttons =====
if st.button("🔒  Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐  Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("⭐  Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button("🚪  Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")

# ===== bottom =====

st.markdown('<div class="bottom-row">', unsafe_allow_html=True) 

col1, col2 = st.columns(2)

with col1:
    if st.button("Report Problem"):
        st.switch_page("pages/ReportProblem.py")

with col2:
    if st.button("Contact Us"):
        st.switch_page("pages/ContactUs.py")
        
        
st.markdown('</div>', unsafe_allow_html=True)
