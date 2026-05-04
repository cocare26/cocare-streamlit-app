# --- منطق عرض الصفحات ---

if selection == "setting":
    
    # ا. القائمة الرئيسية للإعدادات
    if st.session_state.settings_sub_page == 'main_menu':
        st.markdown('<div class="settings-card">', unsafe_allow_html=True)
        
        # العنوان مع سهم العودة في أقصى اليسار
        st.markdown("""
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 25px; position: relative;">
                <div style="position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer;">
                    &lt;
                </div>
                <h2 style="margin: 0; color:#0f2446; font-weight: 700;">Settings</h2>
            </div>
        """, unsafe_allow_html=True)
        
        # أزرار القائمة الرئيسية
        if st.button("🔒 Change Password                                 ›"): nav_settings('change_password_page')
        if st.button("🌐 Change Language                                 ›"): nav_settings('language_page')
        if st.button("⭐ Rate App                                         ›"): nav_settings('rate_page')
        if st.button("🚪 Log Out                                         ›"): nav_settings('logout_page')
        
        st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)
        
        # أزرار الصف السفلي (Report & Contact)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("⚠️ Report\nProblem   ›"): nav_settings('report_page')
        with col2:
            if st.button("✉️ Contact\nUs             ›"): nav_settings('contact_page')
            
        st.markdown('</div>', unsafe_allow_html=True)

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
                .label { color: #0f2446; font-weight: 700; font-size: 14px; }
                .status-mark { font-size: 18px; font-weight: bold; }
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
                    width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
                    border-radius: 42px; padding: 30px; box-sizing: border-box; height: 500px; display: flex; flex-direction: column;
                }
                .header-container { display: flex; align-items: center; justify-content: center; margin-bottom: 30px; position: relative; }
                .back-icon { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
                .title { margin: 0; font-weight: 900; font-size: 20px; color: #0f2446; }
                textarea { 
                    width: 100%; height: 200px; border-radius: 35px; border: none; padding: 20px; box-sizing: border-box; 
                    resize: none; margin-bottom: 20px; font-family: inherit; outline: none; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
                }
                .send-btn { 
                    background: white; border-radius: 100px; padding: 15px; display: flex; justify-content: space-between; 
                    align-items: center; cursor: pointer; border: none; width: 100%; margin-top: auto; box-shadow: 0 4px 12px rgba(0,0,0,0.08);
                }
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
                    <i class="fas fa-paper-plane" style="color: #2f80ed"></i>
                    <span style="color:#0f2446; font-weight:bold">Send Report</span>
                </button>
            </div>
        </body>
        </html>
        """, height=550)

    # هـ. صفحة اتصل بنا
    elif st.session_state.settings_sub_page == 'contact_page':
        if st.button("Back", key="back_contact", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; box-sizing: border-box; display: flex; flex-direction: column; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 45px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .capsule { background: white; border-radius: 100px; padding: 18px 25px; margin-bottom: 20px; display: flex; align-items: center; box-shadow: 0 4px 15px rgba(0,0,0,0.06); cursor: pointer; }
            .text { color: #0f2446; font-weight: 700; font-size: 15px; margin-left: 15px; }
        </style>
        <div class="wrapper">
            <div class="header">
                <div class="back" onclick="parent.window.document.querySelector('button[key=back_contact]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0">Contact Us</h2>
            </div>
            <div class="capsule" onclick="window.location.href='mailto:CoCare26@gmail.com'">
                <span style="color:#0f2446">✉️</span>
                <div class="text">CoCare26@gmail.com</div>
            </div>
            <div class="capsule" onclick="window.location.href='tel:+962791234567'">
                <span style="color:#0f2446">📞</span>
                <div class="text">+962 79 123 4567</div>
            </div>
        </div>
        """, height=550)

    # و. صفحة تسجيل الخروج
    elif st.session_state.settings_sub_page == 'logout_page':
        if st.button("Back", key="back_logout", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .card { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; display: flex; flex-direction: column; align-items: center; box-sizing: border-box;}
            .header { width: 100%; display: flex; align-items: center; justify-content: center; margin-bottom: 60px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; cursor: pointer; color: #0f2446; font-weight: bold; }
            .btn { width: 100%; padding: 15px; border-radius: 100px; background: white; margin-bottom: 15px; cursor: pointer; font-weight: bold; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
        </style>
        <div class="card">
            <div class="header"><div class="back" onclick="parent.window.document.querySelector('button[key=back_logout]').click()"><</div><h2 style="color:#0f2446; margin:0">Log Out</h2></div>
            <p style="color:#0f2446; font-weight:bold; margin-bottom:40px; text-align:center">Are you sure you want to log out?</p>
            <div class="btn" style="color:#eb5757" onclick="alert('Logged Out!')">Log Out</div>
            <div class="btn" style="color:#0f2446" onclick="parent.window.document.querySelector('button[key=back_logout]').click()">Cancel</div>
        </div>
        """, height=550)

    # ز. صفحة التقييم
    elif st.session_state.settings_sub_page == 'rate_page':
        if st.button("Back", key="back_rate", help="hidden"): nav_settings('main_menu')
        components.html("""
        <style>
            body { font-family: 'Segoe UI'; background: transparent; display: flex; justify-content: center; }
            .wrapper { width: 330px; background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); border-radius: 42px; padding: 30px; height: 500px; box-sizing: border-box; display: flex; flex-direction: column; }
            .header { display: flex; align-items: center; justify-content: center; margin-bottom: 40px; position: relative; }
            .back { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: #0f2446; cursor: pointer; }
            .item { background: white; border-radius: 100px; padding: 15px 25px; margin-bottom: 15px; display: flex; align-items: center; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.08); cursor: pointer; }
            .text { font-weight: 700; color: #0f2446; font-size: 14px; }
        </style>
        <div class="wrapper">
            <div class="header">
                <div class="back" onclick="parent.window.document.querySelector('button[key=back_rate]').click()">&lt;</div>
                <h2 style="color:#0f2446; margin:0">Rate App</h2>
            </div>
            <div class="item" onclick="window.open('https://play.google.com')"><span>📱 Google Play</span><span style="font-weight:bold">&gt;</span></div>
            <div class="item" onclick="window.open('https://apps.apple.com')"><span>🍎 App Store</span><span style="font-weight:bold">&gt;</span></div>
            <div class="item" onclick="window.open('https://appgallery.huawei.com')"><span>🏢 AppGallery</span><span style="font-weight:bold">&gt;</span></div>
        </div>
        """, height=550)

else:
    st.title(f"Welcome to {selection} Page")
