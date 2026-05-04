import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Smart App Settings", layout="centered")

# 2. إدارة الحالة للتنقل الداخلي (Navigation Logic)
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

# 3. التنسيق الجمالي العام لستريمليت
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
    margin-bottom: 10px;
    transition: transform 0.2s ease;
}

div.stButton > button:active {
    transform: scale(0.97);
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
        
        if st.button("🔒 Change Password                               ›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language                               ›"): nav_settings('language_page')
        if st.button("⭐ Rate App                                       ›"): nav_settings('rate_page')
        if st.button("🚪 Log Out                                       ›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem   ›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs            ›"): nav_settings('contact_page')
        st.markdown('</div>', unsafe_allow_html=True)

    # ب. صفحة تغيير اللغة (التصميم الجديد والمطلوب)
    elif st.session_state.settings_sub_page == 'language_page':
        if st.button("Back", key="back_lang", help="hidden"): nav_settings('main_menu')
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: transparent; margin: 0; display: flex; justify-content: center; }
                .main-wrapper { 
                    width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
                    border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px; display: flex; flex-direction: column;
                }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; transition: transform 0.2s; }
                .back-icon:active { transform: scale(0.8); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                
                .language-capsule {
                    background: white; border-radius: 100px; padding: 15px 22px; margin-bottom: 15px;
                    display: flex; align-items: center; justify-content: space-between;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; transition: all 0.2s ease;
                }
                .language-capsule:active { transform: scale(0.96); }
                
                .left-content { display: flex; align-items: center; gap: 12px; }
                .icon { color: #0f2446; font-size: 18px; }
                .label { color: #0f2446; font-weight: 700; font-size: 16px; }
                .status-mark { font-size: 18px; font-weight: bold; }
                .check { color: #2f80ed; }
                .arrow { color: #0f2446; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_lang]').click()">&lt;</div>
                    <h2 class="title">Change Language</h2>
                </div>
                
                <!-- English -->
                <div class="language-capsule" onclick="alert('English selected')">
                    <div class="left-content">
                        <div class="icon"><i class="fas fa-globe"></i></div>
                        <div class="label">English</div>
                    </div>
                    <div class="status-mark check"><i class="fas fa-check"></i></div>
                </div>

                <!-- Arabic -->
                <div class="language-capsule" onclick="alert('تم اختيار اللغة العربية')">
                    <div class="left-content">
                        <div class="icon"><i class="fas fa-globe"></i></div>
                        <div class="label">العربية</div>
                    </div>
                    <div class="status-mark arrow">&gt;</div>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تغيير كلمة المرور
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back", key="back_pass", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .card { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; display: flex; flex-direction: column; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 35px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; transition: transform 0.2s; }
            .back:active { transform: scale(0.8); }
            .input-capsule { background: white; border-radius: 100px; padding: 12px 18px; margin-bottom: 15px; display: flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
            input { border: none; outline: none; width: 100%; font-size: 14px; margin-left: 10px; }
            .save-box { background: white; border-radius: 100px; width: 100%; padding: 15px; text-align: center; color: #0f2446; font-weight: bold; font-size: 18px; margin-top: auto; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: 0.3s; }
            .save-box:active { transform: scale(0.95); }
        </style>
        <div class="card">
            <div class="header"><div class="back" onclick="parent.window.document.querySelector('button[key=back_pass]').click()"><</div><h2 style="color:#0f2446; margin:0; font-size:20px;">Change Password</h2></div>
            <div class="input-capsule">🔒 <input type="password" placeholder="Current Password"></div>
            <div class="input-capsule">🔒 <input type="password" placeholder="New Password"></div>
            <div class="input-capsule">🔒 <input type="password" placeholder="Re-write New Password"></div>
            <div class="save-box" onclick="alert('Password Saved!')">Save</div>
        </div>
        """, height=550)

    # د. بقية الصفحات كما هي في الكود الأصلي
    elif st.session_state.settings_sub_page == 'report_page':
        if st.button("Back", key="back_report", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .card { width: 350px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; display: flex; flex-direction: column; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 30px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; }
            textarea { width: 100%; height: 200px; border-radius: 25px; border: none; padding: 15px; box-sizing: border-box; resize: none; margin-bottom: 20px; }
            .send-btn { background: white; border-radius: 100px; padding: 15px; display: flex; justify-content: space-between; align-items: center; cursor: pointer; border: none; width: 100%; margin-top: auto; }
        </style>
        <div class="card">
            <div class="header"><div class="back" onclick="parent.window.document.querySelector('button[key=back_report]').click()"><</div><h2 style="color:#0f2446">Report</h2></div>
            <textarea placeholder="I need help..."></textarea>
            <button class="send-btn" onclick="alert('Sent!')"><span style="color:#808080">✈️</span><span style="color:#0f2446; font-weight:bold">Send Report</span></button>
        </div>
        """, height=550)

    elif st.session_state.settings_sub_page == 'contact_page':
        if st.button("Back", key="back_contact", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .card { width: 350px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; }
            .capsule { background: white; border-radius: 100px; padding: 15px 20px; margin-bottom: 15px; display: flex; align-items: center; color: #0f2446; font-weight: bold; cursor: pointer; }
        </style>
        <div class="card">
            <div class="header"><div class="back" onclick="parent.window.document.querySelector('button[key=back_contact]').click()"><</div><h2 style="color:#0f2446">Contact Us</h2></div>
            <div class="capsule" onclick="window.location.href='mailto:CoCare26@gmail.com'">📧 CoCare26@gmail.com</div>
            <div class="capsule" onclick="window.location.href='tel:+962791234567'">📞 +962 79 123 4567</div>
        </div>
        """, height=550)

    elif st.session_state.settings_sub_page == 'logout_page':
        if st.button("Back", key="back_logout", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .card { width: 350px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; display: flex; flex-direction: column; align-items: center; }
            .header { width: 100%; display: flex; align-items: center; justify-content: center; margin-bottom: 60px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; }
            .btn { width: 100%; padding: 15px; border-radius: 100px; background: white; margin-bottom: 15px; cursor: pointer; font-weight: bold; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        </style>
        <div class="card">
            <div class="header"><div class="back" onclick="parent.window.document.querySelector('button[key=back_logout]').click()"><</div><h2 style="color:#0f2446">Log Out</h2></div>
            <p style="color:#0f2446; font-weight:bold; margin-bottom:40px">Are you sure you want to log out?</p>
            <div class="btn" style="color:#eb5757" onclick="alert('Logged Out!')">Log Out</div>
            <div class="btn" style="color:#0f2446" onclick="parent.window.document.querySelector('button[key=back_logout]').click()">Cancel</div>
        </div>
        """, height=550)

    elif st.session_state.settings_sub_page == 'rate_page':
        if st.button("Back", key="back_rate", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .card { width: 350px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; }
            .store { background: white; border-radius: 100px; padding: 15px 20px; margin-bottom: 15px; display: flex; justify-content: space-between; align-items: center; color: #0f2446; font-weight: bold; cursor: pointer; }
        </style>
        <div class="card">
            <div class="header"><div class="back" onclick="parent.window.document.querySelector('button[key=back_rate]').click()"><</div><h2 style="color:#0f2446">Rate App</h2></div>
            <div class="store" onclick="window.open('https://play.google.com')"><span>▶️ Google Play</span><span>›</span></div>
            <div class="store" onclick="window.open('https://apps.apple.com')"><span>🍎 App Store</span><span>›</span></div>
        </div>
        """, height=550)

else:
    st.title(f"Welcome to {selection} Page")
