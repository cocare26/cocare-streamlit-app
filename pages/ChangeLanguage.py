import streamlit as st

st.set_page_config(page_title="Change Language", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
col1, col2 = st.columns([1,5])

with col1:
    if st.button("‹"):
        st.query_params["page"] = "settings"
        st.rerun()

with col2:
    st.markdown("<h3 style='margin-top:5px;'>Change Language</h3>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== BUTTON STYLE =====
st.markdown("""
<style>
div.stButton > button {
    width:100%;
    border-radius:100px;
    padding:15px;
    margin-bottom:12px;
    background:white;
    border:none;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    font-weight:800;
    text-align:left;
}
</style>
""", unsafe_allow_html=True)

# ===== OPTIONS =====
if st.button("🌐 Arabic   ✔"):
    st.query_params["page"] = "settings-ar"
    st.rerun()

if st.button("🌐 English   ›"):
    st.query_params["page"] = "settings"
    st.rerun()
