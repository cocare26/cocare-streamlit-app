
import time
import streamlit as st

st.set_page_config(page_title="إنشاء حساب", layout="centered")

if "generated_phone_code" not in st.session_state:
    st.session_state.generated_phone_code = ""

st.markdown("""
<style>

:root{
    --navy:#0f2446;
    --accent:#2f80ed;
}

.block-container {
    max-width: 480px;
    padding: 20px 30px;
    background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 40%, #eaf6ff 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

h1 {
    font-size: 24px;
    text-align: center;
    color: var(--navy);
    margin-bottom: 5px;
    font-weight: 900;
}

.signin-line {
    text-align: center;
    font-size: 14px;
    margin-top: -4px;
    margin-bottom: 8px;
    color: #333;
}

div[data-testid="stTextInput"] input {
    border-radius: 25px;
    height: 44px;
    border: none !important;
    outline: none !important;
    padding-right: 16px;
    text-align: right;
    background: rgba(255,255,255,0.95);
}

div[data-testid="stSelectbox"] div {
    border-radius: 25px;
}

div[data-testid="stHorizontalBlock"] .stButton > button {
    width: 70px !important;
    height: 34px !important;
    font-size: 12px !important;
    border-radius: 20px !important;
    background: linear-gradient(90deg,#2f80ed,#1c6fa4);
    color: white;
}

div.stButton > button {
    width: 100% !important;
    height: 48px !important;
    font-size: 16px !important;
    border-radius: 25px !important;
    border: none;
    background: linear-gradient(90deg,#2f80ed,#1c6fa4);
    color: white;
    font-weight: bold;
}

div.stButton:nth-of-type(1) > button {
    background: white;
    color: var(--navy);
    box-shadow: 0 2px 8px rgba(0,0,0,.1);
}

</style>
""", unsafe_allow_html=True)

st.title("إنشاء حساب")

st.markdown(
    '<div class="signin-line">هل لديك حساب بالفعل؟</div>',
    unsafe_allow_html=True
)

if st.button("تسجيل الدخول"):
    st.switch_page("app.py")

username = st.text_input("اسم المستخدم")

if username and not username.replace(" ", "").isalpha():
    st.error("يجب أن يحتوي الاسم على أحرف فقط")

col1, col2 = st.columns([4, 1])

with col1:
    phone = st.text_input("رقم الهاتف أو الهوية", max_chars=11)

with col2:
    st.markdown("<div style='margin-top:28px'></div>", unsafe_allow_html=True)
    send_clicked = st.button("إرسال", key="send_code")

if send_clicked:
    if phone.isdigit() and len(phone) == 10 and phone.startswith("07"):
        st.session_state.generated_phone_code = "0000"
        st.success("تم إرسال الكود")
    elif phone.isdigit() and len(phone) == 11:
        st.session_state.generated_phone_code = "0000"
        st.success("تم إرسال الكود")
    else:
        st.error("رقم الهاتف أو الهوية غير صحيح")

phone_code = st.text_input("أدخل الكود")
email = st.text_input("البريد الإلكتروني")

location = st.selectbox(
    "الموقع",
    [
        "",
        "عمان","إربد","الزرقاء","البلقاء","المفرق",
        "جرش","عجلون","مادبا","الكرك",
        "الطفيلة","معان","العقبة",
    ],
)

password = st.text_input("كلمة المرور", type="password")
confirm_password = st.text_input("تأكيد كلمة المرور", type="password")

create_clicked = st.button("إنشاء الحساب", key="create_account")

if create_clicked:
    if not username or not phone or not phone_code or not email or not location or not password or not confirm_password:
        st.error("يرجى تعبئة جميع الحقول")
    elif not username.replace(" ", "").isalpha():
        st.error("اسم المستخدم غير صحيح")
    elif not phone.isdigit() or not (len(phone) == 10 or len(phone) == 11):
        st.error("رقم الهاتف أو الهوية غير صحيح")
    elif len(phone) == 10 and not phone.startswith("07"):
        st.error("يجب أن يبدأ رقم الهاتف بـ 07")
    elif phone_code != st.session_state.generated_phone_code:
        st.error("الكود غير صحيح")
    elif "@" not in email or "." not in email:
        st.error("البريد الإلكتروني غير صحيح")
    elif password != confirm_password:
        st.error("كلمتا المرور غير متطابقتين")
    else:
        st.success("تم إنشاء الحساب بنجاح")
        time.sleep(1)
        st.switch_page("app.py")
