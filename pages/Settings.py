import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS =====
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
#MainMenu, header, footer { visibility:hidden; }

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* container */
.block-container {
    max-width:430px;
    margin:auto;
    padding:20px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

/* title */
.title {
    text-align:center;
    font-weight:900;
    color:#102646;
    margin-bottom:25px;
    font-size:20px;
}

/* card */
.card {
    position:relative;
    background:white;
    border-radius:100px;
    padding:16px 20px;
    margin-bottom:14px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.25s;
}

.card:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 16px rgba(0,0,0,0.12);
}

/* left side */
.left {
    display:flex;
    align-items:center;
    gap:12px;
}

/* icon */
.left i {
    color:#102646;
    font-size:15px;
    width:20px;
    text-align:center;
}

/* text */
.left span {
    color:#102646;
    font-weight:800;
    font-size:14px;
}

/* arrow */
.arrow {
    font-size:18px;
    color:#102646;
    font-weight:bold;
}

/* button overlay */
div.stButton > button {
    position:absolute;
    left:0;
    width:100%;
    height:60px;
    opacity:0;
    z-index:10;
    cursor:pointer;
}

/* bottom row */
.bottom {
    display:flex;
    gap:10px;
    margin-top:40px;
}

.bottom button {
    width:100%;
    border-radius:100px;
    padding:12px;
    background:white;
    color:#102646;
    font-weight:800;
    border:none;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.25s;
}

.bottom button:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}
</style>

<div class="title">Settings</div>
""", unsafe_allow_html=True)

# ===== عنصر =====
def item(label, icon, page):
    st.markdown(f"""
    <div class="card">
        <div class="left">
            <i class="{icon}"></i>
            <span>{label}</span>
        </div>
        <div class="arrow">›</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button(label):
        st.switch_page(page)

# ===== items =====
item("Change Password", "fas fa-lock", "pages/ChangePassword.py")
item("Change Language", "fas fa-globe", "pages/ChangeLanguage.py")
item("Rate App", "fas fa-star", "pages/RateApp.py")
item("Log Out", "fas fa-sign-out-alt", "main_app.py")

# ===== bottom =====
col1, col2 = st.columns(2)

with col1:
    if st.button("Report Problem"):
        st.switch_page("pages/ReportProblem.py")

with col2:
    if st.button("Contact Us"):
        st.switch_page("pages/ContactUs.py")
