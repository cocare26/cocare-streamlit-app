import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name
    st.rerun()

# 3. تحميل مكتبة الأيقونات وتنسيق الـ CSS
# أضفنا رابط Font Awesome في البداية لضمان ظهور الرموز
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* الكارد الرئيسي */
.block-container{
    max-width:400px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 40px !important;
}

/* الهيدر */
.header-container {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 35px; position: relative;
}
.back-arrow { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: var(--navy); cursor: pointer; }
.settings-header { margin: 0; font-weight: 900; font-size: 22px; color: var(--navy); }

/* تنسيق أزرار ستريمليت لتصبح كبسولات */
div.stButton > button {
    width: 100% !important;
    height: 55px !important;
    border-radius: 100px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    padding: 0 20px !important;
}

/* توزيع الأيقونة والنص والسهم */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; 
    width: 100% !important;
    align-items: center !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    margin: 0 !important;
}

/* تكبير الأيقونات وتغيير لونها */
.icon-style { font-size: 18px; margin-right: 10px; }
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # استخدام نصوص واضحة مع الـ Emoji كحل بديل ومضمون
    if st.button("🔒 Change Password                                 ›"): nav('password')
    if st.button("🌐 Change Language                                 ›"): nav('language')
    if st.button("⭐ Rate App                                         ›"): nav('rate')
    if st.button("🚪 Log Out                                           ›"): pass
    
    st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2) 
    with col1:
        if st.button("⚠️ Report\nProblem"): nav('report')
    with col2:
        if st.button("✉️ Contact\nUs"): nav('contact')

elif st.session_state.page == 'password':
    st.markdown('<div class="header-container"><div class="back-arrow" onclick="window.location.reload()">‹</div><p class="settings-header">Password</p></div>', unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    if st.button("Save Changes"): nav('main')
    if st.button("Back"): nav('main')
