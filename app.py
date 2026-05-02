import streamlit as st
import base64
import os

st.set_page_config(page_title="Telecom App", layout="centered")

# 🔹 Navigation
page = st.query_params.get("page", "")

if page == "create":
    st.switch_page("pages/1_Create_Account.py")
elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")
elif page == "employee":
    st.switch_page("pages/3_Employee.py")
elif page == "todo":
    st.switch_page("pages/4_To_Do.py")

# 🔹 Image
BASE_DIR = os.path.dirname(__file__)
robot_path = os.path.join(BASE_DIR, "robot.png")

with open(robot_path, "rb") as f:
    img = base64.b64encode(f.read()).decode()

# 🔹 Style
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background:#e6eef5;
}

.block-container{
    max-width:360px;
    height:660px;
    margin:auto;
    border-radius:40px;
    background: linear-gradient(145deg,#cfe6f5,#9fbcd1);
    box-shadow: 0 10px 25px rgba(0,0,0,.25);
    padding:100px 40px 40px 40px;
    position:relative;
    overflow:hidden;
}

.robot{
    width:150px;
    position:absolute;
    top:70px;
    left:50%;
    transform:translateX(-50%);
    z-index:5;
}

.stTextInput input{
    width:100%;
    height:45px;
    border-radius:25px;
    border:none;
    padding-left:20px;
    background:#ffffff;
    box-shadow:0 4px 12px rgba(0,0,0,.1);
}

.stButton > button{
    width:100%;
    height:48px;
    border-radius:25px;
    border:none;
    background:#ffffff;
    font-weight:bold;
    margin-top:10px;
}

.small button{
    background:transparent !important;
    color:#333 !important;
    box-shadow:none !important;
    font-size:12px !important;
}

.signup-text{
    text-align:center;
    font-size:13px;
    margin-top:14px;
}

header, footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# 🔹 Robot
st.markdown(
    f'<img class="robot" src="data:image/png;base64,{img}">',
    unsafe_allow_html=True
)

# 🔹 Inputs
user_id = st.text_input("", placeholder="phone / ID Number", max_chars=11)
password = st.text_input("", placeholder="Password", type="password")

# 🔹 Forgot
st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Forgot Password?"):
    st.switch_page("pages/2_Forgot_Password.py")
st.markdown('</div>', unsafe_allow_html=True)

# 🔥 Login Logic (Python فقط)
if st.button("Log In ›"):
    user_id = user_id.strip()

    if (
        (user_id.isdigit() and len(user_id) == 11) or
        (user_id.isdigit() and len(user_id) == 10 and user_id.startswith("07"))
    ):
        st.switch_page("pages/3_Employee.py")
    else:
        st.error("Enter valid phone number or ID")

# 🔹 Create
st.markdown("<div class='signup-text'>👤 New User?</div>", unsafe_allow_html=True)

st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Create Account"):
    st.switch_page("pages/1_Create_Account.py")
st.markdown('</div>', unsafe_allow_html=True)
