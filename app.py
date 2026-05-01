import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Telecom App", layout="centered")

# 🔥 نظام التنقل
page = st.query_params.get("page", "")

if page == "create":
    st.switch_page("pages/1_Create_Account.py")

elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")

elif page == "employee":
    st.switch_page("pages/3_Employee.py")

elif page == "todo":
    st.switch_page("pages/4_To_Do.py")

# 📸 تحميل الصورة
BASE_DIR = os.path.dirname(__file__)
robot_path = os.path.join(BASE_DIR, "robot.png")

with open(robot_path, "rb") as f:
    img = base64.b64encode(f.read()).decode()

# 🎨 الواجهة
html = """
<html>
<head>
<style>
body{margin:0;background:#eef3f6;font-family:Arial}

.phone{
width:360px;height:660px;margin:auto;border-radius:42px;overflow:hidden;
position:relative;background:linear-gradient(180deg,#c9e7f7,#dff4ff)
}

.robot{
position:absolute;top:85px;left:168px;width:145px;z-index:3
}

.form{
position:absolute;top:200px;left:58px;width:244px;z-index:2
}

.input{
width:100%;height:40px;border-radius:25px;margin-bottom:13px;
padding-left:18px;border:none;background:white;box-sizing:border-box
}

.forgot{
text-align:center;font-size:11px;margin:8px 0 20px;
}

.login{
width:100%;height:46px;border-radius:25px;background:white;
text-align:center;line-height:46px;font-weight:bold;cursor:pointer;
margin-top:10px;
}

.signup{
text-align:center;font-size:13px;margin-top:15px;
}
</style>
</head>

<body>
<div class="phone">

<img class="robot" src="data:image/png;base64,IMG_HERE">

<div class="form">

<input class="input" placeholder="Phone Number or ID">
<input class="input" placeholder="Password" type="password">

<div class="forgot">
<a href="?page=forgot" target="_top" style="color:#555;text-decoration:none;">
Forgot Password?
</a>
</div>

<a href="?page=employee" target="_top" style="text-decoration:none;">
<div class="login">Log In ›</div>
</a>

<div class="signup">
👤 New User?
<a href="?page=create" target="_top" style="color:#222;text-decoration:underline;">
Create Account
</a>
</div>

</div>
</div>
</body>
</html>
"""

html = html.replace("IMG_HERE", img)

components.html(html, height=700)
