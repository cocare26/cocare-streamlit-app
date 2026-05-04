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
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}

/* الكارد */
.card {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* نخفي شكل الزر */
div.stButton > button {
    all: unset;
    width:100%;
    cursor:pointer;
}

/* hover */
.card:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.12);
}
</style>

<h2 style="text-align:center; color:#102646;">Settings</h2>
""", unsafe_allow_html=True)

# ===== عنصر reusable =====
def setting_item(label, icon, page):
    container = st.container()
    with container:
        st.markdown(f"""
        <div class="card">
            <div style="display:flex; gap:12px; align-items:center;">
                <i class="{icon}"></i>
                <span style="font-weight:800;">{label}</span>
            </div>
            <span>›</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button(label):
            st.switch_page(page)

# ===== العناصر =====
setting_item("Change Password", "fas fa-lock", "pages/ChangePassword.py")
setting_item("Change Language", "fas fa-globe", "pages/ChangeLanguage.py")
setting_item("Contact Us", "fas fa-envelope", "pages/ContactUs.py")
setting_item("Report Problem", "fas fa-bug", "pages/ReportProblem.py")
