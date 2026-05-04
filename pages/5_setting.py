import streamlit as st

st.set_page_config(page_title="Main App", layout="centered")

st.title("Main App")

st.write("Choose a section:")

st.page_link("pages/2_Customer.py", label="👤 Customer")
st.page_link("pages/5_setting.py", label="⚙️ Settings")

st.write("---")
st.write("App is running correctly 🚀")
