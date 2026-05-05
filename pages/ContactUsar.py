import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="تغيير اللغة", layout="centered")

# 2. التنسيق لجعل الزر يشبه الصورة تماماً (السهم على اليسار والنص على اليمين)
st.markdown("""
<style>
    /* إخفاء القوائم الافتراضية */
    #MainMenu, header, footer {visibility:hidden;}
    
    /* ضبط الخلفية والاتجاه للعربية */
    [data-testid="stAppViewContainer"] {
        background:#f0f7ff;
        direction: rtl;
    }

    /* تنسيق أزرار Streamlit لتشبه التصميم المطلوب */
    div.stButton > button {
        width: 100% !important;
        height: 70px !important;
        background-color: white !important;
        color: #102646 !important;
        border-radius: 35px !important;
        border: none !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1) !important;
        display: flex !important;
        flex-direction: row !important; /* ترتيب العناصر */
        justify-content: space-between !important; /* توزيع النص والسهم */
        align-items: center !important;
        padding: 0 25px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
    }

    /* وضع سهم جهة اليسار للغة الإنجليزية */
    .eng-btn > div.stButton > button::before {
        content: "‹";
        font-size: 25px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#102646;'>تغيير اللغة</h2>", unsafe_allow_html=True)

# 3. زر اللغة العربية (الحالية)
st.button("🌐 العربية ✅")

# 4. زر اللغة الإنجليزية (المعدل للانتقال وتغيير الواجهة)
st.markdown('<div class="eng-btn">', unsafe_allow_html=True)
if st.button("🌐 الإنجليزية"):
    # هذا الأمر سيفتح صفحة الإعدادات الإنجليزية
    # صفحة Settings.py يجب أن تحتوي في الـ CSS الخاص بها على direction: ltr
    st.switch_page("pages/Settings.py")
st.markdown('</div>', unsafe_allow_html=True)
