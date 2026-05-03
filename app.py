import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Telecom App", layout="centered")

page = st.query_params.get("page", "")
if isinstance(page, list):
    page = page[0]
page = page or ""

if page == "create":
    st.switch_page("pages/1_Create_Account.py")
elif page == "customer":
    st.switch_page("pages/2_Customer.py")
elif page == "employee":
    st.switch_page("pages/3_Employee.py")
elif page == "todo":
    st.switch_page("pages/4_To_Do_List.py")
elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")
elif page == "customer_support":
    st.switch_page("pages/5_Customer_Support_Arabic.py")
elif page == "network_diagnostics":
    st.switch_page("pages/6_Network_Diagnostics_Arabic.py")
elif page == "customer_management":
    st.switch_page("pages/7_Customer_Management_Arabic.py")
elif page == "employee_performance":
    st.switch_page("pages/8_Employee_Performance_Arabic.py")
elif page == "service_management":
    st.switch_page("pages/9_Service_Management_Arabic.py")
elif page == "settings":
    st.switch_page("pages/10_Settings_Arabic.py")
elif page == "notifications":
    st.switch_page("pages/11_Notifications_Arabic.py")
elif page == "change_password":
    st.switch_page("pages/Change_Password.py")
elif page == "change_language":
    st.switch_page("pages/Change_Language.py")
elif page == "report_problem":
    st.switch_page("pages/Report_Problem.py")
elif page == "contact_us":
    st.switch_page("pages/Contact_Us.py")
elif page == "rate_app":
    st.switch_page("pages/Rate_App.py")
elif page == "settings_en":
    st.switch_page("pages/setting.py")
elif page == "settings_ar":
    st.switch_page("pages/setting-ar.py")

st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}
.block-container{
    padding-top:20px;
}
header, footer{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

with open("robot.png", "rb") as f:
    img = base64.b64encode(f.read()).decode()

html = f"""
<html>
<body style="margin:0;background:#eef3f6;font-family:Arial">

<div style="
width:360px;
height:660px;
margin:auto;
border-radius:42px;
background:linear-gradient(180deg,#c9e7f7,#dff4ff);
position:relative;
overflow:hidden;
">

<img src="data:image/png;base64,{img}" 
style="position:absolute;top:85px;left:110px;width:140px">

<div style="position:absolute;top:250px;left:60px;width:240px;">

<input id="username" placeholder="phone / ID"
style="
width:100%;
height:40px;
border-radius:25px;
margin-bottom:12px;
border:none;
padding-left:15px;
">

<input id="password" type="password" placeholder="Password"
style="
width:100%;
height:40px;
border-radius:25px;
margin-bottom:12px;
border:none;
padding-left:15px;
">

<div style="text-align:center;font-size:12px;margin-bottom:15px;">
    <a href="/?page=forgot" target="_top" style="color:#333;text-decoration:none;">
        Forgot Password?
    </a>
</div>

<button onclick="login()"
style="
width:100%;
height:45px;
border-radius:25px;
border:none;
font-weight:bold;
background:white;
color:#0f2446;
cursor:pointer;
">
Log In
</button>

<p id="error" style="color:red;text-align:center;font-size:12px;"></p>

<div style="text-align:center;font-size:13px;margin-top:12px;">
    👤 New User?
    <a href="/?page=create" target="_top" style="
        color:#0f2446;
        font-weight:bold;
        text-decoration:underline;
    ">
        Create Account
    </a>
</div>

</div>
</div>

<script>
function go(p){{
    window.top.location.href = "/?page=" + p;
}}

function login(){{
    let v = document.getElementById("username").value;
    let e = document.getElementById("error");

    if(/^07[0-9]{{8}}$/.test(v)){{
        go("customer");
    }}
    else if(/^[0-9]{{11}}$/.test(v)){{
        go("employee");
    }}
    else{{
        e.innerText = "Invalid phone or ID";
    }}
}}
</script>

</body>
</html>
"""

components.html(html, height=700)
