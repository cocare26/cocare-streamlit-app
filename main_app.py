import streamlit as st

st.set_page_config(page_title="App", layout="centered")

# ✅ قراءة query params بشكل صحيح
page = st.query_params.get("page")

if page:
    page = page[0]
else:
    page = ""

# ========= ROUTER =========
if page == "settings":
    st.switch_page("pages/Settings.py")

elif page == "change_password":
    st.switch_page("pages/ChangePassword.py")

elif page == "change_language":
    st.switch_page("pages/ChangeLanguage.py")

elif page == "contact":
    st.switch_page("pages/ContactUs.py")

elif page == "report":
    st.switch_page("pages/ReportProblem.py")

# ========= DEFAULT =========
else:
    st.switch_page("pages/Settings.py")
