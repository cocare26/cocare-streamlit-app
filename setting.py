import streamlit as st
import streamlit.components.v1 as components

# 1. تهيئة حالة الجلسة (لضمان عدم ظهور Error عند التشغيل)
if 'settings_sub_page' not in st.session_state:
    st.session_state.settings_sub_page = 'main_menu'

# 2. دالة التنقل بين صفحات الإعدادات
def nav_settings(page_name):
    st.session_state.settings_sub_page = page_name
    st.rerun()

# 3. إضافة تنسيق CSS للأزرار الرئيسية (لجعلها ممتدة وبأيقونات متباعدة)
st.markdown("""
<style>
    /* تنسيق الحاوية الرئيسية */
    .settings-card {
        background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
        padding: 30px;
        border-radius: 40px;
        color: #0f2446;
    }
    
    /* تنسيق أزرار Streamlit لتصبح عريضة (Stretched) */
    div.stButton > button {
        width: 100%;
        border-radius: 100px !important;
        border: none !important;
        padding: 15px 20px !important;
        background-color: white !important;
        color: #0f2446 !important;
        font-weight: bold !important;
        text-align: left !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
        margin-bottom: 10px !important;
        display: flex;
        justify-content: space-between;
    }
    
    /* إخفاء أزرار Back الخاصة بـ Streamlit لأننا نستخدم سهم HTML */
    button[key^="back_"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# 4. محاكاة قائمة اختيار الصفحات (Sidebar)
selection = st.sidebar.selectbox("Go to", ["setting", "home", "profile"])

# 5. منطق عرض صفحة الإعدادات
if selection == "setting":
    
    # ا. القائمة الرئيسية للإعدادات
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        
        # العنوان مع سهم العودة في أقصى اليسار
        st.markdown("""
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 25px; position: relative;">
                <div style="position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer;" onclick="window.parent.location.reload();">
                    &lt;
                </div>
                <h2 style="margin: 0; color:#0f2446; font-weight: 700;">Settings</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # أزرار القائمة (لاحظ المسافات لضمان دفع السهم لليمين)
        if st.button("🔒 Change Password" + "&nbsp;"*40 + "›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language" + "&nbsp;"*40 + "›"): nav_settings('language_page')
        if st.button("⭐ Rate App" + "&nbsp;"*52 + "›"): nav_settings('rate_page')
        if st.button("🚪 Log Out" + "&nbsp;"*53 + "›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem" + "&nbsp;"*5 + "›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs" + "&nbsp;"*12 + "›"): nav_settings('contact_page')
            
        st.markdown('</div>', unsafe_allow_html=True)

    # ب. صفحة تغيير كلمة المرور
    elif st.session_state.settings_sub_page == 'change_password_page':
        if st.button("Back", key="back_pass"): nav_settings('main_menu')
        components.html(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
            <style>
                body {{ font-family: 'Segoe UI'; background: transparent; margin: 0; display: flex; justify-content: center; }}
                .wrapper {{ width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px; display: flex; flex-direction: column; }}
                .header {{ display: flex; align-items: center; justify-content: center; margin-bottom: 35px; position: relative; }}
                .back {{ position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }}
                .input-box {{ background: white; border-radius: 100px; padding: 12px 18px; margin-bottom: 15px; display: flex; align-items: center; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }}
                .input-box input {{ border: none; outline: none; flex-grow: 1; font-size: 14px; color: #0f2446; }}
                .save-btn {{ background: white; border-radius: 100px; width: 100%; padding: 15px; text-align: center; border: none; color: #0f2446; font-weight: bold; font-size: 18px; margin-top: auto; cursor: pointer; }}
            </style>
        </head>
        <body>
            <div class="wrapper">
                <div class="header">
                    <div class="back" onclick="parent.window.document.querySelector('button[key=back_pass]').click()">&lt;</div>
                    <h2 style="color:#0f2446; margin:0; font-size:20px;">Change Password</h2>
                </div>
                <div class="input-box"><i class="fas fa-lock" style="margin-right:10px"></i><input type="password" placeholder="Current Password"></div>
                <div class="input-box"><i class="fas fa-lock" style="margin-right:10px"></i><input type="password" placeholder="New Password"></div>
                <div class="input-box"><i class="fas fa-lock" style="margin-right:10px"></i><input type="password" placeholder="Re-write New Password"></div>
                <button class="save-btn">Save</button>
            </div>
        </body>
        </html>
        """, height=550)

    # ج. صفحة تغيير اللغة
    elif st.session_state.settings_sub_page == 'language_page':
        if st.button("Back", key="back_lang"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; box-sizing: border-box; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .lang-card { background: white; border-radius: 100px; padding: 15px 25px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); }
        </style>
        <div class="wrapper">
            <div class="header">
                <div class="back" onclick="parent.window.document.querySelector('button[key=back_lang]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0; font-size:20px;">Language</h2>
            </div>
            <div class="lang-card"><span style="font-weight:bold; color:#0f2446">English</span><span style="color:#2f80ed">✔</span></div>
            <div class="lang-card"><span style="font-weight:bold; color:#0f2446">العربية</span><span>&gt;</span></div>
        </div>
        """, height=550)

    # د. صفحة الإبلاغ (Report)
    elif st.session_state.settings_sub_page == 'report_page':
        if st.button("Back", key="back_report"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; display: flex; flex-direction: column; box-sizing: border-box; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 25px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            textarea { width: 100%; height: 200px; border-radius: 30px; border: none; padding: 20px; box-sizing: border-box; outline: none; margin-bottom: 20px; }
            .send-btn { background: white; border-radius: 100px; padding: 15px; text-align: center; font-weight: bold; color: #0f2446; border: none; margin-top: auto; cursor: pointer; }
        </style>
        <div class="wrapper">
            <div class="header">
                <div class="back" onclick="parent.window.document.querySelector('button[key=back_report]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0; font-size:20px;">Report</h2>
            </div>
            <textarea placeholder="How can we help?"></textarea>
            <div class="send-btn">Send Report</div>
        </div>
        """, height=550)

else:
    st.write("Main Page Content")
