import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة الموحدة
st.set_page_config(page_title="Settings App", layout="centered")

# 2. نظام إدارة التنقل (للتنقل بين الواجهات)
if 'page' not in st.session_state:
    st.session_state.page = 'main_settings'

# دالة لتغيير الصفحة وإعادة التشغيل
def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 3. تنسيق CSS الموحد للخلفية (ليظهر في كل الصفحات)
st.markdown("""
<style>
:root{ --navy:#0f2446; --bg1:#d6ecff; --bg2:#bfe3ff; --bg3:#eaf6ff; }
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
.block-container{
    max-width:350px !important; margin:auto !important; padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px; box-shadow:0 15px 35px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# 4. دالة لاستقبال الإشارات من HTML إلى Streamlit
def html_bridge(html_code, height=500):
    return components.html(f"""
        {html_code}
        <script>
        function goPage(p) {{
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                value: p
            }}, '*');
        }}
        </script>
    """, height=height)

# --- منطق عرض الصفحات ---

# أ. الواجهة الرئيسية (Settings)
if st.session_state.page == 'main_settings':
    selection = html_bridge("""
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{ font-family:'Segoe UI', sans-serif; margin:0; background:transparent; display:flex; justify-content:center; }
        .main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
        .header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; }
        .title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
        .setting-item{ background:white; border-radius:100px; padding:14px 18px; margin-bottom:15px; display:flex; align-items:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; }
        .setting-item i.left-icon{ color:#0f2446; font-size:16px; margin-right: auto; }
        .setting-text-right{ font-size:14px; font-weight:600; color:#0f2446; margin-right: 10px; }
        .arrow{ color:#0f2446; font-weight:bold; font-size: 18px; }
    </style>
    </head>
    <body>
    <div class="main-wrapper">
        <div class="header-container"><h2 class="title">Settings</h2></div>
        
        <!-- عند الضغط نرسل كلمة 'change_password_page' لبايثون -->
        <div class="setting-item" onclick="goPage('change_password_page')">
            <i class="fas fa-lock left-icon"></i>
            <span class="setting-text-right">Change Password</span>
            <span class="arrow">›</span>
        </div>

        <div class="setting-item" onclick="goPage('change_language_page')">
            <i class="fas fa-globe left-icon"></i>
            <span class="setting-text-right">Change Language</span>
            <span class="arrow">›</span>
        </div>
    </div>
    </body>
    </html>
    """)
    if selection: navigate_to(selection)

# ب. واجهة تغيير كلمة المرور (Change Password)
elif st.session_state.page == 'change_password_page':
    selection = html_bridge("""
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body{ font-family:'Segoe UI', sans-serif; background:transparent; margin:0; display:flex; justify-content:center; }
        .main-wrapper{ width:100%; max-width:290px; display:flex; flex-direction:column; height:480px; }
        .header-container{ display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; }
        .back-icon{ position:absolute; left:0; font-size:28px; font-weight:bold; color:#0f2446; cursor:pointer; }
        .title{ margin:0; font-weight:900; font-size:20px; color:#0f2446; }
        .input-capsule{ background:white; border-radius:100px; padding:10px 18px; margin-bottom:15px; display:flex; align-items:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); }
        .input-capsule input{ border:none; outline:none; flex-grow:1; font-size:14px; color:#0f2446; background:transparent; }
        .save-btn{ background:white; border-radius:100px; width:100%; padding:12px; margin-top:auto; font-weight:bold; color:#0f2446; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.08); }
    </style>
    </head>
    <body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon" onclick="goPage('main_settings')">&lt;</div>
            <h2 class="title">Change Password</h2>
        </div>
        <div class="input-capsule"><input type="password" placeholder="Current Password"></div>
        <div class="input-capsule"><input type="password" placeholder="New Password"></div>
        <div class="input-capsule"><input type="password" placeholder="Confirm Password"></div>
        <button class="save-btn" onclick="alert('Password Updated!'); goPage('main_settings')">Save</button>
    </div>
    </body>
    </html>
    """)
    if selection: navigate_to(selection)
