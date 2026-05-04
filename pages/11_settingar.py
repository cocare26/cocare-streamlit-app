import streamlit as st

st.set_page_config(page_title="الإعدادات", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

def go(page):
    st.session_state.page = page
    st.rerun()

# ---------------- TEXT ----------------
T = {
    "settings": "الإعدادات",
    "pass": "تغيير كلمة المرور",
    "lang": "تغيير اللغة",
    "rate": "تقييم التطبيق",
    "logout": "تسجيل الخروج",
    "report": "الإبلاغ عن مشكلة",
    "contact": "تواصل معنا",
    "save": "حفظ",
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
    height:600px;
}

body {
    direction: rtl;
}

.header {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}

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
}

.stButton > button:hover {
    transform:translateY(-2px);
}

input {
    border-radius:30px !important;
    padding:12px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}

textarea {
    border-radius:20px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}

.card {
    background:white;
    padding:15px;
    border-radius:25px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    margin-bottom:15px;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown(f"<div class='header'>{T['settings']}</div>", unsafe_allow_html=True)

    if st.button(f"🔒 {T['pass']}"):
        go("pass")

    if st.button(f"🌐 {T['lang']}"):
        st.switch_page("pages/7_Change_Language.py")

    if st.button(f"⭐ {T['rate']}"):
        go("rate")

    if st.button(f"🚪 {T['logout']}"):
        st.session_state.clear()
        st.switch_page("app.py")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"⚠️ {T['report']}"):
            go("report")

    with col2:
        if st.button(f"✉️ {T['contact']}"):
            go("contact")

# ================= SUB =================
else:

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("→"):
            go("main")

    with col2:
        st.markdown(f"<div class='header'>{T[st.session_state.page]}</div>", unsafe_allow_html=True)
