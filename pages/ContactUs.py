import streamlit as st

st.set_page_config(page_title="Contact Us", layout="centered")

st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', sans-serif;
}

.block-container {
    max-width:430px; /* العرض ثابت ما لمسناه */
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}

/* الأزرار - زيادة الطول فقط */
.stButton > button {
    width:100% !important;
    background:white !important;
    color:#102646 !important;
    border-radius:50px !important; /* استدارة مناسبة للطول */
    
    /* 👇 السر هون: زدنا الرقم الأول (الطول) لـ 60 عشان يطلع طويلللل جداً 👇 */
    padding: 60px 25px !important; 
    min-height: 140px !important; /* هاد اللي بيخليه طويل غصب عنه */
    
    border:none !important;
    box-shadow:0 6px 15px rgba(0,0,0,0.08) !important;
    font-weight:800 !important;
    font-size: 18px !important; /* كبرنا الخط شوي عشان يتناسب مع الطول */
    
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important; /* الحكي ورا الرسمة فوراً */
}

/* السهم في الزاوية */
.stButton > button::after {
    content: "›";
    margin-left: auto; 
    font-size: 35px;
    color: #102646;
}

/* زر الرجوع - يضل صغير وما يتأثر بطول البوكسات */
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

div.stButton > button:hover {
    background-color: #fcfcfc !important;
    transform: translateY(-2px);
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

# Buttons
# الحكي ورا الرسمة مباشرة بدون فراغات كبيرة
st.button("✉️ Email: Co.Care26@gmail.com")
st.button("📞 Phone: +962 79 123 4567")
