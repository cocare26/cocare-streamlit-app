import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* 1. جعل الحاوية تفرش بالعرض لآخر الصفحة أو لمدى واسع جداً */
.block-container {
    max-width: 650px; /* كبّرنا العرض ليعطيك المساحة اللي طلبتها بالأسهم */
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

/* 2. جعل البوكس (الزر) يمتد للنهاية ويوصل السهم لقدام */
div.stButton > button {
    width: 100% !important;
    min-height: 70px !important; 
    background: white !important;
    
    /* 👇 السر هون: الـ 8px بتخلي السهم يوصل لآخر البوكس من قدام 👇 */
    padding: 15px 8px 15px 25px !important; 
    
    border-radius: 25px !important; 
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    margin-bottom: 20px !important; 
    border: none !important;
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 16px !important; 
    
    display: flex !important;
    align-items: center !important;
    
    /* دفع السهم لأقصى اليمين */
    justify-content: space-between !important; 
    
    transition: 0.3s ease;
}

div.stButton > button::after {
    content: "›";
    font-size: 32px; /* تكبير السهم ليكون واضح عند النهاية */
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
    transform: scale(1.01); /* تأثير بسيط عند اللمس */
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

# الأزرار ممتدة للنهاية
if st.button("✉️ Email: Co.Care26@gmail.com"): pass
if st.button("📞 Phone: +962 79 123 4567"): pass
