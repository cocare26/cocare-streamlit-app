import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="App Navigation", layout="centered")

# 2. إدارة الحالة للتنقل الداخلي
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

# 3. التنسيق الجمالي العام (CSS) لستريمليت
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

# 4. القائمة الجانبية (Sidebar)
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

    # ب. صفحة الإبلاغ عن مشكلة (HTML المخصص من الصورة)
    elif st.session_state.settings_sub_page == 'report_page':
        if st.button("Back", key="back_report", help="hidden"): nav_settings('main_menu')
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
                    display: flex; flex-direction: column;
                }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                
                .report-textarea {
                    width: 100%; height: 220px; border-radius: 25px; border: none; outline: none; padding: 18px;
                    background: white; font-size: 16px; color: #0f2446; resize: none; box-sizing: border-box;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08); font-family: inherit;
                }
                .report-textarea::placeholder { color: #808080; }
                
                .send-btn {
                    background: white; border-radius: 100px; width: 100%; padding: 14px 22px;
                    display: flex; align-items: center; justify-content: space-between; 
                    border: none; margin-top: auto; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.08); box-sizing: border-box;
                }
                .send-btn span { color: #0f2446; font-weight: 700; font-size: 14px; order: 2; }
                .main-icon { color: #808080; font-size: 18px; order: 1; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_report]').click()"><</div>
                    <h2 class="title">Report a Problem</h2>
                </div>
                <textarea class="report-textarea" placeholder="I need help"></textarea>
                <div style="margin-top: auto; padding-bottom: 10px;">
                    <button class="send-btn" onclick="alert('Report Sent!')">
                        <i class="fas fa-paper-plane main-icon"></i>
                        <span>Send Report</span>
                    </button>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تسجيل الخروج (HTML)
    elif st.session_state.settings_sub_page == 'logout_page':
        if st.button("Back", key="back_logout", help="hidden"): nav_settings('main_menu')
        # ... (كود صفحة اللوق أوت السابق)

    # د. صفحة التقييم وصفحة اللغة وصفحة كلمة المرور...

else:
    st.title(f"Welcome to {selection} Page")
