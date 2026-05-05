import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

# ===== CSS الموحد (تم تعديل العرض ليصبح أطول) =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* 1. تكبير العرض الكلي (تطويل العرض) */
.block-container {
    max-width: 600px; /* زدنا العرض من 430 لـ 600 عشان يفرش أكتر */
    margin: auto;
    padding: 20px 25px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

/* 2. تنسيق البوكسات الموحد - يمتد مع العرض الجديد */
div.stButton > button {
    width: 100% !important; /* بيضمن إن البوكس يوصل لآخر عرض الكونتينر */
    min-height: 70px !important; 
    border-radius: 35px !important;
    margin-bottom: 20px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 5px 12px rgba(0,0,0,0.06) !important;
    
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 16px !important; 
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important; 
    
    padding: 0px 30px !important; /* زيادة التباعد الجانبي شوي */
    transition: 0.3s;
}

/* السهم الصغير في النهاية - يندفع لآخر اليمين مهما كان العرض */
div.stButton > button::after {
    content: "›";
    font-size: 30px;
    color: #102646;
    margin-left: auto; /* هاد السطر السحري اللي بيطرد السهم لليمين مهما كان العرض طويل */
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
    box-shadow: 0 8px 20px rgba(0,0,0,0.1) !important;
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

# ===== الأزرار (أصبحت الآن ممتدة بالعرض الجديد) =====

gap = "&nbsp;" * 4 

if st.button(f"✉️{gap}Email: Co.Care26@gmail.com"):
    pass

if st.button(f"📞{gap}Phone: +962 79 123 4567"):
    pass
