import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# كود الـ CSS المعدل لتكبير البوكسات وإضافة الأسهم البيضاء
st.markdown("""
    <style>
    /* الخلفية السماوية */
    .stApp {
        background-color: #cbdbe5;
    }

    /* تكبير وتنسيق الأزرار لتصل للنهاية */
    .stButton > button {
        background-color: white !important;
        color: #4a4a4a !important;
        border-radius: 15px !important;
        border: none !important;
        width: 100% !important; /* تكبير البوكس للنهاية */
        height: 60px !important; /* زيادة الطول قليلاً */
        font-size: 18px !important;
        font-weight: 500 !important;
        margin-bottom: 15px !important;
        display: flex !important;
        justify-content: space-between !important; /* توزيع النص والسهم */
        align-items: center !important;
        padding: 0 25px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
        transition: 0.3s !important;
    }

    /* إضافة سهم أبيض بجهة اليسار داخل مربع صغير */
    .stButton > button::after {
        content: "→"; 
        background-color: #4a4a4a; /* لون المربع اللي خلف السهم ليظهر السهم أبيض */
        color: white; /* السهم أبيض */
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 16px;
        margin-left: 10px;
    }

    /* تكبير بوكسات الـ Report والـ Contact */
    .stColumn > div > div > button {
        height: 80px !important; /* جعلهم أكبر من البقية */
        flex-direction: column !important;
        justify-content: center !important;
        gap: 5px !important;
    }

    /* تحسين شكل المدخلات */
    .stTextInput > div > div > input {
        border-radius: 12px !important;
        height: 50px !important;
    }

    .stTextArea > div > div > textarea {
        background-color: #fef8e8 !important;
        border-radius: 20px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h1 style='text-align: center; color: #333; margin-bottom: 40px;'>Settings</h1>", unsafe_allow_html=True)
    
    # الأزرار الرئيسية - الآن تأخذ العرض الكامل تلقائياً
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.toast("Logged Out!")
    
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    
    # جعل أزرار Report و Contact عريضة أيضاً
    if st.button("⚠️ Report a Problem"): nav('report')
    if st.button("✉️ Contact Us"): nav('contact')

# --- الشاشات الفرعية (نفس المنطق السابق مع التنسيق الجديد) ---
elif st.session_state.page == 'password':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Change Password</h3>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write New Password", type="password")
    if st.button("Save"): nav('main')

elif st.session_state.page == 'report':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Report a Problem</h3>", unsafe_allow_html=True)
    st.text_area("How can we help?", height=200)
    if st.button("Send Report"): nav('main')

elif st.session_state.page == 'contact':
    if st.button("← Back"): nav('main')
    st.markdown("<h3>Contact Us</h3>", unsafe_allow_html=True)
    st.write("📧 Email: Co.Care26@gmail.com")
    st.write("📞 Phone: +962 79 123 4657")
    
