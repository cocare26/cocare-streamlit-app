import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="CoCare App", layout="centered")
page = st.query_params.get("page", "").lower()

# --- Router Logic ---
if page == "create": st.switch_page("pages/1_Create_Account.py")
elif page == "employee": st.switch_page("pages/3_Employee.py")
elif page == "forgot": st.switch_page("pages/2_Forgot_Password.py")
elif page == "settings_en": st.switch_page("setting.py")
elif page == "change_password": st.switch_page("Change_Password.py")
elif page == "change_language": st.switch_page("Change_Language.py")
elif page == "rate_app": st.switch_page("Rate_App.py")
elif page == "report_problem": st.switch_page("Report_Problem.py")
elif page == "contact_us": st.switch_page("Contact_Us.py")
elif page == "settings-ar": st.switch_page("setting-ar.py")
elif page == "change_password-ar": st.switch_page("changepassword-ar.py")
elif page == "change_language-ar": st.switch_page("changelanguage-ar.py")
elif page == "rate_app-ar": st.switch_page("rate-ar.py")
elif page == "report_problem-ar": st.switch_page("report-ar.py")
elif page == "contact_us-ar": st.switch_page("contact-ar.py")
elif page == "logout":
    st.query_params.clear()
    st.switch_page("app.py")

# واجهة تسجيل الدخول (Login)
try:
    with open("robot.png", "rb") as f: img = base64.b64encode(f.read()).decode()
except: img = ""

html = f"""
<html>
<body style="margin:0;background:#eef3f6;font-family:Arial">
<div style="width:360px;height:660px;margin:auto;border-radius:42px;position:relative;background:linear-gradient(180deg,#c9e7f7,#dff4ff);overflow:hidden">
    <img src="data:image/png;base64,{img}" style="position:absolute;top:85px;left:168px;width:145px">
    <div style="position:absolute;top:200px;left:58px;width:244px">
        <input id="u" style="width:100%;height:40px;border-radius:25px;margin-bottom:13px;padding-left:18px;border:none" placeholder="phone / ID Number">
        <input type="password" style="width:100%;height:40px;border-radius:25px;margin-bottom:13px;padding-left:18px;border:none" placeholder="Password">
        <button onclick="window.top.location.href='/?page=settings_en'" style="width:100%;height:46px;border-radius:25px;background:white;font-weight:bold;border:none;cursor:pointer">Log In ›</button>
    </div>
</div>
</body>
</html>
"""
components.html(html, height=700)
