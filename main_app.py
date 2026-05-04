import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Telecom App", layout="centered")

page = st.query_params.get("page", "")

# ========= LOGIN / MAIN =========
if page == "customer":
    st.switch_page("pages/2_Customer.py")

elif page == "employee":
    st.switch_page("pages/3_Employee.py")

elif page == "create":
    st.switch_page("pages/1_Create_Account.py")

elif page == "forgot":
    st.switch_page("pages/2_Forgot_Password.py")

elif page == "todo":
    st.switch_page("pages/4_To_Do.py")

# ========= SETTINGS =========
elif page == "Change_password-ar":
    st.switch_page("pages/Change_password-ar.py")

elif page == "Change_language-ar":
    st.switch_page("pages/Change_language-ar.py")

elif page == "Rate_app-ar":
    st.switch_page("pages/Rate_app-ar.py")

elif page == "Report_Problem-ar":
    st.switch_page("pages/Report_Problem-ar.py")

elif page == "Contact_Us-ar":
    st.switch_page("pages/Contact_Us-ar.py")

elif page == "logout":
    st.switch_page("pages/logout.py")

# ========= DEFAULT (LOGIN UI) =========
else:
    with open("robot.png", "rb") as f:
        img = base64.b64encode(f.read()).decode()

    html = """
    <html>
    <body style="margin:0;background:#eef3f6;font-family:Arial">
    <div style="width:360px;height:660px;margin:auto;border-radius:42px;overflow:hidden;
    position:relative;background:linear-gradient(180deg,#c9e7f7,#dff4ff)">

    <img src="data:image/png;base64,IMG_HERE" style="position:absolute;top:85px;left:168px;width:145px;">

    <form method="get" action="/" onsubmit="return setPage()" 
    style="position:absolute;top:200px;left:58px;width:244px;">

    <input type="hidden" name="page" id="pageValue">

    <input id="username" placeholder="phone / ID Number"
    style="width:100%;height:40px;border-radius:25px;margin-bottom:13px;padding-left:18px;border:none">

    <input placeholder="Password" type="password"
    style="width:100%;height:40px;border-radius:25px;margin-bottom:13px;padding-left:18px;border:none">

    <button type="submit" 
    style="width:100%;height:46px;border-radius:25px;background:white;font-weight:bold">
    Log In ›</button>

    </form>

    <script>
    function setPage(){
        const v = document.getElementById("username").value;
        const pageValue = document.getElementById("pageValue");

        if(/^[0-9]{11}$/.test(v)){
            pageValue.value = "employee";
            return true;
        }

        if(/^[0-9]{10}$/.test(v)){
            pageValue.value = "customer";
            return true;
        }

        alert("10 digits for Customer, 11 digits for Employee");
        return false;
    }
    </script>

    </div>
    </body>
    </html>
    """

    html = html.replace("IMG_HERE", img)
    components.html(html, height=700)
