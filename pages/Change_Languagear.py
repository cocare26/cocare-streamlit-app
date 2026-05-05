import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# 1. التنسيق (CSS) - جعل أزرار بايثون تبدو كأنها الـ Items التي صممتها
st.markdown("""
<style>
    /* إخفاء الهيدر */
    [data-testid="stHeader"] {display: none !important;}
    
    /* ضبط الخلفية والاتجاه */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
        direction: rtl;
    }

   .block-container {
    max-width: 430px;            /* العرض المثالي */
    border-radius: 42px;         /* زوايا الكبسولة */
    box-shadow: 0 14px 35px rgba(0,0,0,0.15); /* الظل العميق */
    padding: 18px 16px;          /* المسافات الداخلية */
}

/* تنسيق العناصر الداخلية (الأزرار) */
.item {
    border-radius: 100px;        /* جعل الزر كبسولة صغيرة */
    padding: 14px 22px;          /* مسافة مريحة للنص */
    margin-bottom: 15px;         /* مسافة بين كل خيار والثاني */
}

    /* العنوان */
    .title-text {
    font-size: 20px;
    font-weight: 900;            /* وزن عريض جداً */
    color: #102646;
    font-family: 'Segoe UI';     /* الخط المعتمد */
}

    /* تحويل أزرار ستريمليت إلى تصميم الـ Item */
    div.stButton > button {
        width: 100% !important;
        background-color: white !important;
        color: #102646 !important;
        border-radius: 100px !important;
        height: 60px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
        font-size: 18px !important;
        font-weight: 800 !important;
        margin-bottom: 15px !important;
        display: flex !important;
        justify-content: space-between !important;
        padding: 0 25px !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.12) !important;
    }

    /* تنسيق زر السهم الأسود للرجوع */
    .back-btn-box {
        display: flex;
        justify-content: flex-start;
        margin-bottom: 10px;
    }
    
    /* استهداف زر السهم تحديداً ليكون صغير وأسود */
    .back-btn-box .stButton > button {
        width: 45px !important;
        height: 45px !important;
        min-width: 45px !important;
        background-color: transparent !important; /* أو #1a1c22 إذا أردته أسود كما في الصورة */
        color: black !important;
        font-size: 30px !important;
        box-shadow: none !important;
        padding: 0 !important;
        justify-content: center !important;
    }

    .item span {
    font-weight: 800;
    font-size: 16px;
    color: #102646;
}
</style>
""", unsafe_allow_html=True)

# 2. الهيدر وزر الرجوع
st.markdown('<div class="back-btn-box">', unsafe_allow_html=True)
# هذا هو الزر الذي طلبت تعديله ليرجعك لصفحة الإعدادات العربية
if st.button("›"): 
    st.switch_page("pages/settingar.py") 
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

# 3. خيارات اللغة (باستخدام أزرار بايثون لضمان العمل)
if st.button("🌐 العربية \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 ✔"):
    st.switch_page("pages/settingar.py")

if st.button("🌐 English \u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0\u00A0 ›"):
    st.switch_page("pages/Settings.py")
