import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الموحدة
st.set_page_config(page_title="App Settings", layout="centered")

# 2. نظام إدارة التنقل (Navigation System)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

# دالة لتغيير الصفحة وإعادة تشغيل التطبيق
def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 3. تنسيق CSS الموحد للخلفية والحاوية (نفس التصميم لكل الصفحات)
st.markdown("""
<style>
:root{ --navy:#0f2446; --bg1:#d6ecff; --bg2:#bfe3ff; --bg3:#eaf6ff; }
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
.block-container{
    max-width:350px !important; margin:auto !important; padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px; box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
/* إخفاء عناصر ستريمليت الزائدة */
#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 4. دالة سحرية للربط بين HTML و Python
def create_html_component(html_content, height=500):
    # نستخدم postMessage لإرسال اسم الصفحة من JavaScript إلى Python
    response = components.html(f"""
        {html_content}
        <script>
        function sendPage(pageName) {{
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                value: pageName
            }}, '*');
        }}
        // تعديل وظائف الـ onclick في الكود الأصلي لتستخدم sendPage
        document.querySelectorAll('[onclick^="goPage"]').forEach(el => {{
            const match = el.getAttribute('onclick').match(/'([^']+)'/);
            if(match) el.onclick = () => sendPage(match[1]);
        }});
        </script>
    """, height=height)
    return response

# --- منطق عرض الصفحات ---

# أ. الصفحة الرئيسية (Settings)
if st.session_state.page == 'main' or st.session_state.page == 'settings':
    selection = create_html_component("""
    <html>
    <head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{ font-family:'Segoe UI', sans-serif; margin:0; display:flex; justify-content:center; background:transparent; }
        .main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
        .header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; }
        .title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
        .setting-item{ background:white; border-radius:100px; padding:14px 18px; margin-bottom:15px; display:flex; align-items:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; transition:0.3s; }
        .setting-item i.left-icon{ color:#0f2446; font-size:16px; margin-right: auto; }
        .setting-text-right{ font-size:14px; font-weight:600; color:#0f2446; margin-right: 10px; }
        .setting-item .arrow{ color:#0f2446; font-weight:bold; font-size: 18px; }
        .bottom-row{ margin-top:auto; display:flex; gap:10px; }
        .bottom-row .setting-item{ flex:1; padding:12px 14px; justify-content: space-between; }
        .bottom-row .setting-text{ flex:1; text-align:left; margin-left:15px; font-size:13px; font-weight:600; color:#0f2446; }
    </style>
    </head>
    <body>
    <div class="main-wrapper">
        <div class="header-container"><h2 class="title">Settings</h2></div>
        <div class="setting-item" onclick="goPage('Change_password')"><i class="fas fa-lock left-icon"></i><span class="setting-text-right">Change Password</span><span class="arrow">›</span></div>
        <div class="setting-item" onclick="goPage('Change_language')"><i class="fas fa-globe left-icon"></i><span class="setting-text-right">Change Language</span><span class="arrow">›</span></div>
        <div class="setting-item" onclick="goPage('Rate_app')"><i class="fas fa-star left-icon"></i><span class="setting-text-right">Rate App</span><span class="arrow">›</span></div>
        <div class="bottom-row">
            <div class="setting-item" onclick="goPage('Report_Problem')"><i class="fas fa-exclamation-triangle"></i><span class="setting-text">Report</span><span class="arrow">›</span></div>
            <div class="setting-item" onclick="goPage('Contact_Us')"><i class="fas fa-envelope"></i><span class="setting-text">Contact</span><span class="arrow">›</span></div>
        </div>
    </div>
    </body></html>
    """)
    if selection: navigate_to(selection)

# ب. صفحة تغيير كلمة المرور
elif st.session_state.page == 'Change_password':
    selection = create_html_component("""
    <html>
    <head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{ font-family:'Segoe UI', sans-serif; background:transparent; margin:0; display:flex; justify-content:center; }
        .main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
        .header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; }
        .back-icon{ position:absolute; left:0; font-size:28px; font-weight:bold; color:#0f2446; cursor:pointer; }
        .title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
        .input-capsule{ background:white; border-radius:100px; padding:10px 18px; margin-bottom:15px; display:flex; align-items:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); }
        .input-capsule input{ border:none; outline:none; flex-grow:1; font-size:14px; background:transparent; }
        .save-box{ background:white; border-radius:100px; width:100%; padding:12px; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; border:none; margin-top:auto; font-weight:bold; color:#0f2446; }
    </style>
    </head>
    <body>
    <div class="main-wrapper">
        <div class="header-container"><div class="back-icon" onclick="goPage('main')">&lt;</div><h2 class="title">Password</h2></div>
        <div class="input-capsule"><input type="password" placeholder="Current Password"></div>
        <div class="input-capsule"><input type="password" placeholder="New Password"></div>
        <div class="input-capsule"><input type="password" placeholder="Confirm Password"></div>
        <button class="save-box" onclick="alert('Saved!'); goPage('main')">Save</button>
    </div>
    </body></html>
    """)
    if selection: navigate_to(selection)

# ج. صفحة تغيير اللغة
elif st.session_state.page == 'Change_language':
    selection = create_html_component("""
    <html>
    <head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{ font-family:'Segoe UI', sans-serif; background:transparent; margin:0; display:flex; justify-content:center; }
        .main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
        .header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:40px; position:relative; }
        .back-icon{ position:absolute; left:0; font-size:28px; font-weight:bold; color:#0f2446; cursor:pointer; }
        .title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
        .language-capsule{ background:white; border-radius:100px; padding:14px 22px; margin-bottom:15px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; }
        .label{ color:#0f2446; font-weight:700; font-size:14px; }
        .check{ color:#2f80ed; }
    </style>
    </head>
    <body>
    <div class="main-wrapper">
        <div class="header-container"><div class="back-icon" onclick="goPage('main')">&lt;</div><h2 class="title">Language</h2></div>
        <div class="language-capsule" onclick="goPage('main')"><span class="label">English</span><i class="fas fa-check check"></i></div>
        <div class="language-capsule" onclick="goPage('main')"><span class="label">العربية</span><span style="color:#0f2446">></span></div>
    </div>
    </body></html>
    """)
    if selection: navigate_to(selection)

# د. صفحة التقييم (Rate App)
elif st.session_state.page == 'Rate_app':
    selection = create_html_component("""
    <html>
    <head><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{ font-family:'Segoe UI', sans-serif; background:transparent; margin:0; display:flex; justify-content:center; }
        .main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
        .header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:40px; position:relative; }
        .back-icon{ position:absolute; left:0; font-size:28px; font-weight:bold; color:#0f2446; cursor:pointer; }
        .title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
        .store-item{ background:white; border-radius:100px; padding:14px 22px; margin-bottom:15px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; }
        .store-item-text{ font-weight:700; color:#0f2446; font-size:14px; }
    </style>
    </head>
    <body>
    <div class="main-wrapper">
        <div class="header-container"><div class="back-icon" onclick="goPage('main')">&lt;</div><h2 class="title">Rate App</h2></div>
        <div class="store-item" onclick="window.open('https://play.google.com')"><span class="store-item-text">Google Play</span><span>›</span></div>
        <div class="store-item" onclick="window.open('https://apps.apple.com')"><span class="store-item-text">App Store</span><span>›</span></div>
    </div>
    </body></html>
    """)
    if selection: navigate_to(selection)
