import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث (تكبير العرض والتحسين) =====
st.markdown("""
<style>
/* ضبط الاتجاه */
* { direction: rtl; }

/* الخلفية بيضاء */
[data-testid="stAppViewContainer"] {
    background-color: white !important;
}

[data-testid="stHeader"] {display: none !important;}

/* الكبسولة - تكبير العرض */
.block-container {
    max-width: 400px !important; /* زدنا العرض من 320 إلى 400 */
    margin: auto !important;
    padding: 40px 30px !important; /* زيادة المسافة الداخلية */
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff) !important;
    border-radius: 50px;
    box-shadow: 0 15px 45px rgba(0,0,0,0.08);
    
    /* مكان الكبسولة ونزولها */
    margin-top: 60px !important; 
    
    min-height: 620px !important; 
    display: flex;
    flex-direction: column;
}

/* تنسيق العنوان */
.title-text {
    font-size: 24px; /* كبرنا الخط قليلاً ليناسب العرض */
    font-weight: 900;
    color: #102646;
    text-align: center;
    margin-bottom: 40px;
}

/* تنسيق الأزرار */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 100px !important;
    height: 60px !important; /* زيادة ارتفاع الزر */
    margin-bottom: 20px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.06) !important;
    font-weight: 800 !important;
    font-size: 18px !important;
    transition: 0.3s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
}

/* زر الرجوع */
.back-container {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 10px;
}
.back-container .stButton > button {
    width: auto !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 35px !important;
    color: black !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الكبسولة المعدلة =====
st.markdown('<div class="back-container">', unsafe_allow_html=True)
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# الأزرار مع مسافات تناسب العرض الجديد
if st.button("🌐 العربية                             ✔"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English                              ›"):
    st.switch_page("pages/Settings.py")
