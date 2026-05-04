import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings System", layout="centered")

# 2. إدارة الحالة للتنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main_settings'

def navigate(to):
    st.session_state.page = to
    st.rerun()

# 3. CSS الموحد للتصميم الدقيق
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
    :root { --navy: #0f2446; }
    [data-testid="stAppViewContainer"] { background: #f0f2f6; }
    [data-testid="stHeader"] {display: none !important;}
    footer {visibility: hidden;}

    /* الحاوية الزرقاء الرئيسية */
    .block-container {
        max-width: 380px !important;
        margin: auto !important;
        padding: 30px 20px !important;
        background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
        border-radius: 42px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        margin-top: 30px !important;
        min-height: 600px;
    }

    /* تنسيق الهيدر */
    .header {
        display: flex; align-items: center; justify-content: center;
        margin-bottom: 30px; position: relative; color: var(--navy);
    }
    .back-btn { position: absolute; left: 0; font-size: 24px; cursor: pointer; }
    .title { font-weight: 900; font-size: 22px; margin: 0; }

    /* تصميم كبسولة الأزرار (القائمة الرئيسية) */
    div.stButton > button {
        width: 100% !important;
        height: 52px !important;
        border-radius: 100px !important;
        border: none !important;
        background: white !important;
        color: var(--navy) !important;
        margin-bottom: 12px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }
    
    /* توزيع المحتوى داخل الزر (أيقونة يسار | نص وسهم يمين) */
    div.stButton > button p {
        display: flex !important;
        justify-content: space-between !important;
        width: 100% !important;
        align-items: center !important;
        font-weight: 700 !important;
        margin: 0 !important;
    }

    /* تنسيق حقول الإدخال (صفحة كلمة المرور) */
    .stTextInput input {
        border-radius: 100px !important;
        border: none !important;
        padding: 12px 20px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }
    
    /* زر Save في الأسفل */
    .save-container { margin-top: auto; padding-top: 50px; }
</style>
""", unsafe_allow_html=True)

# 4. عرض الصفحات

# أ. صفحة الإعدادات الرئيسية (تصميم صورة image_edbe5e.png)
if st.session_state.page == 'main_settings':
    st.markdown(f'''
        <div class="header">
            <span class="back-btn"><i class="fas fa-chevron-left"></i></span>
            <p class="title">Settings</p>
        </div>
    ''', unsafe_allow_html=True)

    if st.button("🔒                         Change Password   ›"):
        navigate('change_password')
    
    if st.button("🌐                         Change Language   ›"):
        pass
        
    if st.button("⭐                                 Rate App   ›"):
        pass

    if st.button("Logout                                               ›"):
        pass

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report\nProblem   ›"): pass
    with col2:
        if st.button("✉️ Contact\nUs           ›"): pass

# ب. صفحة تغيير كلمة المرور (تصميم صورة image_d3025e.png)
elif st.session_state.page == 'change_password':
    # هيدر مع زر رجوع وظيفي
    col_back, col_title = st.columns([1, 10])
    with col_back:
        if st.button("‹", key="back_home"): navigate('main_settings')
    with col_title:
        st.markdown('<p class="title" style="text-align:center; margin-left:-30px;">Change Password</p>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # حقول الإدخال بتصميم الكبسولة
    st.text_input("Current Password", placeholder="Current Password", type="password", label_visibility="collapsed")
    st.text_input("New Password", placeholder="New Password", type="password", label_visibility="collapsed")
    st.text_input("Re-write", placeholder="Re-write New Password", type="password", label_visibility="collapsed")
    
    st.markdown('<p style="text-align:center; color:white; font-size:14px; font-weight:bold; margin-top:10px;">Report Password</p>', unsafe_allow_html=True)
    
    # زر Save في أسفل البطاقة
    st.markdown('<div style="height: 150px;"></div>', unsafe_allow_html=True)
    if st.button("Save", key="save_btn"):
        st.success("Success!")
        navigate('main_settings')
