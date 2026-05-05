import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث (تصغير الأبعاد) =====
st.markdown("""
<style>
/* ضبط الاتجاه */
* { direction: rtl; }

/* الخلفية بيضاء */
[data-testid="stAppViewContainer"] {
    background-color: white !important;
}

[data-testid="stHeader"] {display: none !important;}

/* الكبسولة - تصغير الأبعاد */
.block-container {
    max-width: 320px !important; /* تقليل العرض من 360 إلى 320 */
    margin: auto !important;
    padding: 35px 20px !important;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff) !important;
    border-radius: 50px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.08);
    
    /* مكان الكبسولة */
    margin-top: 80px !important; 
    
    min-height: 600px !important; /* تقليل الطول من 700 إلى 600 */
    display: flex;
    flex-direction: column;
}

/* تنسيق العنوان */
.title-text {
    font-size: 20px; /* تصغير حجم الخط قليلاً ليناسب الحجم الجديد */
    font-weight: 900;
    color: #102646;
    text-align: center;
    margin-bottom: 35px;
}

/* تنسيق الأزرار */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 100px !important;
    height: 55px !important; /* تقليل ارتفاع الزر قليلاً */
    margin-bottom: 15px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}

/* زر الرجوع */
.back-container {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 15px;
}
.back-container .stButton > button {
    width: auto !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 30px !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الكبسولة المصغرة =====
st.markdown('<div class="back-container">', unsafe_allow_html=True)
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# الأزرار مع تعديل المسافات لتناسب العرض الصغير
if st.button("🌐 العربية                      ✔"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English                       ›"):
    st.switch_page("pages/Settings.py")
