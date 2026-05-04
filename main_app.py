import streamlit as st

st.set_page_config(layout="centered")

def navigate():

    params = st.query_params
    page = params.get("page", "login")

    if isinstance(page, list):
        page = page[0]

    # 🔥 بدل switch_page نستخدم routing داخلي آمن

    if page == "login":
        import pages._0_arabic_app as p
        p.run()

    elif page == "customer":
        import pages._2_Customer as p
        p.run()

    elif page == "settings-ar":
        import pages._11_settingar as p
        p.run()

    elif page == "settings-en":
        import pages._5_setting as p
        p.run()

    elif page == "Change_password-ar":
        import pages._6_Change_Password as p
        p.run()

    elif page == "Change_language-ar":
        import pages._7_Change_Language as p
        p.run()

    elif page == "Rate_app-ar":
        import pages._8_Rate_App as p
        p.run()

    elif page == "Report_Problem-ar":
        import pages._9_Report_Problem as p
        p.run()

    elif page == "Contact_Us-ar":
        import pages._10_Contact_Us as p
        p.run()

    elif page == "logout":
        st.session_state.clear()
        st.query_params.clear()
        import pages._0_arabic_app as p
        p.run()


if __name__ == "__main__":
    navigate()
