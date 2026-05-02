import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (الألوان + الإزاحة لليمين + نحافة الأزرار)
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

/* البوكس الرئيسي مزاح لليمين */
.block-container {
    max-width: 80% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 30px 40px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* تصميم الأزرار النحيفة */
div.stButton > button {
    width: 100% !important;
    height: 55px !important; 
    border-radius: 100px !important; 
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 35px !important;
    padding-right: 35px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}

/* --- تعديل كلمة Settings فقط لتكون ضخمة جداً --- */
.settings-header {
    color: #000000 !important; 
    font-weight: 900 !important;
    font-size: 180px !important; /* تكبير الكلمة فقط */
    margin: 0 !important;
    flex-grow: 1;
    text-align: center;
    padding-left: 50px; 
    line-height: 1;
}

/* تكبير أيقونة السهم الجانبي لتناسب العنوان */
.back-arrow {
    font-size: 100px !important; 
    font-weight: 900 !important; 
    color: #000000 !important; 
}

</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    # هيدر الصفحة
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 80px; padding-left: 20px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار بمسافات مرنة
    def make_btn(emoji, label, page, gap_size):
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # أول زرين: مسافة 130
    make_btn("🔒", "Change Password", "password", gap_size=130)
    make_btn("🌐", "Change Language", "language", gap_size=130)
    
    # الزرين الأخيرين: مسافة 145
    make_btn("⭐", "Rate App", "rate", gap_size=145)
    make_btn("🚪", "Log Out", "main", gap_size=145)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# الشاشات الفرعية
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black;'>Change Password</h1>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black;'>Change Language</h1>", unsafe_allow_html=True)
