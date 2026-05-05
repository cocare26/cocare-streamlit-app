import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

# ===== CSS الموحد (بوكسات طويلة وفخمة) =====
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
    min-height: 650px;
}

/* تنسيق البوكسات - جعلناها طويلة جداً */
div.stButton > button {
    width: 100% !important;
    
    /* 👇 هون السر: زدنا الارتفاع الأدنى لـ 90 عشان يطلع طويل 👇 */
    min-height: 90px !important; 
    
    border-radius: 45px !important; /* زيادة الاستدارة لتناسب الطول */
    margin-bottom: 25px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08) !important;
    
    font-weight: 800 !important; /* تسميك الخط */
    color: #102646 !important;
    font-size: 17px !important; /* تكبير الخط ليناسب حجم البوكس */
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important; 
    
    padding: 0px 30px !important; /* زيادة المسافة الجانبية */
    transition: 0.3s;
}

/* السهم الصغير في النهاية */
div.stButton > button::after {
    content: "›";
    font-size: 32px; /* تكبير السهم */
    color: #102646;
    margin-left: auto; 
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
    transform: translateY(-3px); /* رفعة خفيفة عند التمرير */
    background-color: #fcfcfc !important;
    box-shadow: 0 12px 25px rgba(0,0,0,0.12) !important;
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
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:40px;">Contact Us</h2>', unsafe_allow_html=True)

# ===== الأزرار (طويلة، الكلام جنب الرسمة، والسهم بعيد) =====

# مسافة بسيطة جداً (فراغين)
gap = "&nbsp;" * 2

if st.button(f"✉️{gap}Email: Co.Care26@gmail.com"):
    pass

if st.button(f"📞{gap}Phone: +962 79 123 4567"):
    pass
