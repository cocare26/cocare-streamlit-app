import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS المعدل لزيادة التباعد بين البوكسات =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكونتينر الأساسي */
.block-container {
    max-width:450px;
    margin:auto;
    padding:40px 25px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 20px 40px rgba(0,0,0,0.15);
}

/* العنوان */
.title {
    text-align:center;
    font-size:26px;
    font-weight:900;
    color:#102646;
    margin-bottom:40px;
}

/* أزرار Streamlit */
div.stButton > button {
    width: 100% !important;
    min-height: 90px !important; /* طول البوكس */
    border-radius: 45px !important;
    
    /* 👇 التعديل الرئيسي: زيادة التباعد العمودي من هنا 👇 */
    margin-bottom: 35px !important; /* زدنا المسافة إلى 35px لتكون مثل الرسمة */
    
    background: white !important;
    border: none !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
    
    font-weight: 800 !important;
    color: #102646 !important;
    font-size: 18px !important;
    
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding: 15px 35px !important;
    transition: all 0.4s ease;
}

/* تأثير الـ Hover */
div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 15px 25px rgba(0,0,0,0.15) !important;
}

/* السهم الجانبي */
div.stButton > button::after {
    content: "›";
    font-size: 30px;
    color: #102646;
    font-weight: 200;
}

/* تعديل الأزرار المزدوجة في الأسفل */
[data-testid="stHorizontalBlock"] {
    gap: 15px !important;
    margin-top: 10px; /* تباعد قبل المجموعة السفلية */
}

/* تعديل حجم أزرار الأعمدة لتناسب التباعد الجديد */
[data-testid="stHorizontalBlock"] div.stButton > button {
    min-height: 80px !important;
    font-size: 15px !important;
    padding: 10px 20px !important;
    margin-bottom: 0px !important; /* نلغي المارجن السفلي للأزرار اللي جنب بعض */
}

</style>
<div class="title">Settings</div>
""", unsafe_allow_html=True)

# ===== الأزرار (البوكسات) المتباعدة =====

if st.button("🔒 Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐 Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("⭐ Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button("🛡️ Privacy Policy"):
    st.switch_page("pages/Privacy.py")

if st.button("🚪 Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")

# خط فاصل بسيط يعطي تباعد إضافي
st.markdown("<br>", unsafe_allow_html=True)

# الأزرار السفلية
col1, col2 = st.columns(2)
with col1:
    st.button("⚠️ Report Problem")

with col2:
    st.button("✉️ Contact Us")
