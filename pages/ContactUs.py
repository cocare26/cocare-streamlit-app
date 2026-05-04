import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}

/* buttons */
.stButton > button {
    width:100% !important;
    background:white !important;
    color:#102646 !important;
    border-radius:100px !important;
    padding:22px 20px !important;
    min-height:90px !important;   /* ← كبرنا الطول */
    margin-top:15px !important;   /* ← مسافة بينهم */
    border:none !important;
    box-shadow:0 4px 12px rgba(0,0,0,0.08) !important;
    font-weight:800 !important;
    text-align:left !important;
}

/* back arrow */
.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    font-size:28px !important;
    width:auto !important;
    min-height:auto !important;
    margin-top:0 !important;
}
</style>
""", unsafe_allow_html=True)

# 🔙 Back
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("‹"):
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Title
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900;">Contact Us</h2>', unsafe_allow_html=True)

# Buttons
st.button("✉️ Email: Co.Care26@gmail.com")
st.button("📞 Phone: +962 79 123 4567")
