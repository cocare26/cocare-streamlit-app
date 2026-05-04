import streamlit as st

st.set_page_config(page_title="App", layout="centered")

# ✅ الطريقة الصح لقراءة الرابط
params = st.experimental_get_query_params()
page = params.get("page", [""])[0]

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
