import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width: 550px; 
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

div.stButton > button {
    width: 100% !important;
    min-height: 80px !important; 
    background: white !important;
    border-radius: 35px !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.08) !important;
    margin-bottom: 20px !important;
    border: none !important;
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 16px !important;
    
    display: flex !important;
    align-items: center !important;
    
    /* بيسمح للفراغات اليدوية بالظهور */
    white-space: pre !important; 
    
    /* تأكيد توزيع العناصر من البداية */
    justify-content: flex-start !important; 
    padding: 0px 20px !important;
}

/* السهم الصغير في النهاية - دفع إجباري لليمين */
div.stButton > button::after {
    content: "›";
    font-size: 30px;
    color: #102646;
    
    /* 👇 هاد السطر السحري اللي بيدفع السهم لآخر البوكس 👇 */
    margin-left: auto !important; 
}

/* زر الرجوع */
.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 35px !important;
    width: auto !important;
}
.back-style .stButton > button::after { content: "" !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:35px;">Contact Us</h2>', unsafe_allow_html=True)

# ===== هون بنحط المسافة اللي بدك إياها =====
gap = " " * 5  # مسافة صغيرة بين الأيقونة والكلام
extra_space = " " * 20 # مسافة إضافية تدفش السهم

if st.button(f"✉️{gap}Email: Co.Care26@gmail.com{extra_space}"):
    pass

if st.button(f"📞{gap}Phone: +962 79 123 4567{extra_space}"):
    pass
