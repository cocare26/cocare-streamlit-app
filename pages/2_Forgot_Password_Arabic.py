import time
import streamlit as st

st.set_page_config(page_title="نسيت كلمة المرور", layout="centered")

if "reset_code" not in st.session_state:
    st.session_state.reset_code = ""

st.markdown("""
<style>

:root{
    --navy:#0f2446;
    --accent:#2f80ed;
}

/* الكارد */
.block-container {
    max-width: 390px;
    padding: 22px 30px 30px 30px;
    background: linear-gradient(180deg,#c9e7f7,#dff4ff);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* العنوان */
h1 {
    font-size: 22px !important;
    text-align: center;
    color: var(--navy);
    margin-top: 10px !important;
    font-weight: 900;
}

/* RTL كامل */
body {
    direction: rtl;
}

/* input */
div[data-testid="stTextInput"] input {
    border-radius: 25px;
    height: 44px;
    border: none !important;
    outline: none !important;
    padding-right: 16px;
    background: rgba(255,255,255,0.95);
}

/* الأزرار */
.stButton > button {
    width: 100%;
    height: 46px;
    border-radius: 25px;
    border: none;
    background: linear-gradient(90deg,#2f80ed,#1c6fa4);
    color: white;
    font-weight: bold;
    transition: .2s;
}

.stButton > button:hover {
    transform: translateY(-2px);
}

/* زر الرجوع */
div.stButton:nth-of-type(3) > button {
    background: white;
    color: var(--navy);
}

</style>
""", unsafe_allow_html=True)

st.title("نسيت كلمة المرور")

# 📱 رقم الهاتف
phone = st.text_input("رقم الهاتف", max_chars=10)

# 📩 إرسال الكود
if st.button("إرسال الكود"):
    if phone.isdigit() and len(phone) == 10 and phone.startswith("07"):
        st.session_state.reset_code = "0000"
        st.success("يرجى التحقق من رسالة SMS")
    else:
        st.error("يجب أن يكون الرقم 10 أرقام ويبدأ بـ 07")

# 🔐 إدخال الكود
code = st.text_input("أدخل الكود")

# 🔑 كلمات المرور
new_password = st.text_input("كلمة المرور الجديدة", type="password")
confirm_password = st.text_input("تأكيد كلمة المرور", type="password")

# ✅ إعادة التعيين
if st.button("تغيير كلمة المرور"):
    if not phone or not code or not new_password or not confirm_password:
        st.error("يرجى تعبئة جميع الحقول")
    elif code != st.session_state.reset_code:
        st.error("الكود غير صحيح")
    elif new_password != confirm_password:
        st.error("كلمتا المرور غير متطابقتين")
    else:
        st.success("تم تغيير كلمة المرور بنجاح")
        time.sleep(1)
        st.switch_page("app.py")

# 🔙 رجوع
if st.button("العودة لتسجيل الدخول"):
    st.switch_page("app.py")
