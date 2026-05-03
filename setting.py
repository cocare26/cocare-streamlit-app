import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (تم تعديل العرض ليمتد بالكامل)
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

/* 🔘 السر هنا: جعل الأزرار تمتد (Stretch) لتغطي كل المساحة الخضراء */
div.stButton {
    width: 100% !important;
}

div.stButton > button {
    width: 100% !important; /* يمط الزر لآخر الكارد */
    height: 55px !important;
    border-radius: 25px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 12px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    transition: 0.3s ease;
    padding: 0 20px !important;
}

/* 🎯 توزيع العناصر: الإيموجي أقصى اليسار والكلام أقصى اليمين */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; 
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    white-space: pre-line !important; 
}

/* 🛠️ تعديل السطر الأخير ليكون بنفس العرض الممتد وبطول أكبر للسطرين */
[data-testid="stHorizontalBlock"] div.stButton > button {
    height: 90px !important; 
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
    
    # كل هذه الأزرار ستمتد الآن لتغطي المساحة الخضراء التي رسمتها
    st.button("🔒 Change Password")
    st.button("🌐 Change Language")
    st.button("⭐ Rate App")
    st.button("🚪 Log Out")
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    # السطر الأخير الممتد أيضاً
    col1, col2 = st.columns([1.3, 1]) 
    
    with col1:
        if st.button("⚠️ Report\nto Problem"): 
            nav('report')
            
    with col2:
        if st.button("✉️ Contact\nUs"): 
            nav('contact')

# الشاشات الفرعية
elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h3 style='text-align:center;'>Report a Problem</h3>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h3 style='text-align:center;'>Contact Us</h3>", unsafe_allow_html=True)
