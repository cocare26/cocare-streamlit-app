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

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

/* HEADER */
.header {
    text-align:center;
    position:relative;
    margin-bottom:30px;
}

.title {
    font-weight:900;
    font-size:20px;
    color:#102646;
}

/* CARD */
.card {
    position:relative;
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.3s;
}

.card:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}

.left {
    display:flex;
    align-items:center;
    gap:12px;
}

.left i {
    color:#102646;
    font-size:16px;
    width:20px;
    text-align:center;
}

.left span {
    color:#102646;
    font-weight:800;
    font-size:14px;
}

.arrow {
    color:#102646;
    font-size:18px;
    font-weight:bold;
}

/* الزر الشفاف */
div.stButton > button {
    position:absolute;
    left:0;
    width:100%;
    height:60px;
    opacity:0;
    cursor:pointer;
    z-index:10;
}

/* BOTTOM */
.bottom {
    display:flex;
    gap:10px;
    margin-top:40px;
}

.bottom button {
    width:100%;
    background:white;
    border-radius:100px;
    padding:12px;
    font-weight:800;
    border:none;
    color:#102646;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.bottom button:hover {
    transform:translateY(-2px);
}
</style>

<div class="header">
    <h2 class="title">Settings</h2>
</div>
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

# ===== 6 BUTTONS =====
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
