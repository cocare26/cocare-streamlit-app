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
    max-width:340px !important;
    margin:auto !important;
    padding:25px !important;
    background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}

/* الزر */
.stButton > button{
    width:100%;
    border:none;
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:14px;
    text-align:left;
    font-weight:600;
    color:#0f2446;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.25s;
    font-size:14px;
    position:relative;
}

/* السهم */
.stButton > button::after{
    content:"›";
    position:absolute;
    right:18px;
    font-size:18px;
}

/* hover */
.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* الهيدر */
.header{
    text-align:center;
    font-weight:900;
    font-size:20px;
    margin-bottom:30px;
    color:#0f2446;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown("<div class='header'>Settings</div>", unsafe_allow_html=True)

    if st.button("🔒   Change Password"):
        go("pass")

    if st.button("🌍   Change Language"):
        go("lang")

    if st.button("⭐   Rate App"):
        go("rate")

    if st.button("🚪   Log Out"):
        go("logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚠️ Report"):
            go("report")

    with col2:
        if st.button("✉️ Contact"):
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
        st.markdown(f"<div class='header'>{title}</div>", unsafe_allow_html=True)

    st.write("")

    # -------- محتوى الصفحات --------

    if st.session_state.page == "pass":
        st.text_input("Current Password", type="password")
        st.text_input("New Password", type="password")
        st.text_input("Confirm Password", type="password")
        st.button("Save")

    elif st.session_state.page == "lang":
        st.radio("Select Language", ["English", "Arabic"])
        st.button("Apply")

    elif st.session_state.page == "rate":
        st.slider("Your Rating", 1, 5)
        st.text_area("Feedback")
        st.button("Submit")

    elif st.session_state.page == "logout":
        st.warning("Are you sure you want to log out?")
        st.button("Confirm Logout")

    elif st.session_state.page == "report":
        st.text_area("Describe the issue")
        st.button("Send Report")

    elif st.session_state.page == "contact":
        st.text_input("Email")
        st.text_area("Message")
        st.button("Send")
