import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ---------------- TEXT ----------------
T = {
    "settings": "Settings",
    "pass": "Change Password",
    "lang": "Change Language",
    "rate": "Rate App",
    "logout": "Log Out",
    "report": "Report a Problem",
    "contact": "Contact Us",
}

# ---------------- STYLE ----------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg,#dcefff,#cfe9ff,#eaf6ff);
}

.block-container {
    max-width:370px;
    margin:auto;
    padding:30px 20px;
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(10px);
    border-radius:40px;
}

.header {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}

/* 🔥 التعديل هون */
.stButton > button {
    width:100%;
    border:none;
    background:#ffffff;
    border-radius:50px;
    padding:16px;
    margin-bottom:12px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-size:14px;
    color:#0f2446;
    box-shadow:0 6px 15px rgba(0,0,0,0.08);

    direction: ltr;
}

.stButton > button p {
    width:100%;
    display:flex;
    justify-content:space-between;
    margin:0;
}

.stButton > button:hover {
    transform:translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================

st.markdown(f"<div class='header'>{T['settings']}</div>", unsafe_allow_html=True)

# 🔒 Password
if st.button(f"🔒 {T['pass']}"):
    st.switch_page("pages/Change_Password.py")

# 🌐 Language
if st.button(f"🌐 {T['lang']}"):
    st.switch_page("pages/Language.py")

# ⭐ Rate App
if st.button(f"⭐ {T['rate']}"):
    st.switch_page("pages/Rate_App.py")

# 🚪 Logout
if st.button(f"🚪 {T['logout']}"):
    st.session_state.clear()
    st.switch_page("app.py")

col1, col2 = st.columns(2)

# ⚠️ Report
with col1:
    if st.button(f"⚠️ {T['report']}"):
        st.switch_page("pages/Report.py")

# ✉️ Contact
with col2:
    if st.button(f"✉️ {T['contact']}"):
        st.switch_page("pages/Contact.py")
