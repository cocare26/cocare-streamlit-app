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
    position:relative;
}

/* header */
.header {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:25px;
    color:#0f2446;
}

/* input */
.stTextInput > div > div > input {
    background:#e9e9e9 !important;
    border-radius:40px !important;
    padding:14px !important;
    border:none !important;
    color:#000 !important;
    box-shadow:0 6px 0px #2c2f36;
}

/* icon */
.icon {
    font-size:16px;
    opacity:0.6;
}

/* row layout */
.row {
    display:flex;
    align-items:center;
    gap:10px;
    margin-bottom:20px;
}

/* button (ALL WHITE) */
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

# ================= PASSWORD =================
elif st.session_state.page == "pass":

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown('<div class="header">Change Password</div>', unsafe_allow_html=True)

    # ---- INPUT 1 ----
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.markdown('<div class="icon">🔒</div>', unsafe_allow_html=True)
    with col2:
        st.text_input("", placeholder="Current Password", key="p1", type="password")
    with col3:
        st.markdown('<div class="icon">👁️</div>', unsafe_allow_html=True)

    # ---- INPUT 2 ----
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.markdown('<div class="icon">🔒</div>', unsafe_allow_html=True)
    with col2:
        st.text_input("", placeholder="New Password", key="p2", type="password")
    with col3:
        st.markdown('<div class="icon">👁️</div>', unsafe_allow_html=True)

    # ---- INPUT 3 ----
    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.markdown('<div class="icon">🔒</div>', unsafe_allow_html=True)
    with col2:
        st.text_input("", placeholder="Re-write New Password", key="p3", type="password")
    with col3:
        st.markdown('<div class="icon">👁️</div>', unsafe_allow_html=True)

    # SAVE BUTTON
    st.markdown('<div class="save-wrap">', unsafe_allow_html=True)
    st.button("Save")
    st.markdown('</div>', unsafe_allow_html=True)
