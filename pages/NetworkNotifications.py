import streamlit as st

st.set_page_config(
    page_title="Network Notifications",
    layout="centered"
) 
st.markdown("""
<style>
.stApp {
    background-color: #EAF6FF;
}

div.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 15px;
    border: 2px solid #64B5F6;
    background-color: white;
    color: #2196F3;
    font-size: 16px;
    font-weight: bold;
    margin-top: 10px;
}

div.stButton > button:hover {
    background-color: #BBDEFB;
    color: #0D47A1;
}
</style>
""", unsafe_allow_html=True)

# زر الرجوع
if st.button("⬅ Back"):
    st.switch_page("2_Customer.py")

st.markdown("## 📡 Network Notifications")

st.info("Network maintenance in Amman tonight.")

st.warning("Weak signal detected in your area.")

st.success("Your internet package renewed successfully.")
