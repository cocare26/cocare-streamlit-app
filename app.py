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
[data-testid="stAppViewContainer"] {
    background:#eef3f6;
}

.block-container {
    max-width:360px;
    min-height:660px;
    margin:auto;
    border-radius:42px;
    background:linear-gradient(180deg,#c9e7f7,#dff4ff);
    padding:80px 50px 30px 50px;
}

header, footer {visibility:hidden;}

.robot{
    width:140px;
    position:relative;
    top:40px;      /* نزليه لتحت */
    left:70px;     /* حركيه لليمين */
    z-index:2;
}

.stTextInput{
    margin-top:-30px;  /* يرفع البوكس لفوق تحت البوت */
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

.small button {
    background:transparent !important;
    height:25px !important;
    color:#555 !important;
    font-size:12px !important;
    box-shadow:none !important;
}

.signup-text {
    text-align:center;
    font-size:13px;
    margin-top:12px;
}
</style>
""", unsafe_allow_html=True)

# 🔹 Robot Image
st.markdown(
    f'<img class="robot" src="data:image/png;base64,{img}">',
    unsafe_allow_html=True
)

# 🔹 Inputs
user_id = st.text_input(
    "",
    placeholder="phone / ID Number",
    max_chars=11
)

password = st.text_input(
    "",
    placeholder="Password",
    type="password"
)

# 🔹 Forgot Password
st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Forgot Password?"):
    st.switch_page("pages/2_Forgot_Password.py")
st.markdown('</div>', unsafe_allow_html=True)

# 🔥 Login Logic (UPDATED)
if st.button("Log In ›"):
    user_id = user_id.strip()

    if (
        (user_id.isdigit() and len(user_id) == 11) or  # ID
        (user_id.isdigit() and len(user_id) == 10 and user_id.startswith("07"))  # Phone
    ):
        st.switch_page("pages/3_Employee.py")
    else:
        st.error("Enter valid phone number or ID")

# 🔹 Create Account
st.markdown("<div class='signup-text'>👤 New User?</div>", unsafe_allow_html=True)

st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Create Account"):
    st.switch_page("pages/1_Create_Account.py")
st.markdown('</div>', unsafe_allow_html=True)
