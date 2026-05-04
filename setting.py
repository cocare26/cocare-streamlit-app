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
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important;
    width: 100% !important;
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

    # ب. صفحة تغيير اللغة (كود HTML مخصص)
    elif st.session_state.settings_sub_page == 'language_page':
        if st.button("Back to Menu", key="back_lang", help="hidden"): nav_settings('main_menu')
        
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
                .language-capsule { background: white; border-radius: 100px; padding: 14px 22px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; transition: 0.3s; }
                .left-content { display: flex; align-items: center; gap: 12px; }
                .icon { color: #0f2446; font-size: 16px; }
                .label { color: #0f2446; font-weight: 700; font-size: 14px; }
                .status-mark { font-size: 18px; font-weight: bold; }
                .check { color: #2f80ed; }
                .arrow-icon { color: #0f2446; font-size: 18px; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_lang]').click()"><</div>
                    <h2 class="title">Change Language</h2>
                </div>
                <div class="language-capsule" onclick="alert('Language changed to English')">
                    <div class="left-content"><div class="icon"><i class="fas fa-globe"></i></div><div class="label">English</div></div>
                    <div class="status-mark check"><i class="fas fa-check"></i></div>
                </div>
                <div class="language-capsule" onclick="alert('تم تغيير اللغة للعربية')">
                    <div class="left-content"><div class="icon"><i class="fas fa-globe"></i></div><div class="label">العربية</div></div>
                    <div class="status-mark"><span class="arrow-icon">></span></div>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تغيير كلمة المرور (كود HTML مخصص)
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back to Menu", key="back_pass", help="hidden"): nav_settings('main_menu')
        
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
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 35px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .input-capsule { background: white; border-radius: 100px; padding: 10px 18px; margin-bottom: 15px; display: flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
                .input-capsule i.field-icon { color: #0f2446; margin-right: 12px; font-size: 16px; }
                .input-capsule input { border: none; outline: none; flex-grow: 1; font-size: 14px; color: #0f2446; background: transparent; }
                .report-text { text-align: center; color: white; font-size: 13px; margin-top: 5px; font-weight: bold; }
                .save-btn-container { margin-top: auto; display: flex; justify-content: center; padding-bottom: 10px; }
                .save-box { background: white; border-radius: 100px; width: 100%; padding: 12px; text-align: center; border: none; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
                .save-box span { color: #0f2446; font-weight: bold; font-size: 16px; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_pass]').click()"><</div>
                    <h2 class="title">Change Password</h2>
                </div>
                <div class="input-capsule"><i class="fas fa-lock field-icon"></i><input type="password" placeholder="Current Password"></div>
                <div class="input-capsule"><i class="fas fa-lock field-icon"></i><input type="password" placeholder="New Password"></div>
                <div class="input-capsule"><i class="fas fa-lock field-icon"></i><input type="password" placeholder="Re-write New Password"></div>
                <div class="report-text">Report Password</div>
                <div class="save-btn-container"><button class="save-box" onclick="alert('Password Saved!')"><span>Save</span></button></div>
            </div>
        </body>
        </html>
        """, height=550)

    # د. باقي الصفحات
    elif st.session_state.settings_sub_page in ['rate_page', 'logout_page', 'report_page', 'contact_page']:
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        st.markdown(f'<h2 style="text-align:center; color:#0f2446;">{st.session_state.settings_sub_page.replace("_", " ").title()}</h2>', unsafe_allow_html=True)
        if st.button("‹ Back"): nav_settings('main_menu')
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.title(f"Welcome to {selection} Page")
