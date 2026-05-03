import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS المطور لزيادة المسافة
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

.block-container{
    max-width:420px !important;
    margin:auto !important;
    padding:25px 30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    margin-top: 20px !important;
}

.header-container {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 35px; position: relative;
}

.back-arrow { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: var(--navy); }
.settings-header { margin: 0; font-weight: 900; font-size: 22px; color: var(--navy); }

/* 🔘 الأزرار وتوزيع الأطراف الأقصى */
div.stButton > button {
    width: 100% !important;
    height: 52px !important;
    border-radius: 25px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    transition: 0.3s ease;
    padding: 0 15px !important; /* تقليل المسافة الجانبية ليلتصقوا بالأطراف أكثر */
}

div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; /* دفع العناصر لأقصى اليمين واليسار */
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 15px !important;
}

/* 🎯 إضافة عنصر وهمي في الوسط لضمان التباعد المطلق */
div.stButton > button p::after {
    content: "";
    flex: 1; /* يشغل كل المساحة الفارغة في الوسط */
    order: 1;
}

div.stButton > button p span:first-child { order: 0; } /* الإيموجي يسار */
div.stButton > button p span:last-child { order: 2; }  /* النص يمين */

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
    
    # كتابة الإيموجي أولاً ثم النص، والـ CSS بيتكفل بالباقي
    st.button("🔒 Change Password")
    st.button("🌐 Change Language")
    st.button("⭐ Rate App")
    st.button("🚪 Log Out")
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    st.button("⚠️ Report a Problem")
    st.button("✉️ Contact Us")

elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("### Change Password")
