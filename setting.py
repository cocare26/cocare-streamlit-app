import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل (Navigation State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 3. التنسيقات (CSS) - لتحويل أزرار ستريمليت إلى تصميم "الكبسولة" الممتدة
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* إخفاء العناصر الافتراضية لستريمليت */
[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* الحاوية الزرقاء الرئيسية */
.block-container{
    max-width:400px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15);
    margin-top: 50px !important;
}

/* الهيدر */
.header-container {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 35px; position: relative;
}
.back-arrow { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: var(--navy); cursor: pointer; }
.settings-header { margin: 0; font-weight: 900; font-size: 22px; color: var(--navy); }

/* تعديل شكل زر ستريمليت ليصبح كبسولة ممتدة */
div.stButton > button {
    width: 100% !important;
    height: 55px !important;
    border-radius: 100px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 15px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    transition: 0.3s ease;
}

/* توزيع الأيقونة والنص داخل الزر */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; 
    width: 100% !important;
    align-items: center !important;
    font-weight: 700 !important;
    font-size: 15px !important;
    margin: 0 !important;
}

/* تأثير عند تمرير الماوس */
div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}

/* تنسيق السطر الأخير (Report & Contact) */
[data-testid="stHorizontalBlock"] div.stButton > button {
    height: 70px !important; 
}
</style>
""", unsafe_allow_html=True)

# 4. عرض الصفحات بناءً على الحالة
if st.session_state.page == 'main':
    # الهيدر
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # القائمة الرئيسية - ربط الأزرار بالصفحات الفرعية
    if st.button("🔒 Change Password"): navigate_to('password')
    if st.button("🌐 Change Language"): navigate_to('language')
    if st.button("⭐ Rate App"): navigate_to('rate')
    if st.button("🚪 Log Out"): pass
    
    st.markdown("<div style='margin: 10px 0;'></div>", unsafe_allow_html=True)

    # السطر الأخير: تقسيم الصفحة لعمودين
    col1, col2 = st.columns(2) 
    
    with col1:
        if st.button("⚠️ Report\nProblem"): navigate_to('report')
            
    with col2:
        if st.button("✉️ Contact\nUs"): navigate_to('contact')

# --- الشاشات الفرعية ---

elif st.session_state.page == 'password':
    st.markdown('<div class="header-container"><p class="settings-header">Change Password</p></div>', unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    if st.button("Save Changes"): navigate_to('main')
    if st.button("‹ Back"): navigate_to('main')

elif st.session_state.page == 'report':
    st.markdown('<div class="header-container"><p class="settings-header">Report Problem</p></div>', unsafe_allow_html=True)
    st.text_area("Describe the issue...")
    if st.button("Submit Report"): navigate_to('main')
    if st.button("‹ Back"): navigate_to('main')

# يمكنك إضافة بقية الصفحات بنفس النمط (language, rate, contact)
