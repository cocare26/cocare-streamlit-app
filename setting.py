import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

def go(page):
    st.session_state.page = page
    st.rerun()

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
    min-height:650px;
}

/* header */
.header {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}

/* ===== SETTINGS ROW ===== */
.row {
    background:#ffffff;
    border-radius:50px;
    padding:14px 18px;
    margin-bottom:12px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
    cursor:pointer;
}

.left {
    display:flex;
    align-items:center;
    gap:10px;
    font-weight:600;
    color:#0f2446;
}

.icon {
    font-size:16px;
}

.arrow {
    font-size:18px;
    color:#0f2446;
}

/* ===== INPUT ===== */
.input-box {
    background:#ffffff;
    border-radius:40px;
    padding:14px 18px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:20px;
    box-shadow:0 6px 0px #2c2f36;
}

.input-box input {
    border:none;
    outline:none;
    background:transparent;
    width:100%;
    font-size:14px;
    color:#000;
}

.lock {
    color:#d8c7a0;
}

.eye {
    color:#555;
}

/* ===== BUTTON ===== */
.stButton > button {
    width:100%;
    border:none;
    background:#ffffff;
    border-radius:50px;
    padding:14px;
    font-size:14px;
    color:#000;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}

/* save */
.save-wrap {
    margin-top:40px;
    display:flex;
    justify-content:center;
}

.save-wrap button {
    width:180px;
    padding:16px;
    font-size:16px;
    border-radius:50px;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown('<div class="header">Settings</div>', unsafe_allow_html=True)

    if st.button("🔒  Change Password   ›"):
        go("pass")

    if st.button("🌐  Change Language   ›"):
        go("lang")

    if st.button("⭐  Rate App   ›"):
        go("rate")

    if st.button("🚪  Log Out   ›"):
        go("logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚠️ Report"):
            go("report")

    with col2:
        if st.button("✉️ Contact"):
            go("contact")

# ================= PASSWORD =================
elif st.session_state.page == "pass":

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown('<div class="header">Change Password</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="input-box">
        <span class="lock">🔒</span>
        <input placeholder="Current Password">
        <span class="eye">👁</span>
    </div>

    <div class="input-box">
        <span class="lock">🔒</span>
        <input placeholder="New Password">
        <span class="eye">👁</span>
    </div>

    <div class="input-box">
        <span class="lock">🔒</span>
        <input placeholder="Re-write New Password">
        <span class="eye">👁</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="save-wrap">', unsafe_allow_html=True)
    st.button("Save")
    st.markdown('</div>', unsafe_allow_html=True)

# ================= LANGUAGE =================
elif st.session_state.page == "lang":

    st.markdown('<div class="header">Change Language</div>', unsafe_allow_html=True)

    st.button("English")
    st.button("العربية")

# ================= RATE =================
elif st.session_state.page == "rate":

    st.markdown('<div class="header">Rate App</div>', unsafe_allow_html=True)

    st.button("Google Play Store")
    st.button("Apple App Store")
    st.button("Huawei AppGallery")

# ================= LOGOUT =================
elif st.session_state.page == "logout":

    st.markdown('<div class="header">Log Out</div>', unsafe_allow_html=True)

    st.warning("Are you sure?")
    st.button("Confirm Logout")

# ================= REPORT =================
elif st.session_state.page == "report":

    st.markdown('<div class="header">Report</div>', unsafe_allow_html=True)

    st.text_area("", placeholder="I need help")
    st.button("Send Report")

# ================= CONTACT =================
elif st.session_state.page == "contact":

    st.markdown('<div class="header">Contact Us</div>', unsafe_allow_html=True)

    st.write("📧 CoCare26@gmail.com")
    st.write("📞 +962 79 123 4567")
