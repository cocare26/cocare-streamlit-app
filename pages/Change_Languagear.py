import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث (الخلفية سماوية والبوكس أبيض) =====
st.markdown("""
<style>
/* ضبط الاتجاه */
* { direction: rtl; }

/* 1. الخلفية الخارجية - جعلتها سماوية متدرجة */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff) !important;
}

[data-testid="stHeader"] {display: none !important;}

/* 2. الكبسولة (البوكس) - جعلتها بيضاء */
.block-container {
    max-width: 360px !important;
    margin: auto !important;
    padding: 40px 25px !important;
    background-color: white !important; /* البوكس صار أبيض */
    border-radius: 55px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    margin-top: 30px !important;
    min-height: 700px !important;
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

/* تنسيق الأزرار (Items) - جعلتها بلون سماوي فاتح جداً لتتناسب مع الخلفية */
div.stButton > button {
    width: 100% !important;
    background-color: #f0f7ff !important; 
    color: #102646 !important;
    border: none !important;
    border-radius: 100px !important;
    height: 60px !important;
    margin-bottom: 20px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    font-weight: 800 !important;
    font-size: 17px !important;
    transition: 0.3s !important;
}

div.stButton > button:hover {
    transform: translateY(-3px);
    background-color: #e1f0ff !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
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
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الكبسولة =====
st.markdown('<div class="back-container">', unsafe_allow_html=True)
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# زر العربية
if st.button("🌐 العربية                       ✔"):
    st.switch_page("pages/settingar.py")

# زر الإنجليزية
if st.button("🌐 English                         ›"):
    st.switch_page("pages/Settings.py")
