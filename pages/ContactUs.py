import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}

/* تصغير عرض الكونتينر عشان يصير نحيف */
.block-container {
    max-width:350px; /* قللنا العرض من 430 لـ 350 عشان يصير نحيف */
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}

/* الأزرار - طويلة ونحيفة */
.stButton > button {
    width:100% !important;
    background:white !important;
    color:#102646 !important;
    border-radius:50px !important; 
    
    /* 👇 تحكم بالطول العمودي (زدناه لـ 70) 👇 */
    padding: 70px 15px !important; 
    min-height: 150px !important; 
    
    border:none !important;
    box-shadow:0 6px 15px rgba(0,0,0,0.08) !important;
    font-weight:800 !important;
    font-size: 14px !important; /* صغرنا الخط شوي عشان العرض النحيف */
    
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
}

/* السهم في نهاية البوكس */
.stButton > button::after {
    content: "›";
    font-size: 28px;
    color: #102646;
}

/* زر الرجوع */
.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    font-size:30px !important;
    width:auto !important;
    min-height: unset !important;
    padding: 10px !important;
}
.back-style .stButton > button::after {
    content: "" !important;
}
</style>
""", unsafe_allow_html=True)

# 🔙 Back
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("‹"):
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

# Title
st.markdown('<h2 style="text-align:center; color:#102646; font-weight:900; margin-bottom:40px;">Contact Us</h2>', unsafe_allow_html=True)

# ===== الأزرار (طول جبار وعرض نحيف) =====

# قللنا الفراغات العرضية لأن البوكس صار أنحف
short_gap = "&nbsp;" * 25 

st.button(f"✉️{short_gap}Email: Co.Care26@gmail.com")
st.button(f"📞{short_gap}Phone: +962 79 123 4567")
