import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. تنسيق الـ CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }
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

# 3. إدارة التنقل (هذا الجزء هو الذي منع الخطأ)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 4. عرض الصفحات
if st.session_state.page == 'main':
    # كود العنوان مع السهم المطلوب <
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 25px; direction: ltr;">
            <div style="cursor: pointer; padding-left: 10px;">
                <span style="font-size: 30px; font-weight: bold; color: black;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -40px;">
                <h2 style="color: #4a4a4a; margin: 0;">Settings</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report"): nav('report')
    with col2:
        if st.button("✉️ Contact"): nav('contact')

elif st.session_state.page == 'password':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Change Password</h3>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write New Password", type="password")
    if st.button("Save"): nav('main')

elif st.session_state.page == 'language':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Change Language</h3>", unsafe_allow_html=True)
    st.button("English (Active)")
    st.button("العربية")

elif st.session_state.page == 'report':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Report a Problem</h3>", unsafe_allow_html=True)
    st.text_area("Message", value="I need help...")
    if st.button("Send Report"):
        st.success("Report Sent!")
        nav('main')

elif st.session_state.page == 'contact':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Contact Us</h3>", unsafe_allow_html=True)
    st.info("📧 Email: Co.Care26@gmail.com")
    st.info("📞 Phone: +962 79 123 4657")
