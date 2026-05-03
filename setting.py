import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (المسافات المطاطية مع السهم)
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

/* 🔘 تنسيق الزر الممتد */
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
    padding: 0 20px !important;
}

/* 🎯 توزيع المسافة المطلوب [ إيموجي  ---  نص + سهم ] */
div.stButton > button p {
    display: flex !important;
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 16px !important;
}

/* دفع النص والسهم لليمين بترك فراغ كبير بعد الإيموجي */
div.stButton > button p::before {
    content: "";
    flex-grow: 1; /* هذه هي المسافة التي طلبتها */
    order: 2;
}

/* ترتيب العناصر */
div.stButton > button p span:first-child { order: 1; font-size: 20px; } /* الإيموجي يسار */
div.stButton > button p span:last-child { order: 3; } /* النص والسهم يمين */

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
    
    # لاحظ إضافة السهم ( › ) في نهاية النص لكل زر
    st.button("🔒 Change Password &nbsp; ›")
    st.button("🌐 Change Language &nbsp; ›")
    st.button("⭐ Rate App &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ›")
    st.button("🚪 Log Out &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; ›")
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        st.button("⚠️ Report\nto Problem")
    with col2:
        st.button("✉️ Contact\nUs")

# الشاشات الفرعية
elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
