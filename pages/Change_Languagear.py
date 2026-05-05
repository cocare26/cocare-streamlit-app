import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث (تنزيل البوكس لتحت وتعديل الأبعاد) =====
st.markdown("""
<style>
/* ضبط الاتجاه */
* { direction: rtl; }

/* الخلفية الخارجية بيضاء */
[data-testid="stAppViewContainer"] {
    background-color: white !important;
}

[data-testid="stHeader"] {display: none !important;}

/* الكبسولة - تعديل المكان والأبعاد هنا */
.block-container {
    max-width: 360px !important; /* العرض نحيف */
    margin: auto !important;
    padding: 40px 25px !important;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff) !important;
    border-radius: 55px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    
    /* تنزيل البوكس لتحت - غير هذا الرقم لزيادة النزول */
    margin-top: 100px !important; 
    
    min-height: 700px !important; /* طول الكبسولة */
    display: flex;
    flex-direction: column;
}

/* تنسيق العنوان */
.title-text {
    font-size: 22px;
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
    height: 60px !important;
    margin-bottom: 20px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    font-weight: 800 !important;
    font-size: 17px !important;
}

/* زر الرجوع */
.back-container {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 20px;
}
.back-container .stButton > button {
    width: auto !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 35px !important;
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الكبسولة =====
st.markdown('<div class="back-container">', unsafe_allow_html=True)
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

if st.button("🌐 العربية                       ✔"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English                         ›"):
    st.switch_page("pages/Settings.py")
