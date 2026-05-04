import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="App Navigation", layout="centered")

# 2. إدارة الحالة للتنقل الداخلي
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

# 3. التنسيق الجمالي (CSS) للقائمة الرئيسية
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
</style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to:", ["setting", "Create Account", "Forgot Password", "To Do"])

# --- منطق عرض الصفحات ---

if selection == "setting":
    
    # ا. القائمة الرئيسية للإعدادات
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        st.markdown('<h2 style="text-align:center; color:#0f2446; margin-bottom:25px;">Settings</h2>', unsafe_allow_html=True)
        
        if st.button("🔒 Change Password                               ›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language                               ›"): nav_settings('language_page')
        if st.button("⭐ Rate App                                       ›"): nav_settings('rate_page')
        if st.button("🚪 Log Out                                       ›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem   ›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs           ›"): nav_settings('contact_page')
        st.markdown('</div>', unsafe_allow_html=True)

    # ب. صفحة تسجيل الخروج (HTML)
    elif st.session_state.settings_sub_page == 'logout_page':
        if st.button("Back", key="back_logout", help="hidden"): nav_settings('main_menu')
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: transparent; margin: 0; display: flex; justify-content: center; }
                .main-wrapper { 
                    width: 350px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
                    border-radius: 42px; padding: 30px; box-shadow: 0 15px 35px rgba(0,0,0,0.15); height: 500px;
                    display: flex; flex-direction: column; align-items: center;
                }
                .header-container { width: 100%; display: flex; align-items: center; justify-content: center; margin-bottom: 60px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                
                .logout-msg { color: #0f2446; font-weight: 700; font-size: 18px; margin-bottom: 40px; text-align: center; }
                
                .action-btn { 
                    width: 100%; max-width: 280px; background: white; border-radius: 100px; 
                    padding: 15px; margin-bottom: 15px; display: flex; align-items: center; 
                    justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
                    cursor: pointer; transition: 0.3s; border: none; font-family: inherit;
                }
                .action-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 15px rgba(0,0,0,0.12); }
                
                .btn-text { font-weight: 800; font-size: 16px; }
                .logout-text { color: #eb5757; } /* لون أحمر لتسجيل الخروج */
                .cancel-text { color: #0f2446; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_logout]').click()"><</div>
                    <h2 class="title">Log Out</h2>
                </div>
                
                <div class="logout-msg">Are you sure you want to log out?</div>
                
                <div class="action-btn" onclick="alert('Logged Out Successfully!')">
                    <span class="btn-text logout-text">Log Out</span>
                </div>
                
                <div class="action-btn" onclick="parent.window.document.querySelector('button[key=back_logout]').click()">
                    <span class="btn-text cancel-text">Cancel</span>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تقييم التطبيق (HTML)
    elif st.session_state.settings_sub_page == 'rate_page':
        if st.button("Back", key="back_rate", help="hidden"): nav_settings('main_menu')
        components.html("""
        <!-- (كود صفحة التقييم السابق) -->
        """, height=550)

    # د. باقي الصفحات (Language, Password) كما هي...

else:
    st.title(f"Welcome to {selection} Page")
