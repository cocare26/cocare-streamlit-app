import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. التعديل المطلوب هنا (في قسم الـ CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* --- التعديل المقصود لزيادة الإزاحة لجهة اليمين --- */
    .block-container {
        max-width: 80% !important; /* تقليل العرض قليلاً لتظهر الإزاحة */
        padding-top: 20px !important;
        
        /* دفع الحاوية لليمين */
        margin-left: auto !important;  
        margin-right: 2% !important; /* مسافة بسيطة جداً من اليمين ليبقى قريباً من الحافة */
    }

    /* تنسيق الأزرار (نحيفة وممتدة) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; 
        border: none !important;
        width: 100% !important;
        height: 60px !important; 
        font-size: 20px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important; 
        padding-left: 40px !important;
        padding-right: 40px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }
    /* ------------------------------------------- */
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر (تحريكه أيضاً لليسار قليلاً ليواكب الأزرار)
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; gap: 50px; margin-bottom: 60px; padding-left: 40px;">
            <span style="font-size: 40px; font-weight: 900; color: #000; cursor: pointer;">‹</span>
            <span style="font-size: 40px; font-weight: 900; color: #000;">Settings</span>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة الزر بمسافة هائلة
    def settings_item(emoji, label, page):
        gap = "&nbsp;" * 100 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    settings_item("🔒", "Change Password", "password")
    settings_item("🌐", "Change Language", "language")
    settings_item("⭐", "Rate App", "rate")
    settings_item("🚪", "Log Out", "main")
    
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp;&nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- شاشة فرعية ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Change Password</h2>", unsafe_allow_html=True)
