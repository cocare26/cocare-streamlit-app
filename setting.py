import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الأساسية لتشبه تطبيقات الموبايل
st.set_page_config(page_title="Settings UI", layout="centered")

# 1. نظام إدارة التنقل (Navigation Logic)
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main_settings'

def go_to(page_name):
    st.session_state.current_page = page_name
    st.rerun()

# 2. تصميم الواجهة (CSS) - يوضع خارج الـ HTML للتحكم في حاوية ستريمليت
st.markdown("""
<style>
    /* تنسيق الخلفية الكلية */
    [data-testid="stAppViewContainer"] {
        background: #eef2f7;
    }
    /* تنسيق البطاقة الزرقاء المركزية */
    .block-container {
        max-width: 380px !important;
        margin: auto !important;
        padding: 40px 20px !important;
        background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
        border-radius: 45px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        height: 650px;
    }
    /* إخفاء شعارات ستريمليت */
    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 3. دالة بناء المكونات (HTML Bridge)
def build_ui(html_body, height=550):
    # كود JavaScript لإرسال الأوامر من الـ HTML إلى بايثون
    bridge_script = f"""
        <script>
        function sendAction(pageName) {{
            window.parent.postMessage({{
                type: 'streamlit:setComponentValue',
                value: pageName
            }}, '*');
        }}
        </script>
        <div style="font-family: 'Segoe UI', sans-serif;">
            {html_body}
        </div>
    """
    return components.html(bridge_script, height=height)

# --- منطق عرض الصفحات ---

# أ. الصفحة الرئيسية (التي تظهر في الصورة image_d3025e.png)
if st.session_state.current_page == 'main_settings':
    html_content = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .header { text-align: center; color: #0f2446; margin-bottom: 40px; position: relative; }
        .back-btn { position: absolute; left: 0; font-size: 24px; cursor: pointer; top: -5px; }
        .title { font-weight: 900; font-size: 22px; margin: 0; }
        
        /* تصميم الكبسولة (نفس طلبك في التمطيط) */
        .capsule {
            background: white; border-radius: 100px; padding: 15px 20px;
            margin-bottom: 18px; display: flex; align-items: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05); cursor: pointer;
            transition: 0.3s; width: 100%; box-sizing: border-box;
        }
        .capsule:active { transform: scale(0.98); }
        .icon-box { color: #0f2446; font-size: 18px; margin-right: auto; }
        .label-text { color: #0f2446; font-weight: 600; font-size: 15px; margin-right: 15px; }
        .arrow { color: #0f2446; font-weight: bold; font-size: 18px; }
        
        .row { display: flex; gap: 12px; margin-top: 40px; }
        .small-capsule { flex: 1; padding: 12px 15px; }
    </style>

    <div class="header">
        <span class="back-btn"><i class="fas fa-chevron-left"></i></span>
        <h2 class="title">Settings</h2>
    </div>

    <div class="capsule" onclick="sendAction('change_password')">
        <i class="fas fa-lock icon-box"></i>
        <span class="label-text">Change Password</span>
        <span class="arrow">›</span>
    </div>

    <div class="capsule" onclick="sendAction('change_language')">
        <i class="fas fa-globe icon-box"></i>
        <span class="label-text">Change Language</span>
        <span class="arrow">›</span>
    </div>

    <div class="capsule" onclick="sendAction('rate_app')">
        <i class="fas fa-star icon-box"></i>
        <span class="label-text">Rate App</span>
        <span class="arrow">›</span>
    </div>

    <div class="capsule">
        <i class="fas fa-sign-out-alt icon-box"></i>
        <span class="label-text">Log Out</span>
        <span class="arrow">›</span>
    </div>

    <div class="row">
        <div class="capsule small-capsule" style="justify-content: space-between;">
            <i class="fas fa-exclamation-triangle"></i>
            <span style="font-size: 12px; font-weight: bold; color:#0f2446;">Report Problem</span>
            <span>›</span>
        </div>
        <div class="capsule small-capsule" style="justify-content: space-between;">
            <i class="fas fa-envelope"></i>
            <span style="font-size: 12px; font-weight: bold; color:#0f2446;">Contact Us</span>
            <span>›</span>
        </div>
    </div>
    """
    result = build_ui(html_content)
    if result: go_to(result)

# ب. صفحة تغيير كلمة المرور (عند الربط)
elif st.session_state.current_page == 'change_password':
    html_pwd = """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        .header { text-align: center; color: #0f2446; margin-bottom: 40px; position: relative; }
        .back-btn { position: absolute; left: 0; font-size: 24px; cursor: pointer; top: -5px; }
        .input-field {
            background: white; border-radius: 100px; padding: 12px 20px;
            margin-bottom: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }
        input { border: none; outline: none; width: 100%; font-size: 14px; background: transparent; }
        .save-btn {
            background: white; border-radius: 100px; width: 100%; padding: 15px;
            border: none; font-weight: bold; color: #0f2446; margin-top: 100px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1); cursor: pointer;
        }
    </style>
    <div class="header">
        <span class="back-btn" onclick="sendAction('main_settings')"><i class="fas fa-chevron-left"></i></span>
        <h2 class="title">Password</h2>
    </div>
    <div class="input-field"><input type="password" placeholder="Current Password"></div>
    <div class="input-field"><input type="password" placeholder="New Password"></div>
    <div class="input-field"><input type="password" placeholder="Confirm Password"></div>
    <button class="save-btn" onclick="sendAction('main_settings')">Save Changes</button>
    """
    result = build_ui(html_pwd)
    if result: go_to(result)
