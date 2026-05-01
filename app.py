import streamlit as st
import base64
import os

st.set_page_config(page_title="Telecom App", layout="centered")

page = st.query_params.get("page", "")

if page == "create":
    st.switch_page("pages/1_Create_Account.py")
elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")
elif page == "employee":
    st.switch_page("pages/3_Employee.py")
elif page == "todo":
    st.switch_page("pages/4_To_Do.py")

BASE_DIR = os.path.dirname(__file__)
robot_path = os.path.join(BASE_DIR, "robot.png")

with open(robot_path, "rb") as f:
    img = base64.b64encode(f.read()).decode()

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background:#eef3f6;
}
.block-container {
    max-width:360px;
    height:660px;
    margin:auto;
    border-radius:42px;
    background:linear-gradient(180deg,#c9e7f7,#dff4ff);
    padding:70px 58px 30px 58px;
    position:relative;
}
header, footer {visibility:hidden;}

.robot {
    position:absolute;
    top:85px;
    right:45px;
    width:145px;
    z-index:3;
}

.login-form {
    margin-top:130px;
}

.stTextInput input {
    height:40px;
    border-radius:25px;
    border:none;
    padding-left:18px;
}

.stButton > button {
    width:100%;
    height:46px;
    border-radius:25px;
    border:none;
    background:white;
    color:#111;
    font-weight:bold;
}

.small-btn button {
    background:transparent !important;
    height:25px !important;
    font-size:12px !important;
    color:#555 !important;
    box-shadow:none !important;
}

.signup-text {
    text-align:center;
    font-size:13px;
    margin-top:12px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    f'<img class="robot" src="data:image/png;base64,{img}">',
    unsafe_allow_html=True
)

st.markdown('<div class="login-form">', unsafe_allow_html=True)

st.text_input("Phone Number or ID", label_visibility="collapsed", placeholder="Phone Number or ID")
st.text_input("Password", type="password", label_visibility="collapsed", placeholder="Password")

st.markdown('<div class="small-btn">', unsafe_allow_html=True)
if st.button("Forgot Password?"):
    st.switch_page("pages/2_Forgot_Password.py")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Log In ›"):
    st.switch_page("pages/3_Employee.py")

st.markdown('<div class="signup-text">👤 New User?</div>', unsafe_allow_html=True)

st.markdown('<div class="small-btn">', unsafe_allow_html=True)
if st.button("Create Account"):
    st.switch_page("pages/1_Create_Account.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
