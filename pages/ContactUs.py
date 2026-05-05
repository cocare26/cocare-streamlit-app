import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* 1. وسعنا العرض الكلي هون عشان البوكس يوصل للنهاية اللي طلبتها بالرسم */
.block-container {
    max-width: 550px; /* زدنا العرض من 430 لـ 550 */
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

/* 2. الأزرار - "طويلة بالعرض" زي ما طلبت */
div.stButton > button {
    width: 100% !important; /* بتمد البوكس لآخر عرض الـ container */
    min-height: 65px !important; 
    background: white !important;
    
    /* تباعد داخلي: 25 من اليسار و 15 من اليمين (عشان السهم يوصل للآخر) */
    padding: 15px 15px 15px 25px !important; 
    
    border-radius: 25px !important; 
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    margin-bottom: 20px !important; 
    border: none !important;
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 15px !important; 
    
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important; /* هذا بيدفع السهم لآخر اليمين */
    
    transition: 0.3s ease;
}

div.stButton > button::after {
    content: "›";
    font-size: 28px;
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
.back-style .stButton > button::after { content: "" !important; }

div.stButton > button:hover {
    transform: translateY(-2px);
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

st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:35px;">Contact Us</h2>', unsafe_allow_html=True)

# الأزرار - الآن ممتدة بالعرض للنهاية
if st.button("✉️ Email: Co.Care26@gmail.com"): pass
if st.button("📞 Phone: +962 79 123 4567"): pass
