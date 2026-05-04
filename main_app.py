import streamlit as st

st.set_page_config(page_title="App", layout="centered")

page = st.query_params.get("pages", "")

# ========= ROUTER =========
if page == "settings":
    st.switch_page("Settings")

elif page == "change_password":
    st.switch_page("ChangePassword")

elif page == "change_language":
    st.switch_page("ChangeLanguage")

elif page == "contact":
    st.switch_page("ContactUs")

elif page == "report":
    st.switch_page("ReportProblem")

# ========= DEFAULT =========
else:
st.switch_page("pages/Settings.py")
