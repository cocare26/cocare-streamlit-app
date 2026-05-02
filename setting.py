import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. تنسيق الـ CSS لتحقيق نفس شكل الصورة "بالضبط"
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* تحديد عرض القائمة في منتصف الشاشة مثل الصورة */
    .block-container {
        max-width: 450px !important; 
        padding-top: 50px !important;
        background-color: rgba(255, 255, 255, 0.2); /* خلفية خفيفة جداً للمنطقة المركزية */
        border-radius: 20px;
    }

    /* تصميم الأزرار (شكل الكبسولة كما في الصورة) */
    .stButton > button {
        background-color: #fcfcfc !important;
        color: #000000 !important; 
        border-radius: 40px !important; 
        border: none !important;
        width: 100% !important;
        height: 75px !important; 
        font-size: 19px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 25px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05) !important;
    }

    /* محاذاة النص داخل الزر ليكون مثل الصورة */
    .stButton > button div p {
        width: 100%;
        text-align: center !important;
        margin-right: 35px !important; 
    }

    /* السطر الأخير (Report a Problem & Contact Us) */
    [data-testid="column"] {
        padding: 0 5px !important;
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

# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر: السهم الأسود وكلمة Settings
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; position: relative; margin-bottom: 35px;">
            <div style="position: absolute; left: 10px; font-size: 28px; font-weight: bold; color: #000; cursor: pointer;"> < </div>
            <h1 style="color: #000; font-size: 32px; font-weight: bold; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # قائمة الأزرار بنفس ترتيب الصورة
    # استخدمنا مسافات لضبط الموقع بدقة
    if st.button("🔒 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change Password"): nav('password')
    if st.button("🌐 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Change Language"): nav('language')
    if st.button("⭐ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Rate App"): nav('rate')
    if st.button("🚪 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير المقسم لزرين صغيرين
    col1, col2 = st.columns(2)
    with col1:
        # زر ريبورت يحتاج إزاحة نصية بسيطة ليناسب حجمه
        if st.button("⚠️ Report a Problem", key="rep"): nav('report')
    with col2:
        if st.button("✉️ Contact Us", key="cont"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align:center; color: black;'>Change Password</h2>", unsafe_allow_html=True)
