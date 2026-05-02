import random
import time
import streamlit as st

st.set_page_config(page_title="Forgot Password", layout="centered")

if "reset_code" not in st.session_state:
    st.session_state.reset_code = ""

st.markdown("""
<style>

:root{
    --navy:#0f2446;
    --accent:#2f80ed;
}

/* الكارد */
.block-container {
    max-width: 390px;
    padding: 22px 30px 30px 30px;
    background: linear-gradient(180deg,#c9e7f7,#dff4ff);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* العنوان */
h1 {
    font-size: 22px !important;
    text-align: center;
    color: var(--navy);
    margin-top: 10px !important;
    font-weight: 900;
}

/* input بدون حواف */
div[data-testid="stTextInput"] input {
    border-radius: 25px;
    height: 44px;
    border: none !important;
    outline: none !important;
    padding-left: 16px;
    background: rgba(255,255,255,0.95);
    box-shadow: none !important;
}

/* حتى عند الفوكس */
div[data-testid="stTextInput"] input:focus {
    outline: none !important;
    box-shadow: none !important;
}

/* الأزرار */
.stButton > button {
    width: 100%;
    height: 46px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(90deg,#2f80ed,#1c6fa4);
    color: white;
    font-weight: bold;
    transition: .2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* زر الرجوع */
div.stButton:nth-of-type(3) > button {
    background: white;
    color: var(--navy);
}

</style>
""", unsafe_allow_html=True)

st.title("Forgot Password")

phone = st.text_input("Phone Number or ID", max_chars=11)

if st.button("Send Code"):
    if phone.isdigit() and (
        (len(phone) == 10 and phone.startswith("07")) or len(phone) == 11
    ):
        st.session_state.reset_code = str(random.randint(1000, 9999))
        st.success(f"Reset code: {st.session_state.reset_code}")
    else:
        st.error("Enter valid phone or ID")

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
