import streamlit as st
import streamlit.components.v1 as components
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

html = """
<html>
<head>
<style>
body{margin:0;background:#eef3f6;font-family:Arial}

.phone{
width:360px;height:660px;margin:auto;border-radius:42px;overflow:hidden;
position:relative;background:linear-gradient(180deg,#c9e7f7,#dff4ff)
}

.robot{position:absolute;top:85px;left:110px;width:140px}

.form{position:absolute;top:260px;left:40px;width:280px}

.input{
width:100%;height:42px;border-radius:25px;margin-bottom:12px;
padding-left:18px;border:none;background:white
}

.forgot{text-align:center;font-size:12px;margin:10px 0}

.login{
width:100%;height:46px;border-radius:25px;background:white;
font-weight:bold;border:none;cursor:pointer
}

.signup{text-align:center;font-size:13px;margin-top:12px}

.error{text-align:center;color:red;font-size:11px;margin-top:5px}
</style>
</head>

<body>
<div class="phone">

<img class="robot" src="data:image/png;base64,IMG_HERE">

<div class="form">

<input id="username" class="input" placeholder="phone / ID Number" maxlength="11"
oninput="this.value=this.value.replace(/[^0-9]/g,'')">

<input class="input" placeholder="Password" type="password">

<div class="forgot">
<a href="?page=forgot" target="_top">Forgot Password?</a>
</div>

<button class="login" onclick="login()">Log In ›</button>

<div id="error" class="error"></div>

<div class="signup">
👤 New User?
<a href="?page=create" target="_top">Create Account</a>
</div>

</div>
</div>

<script>
function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");

    if(/^[0-9]{11}$/.test(v)){
        window.top.location.href = "/?page=employee";
    } else {
        e.innerText = "Enter valid ID (11 digits)";
    }
}
</script>

</body>
</html>
"""

html = html.replace("IMG_HERE", img)

components.html(html, height=700)
