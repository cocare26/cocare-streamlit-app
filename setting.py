import streamlit as st

# 1. إعدادات الصفحة - تفعيل القائمة الجانبية مجدداً
st.set_page_config(page_title="Settings System", layout="wide", initial_sidebar_state="expanded")

# 2. إدارة الحالة للتنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main_settings'

def navigate(to):
    st.session_state.page = to
    st.rerun()

# 3. CSS المحدث ليعمل مع Sidebar وبدون إخفاء العناصر
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
    :root { --navy: #0f2446; }
    
    /* خلفية التطبيق */
    [data-testid="stAppViewContainer"] { background: #f0f2f6; }
    [data-testid="stHeader"] {display: none !important;}
    footer {visibility: hidden;}

    /* ضبط البوكس الأزرق ليكون متناسقاً مع وجود الـ Sidebar */
    .block-container {
        max-width: 450px !important;
        margin: auto !important;
        padding: 40px 30px !important;
        background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
        border-radius: 45px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        margin-top: 20px !important;
        min-height: 700px;
    }

    /* تنسيق العناوين */
    .title-text { font-weight: 900; font-size: 24px; color: var(--navy); text-align: center; margin-bottom: 30px; }

    /* تصميم أزرار الكبسولة (توزيع أيقونة يسار وسهم يمين) */
    div.stButton > button {
        width: 100% !important;
        height: 55px !important;
        border-radius: 100px !important;
        border: none !important;
        background: white !important;
        color: var(--navy) !important;
        margin-bottom: 15px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
    }
    div.stButton > button p {
        display: flex !important;
        justify-content: space-between !important;
        width: 100% !important;
        align-items: center !important;
        font-weight: 700 !important;
    }

    /* تصميم الحقول الدائرية */
    .stTextInput input {
        border-radius: 100px !important;
        border: none !important;
        height: 50px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
    }
</style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar) - استرجاع الخيارات
with st.sidebar:
    st.markdown("### Menu")
    selection = st.radio("Go to:", [
        "setting", 
        "Create Account", 
        "Create Account Arabic", 
        "Forgot Password", 
        "Employee", 
        "To Do"
    ])

# 5. منطق العرض
if selection == "setting":
    # عرض محتوى الإعدادات داخل البوكس الأزرق
    if st.session_state.page == 'main_settings':
        st.markdown('<p class="title-text">Settings</p>', unsafe_allow_html=True)
        
        if st.button("🔒                         Change Password   ›"): navigate('password_page')
        if st.button("🌐                         Change Language   ›"): pass
        if st.button("⭐                                 Rate App   ›"): pass
        if st.button("🚪                                   Log Out   ›"): pass

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem   ›"): pass
        with col2:
            if st.button("✉️ Contact\nUs           ›"): pass

    elif st.session_state.page == 'password_page':
        # هيدر صفحة الباسورد
        c1, c2 = st.columns([1, 8])
        with c1:
            if st.button("‹"): navigate('main_settings')
        with c2:
            st.markdown('<p class="title-text" style="margin-left:-40px;">Change Password</p>', unsafe_allow_html=True)

        st.text_input("Current Password", placeholder="Current Password", type="password", label_visibility="collapsed")
        st.text_input("New Password", placeholder="New Password", type="password", label_visibility="collapsed")
        st.text_input("Confirm Password", placeholder="Confirm New Password", type="password", label_visibility="collapsed")
        
        st.markdown('<p style="text-align:center; color:white; font-weight:bold; margin-top:10px;">Report Password</p>', unsafe_allow_html=True)
        
        st.markdown("<div style='height:120px;'></div>", unsafe_allow_html=True)
        if st.button("Save"):
            st.success("Updated!")
            navigate('main_settings')

else:
    # عرض الصفحات الأخرى عند اختيارها من الـ Sidebar
    st.markdown(f"<h1 style='color:var(--navy);'>{selection} Page</h1>", unsafe_allow_html=True)
    st.write("محتوى الصفحة قيد التطوير...")
