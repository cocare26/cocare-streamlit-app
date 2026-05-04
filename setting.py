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
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}

/* شكل الأزرار */
.stButton>button{
    width:100%;
    border:none;
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-weight:600;
    color:#0f2446;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.3s;
}

.stButton>button:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown("<h2 style='text-align:center;color:#0f2446;'>Settings</h2>", unsafe_allow_html=True)

    if st.button("🔒 Change Password   ›"):
        go("pass")

    if st.button("🌍 Change Language   ›"):
        go("lang")

    if st.button("⭐ Rate App   ›"):
        go("rate")

    if st.button("🚪 Log Out   ›"):
        go("logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚠️ Report   ›"):
            go("report")

    with col2:
        if st.button("✉️ Contact   ›"):
            go("contact")

# ================= SUB PAGES =================
else:

    titles = {
        "pass":"Change Password",
        "lang":"Language",
        "rate":"Rate App",
        "logout":"Log Out",
        "report":"Report",
        "contact":"Contact Us"
    }

    title = titles.get(st.session_state.page, "Settings")

    col1, col2 = st.columns([1,4])

    with col1:
        if st.button("←"):
            go("main")

    with col2:
        st.markdown(f"<h3 style='color:#0f2446'>{title}</h3>", unsafe_allow_html=True)

    st.write("---")
    st.write(f"You are in **{title}** page")
