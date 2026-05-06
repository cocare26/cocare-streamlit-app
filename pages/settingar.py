import streamlit as st
import os

from language_guard import check_language

st.set_page_config(page_title="الإعدادات", layout="centered")

check_language(os.path.basename(__file__))

st.markdown("""
<style>

#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    direction: rtl;
}

.block-container {
    max-width: 390px; 
    margin: auto;
    padding: 35px 20px;
    background: linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius: 40px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

.title {
    text-align: center;
    font-weight: 900;
    color: #102646;
    font-size: 28px;
    margin-bottom: 25px;
    width: 100%;
    letter-spacing: 0.5px;
    text-shadow: 0 2px 6px rgba(0,0,0,0.08);
    margin-top: 18px;
}

.back-btn div.stButton > button {
    width:55px !important;
    height:55px !important;
    border-radius:30px !important;
    background:#e9eef3 !important;
    border:none !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08) !important;
    font-size:26px !important;
    color:#102646 !important;
    display:flex !important;
    align-items:center !important;
    justify-content:center !important;
}

div.stButton > button {
    width: 100% !important;
    min-height: 60px !important; 
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
    justify-content: space-between !important; 
    padding: 0px 25px !important;
    position: relative !important;
}

/* الأسهم على طرف البوكس (بعيدة عن النص) */
div.stButton > button::before {
    content: "‹" !important;
    position: absolute !important;
    left: 10px !important;   /* 👈 صار بعيد عن الكلام */
    top: 50% !important;
    transform: translateY(-50%) !important;
    font-size: 28px !important;
    color: #102646 !important;
    font-weight: 900 !important;
}

/* لا نضيف سهم لزر الرجوع */
.back-btn div.stButton > button::before {
    content: "" !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #fcfcfc !important;
}

</style>
""", unsafe_allow_html=True)

# ===== الهيدر =====
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.markdown('<div class="back-btn">', unsafe_allow_html=True)
    if st.button("›"):
        st.switch_page("pages/Customer_ar.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="title">الإعدادات</div>', unsafe_allow_html=True)

# ===== الأزرار =====

normal_gap = "&nbsp;" * 55
normal_gap1 = "&nbsp;" * 63

if st.button(f"🔒{normal_gap}تغيير كلمة المرور"):
    st.switch_page("pages/Change_Passwordar.py")

if st.button(f"🌐{normal_gap1}تغيير اللغة"):
    st.switch_page("pages/Change_Languagear.py")

extreme_gap = "&nbsp;" * 61
extreme_gap1 = "&nbsp;" * 55

if st.button(f"⭐{extreme_gap}تقييم التطبيق"):
    st.switch_page("pages/Rate_Appar.py")

if st.button(f"🚪{extreme_gap1}تسجيل الخروج"):
    st.session_state.clear()
    st.switch_page("arabic-app.py")

# ===== الصف الأخير =====
col_gap = "&nbsp;" * 2

col1, col2 = st.columns(2)

with col1:
    if st.button(f"⚠️{col_gap}تبليغ عن مشكلة"):
        st.switch_page("pages/Report_Problemar.py")

with col2:
    if st.button(f"✉️{col_gap}اتصل بنا"):
        st.switch_page("pages/ContactUsar.py")
