import streamlit as st

# 1. إعدادات الصفحة - عرض كامل
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية وزيادة المسافة من الأعلى */
    .block-container {
        max-width: 100% !important; 
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 40px !important; /* مسافة من سقف الشاشة */
    }

    /* هيدر الإعدادات مع مسافة سفلية ضخمة جداً */
    .header-full {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        /* هذه المسافة هي اللي بتنزّل الأزرار لتحت السهم بمسافة كبيرة */
        margin-bottom: 150px !important; 
        padding: 0 40px;
    }

    /* تصميم الزر (الكبسولة الممتدة) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; 
        border: none !important;
        width: 100% !important; 
        height: 100px !important; 
        font-size: 24px !important;
        font-weight: 900 !important;
        margin-bottom: 25px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 60px !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.05) !important;
    }

    /* إزاحة النص لليمين لزيادة الفراغ عن الإيموجي */
    .stButton > button div p {
        width: 100%;
        text-align: left !important;
        margin-left: 120px !important; 
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
    # الهيدر: السهم وكلمة Settings
    st.markdown("""
        <div class="header-full">
            <div style="position: absolute; left: 40px; font-size: 55px; font-weight: 900; color: #000; cursor: pointer;"> < </div>
            <h1 style="color: #000; font-size: 50px; font-weight: 900; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # فراغ نصي إضافي
    gap = "&nbsp;" * 25

    if st.button(f"🔒 {gap} Change Password"): nav('password')
    if st.button(f"🌐 {gap} Change Language"): nav('language')
    if st.button(f"⭐ {gap} &nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {gap} &nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ &nbsp; Report Problem"): nav('report')
    with col2:
        if st.button("✉️ &nbsp; Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 50px; margin-top: 50px;'>Change Password</h1>", unsafe_allow_html=True)
