import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Settings App", layout="centered") 

# 2. نظام إدارة التنقل (المنادي)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def navigate_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# 3. التنسيق (CSS) - لتحويل الواجهة لشكل كبسولة ممتدة
st.markdown("""
<style>
:root{ --navy:#0f2446; --bg-gradient: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%); }
[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

.block-container{
    max-width:400px !important; margin:auto !important; padding:30px !important;
    background: var(--bg-gradient); border-radius:42px;
    box-shadow:0 15px 35px rgba(0,0,0,0.15); margin-top: 40px !important;
}

/* تصميم الزر ككبسولة ممتدة */
div.stButton > button {
    width: 100% !important; height: 55px !important;
    border-radius: 100px !important; border: none !important;
    background: white !important; color: var(--navy) !important;
    margin-bottom: 12px !important; box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
}
/* توزيع المحتوى داخل الزر */
div.stButton > button p {
    display: flex !important; justify-content: space-between !important; 
    width: 100% !important; align-items: center !important;
    font-weight: 700 !important; font-size: 15px !important; margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# 4. دالات الصفحات (التي سنستدعيها)

def show_main_settings():
    st.markdown('<div style="text-align:center; margin-bottom:30px;"><h2 style="color:#0f2446; font-weight:900;">Settings</h2></div>', unsafe_allow_html=True)
    
    # مناداة الصفحات عند الضغط
    if st.button("🔒 Change Password                               ›"): navigate_to('password')
    if st.button("🌐 Change Language                               ›"): navigate_to('language')
    if st.button("⭐ Rate App                                       ›"): navigate_to('rate')
    
    st.markdown("<div style='margin: 20px 0;'></div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report\nProblem"): navigate_to('report')
    with col2:
        if st.button("✉️ Contact\nUs"): navigate_to('contact')

def show_password_page():
    st.markdown('<h2 style="color:#0f2446; text-align:center;">Password</h2>', unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    if st.button("Save changes"): navigate_to('main')
    if st.button("‹ Back"): navigate_to('main')

def show_report_page():
    st.markdown('<h2 style="color:#0f2446; text-align:center;">Report</h2>', unsafe_allow_html=True)
    st.text_area("What is the issue?")
    if st.button("Send"): navigate_to('main')
    if st.button("‹ Back"): navigate_to('main')

# 5. منطق الاستدعاء (The Logic)
if st.session_state.page == 'main':
    show_main_settings()
elif st.session_state.page == 'password':
    show_password_page()
elif st.session_state.page == 'report':
    show_report_page()
# يمكنك إضافة elif لباقي الصفحات بنفس الطريقة
