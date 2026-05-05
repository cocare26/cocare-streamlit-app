import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# ===== CSS المعدل لزيادة المسافة بين الإيموجي والنص =====
st.markdown("""
<style>
#MainMenu, header, footer {visibility:hidden;}

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

.block-container {
    max-width:450px;
    margin:auto;
    padding:40px 25px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 20px 40px rgba(0,0,0,0.15);
}

.title {
    text-align:center;
    font-size:26px;
    font-weight:900;
    color:#102646;
    margin-bottom:40px;
}

/* تنسيق الزر الرئيسي */
div.stButton > button {
    width: 100% !important;
    min-height: 90px !important;
    border-radius: 45px !important;
    margin-bottom: 30px !important;
    background: white !important;
    border: none !important;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
    
    font-weight: 800 !important;
    color: #102646 !important;
    font-size: 18px !important;
    
    display: flex !important;
    align-items: center !important;
    
    /* 👇 هذا السطر يضمن توزيع العناصر (النص والسهم) 👇 */
    justify-content: flex-start !important; 
    
    /* 👇 المسافة بين الإيموجي والنص - غير الرقم ليزيد الفراغ 👇 */
    gap: 25px !important; 
    
    padding: 0px 35px !important;
}

/* السهم الجانبي (منفصل عن النص) */
div.stButton > button::after {
    content: "›";
    font-size: 30px;
    color: #102646;
    margin-left: auto; /* ليدفع السهم لآخر اليمين ويترك النص مكانه */
}

div.stButton > button:hover {
    transform: scale(1.02);
}

</style>
<div class="title">Settings</div>
""", unsafe_allow_html=True)

# ===== الأزرار =====

# لاحظ أننا نضع الإيموجي داخل النص، والـ CSS سيتكفل بالباقي
if st.button("🔒 Change Password"):
    st.switch_page("pages/ChangePassword.py")

if st.button("🌐 Change Language"):
    st.switch_page("pages/ChangeLanguage.py")

if st.button("⭐ Rate App"):
    st.switch_page("pages/RateApp.py")

if st.button("🚪 Log Out"):
     st.session_state.clear()
     st.switch_page("app.py")

# الأزرار السفلية
st.markdown("<br>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.button("⚠️ Report")
with col2:
    st.button("✉️ Contact")
