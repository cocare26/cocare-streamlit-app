import streamlit as st

st.set_page_config(page_title="CoCare Settings", layout="centered")

# ---------------- STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = "settings"

def go(page):
    st.session_state.page = page
    st.rerun()

# ---------------- CSS ----------------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}

.block-container {
    max-width:600px;
    margin:auto;
    padding:25px 30px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

/* Title */
.title {
    text-align:center;
    color:#102646;
    font-size:42px;
    font-weight:900;
    margin-bottom:35px;
}

/* Card */
.card {
    width:100%;
    background:white;
    padding:28px 35px;
    border-radius:100px;
    margin-top:22px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    font-size:20px;
    font-weight:800;
    color:#102646;
}

/* Back button */
.stButton > button {
    background:transparent !important;
    border:none !important;
    box-shadow:none !important;
    color:#102646 !important;
    font-size:32px !important;
    font-weight:900 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SETTINGS PAGE ----------------
if st.session_state.page == "settings":

    st.markdown("<div class='title'>Settings</div>", unsafe_allow_html=True)

    if st.button("Contact Us"):
        go("contact")

# ---------------- CONTACT PAGE ----------------
elif st.session_state.page == "contact":

    if st.button("‹"):
        go("settings")

    st.markdown("<div class='title'>Contact Us</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>📧 CoCare26@gmail.com</div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>📞 +962 79 123 4567</div>", unsafe_allow_html=True)
