import streamlit as st

st.set_page_config(page_title="الإعدادات", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    direction: rtl;
}

.block-container {
    max-width: 390px;
    margin: auto;
    padding: 35px 20px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

/* العنوان */
.title-ar {
    text-align:center;
    font-weight:900;
    color:#102646;
    font-size:22px;
    margin-bottom:25px;
}

/* البوكسات */
div.stButton > button {
    width: 100% !important;
    min-height: 62px !important;
    border-radius: 35px !important;
    margin-bottom: 18px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 5px 12px rgba(0,0,0,0.06) !important;

    color: #102646 !important;
    font-size: 16px !important;
    font-weight: 700 !important;

    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;

    padding: 0 24px !important;
    text-align: right !important;
}

/* السهم داخل البوكس من اليسار */
div.stButton > button::before {
    content: "‹";
    font-size: 28px;
    color: #102646;
    font-weight: 800;
}

/* لا نريد سهم بعد الزر */
div.stButton > button::after {
    content: "";
}

/* حركة خفيفة */
div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #fcfcfc !important;
}

/* أزرار آخر سطر أصغر شوي */
.small-btn div.stButton > button {
    min-height: 55px !important;
    font-size: 14px !important;
    padding: 0 14px !important;
}

</style>

<div class="title-ar">الإعدادات</div>
""", unsafe_allow_html=True)


if st.button("🔒  تغيير كلمة المرور"):
    st.switch_page("pages/Change_Passwordar.py")

if st.button("🌐  تغيير اللغة"):
    st.switch_page("pages/Change_Languagear.py")

if st.button("⭐  تقييم التطبيق"):
    st.switch_page("pages/Rate_Appar.py")

if st.button("🚪  تسجيل الخروج"):
    st.session_state.clear()
    st.switch_page("arabic-app.py")


col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="small-btn">', unsafe_allow_html=True)
    if st.button("⚠️ تبليغ عن مشكلة"):
        st.switch_page("pages/Report_Problemar.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="small-btn">', unsafe_allow_html=True)
    if st.button("✉️ اتصل بنا"):
        st.switch_page("pages/ContactUsar.py")
    st.markdown('</div>', unsafe_allow_html=True)
