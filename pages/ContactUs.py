import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

# ===== CSS المدمج (ستايل البطاقة مع عرض المسطرة) =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
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

/* تنسيق البوكسات بنمط الـ Card */
div.stButton > button {
    width: 100% !important;
    min-height: 65px !important; 
    
    /* ستايل الـ Card اللي طلبته 👇 */
    background: white !important;
    padding: 15px 25px !important; /* دمجت الـ 15px اللي طلبتها مع تباعد جانبي */
    border-radius: 25px !important; /* الـ Radius الخاص بالبطاقة */
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important; /* الظل الخاص بالبطاقة */
    margin-bottom: 15px !important; /* المسافة بين البطاقات */
    
    border: none !important;
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 15px !important; 
    
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important; /* المسافة الطويلة بالعرض */
    
    transition: 0.3s ease;
}

/* السهم الصغير في نهاية البطاقة */
div.stButton > button::after {
    content: "›";
    font-size: 26px;
    color: #102646;
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
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}
</style>
""", unsafe_allow_html=True)

# 🔙 زر الرجوع
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("‹"):
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

# العنوان
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:35px;">Contact Us</h2>', unsafe_allow_html=True)

# ===== الأزرار بنمط البطاقات الطويلة عرضياً =====

if st.button("✉️ Email: Co.Care26@gmail.com"):
    pass

if st.button("📞 Phone: +962 79 123 4567"):
    pass
