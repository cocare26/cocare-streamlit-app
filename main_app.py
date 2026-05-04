import streamlit as st

st.set_page_config(page_title="App", layout="centered")

page = st.query_params.get("page", "")

# ========= SETTINGS =========
if page == "settings":
    st.switch_page("5 setting")

elif page == "change_password":
    st.switch_page("6 Change Password")

elif page == "change_language":
    st.switch_page("7 Change Language")

elif page == "contact":
    st.switch_page("10 Contact Us")

elif page == "report":
    st.switch_page("11 settingar")

# ========= DEFAULT =========
else:
    st.switch_page("5 setting")
