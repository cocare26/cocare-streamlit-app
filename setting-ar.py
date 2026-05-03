import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="واجهة الإعدادات", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. CSS مخصص للغة العربية (RTL)
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* إخفاء العناصر غير الضرورية */
[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* 📦 الكارد الرئيسي */
.block-container{
    max-width:420px !important;
    margin:auto !important;
    padding:25px 30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    margin-top: 20px !important;
    direction: rtl; /* ضبط الاتجاه للعربية */
}

/* الرأس */
.header-container {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 35px; position: relative;
}
.back-arrow { position: absolute; right: 0; font-size: 28px; font-weight: bold; color: var(--navy); cursor: pointer; }
.settings-header { margin: 0; font-weight: 900; font-size: 22px; color: var(--navy); }

/* 🔘 تنسيق الأزرار */
div.stButton { width: 100% !important; }

div.stButton > button {
    width: 100% !important;
    height: 58px !important;
    border-radius: 25px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    padding: 0 20px !important;
    transition: 0.3s !important;
}

/* 🔥 توزيع الإيموجي والنص للعربي */
div.stButton > button p {
    display: flex !important;
    flex-direction: row-reverse !important; /* عكس الترتيب ليصبح الإيموجي يميناً */
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

/* الإيموجي (جهة اليمين في العربي) */
div.stButton > button p span:first-child {
    font-size: 20px;
    margin-left: 10px;
}

/* دفع النص والسهم لليسار */
div.stButton > button p span:last-child {
    margin-right: auto !important;
    text-align: left;
}

/* تأثير التحويم */
div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,.1) !important;
}
</style>
""", unsafe_allow_html=True)

# 4. الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر العربي
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">›</div>
            <p class="settings-header">الإعدادات</p>
        </div>
    """, unsafe_allow_html=True)
    
    # أزرار الخيارات الرئيسية
    st.button("تغيير كلمة المرور 🔒 ‹")
    st.button("تغيير اللغة 🌐 ‹")
    st.button("تقييم التطبيق ⭐ ‹")
    st.button("تسجيل الخروج 🚪 ‹")
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    # أزرار التواصل (الشبكة)
    col1, col2 = st.columns(2)
    with col1:
        st.button("الإبلاغ عن\nمشكلة ⚠️")
    with col2:
        st.button("تواصل\nمعنا ✉️")
