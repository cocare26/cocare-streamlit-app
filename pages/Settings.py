import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ======= CSS =======
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
#MainMenu, header, footer { visibility:hidden; }

[data-testid="stAppViewContainer"] { background:#f0f7ff; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

.card {
    position:relative;
    margin-bottom:15px;
}

.setting-item { 
    background:white;
    border-radius:100px;
    padding:14px 22px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.item-left {
    display:flex;
    align-items:center;
    gap:12px;
}

.item-text {
    color:#102646;
    font-weight:800;
    font-size:14px;
}

.arrow {
    color:#102646;
    font-weight:bold;
    font-size:18px;
}

/* 🔥 الزر يغطي كل العنصر */
div.stButton > button {
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    opacity:0;
    z-index:10;
    cursor:pointer;
}
</style>

<div style="text-align:center; margin-bottom:30px;">
    <h2 style="color:#102646; font-weight:900;">Settings</h2>
</div>
""", unsafe_allow_html=True)

# ======= ITEM 1 =======
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
<div class="setting-item">
    <div class="item-left">
        <i class="fas fa-lock"></i>
        <span class="item-text">Change Password</span>
    </div>
    <span class="arrow">›</span>
</div>
""", unsafe_allow_html=True)

if st.button("cp"):
    st.switch_page("pages/ChangePassword.py")

st.markdown('</div>', unsafe_allow_html=True)

# ======= ITEM 2 =======
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
<div class="setting-item">
    <div class="item-left">
        <i class="fas fa-globe"></i>
        <span class="item-text">Change Language</span>
    </div>
    <span class="arrow">›</span>
</div>
""", unsafe_allow_html=True)

if st.button("cl"):
    st.switch_page("pages/ChangeLanguage.py")

st.markdown('</div>', unsafe_allow_html=True)

# ======= ITEM 3 =======
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
<div class="setting-item">
    <div class="item-left">
        <i class="fas fa-envelope"></i>
        <span class="item-text">Contact Us</span>
    </div>
    <span class="arrow">›</span>
</div>
""", unsafe_allow_html=True)

if st.button("cu"):
    st.switch_page("pages/ContactUs.py")

st.markdown('</div>', unsafe_allow_html=True)

# ======= ITEM 4 =======
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
<div class="setting-item">
    <div class="item-left">
        <i class="fas fa-bug"></i>
        <span class="item-text">Report Problem</span>
    </div>
    <span class="arrow">›</span>
</div>
""", unsafe_allow_html=True)

if st.button("rp"):
    st.switch_page("pages/ReportProblem.py")

st.markdown('</div>', unsafe_allow_html=True)
