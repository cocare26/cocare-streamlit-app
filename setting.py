import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Smart App Settings", layout="centered")

# 2. إدارة الحالة للتنقل الداخلي
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

def nav_settings(target):
    st.session_state.settings_sub_page = target
    st.rerun()

# 3. التنسيق الجمالي العام (تعديل الألوان والـ block-container)
st.markdown("""
<style>
:root { 
    --navy: #0f2446; 
    --bg1: #d6ecff;
    --bg2: #bfe3ff;
    --bg3: #eaf6ff;
}

/* تعديل الـ Container الرئيسي ليصبح كالبطاقة */
.block-container {
    max-width: 350px !important;
    margin: auto;
    padding: 30px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
}

[data-testid="stAppViewContainer"] { background: #f0f2f6; }
[data-testid="stHeader"] {display: none !important;}

/* تنسيق الأزرار داخل صفحة الإعدادات */
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

/* إخفاء زر Back الافتراضي لستريمليت لأنه سيتم استدعاؤه برمجياً */
button[key^="back_"] {
    display: none !important;
}

/* تنسيق الهيدر المخصص */
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
""", unsafe_allow_html=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to:", ["setting", "Create Account", "Forgot Password", "To Do"])

# --- منطق عرض الصفحات ---

if selection == "setting":
    
    # ا. القائمة الرئيسية للإعدادات (تم التحديث للهيكل الجديد)
    if st.session_state.settings_sub_page == 'main_menu':
        # الهيدر الجديد مع سهم العودة
        st.markdown(f"""
            <div class="header-container">
                <div class="back-icon">&lt;</div>
                <h2 class="title">Settings</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # الأزرار
        if st.button("🔒 Change Password" + " "*30 + "›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language" + " "*30 + "›"): nav_settings('language_page')
        if st.button("⭐ Rate App" + " "*45 + "›"): nav_settings('rate_page')
        if st.button("🚪 Log Out" + " "*45 + "›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\n a Problem ›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs      ›"): nav_settings('contact_page')

    # ب. صفحة تغيير كلمة المرور (الحفاظ على الكود القديم مع تحديث الهيدر)
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back", key="back_pass"): nav_settings('main_menu')
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: transparent; margin: 0; display: flex; justify-content: center; }
                .main-wrapper { width: 330px; border-radius: 42px; padding: 10px; box-sizing: border-box; height: 450px; display: flex; flex-direction: column; }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 35px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .input-capsule { background: white; border-radius: 100px; padding: 12px 18px; margin-bottom: 15px; display: flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
                .input-capsule input { border: none; outline: none; flex-grow: 1; font-size: 14px; color: #0f2446; background: transparent; }
                .save-box { background: white; border-radius: 100px; width: 100%; padding: 15px; text-align: center; border: none; color: #0f2446; font-weight: bold; font-size: 18px; margin-top: auto; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="main-wrapper">
                <div class="header-container">
                    <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_pass]').click()">&lt;</div>
                    <h2 class="title">Change Password</h2>
                </div>
                <div class="input-capsule"><input type="password" placeholder="Current Password"></div>
                <div class="input-capsule"><input type="password" placeholder="New Password"></div>
                <div class="input-capsule"><input type="password" placeholder="Re-write New Password"></div>
                <button class="save-box" onclick="alert('Password Saved!')">Save</button>
            </div>
        </body>
        </html>
        """, height=480)

    # ج. صفحة تغيير اللغة (الحفاظ على الكود القديم)
    elif st.session_state.settings_sub_page == 'language_page':
        if st.button("Back", key="back_lang"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .wrapper { width: 330px; padding: 10px; height: 450px; display: flex; flex-direction: column; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .lang-card { background: white; border-radius: 100px; padding: 15px 25px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); color: #0f2446; font-weight: bold; }
        </style>
        <div class="wrapper">
            <div class="header">
                <div class="back" onclick="parent.window.document.querySelector('button[key=back_lang]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0">Language</h2>
            </div>
            <div class="lang-card"><span>English</span><span style="color:#2f80ed">✔</span></div>
            <div class="lang-card"><span>العربية</span><span>&gt;</span></div>
        </div>
        """, height=480)

    # د. صفحة الإبلاغ
    elif st.session_state.settings_sub_page == 'report_page':
        if st.button("Back", key="back_report"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 25px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            textarea { width: 100%; height: 200px; border-radius: 30px; border: none; padding: 20px; box-sizing: border-box; outline: none; margin-bottom: 20px; }
            .send-btn { background: white; border-radius: 100px; padding: 15px; text-align: center; font-weight: bold; color: #0f2446; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }
        </style>
        <div class="header">
            <div class="back" onclick="parent.window.document.querySelector('button[key=back_report]').click()">&lt;</div>
            <h2 style="color:#0f2446; margin:0">Report</h2>
        </div>
        <textarea placeholder="How can we help?"></textarea>
        <div class="send-btn" onclick="alert('Sent!')">Send Report</div>
        """, height=480)

    # هـ. صفحة اتصل بنا
    elif st.session_state.settings_sub_page == 'contact_page':
        if st.button("Back", key="back_contact"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 45px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .capsule { background: white; border-radius: 100px; padding: 18px 25px; margin-bottom: 20px; display: flex; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.06); color: #0f2446; font-weight: bold; }
        </style>
        <div class="header">
            <div class="back" onclick="parent.window.document.querySelector('button[key=back_contact]').click()">&lt;</div>
            <h2 style="color:#0f2446; margin:0">Contact Us</h2>
        </div>
        <div class="capsule">✉️ CoCare26@gmail.com</div>
        <div class="capsule">📞 +962 79 123 4567</div>
        """, height=480)

    # و. تسجيل الخروج
    elif st.session_state.settings_sub_page == 'logout_page':
        if st.button("Back", key="back_logout"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; text-align: center; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 60px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; }
            .btn { width: 100%; padding: 15px; border-radius: 100px; background: white; margin-bottom: 15px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        </style>
        <div class="header">
            <div class="back" onclick="parent.window.document.querySelector('button[key=back_logout]').click()"><</div>
            <h2 style="color:#0f2446; margin:0">Log Out</h2>
        </div>
        <p style="color:#0f2446; font-weight:bold; margin-bottom:40px">Are you sure you want to log out?</p>
        <div class="btn" style="color:#eb5757">Log Out</div>
        <div class="btn" style="color:#0f2446" onclick="parent.window.document.querySelector('button[key=back_logout]').click()">Cancel</div>
        """, height=480)

    # ز. التقييم
    elif st.session_state.settings_sub_page == 'rate_page':
        if st.button("Back", key="back_rate"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .item { background: white; border-radius: 100px; padding: 15px 25px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); color: #0f2446; font-weight: bold; }
        </style>
        <div class="header">
            <div class="back" onclick="parent.window.document.querySelector('button[key=back_rate]').click()">&lt;</div>
            <h2 style="color:#0f2446; margin:0">Rate App</h2>
        </div>
        <div class="item"><span>Google Play</span><span>&gt;</span></div>
        <div class="item"><span>App Store</span><span>&gt;</span></div>
        """, height=480)

else:
    st.title(f"Welcome to {selection} Page")
