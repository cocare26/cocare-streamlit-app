import streamlit as st
def show():
    st.title("🔄 Renewal Services")
    st.write("Renew your subscription or check expiry dates.")
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()
