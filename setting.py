import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# --- Navigation State ---
if "page" not in st.session_state:
    st.session_state.page = "main"

def go(page):
    st.session_state.page = page
    st.rerun()

# --- Global CSS ---
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
}

/* header */
.header{
    display:flex;
    align-items:center;
    justify-content:center;
    position:relative;
    margin-bottom:30px;
}

.back{
    position:absolute;
    left:0;
    font-size:26px;
    font-weight:bold;
    cursor:pointer;
    color:var(--navy);
}

.title{
    font-size:20px;
    font-weight:900;
    color:var(--navy);
}

/* buttons */
.setting{
    background:white;
    border-radius:100px;
    padding:14px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.3s;
    font-weight:600;
    color:var(--navy);
}

.setting:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

.icon{
    margin-right:10px;
}

.row{
    display:flex;
    gap:10px;
}

.row .setting{
    flex:1;
    font-size:13px;
}
</style>
""", unsafe_allow_html=True)

# --- UI Helpers ---
def header(title, back=False):
    cols = st.columns([1,6,1])
    if back:
        with cols[0]:
            if st.button("←"):
                go("main")
    with cols[1]:
        st.markdown(f"<div class='title'>{title}</div>", unsafe_allow_html=True)

def btn(icon, text, page):
    if st.button(f"{icon}  {text}   ›"):
        go(page)

# --- Pages ---

# MAIN
if st.session_state.page == "main":
    header("Settings")

    btn("🔒","Change Password","pass")
    btn("🌐","Change Language","lang")
    btn("⭐","Rate App","rate")
    btn("🚪","Log Out","logout")

    col1,col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report"):
            go("report")
    with col2:
        if st.button("✉️ Contact"):
            go("contact")

# CHANGE PASSWORD
elif st.session_state.page == "pass":
    header("Change Password", True)

    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Confirm Password", type="password")

    st.button("Save")

# LANGUAGE
elif st.session_state.page == "lang":
    header("Language", True)

    st.button("English ✔")
    st.button("العربية")

# REPORT
elif st.session_state.page == "report":
    header("Report", True)

    st.text_area("Write problem...")
    st.button("Send")

# CONTACT
elif st.session_state.page == "contact":
    header("Contact Us", True)

    st.write("✉️ CoCare26@gmail.com")
    st.write("📞 +962 79 123 4567")

# LOGOUT
elif st.session_state.page == "logout":
    header("Log Out", True)

    st.write("Are you sure?")
    st.button("Log Out")
    if st.button("Cancel"):
        go("main")

# RATE
elif st.session_state.page == "rate":
    header("Rate App", True)

    st.button("Google Play")
    st.button("App Store")
