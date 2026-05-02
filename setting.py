import streamlit as st

st.set_page_config(page_title="Settings UI", layout="wide")

st.markdown("""
<style>
.stApp {
    background-color: #cbdbe5;
}

.block-container {
    max-width: 100% !important;
    padding-left: 60px !important;
    padding-right: 60px !important;
    padding-top: 20px !important;
}

.header-section {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    margin-bottom: 70px !important;
}

.stButton > button {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 100px !important;
    border: none !important;

    width: 100% !important;
    height: 100px !important;
    min-height: 100px !important;

    font-size: 24px !important;
    font-weight: 700 !important;

    margin-bottom: 25px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;

    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;

    padding-left: 80px !important;
}

.stButton > button div p {
    width: 100%;
    text-align: left !important;
    margin-left: 260px !important;
}

/* Report + Contact أصغر */
div[data-testid="column"] .stButton > button {
    height: 60px !important;
    min-height: 60px !important;
    font-size: 16px !important;
    border-radius: 35px !important;
    padding-left: 35px !important;
}

div[data-testid="column"] .stButton > button div p {
    margin-left: 40px !important;
}

[data-testid="column"] {
    padding: 0 10px !important;
}
</style>
""", unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(p):
    st.session_state.page = p

if st.session_state.page == 'main':
    st.markdown("""
    <div class="header-section">
        <div style="position:absolute; left:0px; font-size:45px; font-weight:900; color:black;"> < </div>
        <h1 style="font-size:45px; font-weight:800; color:black;">Settings</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report Problem"): nav('report')
    with col2:
        if st.button("✉️ Contact Us"): nav('contact')

elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Password</h1>", unsafe_allow_html=True)
