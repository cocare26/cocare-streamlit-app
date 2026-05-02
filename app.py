import streamlit as st
import base64
import os

st.set_page_config(page_title="Telecom App", layout="centered")

# تحميل صورة البوت
BASE_DIR = os.path.dirname(__file__)
robot_path = os.path.join(BASE_DIR, "robot.png")

with open(robot_path, "rb") as f:
    img = base64.b64encode(f.read()).decode()

# 🎨 التصميم
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
    top:140px;
    right:-20px;
    width:130px;
    z-index:5;
    transform:translateY(-35%);
}

.spacer { height:150px; }

/* inputs */
.stTextInput input {
    height:46px;
    border-radius:30px;
    border:none;
    outline:none;
    background:rgba(255,255,255,0.95);
    box-shadow:0 6px 16px rgba(0,0,0,0.08);
    padding-left:18px;
}

/* buttons */
.stButton > button {
    width:100%;
    height:46px;
    border-radius:25px;
    border:none;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;
    font-weight:bold;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
    margin-top:10px;
}

/* small buttons */
.small button {
    background:white !important;
    color:#0f2446 !important;
    box-shadow:0 2px 8px rgba(0,0,0,.1) !important;
    height:32px !important;
    font-size:12px !important;
}

.signup-text {
    text-align:center;
    font-size:13px;
    margin-top:14px;
    color:#0f2446;
}

</style>
""", unsafe_allow_html=True)

# عرض البوت
st.markdown(
    f'<img class="robot" src="data:image/png;base64,{img}">',
    unsafe_allow_html=True
)

st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

# 🔹 Inputs
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

# 🔹 Forgot Password
st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Forgot Password?"):
    st.switch_page("pages/2_Forgot_Password.py")
st.markdown('</div>', unsafe_allow_html=True)

# 🔥 Login (المهم)
if st.button("Log In ›"):
    user_value = user_value.strip()

    if (
        user_value.isdigit()
        and (
            (len(user_value) == 10 and user_value.startswith("07"))
            or len(user_value) == 11
        )
    ):
        st.switch_page("pages/3_Employee.py")

    else:
        st.error("Invalid phone or ID number")

# 🔹 Create account
st.markdown('<div class="signup-text">👤 New User?</div>', unsafe_allow_html=True)

st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Create Account"):
    st.switch_page("pages/1_Create_Account.py")
st.markdown('</div>', unsafe_allow_html=True)
