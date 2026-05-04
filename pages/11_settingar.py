import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="الإعدادات", layout="centered")

# 2. التنسيق العام (CSS) ليتناسب مع ديزاين المشروع ويجعل أزرار Streamlit تبدو ككبسولات
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction: rtl; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
section.main > div { padding-top:8px; }
div[data-testid="stVerticalBlock"] { gap:0rem; }

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}

/* تنسيق الهيدر */
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 35px;
    position: relative;
    padding-top: 10px;
}

.title {
    margin: 0;
    font-weight: 900;
    font-size: 20px;
    color: #102646;
    text-align: center;
    width: 100%;
}

/* تنسيق أزرار Streamlit لتصبح كبسولات */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border-radius: 100px !important;
    padding: 25px 22px !important;
    margin-bottom: 15px !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    transition: 0.3s !important;
    text-align: right !important;
    font-weight: 800 !important;
    font-size: 14px !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12) !important;
    background-color: #f9f9f9 !important;
}

/* تنسيق زر الرجوع الصغير */
.back-style div.stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
    width: auto !important;
    font-size: 28px !important;
    color: #102646 !important;
}

/* تنسيق الصف السفلي */
.bottom-btns-container {
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة باستخدام Streamlit Buttons
col_back, _ = st.columns([1, 10])

with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("›", key="back_main"):
        st.switch_page("pages/userdash_arabic.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="header-container"><h2 class="title">الإعدادات</h2></div>', unsafe_allow_html=True)

# الأزرار الرئيسية
if st.button("🔒 تغيير كلمة المرور                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ‹", key="btn_pass"):
    st.switch_page("pages/6_Change_Password.py")

if st.button("🌐 تغيير اللغة                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ‹", key="btn_lang"):
    st.switch_page("pages/7_Change_Language.py")

if st.button("⭐ تقييم التطبيق                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ‹", key="btn_rate"):
    st.switch_page("pages/8_Rate_App.py")

if st.button("🚪 تسجيل الخروج                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ‹", key="btn_logout"):
    st.session_state.clear()
    st.switch_page("app.py")

# الصف السفلي
st.markdown('<div class="bottom-btns-container"></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("⚠️ الإبلاغ عن مشكلة", key="btn_report"):
        st.switch_page("pages/9_Report_Problem.py")

with col2:
    if st.button("✉️ تواصل معنا", key="btn_contact"):
        st.switch_page("pages/10_Contact_Us.py")
