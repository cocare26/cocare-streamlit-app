import streamlit as st

st.set_page_config(page_title="Change Language", layout="centered")

# ===== CSS Updated for English (LTR) =====
st.markdown("""
<style>
/* Set direction to Left-to-Right for English */
* { direction: ltr; }

[data-testid="stAppViewContainer"] {
    background-color: #dff2ff !important;
}

/* Hide Streamlit Header */
[data-testid="stHeader"] {display: none !important;}

/* The Main Container Card */
.block-container {
    max-width:430px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    margin-top: 50px;
}

/* Back Button Container (Aligned to Left) */
.back-container {
    display: flex;
    justify-content: flex-start; 
    margin-bottom: 40px;
    margin-top: 20px;
}

.back-style-btn .stButton > button {
    background-color: #1a1c22 !important; 
    color: white !important;
    width: 45px !important;
    height: 45px !important;
    border-radius: 12px !important; 
    border: none !important;
    font-size: 20px !important;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 !important;
}

/* Title Text (Aligned to Left) */
.title-left {
    font-size: 26px;
    font-weight: 800;
    color: #102646;
    text-align: left;
    margin-left: 15px;
    margin-bottom: 40px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

/* Language Selection Buttons (White Boxes) */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 50px !important; 
    height: 65px !important;
    margin-bottom: 20px !important;
    font-weight: 700 !important;
    font-size: 19px !important;
    display: flex !important;
    justify-content: space-between !important; 
    padding: 0 25px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}

.spacer {
    height: 200px;
}
</style>
""", unsafe_allow_html=True)

# ===== CONTENT =====

# 1. Back Button (Goes back to English Settings)
st.markdown('<div class="back-container back-style-btn">', unsafe_allow_html=True)
if st.button("‹", key="back_btn"):
    st.switch_page("pages/Settings.py")
st.markdown('</div>', unsafe_allow_html=True)

# 2. Page Title
st.markdown('<div class="title-left">Change Language</div>', unsafe_allow_html=True)

# 3. Language Selection
# Spacers to push the checkmark/arrow to the far right of the button
col_gap = "&nbsp;" * 40

# Arabic Option -> Redirects to Arabic Main Settings
if st.button(f"🌐 Arabic {col_gap} ›", key="lang_ar"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

# English Option -> Redirects to English Main Settings
if st.button(f"🌐 English {col_gap} ✔", key="lang_en"):
    st.session_state.lang = "en"
    st.switch_page("pages/Settings.py")

# 4. Bottom Spacer
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
