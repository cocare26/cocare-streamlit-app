import streamlit as st
def show():
    st.title("🌐 Internet Bundles")
    st.write("Manage your 4G/5G data packages here.")
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()
