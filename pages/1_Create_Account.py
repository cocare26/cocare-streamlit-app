import time
import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(page_title="Create Account", layout="centered")

if "generated_phone_code" not in st.session_state:
    st.session_state.generated_phone_code = ""

st.markdown("""
<style>

/* 🎨 ألوان موحّدة */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
}

/* 📱 الكارد (تدرج جديد احترافي) */
.block-container {
    max-width: 480px;
    padding: 20px 30px;
    background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 40%, #eaf6ff 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* 🧠 العنوان */
h1 {
    font-size: 24px;
    text-align: center;
    color: var(--navy);
    margin-bottom: 5px;
    font-weight: 900;
}

/* 🔗 Sign in */
.signin-line {
    text-align: center;
    font-size: 14px;
    margin-top: -4px;
    margin-bottom: 8px;
    color: #333;
}

/* ✨ Inputs بدون حواف */
div[data-testid="stTextInput"] input {
    border-radius: 25px;
    height: 44px;
    border: none !important;
    outline: none !important;
    padding-left: 16px;
    background: rgba(255,255,255,0.95);
}

/* Selectbox */
div[data-testid="stSelectbox"] div {
    border-radius: 25px;
}

/* زر Send */
div[data-testid="stHorizontalBlock"] .stButton > button {
    width: 70px !important;
    height: 34px !important;
    font-size: 12px !important;
    border-radius: 20px !important;
    background: linear-gradient(90deg,#2f80ed,#1c6fa4);
    color: white;
}

/* الأزرار الأساسية */
div.stButton > button {
    width: 100% !important;
    height: 48px !important;
    font-size: 16px !important;
    border-radius: 25px !important;
    border: none;
    background: linear-gradient(90deg,#2f80ed,#1c6fa4);
    color: white;
    font-weight: bold;
    transition: .2s;
}

/* hover */
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,.2);
}

/* زر Sign in (خفيف) */
div.stButton:nth-of-type(1) > button {
    background: white;
    color: var(--navy);
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
}

</style>
""", unsafe_allow_html=True)

st.title("Create Account")

st.markdown("""
<div style="text-align:center; font-size:14px; margin-top:-4px; margin-bottom:12px;">
    Already have an account?
    <a href="/" target="_top" style="
        color:#2f80ed;
        font-weight:bold;
        text-decoration:none;
        margin-left:4px;
    ">Sign in</a>
</div>
""", unsafe_allow_html=True)

components.html("""
<script>
window.parent.location.href = "/";
</script>
""", height=0)

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
    elif phone.isdigit() and len(phone) == 11:
        st.session_state.generated_phone_code = "0000"
        st.success("Please check your SMS")
    else:
        st.error("Invalid phone number or ID")

phone_code = st.text_input("Enter Code")
email = st.text_input("Email")

location = st.selectbox(
    "Location",
    [
        "",
        "Amman","Irbid","Zarqa","Balqa","Mafraq",
        "Jerash","Ajloun","Madaba","Karak",
        "Tafilah","Ma'an","Aqaba",
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
    elif not phone.isdigit() or not (len(phone) == 10 or len(phone) == 11):
        st.error("Phone or ID must be numeric")
    elif len(phone) == 10 and not phone.startswith("07"):
        st.error("Phone must start with 07")
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
