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

# 3. التنسيق الجمالي (تعديل الألوان والـ block-container فقط)
st.markdown("""
<style>
:root { 
    --navy: #0f2446; 
    --bg1: #d6ecff;
    --bg2: #bfe3ff;
    --bg3: #eaf6ff;
}

/* تعديل الـ Container الرئيسي حسب طلبك */
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

/* تنسيق أزرار ستريمليت في القائمة الرئيسية */
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

/* إخفاء أزرار Back الخاصة بـ ستريمليت */
button[key^="back_"] {
    display: none !important;
}
</style>
""", unsafe_allow_html=True)

# 4. القائمة الجانبية
with st.sidebar:
    st.title("Navigation")
    selection = st.radio("Go to:", ["setting", "Create Account", "Forgot Password", "To Do"])

# --- منطق عرض الصفحات ---

if selection == "setting":
    
    # ا. القائمة الرئيسية للإعدادات (تم إضافة الهيدر المطلوب هنا)
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown("""
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 25px; position: relative;">
                <div style="position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer;">&lt;</div>
                <h2 style="margin: 0; color:#0f2446; font-weight: 700;">Settings</h2>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔒 Change Password" + " "*30 + "›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language" + " "*30 + "›"): nav_settings('language_page')
        if st.button("⭐ Rate App" + " "*45 + "›"): nav_settings('rate_page')
        if st.button("🚪 Log Out" + " "*45 + "›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem ›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs      ›"): nav_settings('contact_page')

    # ب. باقي الصفحات (رجعت كودك الأصلي كما هو بدون أي تعديل داخلي)
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back", key="back_pass"): nav_settings('main_menu')
        components.html("""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body { font-family: 'Segoe UI', sans-serif; background: transparent; margin: 0; display: flex; justify-content: center; }
                .main-wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px; display: flex; flex-direction: column; }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 35px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; transition: transform 0.2s; }
                .back-icon:active { transform: scale(0.8); }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                .input-capsule { background: white; border-radius: 100px; padding: 12px 18px; margin-bottom: 15px; display: flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); transition: transform 0.2s; }
                .input-capsule i.field-icon { color: #0f2446; margin-right: 12px; font-size: 16px; }
                .input-capsule input { border: none; outline: none; flex-grow: 1; font-size: 14px; color: #0f2446; background: transparent; }
                .toggle-eye { color: #ccc; cursor: pointer; margin-left: 10px; transition: 0.2s; }
                .save-box { background: white; border-radius: 100px; width: 100%; padding: 15px; text-align: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; transition: 0.3s; border: none; color: #0f2446; font-weight: bold; font-size: 18px; margin-top: auto; }
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
                <button class="save-box" onclick="alert('Password Saved!')">Save</button>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة اللغة (كودك الأصلي)
    elif st.session_state.settings_sub_page == 'language_page':
        if st.button("Back", key="back_lang"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .main-wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px; display: flex; flex-direction: column; }
            .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .language-capsule { background: white; border-radius: 100px; padding: 15px 25px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; }
            .label { color: #0f2446; font-weight: 700; font-size: 14px; }
        </style>
        <div class="main-wrapper">
            <div class="header-container">
                <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_lang]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0; font-size:20px;">Language</h2>
            </div>
            <div class="language-capsule">
                <div class="label">English</div>
                <div style="color: #2f80ed;">✔</div>
            </div>
            <div class="language-capsule">
                <div class="label">العربية</div>
                <div style="color: #0f2446;">&gt;</div>
            </div>
        </div>
        """, height=550)

    # د. صفحة الإبلاغ (كودك الأصلي)
    elif st.session_state.settings_sub_page == 'report_page':
        if st.button("Back", key="back_report"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .main-wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; display: flex; flex-direction: column; box-sizing: border-box; }
            .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 30px; position: relative; }
            .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            textarea { width: 100%; height: 200px; border-radius: 35px; border: none; padding: 20px; box-sizing: border-box; outline: none; margin-bottom: 20px; }
            .send-btn { background: white; border-radius: 100px; padding: 15px; text-align: center; font-weight: bold; color: #0f2446; border: none; margin-top: auto; cursor: pointer; }
        </style>
        <div class="main-wrapper">
            <div class="header-container">
                <div class="back-icon" onclick="parent.window.document.querySelector('button[key=back_report]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0; font-size:20px;">Report</h2>
            </div>
            <textarea placeholder="I need help..."></textarea>
            <div class="send-btn" onclick="alert('Sent!')">Send Report</div>
        </div>
        """, height=550)

else:
    st.title(f"Welcome to {selection} Page")
