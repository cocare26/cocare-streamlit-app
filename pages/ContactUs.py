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
    padding:30px !important;
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
}
</style>
""", unsafe_allow_html=True)

# 🔙 Back
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown("""
<div style="
background:white;
padding:30px;
border-radius:30px;
margin-top:15px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
font-weight:800;
color:#102646;
">
✉️ Email: Co.Care26@gmail.com
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
background:white;
padding:30px;
border-radius:30px;
margin-top:15px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
font-weight:800;
color:#102646;
">
📞 Phone: +962 79 123 4567
</div>
""", unsafe_allow_html=True)
