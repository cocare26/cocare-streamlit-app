import streamlit as st

# 1. إعدادات الصفحة - إخفاء القائمة الجانبية افتراضياً
st.set_page_config(page_title="Settings UI", layout="centered", initial_sidebar_state="collapsed")

# 2. إدارة الحالة للتنقل بين الصفحات الداخلية
if 'page' not in st.session_state:
    st.session_state.page = 'main_settings'

def navigate(to):
    st.session_state.page = to
    st.rerun()

# 3. CSS المخصص لتصميم الكبسولات والخلفية بدون Sidebar
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
    :root { --navy: #0f2446; }
    
    /* إخفاء أي أثر للقائمة الجانبية أو الهيدر الأصلي */
    [data-testid="stSidebar"], [data-testid="stSidebarNav"] {display: none !important;}
    [data-testid="stHeader"] {display: none !important;}
    footer {visibility: hidden;}

    /* تلوين خلفية التطبيق كاملة */
    [data-testid="stAppViewContainer"] { background: #f0f2f6; }

    /* الحاوية الزرقاء (تطبيق الموبايل) */
    .block-container {
        max-width: 400px !important;
        margin: auto !important;
        padding: 30px 25px !important;
        background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
        border-radius: 45px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        margin-top: 40px !important;
        min-height: 650px;
    }

    /* تصميم الهيدر (العنوان وزر الرجوع) */
    .header-box {
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 40px; position: relative; color: var(--navy);
    }
    .title-text { font-weight: 900; font-size: 24px; margin: 0; font-family: 'sans-serif'; }

    /* تنسيق أزرار ستريمليت (الكبسولات) */
    div.stButton > button {
        width: 100% !important;
        height: 55px !important;
        border-radius: 100px !important;
        border: none !important;
        background: white !important;
        color: var(--navy) !important;
        margin-bottom: 15px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
        transition: 0.3s;
    }
    
    /* توزيع المحتوى داخل الكبسولة */
    div.stButton > button p {
        display: flex !important;
        justify-content: space-between !important;
        width: 100% !important;
        align-items: center !important;
        font-weight: 700 !important;
        font-size: 16px !important;
    }

    /* تنسيق حقول الإدخال في صفحة الباسورد */
    .stTextInput input {
        border-radius: 100px !important;
        border: none !important;
        height: 50px !important;
        padding-left: 20px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
    }
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى بناءً على الصفحة الحالية

# --- صفحة الإعدادات الرئيسية ---
if st.session_state.page == 'main_settings':
    st.markdown('<div class="header-box"><p class="title-text">Settings</p></div>', unsafe_allow_html=True)

    # الأزرار بتصميم الكبسولة الموزع
    if st.button("🔒                         Change Password   ›"): navigate('password_page')
    if st.button("🌐                         Change Language   ›"): pass
    if st.button("⭐                                 Rate App   ›"): pass
    if st.button("🚪                                   Log Out   ›"): pass

    st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)
    
    # الأزرار الصغيرة في الأسفل
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report\nProblem   ›"): pass
    with col2:
        if st.button("✉️ Contact\nUs           ›"): pass

# --- صفحة تغيير كلمة المرور ---
elif st.session_state.page == 'password_page':
    # هيدر مع زر رجوع وظيفي
    c1, c2 = st.columns([1, 8])
    with c1:
        if st.button("‹"): navigate('main_settings')
    with c2:
        st.markdown('<p class="title-text" style="text-align:center; margin-left:-35px;">Change Password</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # حقول الإدخال
    st.text_input("Current Password", placeholder="Current Password", type="password", label_visibility="collapsed")
    st.text_input("New Password", placeholder="New Password", type="password", label_visibility="collapsed")
    st.text_input("Confirm Password", placeholder="Re-write New Password", type="password", label_visibility="collapsed")
    
    st.markdown('<p style="text-align:center; color:white; font-weight:bold; cursor:pointer;">Report Password</p>', unsafe_allow_html=True)
    
    # زر الحفظ في الأسفل
    st.markdown("<div style='height:150px;'></div>", unsafe_allow_html=True)
    if st.button("Save"):
        st.success("Password Updated!")
        navigate('main_settings')
        
