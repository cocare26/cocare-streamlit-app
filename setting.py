import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="App Navigation", layout="centered")

# 2. إدارة الحالة للتنقل الداخلي داخل صفحة الإعدادات
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

# دالة المنادي الداخلي
def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

# 3. التنسيق الجمالي (CSS) للكبسولات والخلفية
st.markdown("""
<style>
:root { --navy: #0f2446; }
[data-testid="stAppViewContainer"] { background: #f0f2f6; }

/* تصميم الحاوية الزرقاء */
.settings-card {
    background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
    border-radius: 42px;
    padding: 30px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

/* تحويل أزرار ستريمليت لشكب كبسولات ممتدة */
div.stButton > button {
    width: 100% !important;
    height: 55px !important;
    border-radius: 100px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    font-weight: 700 !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
}
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important;
    width: 100% !important;
}
</style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar) كما تظهر في صورتك
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to:", ["setting", "Create Account", "Forgot Password", "To Do"])

# --- منطق عرض الصفحات ---

if selection == "setting":
    # البدء برسم الكارد الأزرق
    st.markdown('<div class="settings-card">', unsafe_allow_html=True)
    
    # ا. عرض القائمة الرئيسية للإعدادات
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown('<h2 style="text-align:center; color:#0f2446;">Settings</h2>', unsafe_allow_html=True)
        
        # عند الضغط على هذا الزر، ننتقل لصفحة كلمة المرور داخلياً
        if st.button("🔒 Change Password                               ›"):
            nav_settings('change_password_page')
            
        if st.button("🌐 Change Language                               ›"):
            pass # يمكن إضافة صفحة لغة هنا بنفس الطريقة
            
    # ب. عرض صفحة تغيير كلمة المرور عند طلبها
    elif st.session_state.settings_sub_page == 'change_password_page':
        st.markdown('<h2 style="text-align:center; color:#0f2446;">Password</h2>', unsafe_allow_html=True)
        
        current_pwd = st.text_input("Current Password", type="password")
        new_pwd = st.text_input("New Password", type="password")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save"):
                st.success("Updated!")
                nav_settings('main_menu')
        with col2:
            if st.button("‹ Back"):
                nav_settings('main_menu')

    st.markdown('</div>', unsafe_allow_html=True)

else:
    # عرض محتوى الصفحات الأخرى
    st.title(f"Welcome to {selection} Page")
    st.write("Content goes here...")
