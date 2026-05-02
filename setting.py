import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# دمج كود الـ CSS داخل Streamlit بشكل صحيح لتجنب خطأ SyntaxError
st.markdown("""
    <style>
    /* تغيير خلفية التطبيق كاملة */
    .stApp {
        background-color: #cbdbe5;
    }

    /* تنسيق الحاوية الرئيسية لتشبه الحاويات في الصورة */
    .main-container {
        background-color: rgba(255, 255, 255, 0.3);
        border-radius: 30px;
        padding: 30px;
        text-align: center;
        backdrop-filter: blur(10px);
    }

    /* تنسيق الأزرار البيضاء */
    .stButton > button {
        background-color: white !important;
        color: #4a4a4a !important;
        border-radius: 20px !important;
        border: none !important;
        width: 100% !important;
        height: 50px !important;
        font-size: 16px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 10px !important;
    }

    /* تنسيق خانات الإدخال */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: none !important;
        padding: 12px !important;
    }
    
    /* تنسيق مربع النص في البلاغات */
    .stTextArea > div > div > textarea {
        background-color: #fef8e8 !important;
        border-radius: 20px !important;
        border: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل بين الشاشات باستخدام Session State
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h2 style='text-align: center; color: #4a4a4a;'>Settings</h2>", unsafe_allow_html=True)
    
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report"): nav('report')
    with col2:
        if st.button("✉️ Contact"): nav('contact')

# --- شاشة تغيير كلمة المرور ---
elif st.session_state.page == 'password':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Change Password</h3>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write New Password", type="password")
    if st.button("Save"): nav('main')

# --- شاشة اللغة ---
elif st.session_state.page == 'language':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Change Language</h3>", unsafe_allow_html=True)
    st.button("English (Active)")
    st.button("العربية")

# --- شاشة البلاغات ---
elif st.session_state.page == 'report':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Report a Problem</h3>", unsafe_allow_html=True)
    st.text_area("Message", value="I need help...")
    if st.button("Send Report"):
        st.success("Report Sent!")
        nav('main')

# --- شاشة التواصل ---
elif st.session_state.page == 'contact':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Contact Us</h3>", unsafe_allow_html=True)
    st.info("📧 Email: Co.Care26@gmail.com")
    st.info("📞 Phone: +962 79 123 4657")
