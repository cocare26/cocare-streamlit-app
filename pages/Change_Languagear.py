import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== الـ CSS (نفس الديزاين تبعك مع تعديلات بسيطة للأزرار) =====
st.markdown("""
<style>
/* ضبط الاتجاه والخلفية */
* { direction: rtl; }
[data-testid="stAppViewContainer"] {
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
}
[data-testid="stHeader"] {display: none !important;}

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background: white; /* البوكس الأساسي */
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    margin-top: 20px;
}

/* تنسيق العنوان */
.title-text {
    font-size:20px;
    font-weight:900;
    color:#102646;
    text-align: center;
    margin-bottom: 30px;
}

/* تعديل أزرار ستريمليت لتبدو مثل الـ Items في تصميمك */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: 1px solid #f0f0f0 !important;
    border-radius: 100px !important;
    padding: 14px 22px !important;
    margin-bottom: 15px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    transition: 0.2s !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    border-color: #2f80ed !important;
}

/* تنسيق السهم الصغير للرجوع */
.back-container {
    display: flex;
    justify-content: flex-start;
}
.back-container .stButton > button {
    width: auto !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 30px !important;
    color: black !important;
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="back-container">', unsafe_allow_html=True)
# السهم يرجعك لصفحة الإعدادات العربية
if st.button("›"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# ===== الأزرار (نفس ديزاين الـ Item) =====

# زر العربية
if st.button("🌐 العربية                        ✔"):
    st.switch_page("pages/settingar.py")

# زر الإنجليزية
if st.button("🌐 English                             ›"):
    st.switch_page("pages/Settings.py")
