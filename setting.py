import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المخصص
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* تركيز المحتوى في المنتصف */
    .block-container {
        max-width: 500px !important;
        padding-top: 40px !important;
    }

    /* تصميم الأزرار - زيادة الطول وزيادة المسافات الداخلية */
    .stButton > button {
        background-color: #f8f9fa !important;
        color: #000000 !important; 
        border-radius: 50px !important; 
        border: none !important;
        width: 100% !important;
        height: 95px !important; /* زيادة الطول أكثر */
        font-size: 22px !important; /* تكبير الخط ليتناسب مع الضخامة */
        font-weight: 700 !important;
        margin-bottom: 18px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 35px !important; /* زيادة المسافة من الحافة اليسرى */
        box-shadow: 0 5px 10px rgba(0,0,0,0.1) !important;
        transition: 0.3s;
    }

    /* زيادة المسافة بين الإيموجي والنص بشكل يدوي عن طريق الـ CSS */
    .stButton > button div p {
        width: 100%;
        text-align: center !important;
        margin-right: 50px !important; /* موازنة المسافة ليبقى النص في المنتصف */
    }

    /* تنسيق السطر الأخير */
    [data-testid="column"] {
        padding: 0 7px !important;
    }
    [data-testid="stHorizontalBlock"] {
        gap: 0px !important;
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
    # الهيدر: السهم وكلمة Settings باللون الأسود
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; position: relative; margin-bottom: 45px;">
            <div style="position: absolute; left: 10px; font-size: 35px; font-weight: 900; color: #000000; cursor: pointer;"> < </div>
            <h1 style="color: #000000; font-size: 38px; font-weight: bold; margin: 0; text-align: center;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # قائمة الخيارات مع زيادة المسافة يدوياً (عن طريق مسافات نصية إضافية)
    if st.button("🔒 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change Password"): nav('password')
    if st.button("🌐 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change Language"): nav('language')
    if st.button("⭐ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Rate App"): nav('rate')
    if st.button("🚪 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ &nbsp;&nbsp; Report a Problem"): nav('report')
    with col2:
        if st.button("✉️ &nbsp;&nbsp;&nbsp;&nbsp; Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align:center; color: black;'>Change Password</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align:center; color: black;'>Report a Problem</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align:center; color: black;'>Contact Us</h2>", unsafe_allow_html=True)
