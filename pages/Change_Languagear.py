import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS التصميم المماثل للصورة =====
st.markdown("""
<style>
/* ضبط الاتجاه للعربية */
* { direction: rtl; }

/* الخلفية الخارجية بيضاء */
[data-testid="stAppViewContainer"] {
    background-color: white !important;
}

[data-testid="stHeader"] {display: none !important;}

/* الكبسولة السماوية */
.block-container {
    max-width: 360px !important;
    margin: auto !important;
    padding: 30px 20px !important;
    background-color: #e1f1ff !important; /* لون سماوي فاتح صلب مثل الصورة */
    border-radius: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    margin-top: 50px !important;
    min-height: 650px !important;
}

/* العنوان (تغيير اللغة) */
.title-text {
    font-size: 20px;
    font-weight: 900;
    color: #102646;
    text-align: center;
    margin-bottom: 40px;
    margin-top: 20px;
}

/* تصميم الأزرار الطويلة */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 100px !important;
    height: 55px !important;
    margin-bottom: 15px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    display: flex !important;
    justify-content: space-between !important;
    padding: 0 20px !important;
}

/* الأزرار الصغيرة في الأسفل (بجانب بعضها) */
.footer-buttons {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

.footer-buttons div {
    flex: 1;
}

/* تنسيق خاص للأزرار السفلية لضمان الشكل البيضاوي */
.footer-buttons div.stButton > button {
    height: 50px !important;
    font-size: 14px !important;
}

/* زر الرجوع العلوي */
.back-container {
    display: flex;
    justify-content: flex-end; /* لجعله في الزاوية مثل الصورة */
}
.back-container .stButton > button {
    width: 40px !important;
    height: 40px !important;
    background: white !important;
    border-radius: 50% !important;
    font-size: 20px !important;
    color: #102646 !important;
    min-width: 40px !important;
    padding: 0 !important;
    justify-content: center !important;
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الكبسولة =====

# 1. زر الرجوع (أعلى اليسار/اليمين حسب الاتجاه)
st.markdown('<div class="back-container">', unsafe_allow_html=True)
if st.button("›", key="back"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

# 2. العنوان
st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# 3. خيارات اللغة (الأزرار الطويلة)
if st.button("🌐 العربية \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 ✔", key="lang_ar"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 ›", key="lang_en"):
    st.switch_page("pages/Settings.py")

# 4. الأزرار السفلية (مثل اتصل بنا وتبليغ عن مشكلة)
st.markdown('<div class="footer-buttons">', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    if st.button("📧 اتصل بنا", key="contact"):
        pass # أضف الأكشن هنا

with col2:
    if st.button("⚠️ مشكلة", key="report"):
        pass # أضف الأكشن هنا
st.markdown('</div>', unsafe_allow_html=True)
