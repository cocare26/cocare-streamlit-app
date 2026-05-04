import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Telecom App", layout="centered")

page = st.query_params.get("page", "")
page = page or ""

if page == "create":
    st.switch_page("pages/1_Create_Account.py")

elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")

elif page == "customer":
    st.switch_page("pages/2_Customer.py")

elif page == "employee":
    st.switch_page("pages/3_Employee.py")

elif page == "todo":
    st.switch_page("pages/4_To_Do.py")
    
with open("robot.png", "rb") as f:
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
.robot{position:absolute;top:85px;left:168px;width:145px;z-index:3}
.form{position:absolute;top:200px;left:58px;width:244px;z-index:2}
.input{
width:100%;height:40px;border-radius:25px;margin-bottom:13px;
padding-left:18px;border:none;background:white;box-sizing:border-box
}
.forgot{text-align:center;font-size:11px;color:#555;margin:8px 0 20px;cursor:pointer}
.login{
width:100%;height:46px;border-radius:25px;background:white;
text-align:center;line-height:46px;font-weight:bold;border:none;cursor:pointer
}
.signup{
display:block;
text-align:center;
font-size:13px;
margin-top:15px;
cursor:pointer;
color:#222;
text-decoration:none;
}
.error{text-align:center;color:#c62828;font-size:11px;margin-top:8px}

.signup-line{
    text-align:center;
    font-size:13px;
    margin-top:15px;
    color:#222;
}

.signup-line span{
    color:#1c6fa4;
    font-weight:bold;
    text-decoration:none;
    margin-left:4px;
    cursor:pointer;
}
</style>
</head>

<body>
<div class="phone">
<img class="robot" src="data:image/png;base64,IMG_HERE">

<form class="form" id="loginForm" method="get" target="_top">
    <input type="hidden" name="page" id="pageValue">

    <input id="username" class="input" placeholder="phone / ID Number"
    inputmode="numeric" maxlength="11"
    oninput="this.value=this.value.replace(/[^0-9]/g,'')">

    <input class="input" placeholder="Password" type="password">

    <div class="forgot">
    <a href="/?page=forgot" target="_self" style="color:#555; text-decoration:none;">
        Forgot Password?
    </a>
</div>
    <button class="login" type="button" onclick="login()">Log In ›</button>
    <div id="error" class="error"></div>
    <div class="signup">
    👤 New User?
    <a href="/?page=create" target="_self" style="color:#222; text-decoration:underline;">
        Create Account
    </a>
</div>
</form>
</div>

<script>
function goPage(p){
    window.top.location.href = "/?page=" + p;
}

function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");

    if(/^07[0-9]{8}$/.test(v)){
        goPage("customer");
    }
    else if(/^[0-9]{11}$/.test(v)){
        goPage("employee");
    }
    else{
        e.innerText = "Invalid phone or ID number";
    }
}
</script>
</body>
</html>
"""

html = html.replace("IMG_HERE", img)
components.html(html, height=700)
