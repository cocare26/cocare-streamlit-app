import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. تنسيق الـ CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* الحاوية المركزية - عرض ثابت كما في الصورة */
    .block-container {
        max-width: 480px !important; 
        padding-top: 50px !important;
    }

    /* تصميم الأزرار (الكبسولة) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 50px !important; 
        border: none !important;
        width: 100% !important;
        height: 80px !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 30px !important; /* مسافة الإيموجي عن الحافة اليسرى */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }

    /* جعل النص ينجذب لليمين قليلاً ليعطي مساحة للفراغ الكبير */
    .stButton > button div p {
        width: 100%;
        text-align: left !important;
        display: flex;
        align-items: center;
    }

    /* السطر الأخير */
    [data-testid="column"] {
        padding: 0 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر باللون الأسود
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; position: relative; margin-bottom: 40px;">
            <div style="position: absolute; left: 10px; font-size: 30px; font-weight: bold; color: #000; cursor: pointer;"> < </div>
            <h1 style="color: #000; font-size: 35px; font-weight: bold; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # زيادة المسافات (Nbsp) بشكل كبير جداً (15 مسافة) لزيادة طول الفراغ
    long_gap = "&nbsp;" * 15

    if st.button(f"🔒 {long_gap} Change Password"): nav('password')
    if st.button(f"🌐 {long_gap} Change Language"): nav('language')
    if st.button(f"⭐ {long_gap} &nbsp;&nbsp;&nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {long_gap} &nbsp;&nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem"): nav('report')
    with col2:
        if st.button("✉️ Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.title("Change Password")
