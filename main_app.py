import streamlit as st

st.set_page_config(page_title="App", layout="centered")

# قراءة الصفحة من الرابط
page = st.query_params.get("page", "")

# ========= SETTINGS ROUTER =========
if page == "settings":
    st.switch_page("pages/Settings.py")

elif page == "Change_password-ar":
    st.switch_page("pages/Change_password-ar.py")

elif page == "Change_language-ar":
    st.switch_page("pages/Change_language-ar.py")

elif page == "Rate_app-ar":
    st.switch_page("pages/Rate_app-ar.py")

elif page == "Report_Problem-ar":
    st.switch_page("pages/Report_Problem-ar.py")

elif page == "Contact_Us-ar":
    st.switch_page("pages/Contact_Us-ar.py")

elif page == "logout":
    st.switch_page("pages/logout.py")

# ========= DEFAULT =========
else:
    st.switch_page("pages/Settings.py")
