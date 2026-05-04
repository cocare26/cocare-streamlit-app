import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
#MainMenu, header, footer { visibility:hidden; }

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}

/* الكارد */
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
}

/* زر شفاف يغطي الكارد */
.card button {
    position:absolute;
    top:0;
    left:0;
    width:100%;
    height:100%;
    opacity:0;
    cursor:pointer;
}

/* hover */
.card:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}
</style>

<h2 style="text-align:center;color:#102646;">Settings</h2>
""", unsafe_allow_html=True)

# ===== عنصر =====
def item(label, icon, page):
    st.markdown(f"""
    <div class="card">
        <div style="display:flex;gap:12px;align-items:center;">
            <i class="{icon}"></i>
            <span style="font-weight:800;">{label}</span>
        </div>
        <span>›</span>
    </div>
    """, unsafe_allow_html=True)

    if st.button(label):
        st.switch_page(page)

# ===== العناصر =====
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
