import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="App Navigation", layout="centered")

# 2. إدارة الحالة للتنقل الداخلي (إضافة الحالات الجديدة)
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

# 3. التنسيق الجمالي (CSS) - محدث ليتناسب مع الأزرار الكبيرة والصغيرة
st.markdown("""
<style>
:root { --navy: #0f2446; }
[data-testid="stAppViewContainer"] { background: #f0f2f6; }
[data-testid="stHeader"] {display: none !important;}

.settings-card {
    background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
    border-radius: 42px;
    padding: 30px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

/* تصميم الأزرار ككبسولات ممتدة */
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

/* توزيع الأيقونة والنص والسهم */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important;
    width: 100% !important;
    align-items: center !important;
}

/* تعديل المسافات بين الأزرار */
.stButton { margin-bottom: -10px; }
</style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to:", ["setting", "Create Account", "Forgot Password", "To Do"])

# --- منطق عرض الصفحات ---

if selection == "setting":
    st.markdown('<div class="settings-card">', unsafe_allow_html=True)
    
    # ا. القائمة الرئيسية للإعدادات
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown('<h2 style="text-align:center; color:#0f2446; margin-bottom:25px;">Settings</h2>', unsafe_allow_html=True)
        
        if st.button("🔒 Change Password                               ›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language                               ›"): nav_settings('language_page')
        if st.button("⭐ Rate App                                       ›"): nav_settings('rate_page')
        if st.button("🚪 Log Out                                       ›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
        
        # الأزرار الصغيرة (Report & Contact)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem   ›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs           ›"): nav_settings('contact_page')

    # ب. صفحة تغيير كلمة المرور
    elif st.session_state.settings_sub_page == 'change_password_page':
        st.markdown('<h2 style="text-align:center; color:#0f2446;">Password</h2>', unsafe_allow_html=True)
        st.text_input("Current Password", type="password")
        st.text_input("New Password", type="password")
        if st.button("Save"):
            st.success("Updated!")
            nav_settings('main_menu')
        if st.button("‹ Back"): nav_settings('main_menu')

    # ج. صفحة تقييم التطبيق (Rate App)
    elif st.session_state.settings_sub_page == 'rate_page':
        st.markdown('<h2 style="text-align:center; color:#0f2446;">Rate App</h2>', unsafe_allow_html=True)
        st.select_slider("Rate us:", options=["1", "2", "3", "4", "5"], value="5")
        if st.button("Submit"): nav_settings('main_menu')
        if st.button("‹ Back"): nav_settings('main_menu')

    # د. صفحة البلاغات (Report Problem)
    elif st.session_state.settings_sub_page == 'report_page':
        st.markdown('<h2 style="text-align:center; color:#0f2446;">Report</h2>', unsafe_allow_html=True)
        st.text_area("Describe the problem:")
        if st.button("Send Report"): nav_settings('main_menu')
        if st.button("‹ Back"): nav_settings('main_menu')

    # هـ. صفحة تسجيل الخروج (Log Out)
    elif st.session_state.settings_sub_page == 'logout_page':
        st.markdown('<h2 style="text-align:center; color:#0f2446;">Log Out</h2>', unsafe_allow_html=True)
        st.warning("Are you sure you want to log out?")
        if st.button("Confirm Logout"): st.info("Logged out!")
        if st.button("‹ Cancel"): nav_settings('main_menu')

    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.title(f"Welcome to {selection} Page")
    st.write("Content goes here...")
