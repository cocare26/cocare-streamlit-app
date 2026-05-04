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

/* ===== Card Button ===== */
.card{
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:14px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.25s;
}

.card:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

.left{
    font-weight:600;
    color:#0f2446;
}

.right{
    display:flex;
    align-items:center;
    gap:10px;
    color:#0f2446;
}

/* hide real button */
.stButton > button{
    opacity:0;
    height:0;
    padding:0;
    margin:0;
}

/* header */
.header{
    text-align:center;
    font-weight:900;
    font-size:20px;
    margin-bottom:30px;
    color:#0f2446;
}

/* inner page card */
.inner-card{
    background:white;
    padding:18px;
    border-radius:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:15px;
}

/* nicer inputs */
input, textarea{
    border-radius:10px !important;
}
</style>
""", unsafe_allow_html=True)

# -------- helper ----------
def card(label, icon, page, key):
    st.markdown(f"""
    <div class="card">
        <div class="left">{label}</div>
        <div class="right">
            <span>{icon}</span>
            <span>›</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key=key):
        go(page)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown("<div class='header'>Settings</div>", unsafe_allow_html=True)

    card("Change Password", "🔒", "pass", "p1")
    card("Change Language", "🌍", "lang", "p2")
    card("Rate App", "⭐", "rate", "p3")
    card("Log Out", "🚪", "logout", "p4")

    col1, col2 = st.columns(2)

    with col1:
        card("Report", "⚠️", "report", "p5")

    with col2:
        card("Contact", "✉️", "contact", "p6")

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

    # ===== CONTENT =====

    if st.session_state.page == "pass":

        st.markdown("<div class='inner-card'>", unsafe_allow_html=True)
        st.text_input("Current Password", type="password")
        st.text_input("New Password", type="password")
        st.text_input("Confirm Password", type="password")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Save Password")

    elif st.session_state.page == "lang":

        st.markdown("<div class='inner-card'>", unsafe_allow_html=True)
        st.radio("Select Language", ["English", "Arabic"])
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Apply")

    elif st.session_state.page == "rate":

        st.markdown("<div class='inner-card'>", unsafe_allow_html=True)
        st.slider("Rating", 1, 5)
        st.text_area("Feedback")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Submit")

    elif st.session_state.page == "logout":

        st.markdown("<div class='inner-card'>", unsafe_allow_html=True)
        st.warning("Are you sure you want to log out?")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Confirm Logout")

    elif st.session_state.page == "report":

        st.markdown("<div class='inner-card'>", unsafe_allow_html=True)
        st.text_area("Describe the issue")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Send Report")

    elif st.session_state.page == "contact":

        st.markdown("<div class='inner-card'>", unsafe_allow_html=True)
        st.text_input("Email")
        st.text_area("Message")
        st.markdown("</div>", unsafe_allow_html=True)

        st.button("Send Message")
