import streamlit as st

st.set_page_config(page_title="App", layout="centered")

page = st.query_params.get("page")

if page:
    page = page[0]
else:
    page = ""

# ========= ROUTER =========
if page == "customer":
    st.switch_page("pages/0_arabic_app.py")

elif page == "Change_password-ar":
    st.switch_page("pages/ChangePassword.py")

elif page == "Change_language-ar":
    st.switch_page("pages/ChangeLanguage.py")

elif page == "Contact_Us-ar":
    st.switch_page("pages/ContactUs.py")

elif page == "Report_Problem-ar":
    st.switch_page("pages/ReportProblem.py")

elif page == "logout":
    st.switch_page("main_app.py")

# default
else:
    st.switch_page("pages/Settings.py")
