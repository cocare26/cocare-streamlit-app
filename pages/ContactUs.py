import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width: 550px; /* العرض مريح عشان الفراغات تأخذ راحتها */
    margin: auto;
    padding: 20px 16px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

div.stButton > button {
    width: 100% !important;
    min-height: 70px !important; 
    background: white !important;
    border-radius: 30px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    margin-bottom: 20px !important;
    border: none !important;
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 15px !important;
    
    display: flex !important;
    align-items: center !important;
    
    /* 👇 التعديل المهم: البدء من اليسار عشان الفراغات تدفش السهم 👇 */
    justify-content: flex-start !important; 
    
    /* 👇 التعديل السحري: إجبار المتصفح على قراءة الفراغات اليدوية 👇 */
    white-space: pre !important; 
    
    padding: 0px 15px !important;
}

/* السهم بيظهر في نهاية النص اللي أنت كاتبه */
div.stButton > button::after {
    content: "›";
    font-size: 28px;
    color: #102646;
    margin-left: 0px; /* السهم رح يلحق آخر فراغ أنت بتكتبه */
}

/* زر الرجوع */
.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 35px !important;
    width: auto !important;
}
</style>
""", unsafe_allow_html=True)

# العنوان
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:35px;">Contact Us</h2>', unsafe_allow_html=True)

# ===== استخدام الفراغات اليدوية كما طلبت =====

# زد الفراغات (المسطرة) في نهاية النص لتوصل السهم للنهاية
spaces = " " * 35 

if st.button(f"✉️ Email: Co.Care26@gmail.com{spacesspaces}"):
    pass

if st.button(f"📞 Phone: +962 79 123 4567{spacesspacesspaces}"):
    pass
