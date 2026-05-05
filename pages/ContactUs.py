import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width: 430px; 
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

div.stButton > button {
    width: 100% !important;
    min-height: 65px !important; 
    background: white !important;
    
    /* 👇 قللنا الرقم الثاني (10px) عشان السهم يوصل لآخر الحافة قدام 👇 */
    padding: 15px 10px 15px 25px !important; 
    
    border-radius: 25px !important; 
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    margin-bottom: 15px !important; 
    border: none !important;
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 15px !important; 
    
    display: flex !important;
    align-items: center !important;
    
    /* هاد السطر هو اللي بيفتح المسافة العرضية كاملة */
    justify-content: space-between !important; 
    
    transition: 0.3s ease;
}

div.stButton > button::after {
    content: "›";
    font-size: 30px; /* كبّرنا السهم شوي عشان يبين أوضح بالنهاية */
    color: #102646;
    /* تأكد إنه ما في margin مضايقه */
    margin: 0 !important; 
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

# الأزرار
if st.button("✉️ Email: Co.Care26@gmail.com"): pass
if st.button("📞 Phone: +962 79 123 4567"): pass
