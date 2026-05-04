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
}
</style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية (Sidebar)
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to:", ["setting", "Create Account", "Forgot Password", "To Do"])

# --- منطق عرض الصفحات ---

# السطر 50 يبدأ هنا
if selection == "setting":
    
    # ا. القائمة الرئيسية للإعدادات (يجب أن تكون مزاحة بـ 4 مسافات عن الـ if أعلاها)
    # ا. القائمة الرئيسية للإعدادات
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown("""
            <style>
                :root {
                    --navy: #0f2446;
                    --blue-primary: #2f80ed; /* أزرق صريح */
                    --blue-light: #d6ecff;
                }
                
                [data-testid="stAppViewBlockContainer"] {
                    max-width: 350px !important;
                    margin: auto !important;
                    padding: 30px !important;
                    /* تعديل التدرج ليكون أزرق أوضح */
                    background: linear-gradient(180deg, #bfe3ff 0%, #2f80ed 100%) !important;
                    border-radius: 42px !important;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                }

                .header-container {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    margin-bottom: 25px;
                    position: relative;
                    width: 100%;
                }
                .back-icon {
                    position: absolute;
                    left: 0;
                    font-size: 28px;
                    font-weight: bold;
                    color: var(--navy);
                    cursor: pointer;
                }
                .title {
                    margin: 0;
                    color: var(--navy);
                    font-weight: 700;
                    font-size: 24px;
                }
            </style>
            
            <div class="header-container">
                <div class="back-icon">&lt;</div>
                <h2 class="title">Settings</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # الأزرار
        if st.button("🔒 Change Password" + " " * 30 + "›"): 
            nav_settings('change_password_page')
            
        if st.button("🌐 Change Language" + " " * 30 + "›"): 
            nav_settings('language_page')
            
        if st.button("⭐ Rate App" + " " * 45 + "›"): 
            nav_settings('rate_page')
            
        if st.button("🚪 Log Out" + " " * 45 + "›"): 
            nav_settings('logout_page')
        
        st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem ›"): 
                nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs      ›"): 
                nav_settings('contact_page')
    # ب. صفحة تغيير كلمة المرور
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back", key="back_pass", help="hidden"): nav_settings('main_menu')
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
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 35px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; transition: transform 0.2s; }
                .back-icon:active { transform: scale(0.8); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .input-capsule { background: white; border-radius: 100px; padding: 12px 18px; margin-bottom: 15px; display: flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: transform 0.2s; }
                .input-capsule:focus-within { transform: scale(1.02); }
                .input-capsule i.field-icon { color: #0f2446; margin-right: 12px; font-size: 16px; }
                .input-capsule input { border: none; outline: none; flex-grow: 1; font-size: 14px; color: #0f2446; background: transparent; }
                .toggle-eye { color: #ccc; cursor: pointer; margin-left: 10px; transition: 0.2s; }
                .toggle-eye:active { transform: scale(0.7); color: #0f2446; }
                .report-text { text-align: center; color: white; font-size: 14px; margin: 10px 0 20px 0; cursor: pointer; font-weight: bold; text-shadow: 0px 1px 2px rgba(0,0,0,0.1); transition: 0.2s; }
                .report-text:active { opacity: 0.6; transform: scale(0.95); }
                .save-box { background: white; border-radius: 100px; width: 100%; padding: 15px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; transition: 0.3s; border: none; color: #0f2446; font-weight: bold; font-size: 18px; margin-top: auto; }
                .save-box:active { transform: scale(0.95); background: #f9f9f9; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_pass]').click()">&lt;</div>
                    <h2 class="title">Change Password</h2>
                </div>
                <div class="input-capsule"><i class="fas fa-lock field-icon"></i><input type="password" placeholder="Current Password"><i class="fas fa-eye-slash toggle-eye"></i></div>
                <div class="input-capsule"><i class="fas fa-lock field-icon"></i><input type="password" placeholder="New Password"><i class="fas fa-eye-slash toggle-eye"></i></div>
                <div class="input-capsule"><i class="fas fa-lock field-icon"></i><input type="password" placeholder="Re-write New Password"><i class="fas fa-eye-slash toggle-eye"></i></div>
                <div class="report-text">Report Password</div>
                <button class="save-box" onclick="alert('Password Saved!')">Save</button>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تغيير اللغة
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
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; transition: transform 0.2s ease; }
                .back-icon:active { transform: scale(0.7); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .language-capsule { 
                    background: white; border-radius: 100px; padding: 15px 25px; margin-bottom: 15px; 
                    display: flex; align-items: center; justify-content: space-between; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; 
                    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
                }
                .language-capsule:active { transform: scale(0.95); box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
                .left-content { display: flex; align-items: center; gap: 12px; }
                .icon { color: #0f2446; font-size: 18px; transition: transform 0.3s ease; }
                .language-capsule:active .icon { transform: rotate(20deg) scale(1.2); }
                .label { color: #0f2446; font-weight: 700; font-size: 14px; }
                .status-mark { font-size: 18px; font-weight: bold; transition: transform 0.3s ease; }
                .language-capsule:active .status-mark { transform: translateX(5px); }
                .check { color: #2f80ed; } 
                .arrow-icon { color: #0f2446; font-size: 18px; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_lang]').click()">&lt;</div>
                    <h2 class="title">Language</h2>
                </div>
                <div class="language-capsule" onclick="alert('English Selected')">
                    <div class="left-content">
                        <div class="icon"><i class="fas fa-globe"></i></div>
                        <div class="label">English</div>
                    </div>
                    <div class="status-mark check"><i class="fas fa-check"></i></div>
                </div>
                <div class="language-capsule" onclick="alert('العربية مختارة')">
                    <div class="left-content">
                        <div class="icon"><i class="fas fa-globe"></i></div>
                        <div class="label">العربية</div>
                    </div>
                    <div class="status-mark"><span class="arrow-icon">&gt;</span></div>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # د. صفحة الإبلاغ عن مشكلة
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
                    width: 330px;
                    background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
                    border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px;
                    display: flex; flex-direction: column;
                }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 30px; position: relative; }
                .back-icon { 
                    position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; 
                    cursor: pointer; transition: all 0.3s ease; 
                }
                .back-icon:hover { transform: translateX(-5px); }
                .back-icon:active { transform: scale(0.7); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                
                textarea { 
                    width: 100%; height: 200px; border-radius: 35px; border: none; 
                    padding: 20px; box-sizing: border-box; resize: none; margin-bottom: 20px;
                    font-family: inherit; font-size: 14px; outline: none;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
                }
                
                .send-btn { 
                    background: white; border-radius: 100px; padding: 15px 25px; 
                    display: flex; justify-content: space-between; align-items: center; 
                    cursor: pointer; border: none; width: 100%; margin-top: auto;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: all 0.3s ease;
                }
                .send-btn:hover { transform: translateY(-3px); }
                .send-btn:active { transform: scale(0.96); }
                
                .main-icon { color: #808080; font-size: 18px; transition: all 0.4s ease; }
                .send-btn:hover .main-icon { transform: translate(5px, -5px); color: #2f80ed; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_report]').click()">&lt;</div>
                    <h2 class="title">Report</h2>
                </div>
                <textarea placeholder="I need help..."></textarea>
                <button class="send-btn" onclick="alert('Sent!')">
                    <i class="fas fa-paper-plane main-icon"></i>
                    <span style="color:#0f2446; font-weight:bold">Send Report</span>
                </button>
            </div>
        </body>
        </html>
        """, height=550)

    # هـ. صفحة اتصل بنا (تم التحديث كما هو مطلوب)
    elif st.session_state.settings_sub_page == 'contact_page':
        if st.button("Back", key="back_contact", help="hidden"): nav_settings('main_menu')
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
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 45px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; transition: all 0.3s ease; }
                .back-icon:hover { transform: translateX(-5px); }
                .back-icon:active { transform: scale(0.7); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .capsule {
                    background: white; border-radius: 100px; padding: 18px 25px; margin-bottom: 20px;
                    display: flex; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.06);
                    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); cursor: pointer;
                }
                .capsule:hover { transform: translateY(-6px) scale(1.03); box-shadow: 0 12px 20px rgba(15, 36, 70, 0.15); }
                .icon { margin-right: 18px; color: #0f2446; font-size: 19px; width: 25px; display: flex; justify-content: center; }
                .text { color: #0f2446; font-weight: 700; font-size: 15px; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_contact]').click()">&lt;</div>
                    <h2 class="title">Contact Us</h2>
                </div>
                <div class="capsule" onclick="window.location.href='mailto:CoCare26@gmail.com'">
                    <div class="icon"><i class="fas fa-envelope"></i></div>
                    <div class="text">CoCare26@gmail.com</div>
                </div>
                <div class="capsule" onclick="window.location.href='tel:+962791234567'">
                    <div class="icon"><i class="fas fa-phone-alt"></i></div>
                    <div class="text">+962 79 123 4567</div>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

    # و. صفحة تسجيل الخروج
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

    # ز. صفحة التقييم
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
                    width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
                    border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px; display: flex; flex-direction: column;
                }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; transition: transform 0.2s ease; }
                .back-icon:active { transform: scale(0.7); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }

                .store-item { 
                    background: white; border-radius: 100px; padding: 14px 22px; margin-bottom: 15px; 
                    display: flex; align-items: center; justify-content: space-between; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; 
                    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
                }
                .store-item:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.1); }
                .store-item:active { transform: scale(0.96); }

                .store-item-left { display: flex; align-items: center; gap: 15px; }
                .store-item-icon { font-size: 18px; color: #0f2446; transition: transform 0.4s ease; }
                .store-item:hover .store-item-icon { transform: scale(1.2) rotate(10deg); color: #2f80ed; }
                .store-item-text { font-weight: 700; color: #0f2446; font-size: 14px; }
                .store-item-arrow { font-size: 18px; font-weight: bold; color: #0f2446; transition: transform 0.3s ease; }
                .store-item:hover .store-item-arrow { transform: translateX(5px); }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_rate]').click()">&lt;</div>
                    <h2 class="title">Rate App</h2>
                </div>
                <div class="store-item" onclick="window.open('https://play.google.com', '_blank')">
                    <div class="store-item-left">
                        <span class="store-item-icon"><i class="fab fa-google-play"></i></span>
                        <span class="store-item-text">Google Play Store</span>
                    </div>
                    <span class="store-item-arrow">&gt;</span>
                </div>
                <div class="store-item" onclick="window.open('https://apps.apple.com', '_blank')">
                    <div class="store-item-left">
                        <span class="store-item-icon"><i class="fab fa-apple"></i></span>
                        <span class="store-item-text">Apple App Store</span>
                    </div>
                    <span class="store-item-arrow">&gt;</span>
                </div>
                <div class="store-item" onclick="window.open('https://appgallery.huawei.com', '_blank')">
                    <div class="store-item-left">
                        <span class="store-item-icon"><i class="fas fa-mobile-alt"></i></span>
                        <span class="store-item-text">Huawei AppGallery</span>
                    </div>
                    <span class="store-item-arrow">&gt;</span>
                </div>
            </div>
        </body>
        </html>
        """, height=550)

else:
    st.title(f"Welcome to {selection} Page")
