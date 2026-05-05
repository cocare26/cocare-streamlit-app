import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="اتصل بنا", layout="centered")

# 2. التنسيق (CSS) لضبط الواجهة العربية
st.markdown("""
<style>
    #MainMenu, header, footer {visibility:hidden;}
    
    [data-testid="stAppViewContainer"] {
        background:#f0f7ff;
        direction: rtl; /* اتجاه عربي */
    }

    .block-container {
        max-width: 400px;
        margin: auto;
        padding: 20px;
        background: white;
        border-radius: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    }

    /* تنسيق الأزرار */
    div.stButton > button {
        width: 100% !important;
        min-height: 60px !important;
        border-radius: 20px !important;
        background-color: #ffffff !important;
        color: #102646 !important;
        font-weight: 700 !important;
        border: 1px solid #e0e0e0 !important;
        margin-bottom: 15px !important;
        display: flex !important;
        justify-content: flex-start !important;
        padding: 0 20px !important;
    }

    /* زر الرجوع الخاص */
    .back-btn > div.stButton > button {
        background: transparent !important;
        border: none !important;
        font-size: 30px !important;
        width: auto !important;
        box-shadow: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. زر الرجوع (يرجعك لصفحة الإعدادات العربية)
st.markdown('<div class="back-btn">', unsafe_allow_html=True)
if st.button("›"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<h2 style='text-align:center; color:#102646;'>اتصل بنا</h2>", unsafe_allow_html=True)

# 4. أزرار التواصل
if st.button("✉️ البريد: Co.Care26@gmail.com"):
    pass

if st.button("📞 الهاتف: 962791234567+"):
    pass
