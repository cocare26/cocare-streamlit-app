import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ===== CSS المطابق للصورة =====
st.markdown("""
<style>
/* ضبط الاتجاه العام */
* { direction: rtl; }
[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}


/* الخلفية السماوية الفاتحة */
[data-testid="stAppViewContainer"] {
    background-color: #dff2ff !important;
}

/* إخفاء الهيدر */
[data-testid="stHeader"] {display: none !important;}

/* الكبسولة (الحاوية) */
.block-container {
    max-width:430px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    position: relative; /* ضروري لضبط موقع السهم داخلياً */
    margin-top: 50px;
}


/* زر الرجوع (البوكس الأسود) */
.back-container {
    display: flex;
    justify-content: flex-end; /* لليمين */
    margin-bottom: 40px;
    margin-top: 20px;
}

.back-style-btn .stButton > button {
    background-color: #1a1c22 !important; /* أسود مطفي */
    color: white !important;
    width: 45px !important;
    height: 45px !important;
    border-radius: 12px !important; /* زوايا منحنية قليلاً */
    border: none !important;
    font-size: 20px !important;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 !important;
}

/* العنوان (على اليمين) */
.title-right {
    font-size: 26px;
    font-weight: 800;
    color: #102646;
    text-align: right;
    margin-right: 15px;
    margin-bottom: 40px;
}

/* تنسيق البوكسات البيضاء (اللغات) */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 50px !important; /* شكل بيضاوي */
    height: 65px !important;
    margin-bottom: 20px !important;
    font-weight: 700 !important;
    font-size: 19px !important;
    display: flex !important;
    justify-content: space-between !important; /* توزيع المحتوى */
    padding: 0 25px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}

/* فراغ تحت البوكسات */
.spacer {
    height: 200px;
}
</style>
""", unsafe_allow_html=True)

# ===== المحتوى =====

# 1. زر الرجوع
st.markdown('<div class="back-container back-style-btn">', unsafe_allow_html=True)
if st.button("‹", key="back_btn"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

# 2. العنوان
st.markdown('<div class="title-right">تغيير اللغة</div>', unsafe_allow_html=True)

# 3. أزرار اللغات (مع محاكاة التصميم الداخلي بالمسافات)
# ملاحظة: في ستريم ليت نستخدم المسافات الشفافة لضبط المواقع داخل الزر
if st.button("🌐  العربية                              ✔️"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

if st.button("🌐  English                             ‹"):
    st.session_state.lang = "en"

    st.switch_page("pages/Settings.py")

# 4. الفراغ السفلي
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
