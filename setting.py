import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS الموحد والمطور
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

/* 📦 الكارد الرئيسي (350px نحيف) */
.block-container {
    max-width: 350px !important;
    margin: auto !important;
    padding: 30px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

/* 🔝 هيدر الإعدادات */
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

/* 🔘 تنسيق الأزرار (توزيع الأطراف) */
div.stButton > button {
    background: white !important;
    border-radius: 100px !important;  
    width: 100% !important;
    height: 54px !important; /* طولت البوكس شوي ليطلع أفخم */
    padding: 0 25px !important; /* مسافات جانبية داخل الزر */
    border: none !important;
    margin-bottom: 12px !important;
    cursor: pointer !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    color: var(--navy) !important;
    transition: 0.3s ease;
}

/* 🎯 السحر هنا: توزيع المحتوى داخل الزر */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; /* يرمي الإيموجي شمال والنص يمين */
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    # هيدر الصفحة
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # بناء الأزرار (لاحظ ترتيب الإيموجي أولاً ثم النص)
    # الـ CSS سيتكفل برمي الإيموجي لليسار والنص لليمين
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): nav('main')
    
    # فاصل بسيط
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    # أزرار السطر الأخير
    if st.button("⚠️ Report a Problem"): nav('report')
    if st.button("✉️ Contact Us"): nav('contact')

# الشاشات الفرعية
elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.write("Report logic here...")
