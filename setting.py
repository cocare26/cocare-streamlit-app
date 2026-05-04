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

    # ب. صفحة تقييم التطبيق (HTML)
    elif st.session_state.settings_sub_page == 'rate_page':
        if st.button("Back", key="back_rate", help="hidden"): nav_settings('main_menu')
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
                }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .store-item { background: white; border-radius: 100px; padding: 14px 22px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; transition: 0.3s; }
                .store-item-left { display: flex; align-items: center; gap: 12px; }
                .store-item-icon { font-size: 16px; color: #0f2446; width: 20px; text-align: center; }
                .store-item-text { font-weight: 700; color: #0f2446; font-size: 14px; }
                .store-item-arrow { font-size: 18px; font-weight: bold; color: #0f2446; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_rate]').click()"><</div>
                    <h2 class="title">Rate App</h2>
                </div>
                <div class="store-item" onclick="window.open('https://play.google.com', '_blank')">
                    <div class="store-item-left"><span class="store-item-icon"><i class="fab fa-google-play"></i></span><span class="store-item-text">Google Play Store</span></div>
                    <span class="store-item-arrow">›</span>
                </div>
                <div class="store-item" onclick="window.open('https://apps.apple.com', '_blank')">
                    <div class="store-item-left"><span class="store-item-icon"><i class="fab fa-apple"></i></span><span class="store-item-text">Apple App Store</span></div>
                    <span class="store-item-arrow">›</span>
                </div>
                <div class="store-item" onclick="window.open('https://appgallery.huawei.com', '_blank')">
                    <div class="store-item-left"><span class="store-item-icon"><i class="fas fa-mobile-alt"></i></span><span class="store-item-text">Huawei AppGallery</span></div>
                    <span class="store-item-arrow">›</span>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تغيير اللغة (HTML)
    elif st.session_state.settings_sub_page == 'language_page':
        if st.button("Back", key="back_lang", help="hidden"): nav_settings('main_menu')
        components.html("""
        <!-- (كود صفحة اللغة كما هو في الرد السابق) -->
        """, height=550)

    # د. صفحة تغيير كلمة المرور (HTML)
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back", key="back_pass", help="hidden"): nav_settings('main_menu')
        components.html("""
        <!-- (كود صفحة كلمة المرور كما هو في الرد السابق) -->
        """, height=550)

else:
    st.title(f"Welcome to {selection} Page")
