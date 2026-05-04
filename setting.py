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

/* ===== BUTTON CARD ===== */
.stButton > button{
    width:100%;
    border:none;
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:14px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    font-weight:600;
    color:#0f2446;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.25s;
}

/* hover */
.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

/* نص يسار */
.stButton > button span{
    display:flex;
    width:100%;
    justify-content:space-between;
    align-items:center;
}

/* header */
.header{
    text-align:center;
    font-weight:900;
    font-size:20px;
    margin-bottom:30px;
    color:#0f2446;
}

/* sub pages card */
.card{
    background:white;
    padding:18px;
    border-radius:20px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:15px;
}
</style>
""", unsafe_allow_html=True)

# -------- helper ----------
def item(label, icon, page):
    text = f"{label}|||{icon}›"  # separator trick
    if st.button(text):
        go(page)

# CSS trick to split text
st.markdown("""
<script>
const buttons = window.parent.document.querySelectorAll('button');
buttons.forEach(btn=>{
    if(btn.innerText.includes('|||')){
        let parts = btn.innerText.split('|||');
        btn.innerHTML = `
            <div style="display:flex; width:100%; justify-content:space-between;">
                <div>${parts[0]}</div>
                <div>${parts[1]}</div>
            </div>
        `;
    }
});
</script>
""", unsafe_allow_html=True)

# ================= MAIN =================
if st.session_state.page == "main":

    st.markdown("<div class='header'>Settings</div>", unsafe_allow_html=True)

    item("Change Password", "🔒", "pass")
    item("Change Language", "🌍", "lang")
    item("Rate App", "⭐", "rate")
    item("Log Out", "🚪", "logout")

    col1, col2 = st.columns(2)

    with col1:
        item("Report", "⚠️", "report")

    with col2:
        item("Contact", "✉️", "contact")

# ================= SUB =================
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
        if st.button("← Back"):
            go("main")

    with col2:
        st.markdown(f"<div class='header'>{title}</div>", unsafe_allow_html=True)

    # ===== content =====

    if st.session_state.page == "pass":
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.text_input("Current Password", type="password")
        st.text_input("New Password", type="password")
        st.text_input("Confirm Password", type="password")
        st.markdown("</div>", unsafe_allow_html=True)
        st.button("Save")

    elif st.session_state.page == "lang":
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.radio("Language", ["English", "Arabic"])
        st.markdown("</div>", unsafe_allow_html=True)
        st.button("Apply")

    elif st.session_state.page == "rate":
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.slider("Rating", 1, 5)
        st.text_area("Feedback")
        st.markdown("</div>", unsafe_allow_html=True)
        st.button("Submit")

    elif st.session_state.page == "logout":
        st.warning("Are you sure?")
        st.button("Confirm Logout")

    elif st.session_state.page == "report":
        st.text_area("Describe issue")
        st.button("Send")

    elif st.session_state.page == "contact":
        st.text_input("Email")
        st.text_area("Message")
        st.button("Send")
