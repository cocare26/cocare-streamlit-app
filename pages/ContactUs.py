import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* 1. الحاوية الزرقاء: قللنا الـ padding الجانبي لـ 5px عشان البوكسات تفرش */
.block-container {
    max-width: 500px; 
    margin: auto;
    padding: 20px 5px !important; /* مساحة جانبية شبه معدومة */
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

/* 2. الأزرار: تم إلغاء المسافات الجانبية لتطويل البوكس أفقياً */
div.stButton > button {
    width: 100% !important; /* يمتد لكامل عرض الحاوية */
    min-height: 70px !important; 
    border-radius: 25px !important;
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
    
    /* حطينا padding بسيط جداً عشان النص ما يلزق بالحافة */
    padding: 0px 15px !important; 
    transition: 0.3s;
}

/* السهم: يندفع لآخر اليمين تماماً */
div.stButton > button::after {
    content: "›";
    font-size: 30px;
    color: #102646;
    margin-left: auto !important;
}

/* زر الرجوع */
.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 35px !important;
    width: auto !important;
    padding: 0 !important;
    margin-left: 15px !important; /* عشان يضل بعيد عن الحافة نتفة */
}
.back-style .stButton > button::after { content: "" !important; }
</style>
""", unsafe_allow_html=True)

# 🔙 زر الرجوع
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("‹"):
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:40px;">Contact Us</h2>', unsafe_allow_html=True)

# الأزرار ممتدة الآن بدون "سماحة" جانبية كبيرة
gap = "&nbsp;" * 2 

if st.button(f"✉️{gap}Email: Co.Care26@gmail.com"):
    pass

if st.button(f"📞{gap}Phone: +962 79 123 4567"):
    pass
