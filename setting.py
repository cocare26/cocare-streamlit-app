import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS الموحد
st.markdown("""
<style>
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
}

[data-testid="stAppViewContainer"] { 
    background: #eef2f7; 
}

/* البوكس الرئيسي */
.block-container {
    max-width: 450px !important;
    margin: auto !important;
    padding: 30px 40px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* تصميم الأزرار (الكبسولة البيضاء) */
div.stButton > button {
    width: 100% !important;
    height: 55px !important; 
    border-radius: 100px !important; 
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 17px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 25px !important;
    padding-right: 25px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    transition: 0.3s;
    margin-bottom: 10px;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}

/* العنوان وسهم الرجوع */
.settings-header {
    color: #000000 !important; 
    font-weight: 900 !important;
    font-size: 45px !important;
    margin: 0 !important;
    flex-grow: 1;
    text-align: center;
    line-height: 1.2;
}

.back-arrow {
    font-size: 40px !important; 
    font-weight: 900 !important; 
    color: #000000 !important;
    cursor: pointer;
}

/* إخفاء عناصر Streamlit الافتراضية للجمالية */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى بناءً على الصفحة الحالية
if st.session_state.page == 'main':
    # هيدر الصفحة
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 30px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار لتجنب التكرار
    # نستخدم &nbsp; لعمل مسافات بين الإيموجي والنص لدفعه لليمين
    def make_btn(emoji, label, target_page, spaces):
        if st.button(f"{emoji} {'&nbsp;'*spaces} {label} {'&nbsp;'*spaces} ›"):
            nav(target_page)

    # الأزرار الرئيسية
    make_btn("🔒", "Change Password", "password", 15)
    make_btn("🌐", "Change Language", "language", 15)
    make_btn("⭐", "Rate App", "rate", 22)
    make_btn("🚪", "Log Out", "main", 24)
    
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

    # السطر الأخير (الريبورت والكونتاكت بجانب بعض)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem ›"): 
            nav('report')
    with col2:
        if st.button("✉️ Contact Us ›"): 
            nav('contact')

# الشاشات الفرعية (كمثال)
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Change Password</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Select Language</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Report a Problem</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'rate':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Rate App</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Contact Us</h2>", unsafe_allow_html=True)
