import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (تم ضبط المسافات بناءً على الصورة)
st.markdown("""
<style>
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"] { background: #eef2f7; }
footer {visibility: hidden;}

/* الكارد الرئيسي */
.block-container {
    max-width: 350px !important;
    margin: auto !important;
    padding: 30px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

/* الهيدر */
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 40px;
    position: relative;
}

.back-arrow {
    position: absolute; left: 0;
    font-size: 28px;
    font-weight: bold; color: var(--navy);
}

.settings-header {
    margin: 0;
    font-weight: 900;
    font-size: 20px;
    color: var(--navy);
}

/* 🔘 تصميم الأزرار بناءً على الصورة المرسلة */
div.stButton > button {
    background: white !important;
    border-radius: 100px !important;  
    width: 100% !important;
    height: 54px !important; 
    padding: 0 25px !important; 
    border: none !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    transition: 0.3s ease;
}

/* 🎯 توزيع العناصر: الإيموجي يسار - مسافة كبيرة - النص يمين */
div.stButton > button p {
    display: flex !important;
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    color: var(--navy) !important;
    font-weight: 800 !important; /* خط عريض كما في الصورة */
    font-size: 16px !important;
}

/* دفع النص لليمين بترك مسافة مطاطية بعد الإيموجي مباشرة */
div.stButton > button p::before {
    content: "";
    flex-grow: 1; /* هذه تصنع الفراغ الكبير في الوسط */
    order: 2;
}

/* ترتيب العناصر داخل الزر */
div.stButton > button p {
    justify-content: flex-start !important;
}

/* الإيموجي (أول عنصر) */
div.stButton > button p :first-child {
    order: 1;
    font-size: 20px; /* تكبير الإيموجي قليلاً */
}

/* النص (ثاني عنصر) */
div.stButton > button p :last-child {
    order: 3;
    padding-right: 5px; /* مسافة بسيطة عن الحافة اليمنى */
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # توزيع العناصر: إيموجي ثم نص
    st.button("🔒 Change Password")
    st.button("🌐 Change Language")
    st.button("⭐ Rate App")
    st.button("🚪 Log Out")
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    if st.button("⚠️ Report a Problem"): nav('report')
    if st.button("✉️ Contact Us"): nav('contact')

elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.write("Report page content...")
