import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="الإعدادات", layout="centered")

# 2. التنسيق العام (CSS)
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

/* تنسيق أزرار Streamlit لتصبح كبسولات */
.stButton > button {
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
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12) !important;
    background-color: #f9f9f9 !important;
}

/* زر الرجوع الصغير */
.back-btn-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 28px !important;
    width: auto !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# 3. المحتوى
col_back, col_title = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-btn-style">', unsafe_allow_html=True)
    if st.button("›", key="back_home"):
        st.switch_page("pages/userdash_arabic.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:30px;">الإعدادات</h2>', unsafe_allow_html=True)

if st.button("🔒 تغيير كلمة المرور          ‹"):
    st.switch_page("pages/6_Change_Password.py")

if st.button("🌐 تغيير اللغة                  ‹"):
    st.switch_page("pages/7_Change_Language.py")

if st.button("⭐ تقييم التطبيق               ‹"):
    st.switch_page("pages/8_Rate_App.py")

if st.button("🚪 تسجيل الخروج              ‹"):
    st.session_state.clear()
    st.switch_page("app.py")

st.markdown('<div style="margin-top: 40px;"></div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    if st.button("⚠️ الإبلاغ عن مشكلة"):
        st.switch_page("pages/9_Report_Problem.py")
with c2:
    if st.button("✉️ تواصل معنا"):
        st.switch_page("pages/10_Contact_Us.py")
