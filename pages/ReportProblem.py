import streamlit as st
import streamlit.components.v1 as components

PHONE_WIDTH = 430
PHONE_HEIGHT = 820

st.set_page_config(page_title="Report a Problem", layout="centered")

# ===== CSS =====
st.markdown(f"""
<style>
:root{{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}}

[data-testid="stHeader"] {{display: none !important;}}

.block-container{{
    max-width:{PHONE_WIDTH}px !important;    
    min-height:{PHONE_HEIGHT}px !important;
    margin:auto !important;
    padding:30px !important;       
    background:linear-gradient(160deg, var(--bg1), var(--bg2), var(--bg3));
    border-radius:42px;            
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}}

[data-testid="stAppViewContainer"]{{ background:#eef2f7; }}
footer {{visibility: hidden;}}

/* ===== HEADER ===== */
.header {{
    position: relative;
    height: 110px;
    margin-bottom: 40px;
}}

.back-style {{
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
}}

.back-style .stButton > button {{
    background:transparent !important;
    box-shadow:none !important;
    color:#0f2446 !important;
    font-size:28px !important;
    border: none !important;
}}

.title-text {{
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -160%);
    font-size:20px;
    font-weight:900;
    color:#0f2446;
    white-space: nowrap;
}}
</style>
""", unsafe_allow_html=True)
