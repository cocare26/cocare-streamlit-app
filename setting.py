import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. تنسيق الـ CSS (تكبير الطول لأقصى حد)
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #cbdbe5;
    }

    /* تنسيق الأزرار لتكون "طويلة جداً" وضخمة */
    .stButton > button {
        background-color: #f8f1e5 !important; 
        color: #000000 !important; 
        border-radius: 60px !important; /* حواف دائرية جداً لتناسب الطول */
        border: none !important;
        width: 100% !important; 
        height: 150px !important; /* زيادة الارتفاع بشكل كبير جداً كما طلبت */
        font-size: 30px !important; /* تكبير الخط ليتناسب مع حجم البوكس */
        font-weight: bold !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1) !important;
        margin-bottom: 30px !important; /* مسافة بين البوكسات الطويلة */
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* تكبير حجم الأيقونات والنصوص داخل الأزرار */
    .stButton > button p {
        font-size: 30px !important;
        font-weight: bold !important;
    }

    /* توسيع الحاوية لتستوعب الحجم الجديد */
    .block-container {
        max-width: 900px !important;
        padding-top: 2rem !important;
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
    # العنوان: السهم < وكلمة Settings باللون الأسود
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 40px; direction: ltr;">
            <div style="padding-left: 10px;">
                <span style="font-size: 45px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -50px;">
                <h1 style="color: #000000; margin: 0; font-weight: bold; font-size: 40px;">Settings</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # أول 4 بوكسات (طوال جداً)
    if st.button("🔒   Change Password"): nav('password')
    if st.button("🌐   Change Language"): nav('language')
    if st.button("⭐   Rate App"): nav('rate')
    if st.button("🚪   Log Out"): st.write("Logged Out!")
    
    # الباقي بنفس الطول لتوحيد الشكل
    if st.button("⚠️   Report"): nav('report')
    if st.button("✉️   Contact"): nav('contact')

# --- باقي الشاشات ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='color: black; text-align: center;'>Change Password</h1>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    if st.button("Save Now"):
        st.success("Done!")
        nav('main')

elif st.session_state.page == 'language':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='color: black; text-align: center;'>Select Language</h1>", unsafe_allow_html=True)
    st.button("English")
    st.button("العربية")
