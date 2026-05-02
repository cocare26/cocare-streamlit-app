import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS لتحويل الأزرار إلى كبسولات (Capsules) كما في الصورة
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إضافة هوامش جانبية لجعل القائمة في المنتصف مثل الصورة */
    .block-container {
        max-width: 600px !important;
        padding-top: 50px !important;
    }

    /* تنسيق الأزرار لتصبح دائرية الحواف (Capsule shape) */
    .stButton > button {
        background-color: #f8f9fa !important;
        color: #333333 !important; 
        border-radius: 50px !important; /* حواف دائرية جداً */
        border: none !important;
        width: 100% !important;
        height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important; /* مسافة بين كل زر وزر */
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 25px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
    }

    /* تنسيق النصوص داخل الأزرار */
    .stButton > button div p {
        width: 100%;
        text-align: center !important; /* النص في المنتصف */
        margin-right: 40px !important; /* توازن بسبب وجود الإيموجي يسار */
    }

    /* تنسيق خاص للأعمدة في السطر الأخير */
    [data-testid="column"] {
        padding: 0 5px !important;
    }
    
    [data-testid="stHorizontalBlock"] {
        gap: 0px !important;
    }

    /* هيدر الإعدادات */
    .settings-header {
        text-align: center;
        color: #333;
        font-weight: bold;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
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
    # الهيدر مع سهم الرجوع
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; position: relative; margin-bottom: 30px;">
            <div style="position: absolute; left: 20px; font-size: 24px; font-weight: bold; cursor: pointer;"> < </div>
            <h1 style="font-size: 32px; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # الأزرار الرئيسية بتنسيق الصورة
    if st.button("🔒                       Change Password"): nav('password')
    if st.button("🌐                       Change Language"): nav('language')
    if st.button("⭐                               Rate App"): nav('rate')
    if st.button("🚪                               Log Out"): st.write("Logged Out!")
    
    # السطر الأخير المقسم لزرين دائريين
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️   Report a Problem"): nav('report')
    with col2:
        if st.button("✉️       Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.header("Change Password")

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.header("Report a Problem")

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.header("Contact Us")
