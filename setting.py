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

/* الخلفية */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg,#dcefff,#cfe9ff,#eaf6ff);
}

/* الكارد */
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

/* العنوان */
.header {
    text-align:center;
    font-size:20px;
    font-weight:700;
    margin-bottom:30px;
    color:#0f2446;
}

/* زر الرجوع */
.back-btn button {
    width:50px;
    height:50px;
    border-radius:50%;
    background:#ffffff;
    border:none;
    font-size:20px;
    box-shadow:0 4px 10px rgba(0,0,0,0.1);
}

/* ===== INPUT STYLE مطابق للصورة ===== */
input {
    background:#eaeaea !important;
    color:#000 !important;
    border:none !important;
    border-radius:30px !important;
    padding:14px 18px !important;
    margin-bottom:20px !important;
    font-size:14px !important;

    /* shadow تحت غامق */
    box-shadow:0 6px 0px #2c2f36 !important;
}

/* placeholder */
input::placeholder {
    color:#000 !important;
    opacity:0.6;
}

/* زر الحفظ */
.save-btn {
    position:absolute;
    bottom:30px;
    left:20px;
    right:20px;
}

.save-btn button {
    width:100%;
    border:none;
    background:#e6e6e6;
    border-radius:50px;
    padding:16px;
    font-size:15px;
    color:#0f2446;
    box-shadow:0 6px 15px rgba(0,0,0,0.08);
}

/* hover */
.save-btn button:hover {
    transform:translateY(-2px);
}

</style>
""", unsafe_allow_html=True)

# ================= PAGE =================

if st.session_state.page == "pass":

    # زر رجوع + عنوان
    col1, col2 = st.columns([1,4])

    with col1:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("←"):
            go("main")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="header">Change Password</div>', unsafe_allow_html=True)

    # ===== INPUTS =====
    st.text_input("", placeholder="Current Password")
    st.text_input("", placeholder="New Password")
    st.text_input("", placeholder="Re-write Password")

    # ===== SAVE BUTTON (أسفل الصفحة) =====
    st.markdown('<div class="save-btn">', unsafe_allow_html=True)
    st.button("Save")
    st.markdown('</div>', unsafe_allow_html=True)

# ================= MAIN =================
else:
    st.markdown('<div class="header">Settings</div>', unsafe_allow_html=True)

    if st.button("Change Password"):
        go("pass")
