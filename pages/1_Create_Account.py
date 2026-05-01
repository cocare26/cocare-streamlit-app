import random
import time
import streamlit as st

st.set_page_config(page_title="Create Account", layout="centered")

if "generated_phone_code" not in st.session_state:
    st.session_state.generated_phone_code = ""

st.markdown("""
<style>
.block-container {
    max-width: 480px;
    padding: 20px 30px;
    background: linear-gradient(180deg,#c9e7f7,#dff4ff);
    border-radius: 42px;
}

h1 {
    font-size: 26px;
    text-align: center;
    color: #0f2446;
    margin-bottom: 5px;
}

.signin-line {
    text-align: center;
    font-size: 14px;
    margin-top: -4px;
    margin-bottom: 12px;
}

.signin-line a {
    color: #1c6fa4;
    font-weight: bold;
    text-decoration: none;
    margin-left: 4px;
}

div[data-testid="stTextInput"] {
    margin-bottom: 6px;
}

div[data-testid="stTextInput"] label {
    margin-bottom: 3px;
}

div[data-testid="stSelectbox"] {
    margin-bottom: 6px;
}

div[data-testid="stSelectbox"] label {
    margin-bottom: 3px;
}

div[data-testid="stTextInput"] input {
    border-radius: 25px;
    height: 44px;
}

div[data-testid="stSelectbox"] div {
    border-radius: 25px;
}


div[data-testid="stHorizontalBlock"] .stButton > button {
    width: 70px !important;
    height: 32px !important;
    font-size: 12px !important;
    padding: 0 !important;
}

/* زر Create Account أكبر وممتد */
div.stButton > button {
    width: 100% !important;
    height: 48px !important;
    font-size: 16px !important;
    border-radius: 25px !important;
}

</style>
""", unsafe_allow_html=True)

st.title("Create Account")

st.markdown("""
<div style="text-align:center; font-size:14px;">
st.markdown("""
<div style="text-align:center; margin-bottom:10px;">
    Already have an account?
    <a href="/" target="_self" style="color:#1c6fa4; font-weight:bold; text-decoration:none; margin-left:4px;">
        Sign in
    </a>
</div>
""", unsafe_allow_html=True)
<a href="/" target="_top">Sign in</a>
color:#1c6fa4;
font-weight:bold;
text-decoration:none;
margin-left:4px;
">
Sign in
</a>
</div>
""", unsafe_allow_html=True)
username = st.text_input("Username")

if username and not username.replace(" ", "").isalpha():
    st.error("Username must contain letters only")

col1, col2 = st.columns([4, 1])

with col1:
    phone = st.text_input("Phone Number or ID", max_chars=11)

with col2:
    st.markdown("<div style='margin-top:28px'></div>", unsafe_allow_html=True)
    send_clicked = st.button("Send", key="send_code")

if send_clicked:
    if phone.isdigit() and len(phone) == 10 and phone.startswith("07"):
        st.session_state.generated_phone_code = "0000"
        st.success("Please check your SMS")
    else:
        st.error("Invalid")

phone_code = st.text_input("Enter Code")
email = st.text_input("Email")

location = st.selectbox(
      "Location",
    [
        "",
        "Amman",
        "Irbid",
        "Zarqa",
        "Balqa",
        "Mafraq",
        "Jerash",
        "Ajloun",
        "Madaba",
        "Karak",
        "Tafilah",
        "Ma'an",
        "Aqaba",
    ],
)

password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

create_clicked = st.button("Create Account", key="create_account")

if create_clicked:
    if not username or not phone or not phone_code or not email or not location or not password or not confirm_password:
        st.error("Fill all fields")
    elif not username.replace(" ", "").isalpha():
        st.error("Username must contain letters only")
    elif not phone.isdigit() or len(phone) != 10 or not phone.startswith("07"):
        st.error("Phone must be 10 digits and start with 07")
    elif phone_code != st.session_state.generated_phone_code:
        st.error("Wrong phone code")
    elif "@" not in email or "." not in email:
        st.error("Invalid email")
    elif password != confirm_password:
        st.error("Passwords do not match")
    else:
        st.success("Account created successfully")
        time.sleep(1)
        st.switch_page("app.py")
