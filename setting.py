import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "main"

# حالة إظهار/إخفاء لكل حقل
for k in ["show1", "show2", "show3"]:
    if k not in st.session_state:
        st.session_state[k] = False

def go(page):
    st.session_state.page = page
    st.rerun()

def toggle(key):
    st.session_state[key] = not st.session_state[key]

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

/* input style */
.stTextInput > div > div > input {
    background:#ffffff !important;
    border-radius:40px !important;
    padding:14px !important;
    border:none !important;
    color:#000 !important;
    box-shadow:0 6px 0px #2c2f36;
}

/* icon */
.icon {
    font-size:16px;
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

/* buttons */
.stButton > button {
    border:none;
    background:#ffffff;
    border-radius:50px;
    padding:10px 14px;
    color:#000;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown('<div class="header">Settings</div>', unsafe_allow_html=True)

    if st.button("🔒  Change Password   ›"):
        go("pass")

# ================= PASSWORD =================
elif st.session_state.page == "pass":

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown('<div class="header">Change Password</div>', unsafe_allow_html=True)

    # -------- INPUT 1 --------
    c1, c2, c3 = st.columns([1,6,1])
    with c1:
        st.markdown("🔒")
    with c2:
        st.text_input(
            "",
            placeholder="Current Password",
            key="p1",
            type="default" if st.session_state.show1 else "password"
        )
    with c3:
        if st.button("👁", key="eye1"):
            toggle("show1")

    # -------- INPUT 2 --------
    c1, c2, c3 = st.columns([1,6,1])
    with c1:
        st.markdown("🔒")
    with c2:
        st.text_input(
            "",
            placeholder="New Password",
            key="p2",
            type="default" if st.session_state.show2 else "password"
        )
    with c3:
        if st.button("👁", key="eye2"):
            toggle("show2")

    # -------- INPUT 3 --------
    c1, c2, c3 = st.columns([1,6,1])
    with c1:
        st.markdown("🔒")
    with c2:
        st.text_input(
            "",
            placeholder="Re-write New Password",
            key="p3",
            type="default" if st.session_state.show3 else "password"
        )
    with c3:
        if st.button("👁", key="eye3"):
            toggle("show3")

    # SAVE
    st.markdown('<div class="save-wrap">', unsafe_allow_html=True)
    st.button("Save")
    st.markdown('</div>', unsafe_allow_html=True)
