import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* 1. تكبير عرض الحاوية الزرقاء عشان البوكس الأبيض يفرش لليمين */
.block-container {
    max-width: 650px; /* وسعنا العرض هون عشان البوكس يطول */
    margin: auto;
    padding: 20px 10px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    min-height: 600px;
}

/* 2. تنسيق البوكس الأبيض - ممتد وباللون الأبيض */
div.stButton > button {
    width: 100% !important; /* بياخد كامل العرض المتاح */
    min-height: 75px !important; 
    background-color: #FFFFFF !important; /* لون أبيض ناصع */
    border-radius: 30px !important;
    margin-bottom: 20px !important;
    border: none !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.07) !important;
    
    font-weight: 700 !important;
    color: #102646 !important;
    font-size: 16px !important; 
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important; /* النص بيبدأ من اليسار */
    
    padding: 0px 25px !important;
    transition: 0.3s;
}

/* 3. السهم - اندفاع لآخر اليمين لخلق مسافة بعد الحكي */
div.stButton > button::after {
    content: "›";
    font-size: 32px;
    color: #102646;
    margin-left: auto !important; /* هاد اللي بيعمل المسافة الكبيرة بعد الحكي */
}

/* زر الرجوع */
.back-style .stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 35px !important;
    width: auto !important;
    min-height: unset !important;
}
.back-style .stButton > button::after { content: "" !important; }

div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #ffffff !important;
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

st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:40px;">Contact Us</h2>', unsafe_allow_html=True)

# الأزرار (البوكس الأول والثاني صاروا طوال وبالعرض اللي بدك إياه)
gap = "&nbsp;" * 4 

if st.button(f"✉️{gap}Email: Co.Care26@gmail.com"):
    pass

if st.button(f"📞{gap}Phone: +962 79 123 4567"):
    pass
