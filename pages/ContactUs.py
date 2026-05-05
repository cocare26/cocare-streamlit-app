import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

# ===== CSS الموحد (مبدأ الإعدادات) =====
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
    font-size: 14px !important; /* صغرنا الخط شوي عشان المسافة الـ 60 ما تكسر السطر */
    
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important; 
    
    padding: 0px 20px !important;
    transition: 0.3s;
}

/* السهم الصغير في النهاية */
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
    background-color: #fcfcfc !important;
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

# ===== الأزرار بمسافة 60 فراغ =====

# المتغير اللي طلبته بـ 60 فراغ
super_gap = "&nbsp;" * 60 

if st.button(f"✉️{super_gap}Email: Co.Care26@gmail.com"):
    pass

if st.button(f"📞{super_gap}Phone: +962 79 123 4567"):
    pass
