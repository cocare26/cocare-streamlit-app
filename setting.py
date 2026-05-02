import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide")

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. التنسيق البرمجي (CSS) الموحد - تم إصلاح الخطأ هنا
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

.block-container {
    max-width: 80% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 30px 40px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
}

/* تكبير العنوان والسهم */
.settings-header {
    color: #000000 !important; 
    font-weight: 950;
    font-size: 150px; 
    margin: 0;
    flex-grow: 1;
    text-align: center;
    line-height: 1;
}

.back-arrow {
    font-size: 100px; 
    font-weight: 900; 
    color: #000000; 
    cursor: pointer;
    line-height: 1;
}

/* تنسيق الأزرار (الكبسولة) */
div.stButton > button {
    width: 100% !important;
    height: 65px !important; 
    border-radius: 100px !important; 
    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 20px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 35px !important;
    padding-right: 35px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    border: none !important;
    transition: 0.3s;
    margin-bottom: 10px;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(0,0,0,0.15) !important;
}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى بناءً على الصفحة
if st.session_state.page == 'main':
    # الهيدر الكبير
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 50px; padding-left: 20px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار
    def make_btn(emoji, label, page):
        if st.button(f"{emoji} &nbsp;&nbsp; {label} &nbsp;&nbsp; ›"):
            nav(page)

    # قائمة الأزرار
    make_btn("🔒", "Change Password", "password")
    make_btn("🌐", "Change Language", "language")
    make_btn("⭐", "Rate App", "rate")
    make_btn("🚪", "Log Out", "main")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us ›"): nav('contact')

# الصفحات الفرعية (أمثلة لتعمل الأزرار)
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.title("Change Password")

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.title("Select Language")
