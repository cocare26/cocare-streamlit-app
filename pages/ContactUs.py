import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

# ===== CSS المطور للبوكسات الضخمة جداً =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الكونتينر */
.block-container {
    max-width: 430px; 
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 700px;
}

/* تنسيق البوكسات الضخمة */
div.stButton > button {
    width: 100% !important;
    
    /* 1. زيادة الطول لأقصى حد (120px) ليعطيك الطول اللي بدك إياه */
    min-height: 120px !important; 
    
    border-radius: 50px !important; 
    margin-bottom: 25px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1) !important;
    
    font-weight: 800 !important;
    color: #102646 !important;
    font-size: 18px !important; /* تكبير الخط ليتناسب مع البوكس الضخم */
    
    display: flex !important;
    align-items: center !important;
    
    /* 2. جعل الكلام وراء بعضه من البداية */
    justify-content: flex-start !important; 
    
    padding: 0px 35px !important;
    transition: 0.4s;
}

/* السهم الصغير في أقصى اليمين */
div.stButton > button::after {
    content: "›";
    font-size: 35px;
    color: #102646;
    margin-left: auto; /* يدفعه لآخر اليمين مهما كبر البوكس */
}

/* زر الرجوع */
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
    transform: scale(1.02); /* تكبير خفيف عند اللمس */
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
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:45px;">Contact Us</h2>', unsafe_allow_html=True)

# ===== الأزرار الضخمة (المسافة صغيرة جداً ليكون الكلام وراء بعض) =====

# مسافة فراغ واحد فقط لضمان التلاصق التام وراء الرسمة
tight_gap = "&nbsp;" * 1 

if st.button(f"✉️{tight_gap}Email: Co.Care26@gmail.com"):
    pass

if st.button(f"📞{tight_gap}Phone: +962 79 123 4567"):
    pass
