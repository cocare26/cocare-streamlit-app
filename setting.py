import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = nav

# 3. تنسيق الـ CSS (تركيز كامل على المسافة القصوى)
st.markdown("""
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

/* 📦 الكارد الرئيسي */
.block-container{
    max-width:420px !important;
    margin:auto !important;
    padding:25px 30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    margin-top: 20px !important;
}

/* 🔝 الهيدر */
.header-container {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 35px; position: relative;
}
.back-arrow { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: var(--navy); }
.settings-header { margin: 0; font-weight: 900; font-size: 22px; color: var(--navy); }

/* 🔘 الزر الممتد */
div.stButton { width: 100% !important; }

div.stButton > button {
    width: 100% !important;
    height: 58px !important;
    border-radius: 25px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    padding: 0 20px !important; /* مسافة أمان عن الأطراف */
}

/* 🎯 التوزيع المطلوب: دفع الإيموجي لليسار والنص لليمين بأقصى مسافة */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; /* رمي العناصر على الأطراف */
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,.1) !important;
}
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
    
    # الترتيب في الكود: الإيموجي ثم النص + السهم
    st.button("🔒 <span>Change Password ›</span>")
    st.button("🌐 <span>Change Language ›</span>")
    st.button("⭐ <span>Rate App ›</span>")
    st.button("🚪 <span>Log Out ›</span>")
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    # السطر الأخير بنفس التنسيق
    col1, col2 = st.columns(2)
    with col1:
        st.button("⚠️ <span>Report a\\nProblem</span>")
    with col2:
        st.button("✉️ <span>Contact Us</span>")
