import streamlit as st

st.set_page_config(layout="centered")

def navigate():

    params = st.query_params
    page = params.get("page", "login")

    if isinstance(page, list):
        page = page[0]

    # 🔥 IMPORTANT: switch_page يحتاج اسم الملف داخل pages بدون "pages/"
    
    if page == "login":
        st.switch_page("0_arabic_app")

    elif page == "customer":
        st.switch_page("2_Customer")

    elif page == "settings-ar":
        st.switch_page("11_settingar")

    elif page == "settings-en":
        st.switch_page("5_setting")

    elif page == "Change_password-ar":
        st.switch_page("6_Change_Password")

    elif page == "Change_language-ar":
        st.switch_page("7_Change_Language")

    elif page == "Rate_app-ar":
        st.switch_page("8_Rate_App")

    elif page == "Report_Problem-ar":
        st.switch_page("9_Report_Problem")

    elif page == "Contact_Us-ar":
        st.switch_page("10_Contact_Us")

    elif page == "logout":
        st.session_state.clear()
        st.query_params.clear()
        st.switch_page("0_arabic_app")


if __name__ == "__main__":
    navigate()
