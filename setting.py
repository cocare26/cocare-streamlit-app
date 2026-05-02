import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. تنسيق الـ CSS المطور
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #cbdbe5;
    }

    /* تنسيق الأزرار لتكون عريضة جداً (من البداية للنهاية) */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; /* اللون أسود كما طلبت */
        border-radius: 20px !important;
        border: none !important;
        width: 100% !important; /* العرض كامل */
        height: 60px !important; /* زيادة الطول قليلاً لتبدو أفضل */
        font-size: 18px !important;
        font-weight: 500 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 15px !important;
        display: block !important;
    }

    /* تحسين مظهر خانات الإدخال */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: none !important;
        padding: 12px !important;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #fef8e8 !important;
        border-radius: 20px !important;
        border: none !important;
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
    # العنوان: السهم < وكلمة Settings بالأسود
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 30px; direction: ltr;">
            <div style="padding-left: 10px;">
                <span style="font-size: 30px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -40px;">
                <h2 style="color: #000000; margin: 0; font-weight: bold;">Settings</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # الأزرار الرئيسية (كل زر يأخذ سطر كامل تلقائياً بسبب عرض 100%)
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")
    
    # أزرار البلاغات والتواصل (جعلتها أيضاً تحت بعض لتكون عريضة، أو يمكن تركها بجانب بعض)
    # إذا كنت تريدها عريضة أيضاً، نلغي الـ columns:
    if st.button("⚠️ Report"): nav('report')
    if st.button("✉️ Contact"): nav('contact')

# --- شاشة تغيير كلمة المرور ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Change Password</h3>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write New Password", type="password")
    if st.button("Save"): nav('main')

# --- شاشة اللغة ---
elif st.session_state.page == 'language':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Change Language</h3>", unsafe_allow_html=True)
    st.button("English (Active)")
    st.button("العربية")

# --- شاشة البلاغات ---
elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Report a Problem</h3>", unsafe_allow_html=True)
    st.text_area("Message", value="I need help...")
    if st.button("Send Report"):
        st.success("Report Sent!")
        nav('main')

# --- شاشة التواصل ---
elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Contact Us</h3>", unsafe_allow_html=True)
    st.info("📧 Email: Co.Care26@gmail.com")
    st.info("📞 Phone: +962 79 123 4657")
