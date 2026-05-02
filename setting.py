import streamlit as st

# 1. إعدادات الصفحة (تبقى في البداية)
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. هنا تضع كود التكبير (داخل الـ CSS)
st.markdown("""
<style>
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; --bg2: #bfe3ff; --bg3: #eaf6ff;
}

[data-testid="stAppViewContainer"] { background: #eef2f7; }

.block-container {
    max-width: 80% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 30px 40px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
}

/* التعديل المطلوب هنا */
.settings-header {
    color: #000000 !important; 
    font-weight: 950;
    font-size: 150px; /* <--- غير هذا الرقم كما تشاء لتكبير الكلمة */
    margin: 0;
    flex-grow: 1;
    text-align: center;
    padding-left: 50px; 
    line-height: 1;
}

.back-arrow {
    font-size: 100px; 
    font-weight: 900; 
    color: #000000; 
    cursor: pointer;
}

div.stButton > button {
    width: 100% !important;
    height: 55px !important; 
    border-radius: 100px !important; 
    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 35px !important;
    padding-right: 35px !important;
}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 70px; padding-left: 20px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار
    def make_btn(emoji, label, page, gap_size):
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    make_btn("🔒", "Change Password", "password", gap_size=130)
    make_btn("🌐", "Change Language", "language", gap_size=130)
    make_btn("⭐", "Rate App", "rate", gap_size=145)
    make_btn("🚪", "Log Out", "main", gap_size=145)
