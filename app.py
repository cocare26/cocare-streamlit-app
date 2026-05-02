import streamlit as st
import streamlit.components.v1 as components
import base64

# تأكدي من وجود المجلد والملفات بنفس الأسماء
# pages/3_Employee.py

st.set_page_config(page_title="Telecom App", layout="centered")

# قراءة البارامترات
page = st.query_params.get("page", "")

# تحويل الصفحات بناءً على الرابط
if page == "employee":
    st.switch_page("pages/3_Employee.py")
elif page == "customer":
    st.switch_page("pages/2_Customer.py")
elif page == "create":
    st.switch_page("pages/1_Create_Account.py")
elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")

# كود تحويل الصورة
try:
    with open("robot.png", "rb") as f:
        img = base64.b64encode(f.read()).decode()
except:
    img = ""

html_code = f"""
<html>
<head>
    <style>
        /* نفس التنسيقات السابقة */
        body {{ margin:0; background:#eef2f7; font-family:Arial; }}
        .phone {{ width:360px; height:660px; margin:auto; border-radius:42px; overflow:hidden; position:relative; background:linear-gradient(160deg,#d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); box-shadow:0 10px 30px rgba(0,0,0,.22); }}
        .robot {{ position:absolute; top:85px; left:168px; width:145px; z-index:3; }}
        .form {{ position:absolute; top:200px; left:58px; width:244px; z-index:2; }}
        .input {{ width:100%; height:44px; border-radius:25px; margin-bottom:13px; padding-left:18px; border:none; outline:none; background:rgba(255,255,255,0.95); box-sizing:border-box; }}
        .login {{ width:100%; height:46px; border-radius:25px; background:linear-gradient(90deg,#2f80ed,#1c6fa4); color:white; text-align:center; line-height:46px; font-weight:bold; border:none; cursor:pointer; }}
        .error {{ text-align:center; color:#c62828; font-size:11px; margin-top:8px; }}
    </style>
</head>
<body>
    <div class="phone">
        <img class="robot" src="data:image/png;base64,{img}">
        <div class="form">
            <input id="username" class="input" placeholder="phone / ID Number" type="text">
            <input class="input" placeholder="Password" type="password">
            <button class="login" onclick="validateAndLogin()">Log In ›</button>
            <div id="error" class="error"></div>
        </div>
    </div>

    <script>
    function validateAndLogin() {{
        const userVal = document.getElementById("username").value;
        const errorDiv = document.getElementById("error");
        
        // إذا كان الرقم 11 خانة (موظف)
        if (userVal.length === 11) {{
            // استخدام window.parent للوصول للرابط الأساسي في Streamlit
            window.parent.location.href = window.parent.location.origin + window.parent.location.pathname + "?page=employee";
        }} 
        else if (userVal.startsWith("07") && userVal.length === 10) {{
            window.parent.location.href = window.parent.location.origin + window.parent.location.pathname + "?page=customer";
        }}
        else {{
            errorDiv.innerText = "Check ID or Phone Number";
        }}
    }}
    </script>
</body>
</html>
"""

components.html(html_code, height=700)
