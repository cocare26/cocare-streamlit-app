import streamlit as st
import streamlit.components.v1 as components

# إعدادات الصفحة الأساسية
st.set_page_config(page_title="Settings", layout="centered")

# 1. نظام إدارة الصفحات (Session State)
# نستخدم هذا المتغير لتخزين الصفحة الحالية التي يتواجد فيها المستخدم
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'main'

# 2. منطق عرض واجهة "تغيير كلمة المرور"
if st.session_state.current_page == "Change_password":
    st.markdown("<h2 style='text-align:center; color:#0f2446;'>🔒 Change Password</h2>", unsafe_allow_html=True)
    
    # واجهة إدخال كلمة المرور (بأدوات ستريمليت الأصلية)
    with st.container():
        old_p = st.text_input("Current Password", type="password")
        new_p = st.text_input("New Password", type="password")
        conf_p = st.text_input("Confirm New Password", type="password")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Save Changes", use_container_width=True):
                st.success("Password Updated!")
        with col2:
            if st.button("Back", use_container_width=True):
                st.session_state.current_page = 'main'
                st.rerun()
    st.stop() # إيقاف التنفيذ لضمان عدم ظهور القائمة الرئيسية بالأسفل

# 3. تنسيق CSS للقائمة الرئيسية
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

# 4. المكون الذي يربط الـ HTML بـ Python
# القيمة التي يتم إرسالها من 'onclick' ستخزن في المتغير 'selection'
selection = components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
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

    <!-- عند الضغط هنا، نرسل كلمة 'Change_password' لستريمليت -->
    <div class="setting-item" onclick="send('Change_password')">
        <i class="fas fa-lock left-icon"></i>
        <span class="setting-text-right">Change Password</span>
        <span class="arrow">›</span>
    </div>

    <div class="setting-item" onclick="send('Change_language')">
        <i class="fas fa-globe left-icon"></i>
        <span class="setting-text-right">Change Language</span>
        <span class="arrow">›</span>
    </div>

    <div class="bottom-row">
        <div class="setting-item" onclick="send('Report')">
            <i class="fas fa-exclamation-triangle"></i>
            <span class="setting-text">Report</span>
            <span class="arrow">›</span>
        </div>
        <div class="setting-item" onclick="send('Contact')">
            <i class="fas fa-envelope"></i>
            <span class="setting-text">Contact</span>
            <span class="arrow">›</span>
        </div>
    </div>
</div>

<script>
// هذه الدالة السحرية التي تربط العالمين ببعضهما
function send(val) {
    window.parent.postMessage({
        type: 'streamlit:setComponentValue',
        value: val
    }, '*');
}
</script>
</body>
</html>
""", height=480)

# 5. معالجة الإشارة القادمة من الـ HTML
if selection:
    st.session_state.current_page = selection
    st.rerun() # إعادة تشغيل الكود ليتم تطبيق الشرط في البداية (Page Router)
