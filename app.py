import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Telecom App", layout="centered")

page = st.query_params.get("page", "")

if page == "create":
    st.switch_page("pages/1_Create_Account.py")

elif page == "employee":
    st.switch_page("pages/3_Employee.py")

elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")

with open("robot.png", "rb") as f:
    img = base64.b64encode(f.read()).decode()

html = """
<html>
<head>
<style>
body{margin:0;background:#eef3f6;font-family:Arial}
.phone{
width:360px;height:660px;margin:auto;border-radius:42px;overflow:hidden;
position:relative;background:linear-gradient(160deg,#d6ecff,#bfe3ff,#eaf6ff)
}
.robot{
position:absolute;
top:140px;
right:-20px;
width:130px;
z-index:3;
transform:translateY(-35%);
}
.form{position:absolute;top:200px;left:58px;width:244px}
.input{
width:100%;height:44px;border-radius:25px;margin-bottom:13px;
padding-left:18px;border:none;background:white;
box-shadow:0 6px 16px rgba(0,0,0,0.08)
}
.login{
width:100%;height:46px;border-radius:25px;
background:linear-gradient(90deg,#2f80ed,#1c6fa4);
color:white;font-weight:bold;border:none;cursor:pointer
}
.forgot a,
.signup a{
display:block;
width:100%;
height:42px;
line-height:42px;
border-radius:25px;
margin-top:10px;
background:linear-gradient(90deg,#2f80ed,#1c6fa4);
color:white;
text-align:center;
text-decoration:none;
font-weight:700;
}
.error{text-align:center;color:red;font-size:12px;margin-top:8px}
</style>
</head>

<body>
<div class="phone">

<img class="robot" src="data:image/png;base64,IMG_HERE">

<div class="form">

<input id="username" class="input" placeholder="phone / ID Number"
inputmode="numeric" maxlength="11"
oninput="this.value=this.value.replace(/[^0-9]/g,'')">

<input class="input" placeholder="Password" type="password">

<div class="forgot">
<a href="/?page=forgot" target="_top">Forgot Password?</a>
</div>

<button class="login" onclick="login()">Log In ›</button>

<div id="error" class="error"></div>

<div class="signup">
<a href="/?page=create" target="_top">Create Account</a>
</div>

</div>
</div>

<script>
function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");

    // 🔥 دخول مباشر للموظف
    if(/^[0-9]{11}$/.test(v)){
        window.parent.location.href = "?page=employee";
    } 
    else{
        e.innerText = "Enter valid ID (11 digits)";
    }
}
</script>

</body>
</html>
"""

html = html.replace("IMG_HERE", img)
components.html(html, height=700)
