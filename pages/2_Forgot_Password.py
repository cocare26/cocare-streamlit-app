import random
import time
import streamlit as st

st.set_page_config(page_title="Forgot Password", layout="centered")

if "reset_code" not in st.session_state:
    st.session_state.reset_code = ""

st.markdown("""
<style>
.block-container {
    max-width: 390px;
    padding: 22px 30px 30px 30px;
    background: linear-gradient(180deg,#c9e7f7,#dff4ff);
    border-radius: 42px;
}

h1 {
    font-size: 26px;
    text-align: center;
    color: #0f2446;
    margin-bottom: 16px;
}
h1 {
    font-size: 22px !important;   /* تصغير الحجم */
    margin-top: 10px !important;  /* تنزيله لتحت */
}

div[data-testid="stTextInput"] {
    margin-bottom: 8px;
}

div[data-testid="stTextInput"] label {
    margin-bottom: 3px;
}

div[data-testid="stTextInput"] input {
    border-radius: 25px;
    height: 44px;
}

.stButton > button {
    width: 100%;
    height: 44px;
    border-radius: 25px;
    border: none;
    background: #1c6fa4;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.title("Forgot Password")

phone = st.text_input("Phone Number", max_chars=10)

if st.button("Send Code"):
    if phone.isdigit() and len(phone) == 10 and phone.startswith("07"):
        st.session_state.reset_code = str(random.randint(1000, 9999))
        st.success(f"Reset code: {st.session_state.reset_code}")
    else:
        st.error("Phone must be 10 digits and start with 07")

code = st.text_input("Enter Code")
new_password = st.text_input("New Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Reset Password"):
    if not phone or not code or not new_password or not confirm_password:
        st.error("Fill all fields")
    elif code != st.session_state.reset_code:
        st.error("Wrong code")
    elif new_password != confirm_password:
        st.error("Passwords do not match")
    else:
        st.success("Password changed successfully")
        time.sleep(1)
        st.switch_page("app.py")

if st.button("Back to Login"):
    st.switch_page("app.py")
