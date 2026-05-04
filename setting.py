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

/* Button reset */
.stButton > button{
    width:100%;
    border:none;
    background:white;
    border-radius:100px;
    padding:0px;
    margin-bottom:14px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.25s;
}

/* Hover */
.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* Inner content */
.btn-row{
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:14px 18px;
    font-family:'Segoe UI';
    font-weight:600;
    color:#0f2446;
}

/* left side */
.left{
    display:flex;
    align-items:center;
    gap:12px;
}

/* icon */
.icon{
    font-size:16px;
}

/* arrow */
.arrow{
    font-size:18px;
}

/* header */
.header{
    text-align:center;
    font-weight:900;
    font-size:20px;
    margin-bottom:30px;
    color:#0f2446;
}

/* bottom row */
.bottom-row{
    display:flex;
    gap:10px;
}
.bottom-row .stButton > button{
    margin-bottom:0px;
}
</style>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown("<div class='header'>Settings</div>", unsafe_allow_html=True)

    def item(icon, text, key, page):
        if st.button(f"""
        <div class="btn-row">
            <div class="left">
                <div class="icon">{icon}</div>
                <div>{text}</div>
            </div>
            <div class="arrow">›</div>
        </div>
        """, key=key):
            go(page)

    item("🔒", "Change Password", "pass", "pass")
    item("🌍", "Change Language", "lang", "lang")
    item("⭐", "Rate App", "rate", "rate")
    item("🚪", "Log Out", "logout", "logout")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("""
        <div class="btn-row">
            <div>⚠️ Report</div>
            <div class="arrow">›</div>
        </div>
        """, key="report"):
            go("report")

    with col2:
        if st.button("""
        <div class="btn-row">
            <div>✉️ Contact</div>
            <div class="arrow">›</div>
        </div>
        """, key="contact"):
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

    # -------- CONTENT DESIGN --------

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
        st.warning("Are you sure?")
        st.button("Confirm Logout")

    elif st.session_state.page == "report":
        st.text_area("Describe problem")
        st.button("Send Report")

    elif st.session_state.page == "contact":
        st.text_input("Email")
        st.text_area("Message")
        st.button("Send")
