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
    min-height:660px;
    margin:auto;
    border-radius:42px;
    background:linear-gradient(180deg,#c9e7f7,#dff4ff);
    padding:80px 58px 30px 58px;
}
header, footer {visibility:hidden;}

.robot {
    width:145px;
    display:block;
    margin-left:auto;
    margin-right:5px;
    margin-bottom:-10px;
}

.stTextInput input {
    height:42px;
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

st.markdown(
    f'<img class="robot" src="data:image/png;base64,{img}">',
    unsafe_allow_html=True
)

user_id = st.text_input(
    "ID",
    placeholder="phone / ID Number",
    max_chars=11,
    label_visibility="collapsed"
)

password = st.text_input(
    "Password",
    placeholder="Password",
    type="password",
    label_visibility="collapsed"
)

st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Forgot Password?"):
    st.switch_page("pages/2_Forgot_Password.py")
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Log In ›"):
    user_id = user_id.strip()
    if user_id.isdigit() and len(user_id) == 11:
        st.switch_page("pages/3_Employee.py")
    else:
        st.error("Enter valid ID: 11 digits")

st.markdown("<div class='signup-text'>👤 New User?</div>", unsafe_allow_html=True)

st.markdown('<div class="small">', unsafe_allow_html=True)
if st.button("Create Account"):
    st.switch_page("pages/1_Create_Account.py")
st.markdown('</div>', unsafe_allow_html=True)حطلي <script>
function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");

    // يقبل Phone يبدأ بـ 07 وطوله 10
    // أو ID طوله 11
    if(/^07[0-9]{8}$/.test(v) || /^[0-9]{11}$/.test(v)){
        window.top.location.href = "/?page=employee";
    } else {
        e.innerText = "Enter valid phone number or ID";
    }
}
</script>
