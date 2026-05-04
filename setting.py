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
    min-height:600px;
}

/* header */
.header {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}

/* custom input container */
.input-box {
    background:#ffffff;
    border-radius:40px;
    padding:12px 15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:18px;
    box-shadow:0 6px 0px #2c2f36;
}

/* text input */
.input-box input {
    border:none;
    outline:none;
    background:transparent;
    width:100%;
    font-size:14px;
    color:#000;
}

/* icons */
.icon {
    opacity:0.6;
    font-size:15px;
}

/* button */
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

/* save button */
.save-wrap {
    margin-top:20px;
    display:flex;
    justify-content:flex-start;
}

.save-wrap button {
    width:120px;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown('<div class="header">Settings</div>', unsafe_allow_html=True)

    if st.button("Change Password"):
        go("pass")

    if st.button("Change Language"):
        go("lang")

    if st.button("Rate App"):
        go("rate")

    if st.button("Log Out"):
        go("logout")

# ================= PASSWORD =================
elif st.session_state.page == "pass":

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown('<div class="header">Change Password</div>', unsafe_allow_html=True)

    # ---- INPUTS ----
    st.markdown("""
    <div class="input-box">
        <span class="icon">🔒</span>
        <input placeholder="Current Password">
        <span class="icon">👁️</span>
    </div>

    <div class="input-box">
        <span class="icon">🔒</span>
        <input placeholder="New Password">
        <span class="icon">👁️</span>
    </div>

    <div class="input-box">
        <span class="icon">🔒</span>
        <input placeholder="Re-write New Password">
        <span class="icon">👁️</span>
    </div>
    """, unsafe_allow_html=True)

    # SAVE
    st.markdown('<div class="save-wrap">', unsafe_allow_html=True)
    st.button("Save")
    st.markdown('</div>', unsafe_allow_html=True)

# ================= LANGUAGE =================
elif st.session_state.page == "lang":

    st.markdown('<div class="header">Language</div>', unsafe_allow_html=True)

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
