import streamlit as st
def show():
    st.title("📞 Call Minutes")
    st.write("Check your international and local minutes.")
    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()
