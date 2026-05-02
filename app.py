import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Telecom App", layout="centered")

page = st.query_params.get("page", "")

if page == "create":
    st.switch_page("pages/1_Create_Account.py")
elif page == "customer":
    st.switch_page("pages/2_Customer.py")
elif page == "employee":
    st.switch_page("pages/3_Employee.py")
elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")
elif page == "todo":
    st.switch_page("pages/4_To_Do.py")

BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, "robot.png"), "rb") as f:
    img = base64.b64encode(f.read()).decode()

html = """
<html>
<head>
<style>
body{margin:0;background:#eef2f7;font-family:Arial}
.phone{
    width:360px;height:660px;margin:auto;border-radius:42px;overflow:hidden;
    position:relative;background:linear-gradient(160deg,#d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
    box-shadow:0 10px 30px rgba(0,0,0,.22);
}
.robot{
    position:absolute;top:85px;left:168px;width:145px;z-index:3;
    filter:drop-shadow(0 8px 12px rgba(0,0,0,.18));
}
.form{position:absolute;top:200px;left:58px;width:244px;z-index:2}
.input{
    width:100%;height:44px;border-radius:25px;margin-bottom:13px;
    padding-left:18px;border:none;outline:none;background:rgba(255,255,255,0.95);
    box-sizing:border-box;box-shadow:0 3px 10px rgba(0,0,0,.08);
}
.forgot{text-align:center;font-size:11px;margin:8px 0 20px}
.login{
    width:100%;height:46px;border-radius:25px;
    background:linear-gradient(90deg,#2f80ed,#1c6fa4);
    color:white;font-weight:bold;border:none;cursor:pointer;
    box-shadow:0 6px 14px rgba(47,128,237,.25);
}
.signup{text-align:center;font-size:13px;margin-top:15px;color:#222}
.error{text-align:center;color:#c62828;font-size:11px;margin-top:8px}
</style>
</head>

<body>
<div class="phone">
<img class="robot" src="data:image/png;base64,IMG_HERE">

<form class="form" id="loginForm" action="/" method="get" target="_top">
    <input type="hidden" name="page" id="pageValue">

    <input id="username" class="input" placeholder="phone / ID Number"
    inputmode="numeric" maxlength="11"
    oninput="this.value=this.value.replace(/[^0-9]/g,'')">

    <input class="input" placeholder="Password" type="password">

    <div class="forgot">
        <a href="?page=forgot" target="_top" style="color:#555; text-decoration:none;">
            Forgot Password?
        </a>
    </div>

    <button class="login" type="button" onclick="login()">Log In ›</button>

    <div id="error" class="error"></div>

    <div class="signup">
        👤 New User?
        <a href="?page=create" target="_top" style="color:#222; text-decoration:underline;">
            Create Account
        </a>
    </div>
</form>
</div>

<script>
function login(){
    const v = document.getElementById("username").value;
    const e = document.getElementById("error");
    const pageValue = document.getElementById("pageValue");
    const form = document.getElementById("loginForm");

    if(/^07[0-9]{8}$/.test(v)){
        pageValue.value = "customer";
        form.submit();
    }
    else if(/^[0-9]{11}$/.test(v)){
        pageValue.value = "employee";
        form.submit();
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
