import streamlit as st
import base64

st.set_page_config(page_title="تطبيق الاتصالات", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#eef3f6;
    direction: rtl;
}

.block-container {
    max-width: 430px;
    height: 700px;
    margin: auto;
    padding: 40px 35px;
    background: linear-gradient(180deg,#c9e7f7,#dff4ff);
    border-radius: 42px;
}

input {
    text-align: right;
    border-radius: 25px !important;
}

div.stButton > button {
    width: 100%;
    height: 46px;
    border-radius: 25px;
    background: white;
    color: black;
    font-weight: bold;
    border: none;
}
</style>
""", unsafe_allow_html=True)

with open("robot.png", "rb") as f:
    img = base64.b64encode(f.read()).decode()

st.markdown(
    f"""
    <div style="text-align:center;">
        <img src="data:image/png;base64,{img}" width="145">
    </div>
    """,
    unsafe_allow_html=True
)

username = st.text_input(
    "رقم الهاتف / رقم الهوية",
    max_chars=11,
    placeholder="رقم الهاتف / رقم الهوية"
)

password = st.text_input(
    "كلمة المرور",
    type="password",
    placeholder="كلمة المرور"
)

if st.button("تسجيل الدخول ›"):
    username = username.strip()

    if username.isdigit() and len(username) == 11:
        st.switch_page("pages/employee_dashboard_ara.py")

    elif username.startswith("07") and username.isdigit() and len(username) == 10:
        st.switch_page("pages/Customer_ar.py")

    else:
        st.error("رقم الهاتف أو الهوية غير صحيح")

col1, col2 = st.columns(2)

with col1:
    if st.button("هل نسيت كلمة المرور؟"):
        st.switch_page("pages/2_Forgot_Password.py")

with col2:
    if st.button("إنشاء حساب"):
        st.switch_page("pages/1_Create_Account.py")
