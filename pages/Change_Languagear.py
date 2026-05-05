import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المحدث (زيادة العرض ليطابق الصورة) =====
st.markdown("""
<style>
/* ضبط الاتجاه للعربية */
* { direction: rtl; }

/* الخلفية الخارجية بيضاء */
[data-testid="stAppViewContainer"] {
    background-color: white !important;
}

[data-testid="stHeader"] {display: none !important;}

/* الكبسولة السماوية - جعلناها أعرض هنا */
.block-container {
    max-width: 420px !important; /* زدنا العرض من 360 إلى 420 */
    margin: auto !important;
    padding: 30px 25px !important;
    background-color: #e1f1ff !important; 
    border-radius: 50px; /* زوايا دائرية ناعمة */
    box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    margin-top: 40px !important;
    min-height: 600px !important;
}

/* العنوان */
.title-text {
    font-size: 22px;
    font-weight: 900;
    color: #102646;
    text-align: center;
    margin-bottom: 45px;
    margin-top: 10px;
}

/* الأزرار الطويلة */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 100px !important;
    height: 60px !important; /* زيادة الارتفاع قليلاً للفخامة */
    margin-bottom: 18px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.04) !important;
    font-weight: 800 !important;
    font-size: 18px !important;
}

/* الأزرار السفلية الصغيرة بجانب بعضها */
.footer-buttons {
    display: flex;
    gap: 15px;
    margin-top: 25px;
}

/* زر الرجوع الدائري العلوي */
.back-container {
    display: flex;
    justify-content: flex-end;
}
.back-container .stButton > button {
    width: 45px !important;
    height: 45px !important;
    background: white !important;
    border-radius: 50% !important;
    font-size: 22px !important;
    color: #102646 !important;
    min-width: 45px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
}
</style>
""", unsafe_allow_html=True)

# ===== محتوى الكبسولة العريضة =====

# 1. زر الرجوع
st.markdown('<div class="back-container">', unsafe_allow_html=True)
if st.button("›", key="back"): 
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

# 2. العنوان
st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# 3. الأزرار الأساسية
if st.button("🌐 العربية                       ✔", key="lang_ar"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English                          ›", key="lang_en"):
    st.switch_page("pages/Settings.py")

# 4. الأزرار السفلية الصغيرة
col1, col2 = st.columns(2)
with col1:
    if st.button("📧 اتصل بنا"):
        pass

with col2:
    if st.button("⚠️ مشكلة"):
        pass
