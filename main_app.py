import streamlit as st

st.set_page_config(page_title="App", layout="centered")

page = st.query_params.get("page")

if page:
    page = page[0]
else:
    page = ""

if page == "change_password":
    st.switch_page("pages/ChangePassword.py")

elif page == "change_language":
    st.switch_page("pages/ChangeLanguage.py")

elif page == "rate_app":
    st.switch_page("pages/RateApp.py")

elif page == "contact":
    st.switch_page("pages/ContactUs.py")

elif page == "report":
    st.switch_page("pages/ReportProblem.py")

else:
    st.switch_page("pages/Settings.py")
