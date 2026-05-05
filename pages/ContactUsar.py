import streamlit as st

st.set_page_config(page_title="اتصل بنا", layout="centered")

# ===== CSS الموحد (مبدأ الإعدادات) =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    direction: rtl; /* إضافة اتجاه اليمين للعربية */
}

/* الكونتينر النحيف */
.block-container {
    max-width: 430px; 
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

/* تنسيق البوكسات الموحد */
div.stButton > button {
    width: 100% !important;
    min-height: 65px !important; 
    border-radius: 35px !important;
    margin-bottom: 20px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 5px 12px rgba(0,0,0,0.06) !important;
    
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 15px !important; 
    
    display: flex !important;
    align-items: center !important;
    /* التعديل السحري: النص يلزق باليمين والسهم يروح يسار */
    justify-content: flex-start !important; 
    
    padding: 0px 25px !important;
    transition: 0.3s;
}

/* السهم الصغير في النهاية - نخليه يندفع لآخر اليسار (في الواجهة العربية) */
div.stButton > button::after {
    content: "‹"; /* تغيير اتجاه السهم للعربي */
    font-size: 26px;
    color: #102646;
    margin-right: auto; /* دفع السهم للجهة المقابلة */
}

/* ستايل زر الرجوع */
.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 35px !important;
    width: auto !important;
    min-height: unset !important;
    padding: 0 !important;
}
.back-style .stButton > button::after {
    content: "" !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #fcfcfc !important;
}
</style>
""", unsafe_allow_html=True)

# 🔙 زر الرجوع
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("›"): # سهم الرجوع لليمين في العربي
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

# العنوان
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:35px;">اتصل بنا</h2>', unsafe_allow_html=True)

# ===== الأزرار (نفس المسافات اللي حطيتها إنت بالظبط) =====

gap1 = "&nbsp;" * 29
if st.button(f"✉️ البريد الإلكتروني: Co.Care26@gmail.com {gap1}"):
    pass

gap2 = "&nbsp;" * 20 
if st.button(f"📞 الهاتف: +962 79 123 4567 {gap2}{gap2}"):
    pass
