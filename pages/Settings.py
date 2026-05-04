import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS =====
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
#MainMenu, header, footer { visibility:hidden; }

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* container */
.block-container {
    max-width:430px;
    margin:auto;
    padding:20px 16px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

/* TITLE */
.title {
    text-align:center;
    font-weight:900;
    font-size:20px;
    color:#102646;
    margin-bottom:25px;
}

/* زر = كارد */
div.stButton > button {
    width:100%;
    border-radius:100px;
    padding:16px;
    margin-bottom:15px;
    background:white;
    border:none;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    font-weight:800;
    color:#102646;
    text-align:left;
    transition:0.2s;
}

/* hover */
div.stButton > button:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* arrow */
div.stButton > button::after {
    content: "›";
    float:right;
    font-size:18px;
}

/* bottom */
.bottom-row {
    display:flex;
    gap:10px;
    margin-top:40px;
}

.bottom-row div.stButton > button {
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
    st.switch_page("main_app.py")

# ===== bottom =====
col1, col2 = st.columns(2)

with col1:
    if st.button("Report Problem"):
        st.switch_page("pages/ReportProblem.py")

with col2:
    if st.button("Contact Us"):
        st.switch_page("pages/ContactUs.py")
