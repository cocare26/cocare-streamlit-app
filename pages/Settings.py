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
.title {
    text-align:center;
    font-weight:900;
    font-size:20px;
    color:#102646;
    margin-bottom:30px;
}

/* WRAPPER مهم */
.card-wrapper {
    position:relative;
    margin-bottom:15px;
}

/* CARD UI */
.card-ui {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition:0.3s;
}

.card-ui:hover {
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
}

.left span {
    color:#102646;
    font-weight:800;
    font-size:14px;
}

.arrow {
    font-size:18px;
    font-weight:bold;
    color:#102646;
}

/* 💥 الزر يغطي كل الكارد */
.card-wrapper button {
    position:absolute !important;
    top:0;
    left:0;
    width:100% !important;
    height:100% !important;
    opacity:0;
    cursor:pointer;
    z-index:10;
}

/* ===== bottom ===== */
.bottom-row {
    display:flex;
    gap:10px;
    margin-top:40px;
}

.bottom-wrapper {
    position:relative;
    flex:1;
}

.bottom-ui {
    background:white;
    border-radius:100px;
    padding:12px;
    text-align:center;
    font-weight:800;
    font-size:12px;
    color:#102646;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.bottom-wrapper button {
    position:absolute !important;
    top:0;
    left:0;
    width:100% !important;
    height:100% !important;
    opacity:0;
    cursor:pointer;
}
</style>

<div class="title">Settings</div>
""", unsafe_allow_html=True)

# ===== عنصر =====
def item(label, icon, page, key):
    st.markdown(f"""
    <div class="card-wrapper">
        <div class="card-ui">
            <div class="left">
                <i class="{icon}"></i>
                <span>{label}</span>
            </div>
            <div class="arrow">›</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key=key):
        st.switch_page(page)

# ===== العناصر =====
item("Change Password", "fas fa-lock", "pages/ChangePassword.py", "p1")
item("Change Language", "fas fa-globe", "pages/ChangeLanguage.py", "p2")
item("Rate App", "fas fa-star", "pages/RateApp.py", "p3")
item("Log Out", "fas fa-sign-out-alt", "main_app.py", "p4")

# ===== bottom =====
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="bottom-wrapper">
        <div class="bottom-ui">Report Problem</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key="report"):
        st.switch_page("pages/ReportProblem.py")

with col2:
    st.markdown("""
    <div class="bottom-wrapper">
        <div class="bottom-ui">Contact Us</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("", key="contact"):
        st.switch_page("pages/ContactUs.py")
