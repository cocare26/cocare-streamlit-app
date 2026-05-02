import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS (لجعل التصميم عريض وممتد للحواف)
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    .block-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
    }

    .stButton > button {
        background-color: white !important;
        color: #000000 !important; 
        border-radius: 0px !important; 
        border: none !important;
        width: 100% !important;
        height: 60px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
        margin-bottom: 2px !important; 
        display: flex;
        justify-content: space-between; 
        padding: 0 20px !important;
        text-align: left !important;
    }

    /* تنسيق النصوص داخل الأزرار لتبدو مرتبة مع الأسهم */
    .stButton > button p {
        width: 100%;
        display: flex;
        justify-content: space-between;
        margin: 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 4. عرض الصفحات
if st.session_state.page == 'main':
    # هيدر الصفحة
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 25px; direction: ltr; padding: 20px;">
            <div style="padding-left: 10px;">
                <span style="font-size: 30px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -40px;">
                <h2 style="color: #000000; margin: 0; font-weight: bold;">Settings</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # القائمة العلوية
    if st.button("🔒 Change Password                                                                                                             >"): nav('password')
    if st.button("🌐 Change Language                                                                                                           >"): nav('language')
    if st.button("⭐ Rate App                                                                                                                     >"): nav('rate')
    if st.button("🚪 Log Out                                                                                                                       >"): st.write("Logged Out!")
    
    # الترتيب المطلوب: Report a Problem ثم Contact Us
    if st.button("⚠️ Report a Problem                                                                                                         >"): nav('report')
    if st.button("✉️ Contact Us                                                                                                                   >"): nav('contact')

# --- شاشات فرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.title("Change Password")

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.title("Report a Problem")

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.title("Contact Us")
