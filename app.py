import streamlit as st
import base64
import os

st.set_page_config(page_title="Telecom App", layout="centered")

if "login_error" not in st.session_state:
    st.session_state.login_error = ""

BASE_DIR = os.path.dirname(__file__)
robot_path = os.path.join(BASE_DIR, "robot.png")

with open(robot_path, "rb") as f:
    img = base64.b64encode(f.read()).decode()

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background:#eef2f7;
}

.block-container {
    max-width:360px;
    height:660px;
    margin:auto;
    border-radius:42px;
    background:linear-gradient(160deg,#d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
    box-shadow:0 10px 30px rgba(0,0,0,.22);
    padding:95px 58px 30px 58px;
    position:relative;
}

header, footer {visibility:hidden;}

.robot{
    position:absolute;

    top:140px;      /* مستوى بوكس الفون */
    right:-20px;    /* 🔥 هذا السر — يطلعه لبرا */

    width:130px;
    z-index:5;

    transform: translateY(-35%);
}
.spacer {
    height:150px;
}

.stTextInput input {
    height:44px;
    border-radius:25px;
    border:none;
    outline:none;
    background:rgba(255,255,255,0.95);
    box-shadow:0 3px 10px rgba(0,0,0,.08);
    padding-left:18px;
}

.stButton > button {
    width:100%;
    height:46px;
    border-radius:25px;
    border:none;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;
    font-weight:bold;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

.small button {
    background:transparent !important;
    color:#555 !important;
    box-shadow:none !important;
    height:25px !important;
    font-size:12px !important;
}

.forgot,
.signup{
    text-align:center;
    width:100%;
}

.forgot a{
    display:block;
    width:100%;
    height:42px;
    line-height:42px;
    border-radius:25px;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white !important;
    text-decoration:none !important;
    font-weight:700;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
}

.login{
    width:100%;
    height:46px;
    border-radius:25px;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;
    text-align:center;
    line-height:46px;
    font-weight:bold;
    border:none;
    cursor:pointer;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
    margin:10px 0 14px;
}

.signup{
    font-size:13px;
    margin-top:0;
    color:#0f2446;
}

.signup a{
    display:block;
    width:100%;
    height:42px;
    line-height:42px;
    border-radius:25px;
    margin-top:10px;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white !important;
    text-decoration:none !important;
    font-weight:700;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
}
.input{
    width:100%;
    height:46px;

    border:none;              /* ❌ إزالة الحواف */
    outline:none;             /* ❌ إزالة إطار التركيز */

    border-radius:30px;       /* 🔥 نعومة أكثر */
    padding-left:18px;

    background:rgba(255,255,255,0.95);

    /* ✨ سموث */
    box-shadow:0 6px 16px rgba(0,0,0,0.08);

    transition:all 0.25s ease;
}
.input:focus{
    box-shadow:0 8px 20px rgba(47,128,237,0.25);
    background:white;
}
</style>
""", unsafe_allow_html=True)

st.markdown(f'<img class="robot" src="data:image/png;base64,{img}">', unsafe_allow_html=True)
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

user_value = st.text_input(
    "phone / ID Number",
    max_chars=11,
    label_visibility="collapsed",
    placeholder="phone / ID Number"
)

password = st.text_input(
    "Password",
    type="password",
    label_visibility="collapsed",
    placeholder="Password"
)
<div class="forgot">
    <a href="/?page=forgot" target="_top">Forgot Password?</a>
</div>

<button class="login" type="button" onclick="login()">Log In ›</button>

<div class="signup">
    👤 New User?
    <a href="/?page=create" target="_top">Create Account</a>
</div>
st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Forgot Password?"):
    st.switch_page("pages/2_Forgot_Password.py")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Log In ›"):
    user_value = user_value.strip()

    if user_value.isdigit() and len(user_value) == 10 and user_value.startswith("07"):
        st.switch_page("pages/2_Customer.py")

    elif user_value.isdigit() and len(user_value) == 11:
        st.switch_page("pages/3_Employee.py")

    else:
        st.error("Invalid phone or ID number")

st.markdown('<div class="signup-text">👤 New User?</div>', unsafe_allow_html=True)

st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Create Account"):
    st.switch_page("pages/1_Create_Account.py")
st.markdown('</div>', unsafe_allow_html=True)
