import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "settings"

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #dceff7, #cce6ef, #e8f6fa);
}

.block-container {
    padding-top: 20px;
}

div.stButton > button {
    width: 100%;
    height: 58px;
    background-color: #f7f3e8;
    color: black;
    border-radius: 35px;
    border: none;
    font-size: 18px;
    font-weight: 600;
    margin: 8px 0;
    box-shadow: 0 6px 16px rgba(0,0,0,0.15);
    text-align: right;
    padding-right: 25px;
}

div.stButton > button:hover {
    background-color: #f5efe6;
    color: black;
    border: none;
}

.box {
    background: rgba(160, 195, 195, 0.55);
    padding: 25px;
    border-radius: 8px;
}

.title {
    font-size: 30px;
    font-weight: 700;
    color: black;
    text-align: center;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

if st.session_state.page == "settings":

    st.markdown('<div class="box">', unsafe_allow_html=True)
    st.markdown('<div class="title">‹ &nbsp;&nbsp;&nbsp;&nbsp; Settings</div>', unsafe_allow_html=True)

    if st.button("🔒   Change Password        ›"):
        st.session_state.page = "password"

    if st.button("🌐   Change Language        ›"):
        st.session_state.page = "language"

    if st.button("⭐   Rate App        ›"):
        st.session_state.page = "rate"

    if st.button("🚪   Log Out        ›"):
        st.session_state.page = "logout"

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚠️ Report a Problem ›"):
            st.session_state.page = "report"

    with col2:
        if st.button("✉️ Contact Us ›"):
            st.session_state.page = "contact"

    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "password":
    st.title("Change Password")
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write Password", type="password")
    st.button("Save")
    if st.button("← Back"):
        st.session_state.page = "settings"

elif st.session_state.page == "language":
    st.title("Change Language")
    st.button("🌐 English")
    st.button("🌐 العربية")
    if st.button("← Back"):
        st.session_state.page = "settings"

elif st.session_state.page == "rate":
    st.title("Rate App")
    st.button("▶ Google Play Store")
    st.button(" Apple App Store")
    st.button("🛍 Huawei AppGallery")
    if st.button("← Back"):
        st.session_state.page = "settings"

elif st.session_state.page == "logout":
    st.title("Log Out")
    st.success("Logged out successfully")
    if st.button("← Back"):
        st.session_state.page = "settings"

elif st.session_state.page == "report":
    st.title("Report a Problem")
    st.text_area("I need help")
    st.button("✈ Send Report")
    if st.button("← Back"):
        st.session_state.page = "settings"

elif st.session_state.page == "contact":
    st.title("Contact Us")
    st.info("Email: Co.Care26@gmail.com")
    st.info("Phone: +962 79 123 4567")
    if st.button("← Back"):
        st.session_state.page = "settings"
