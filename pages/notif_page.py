import streamlit as st
def show():
    st.title("🔔 Notifications")
    st.write("Stay updated with our latest offers.")
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()
