import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم لتحقيق الشكل المطلوب
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* الحاوية المركزية */
    .block-container {
        max-width: 100% !important; 
        padding-left: 20px !important;
        padding-right: 20px !important;
        padding-top: 30px !important;
    }

    /* الهيدر: السهم وكلمة Settings */
    .header-style {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 150px; /* مسافة كبيرة بين السهم والكلمة */
        margin-bottom: 80px;
        padding-left: 20px;
    }

    /* تصميم الأزرار (الكبسولة) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; 
        border: none !important;
        width: 100% !important;
        height: 85px !important; 
        font-size: 22px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important; /* لتوزيع المحتوى بين الطرفين */
        padding: 0 40px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }

    /* تنسيق المحتوى الداخلي للزر (الإيموجي + النص) */
    .button-content {
        display: flex;
        align-items: center;
        width: 100%;
    }

    .emoji-space {
        margin-right: 80px; /* المسافة الكبيرة بعد الإيموجي */
        font-size: 26px;
    }

    /* السطر الأخير */
    [data-testid="column"] {
        padding: 0 10px !important;
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
    # الهيدر المخصص
    st.markdown("""
        <div class="header-style">
            <span style="font-size: 40px; font-weight: bold; color: #000; cursor: pointer;">‹</span>
            <span style="font-size: 45px; font-weight: bold; color: #000;">Settings</span>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة مساعدة لإنشاء الأزرار بالشكل الجديد (نص + سهم في الآخر)
    def settings_btn(emoji, label, page):
        # نستخدم markdown لعرض الشكل، و Streamlit Button للضغط
        # لجعل السهم في الآخر، ندمجه في نص الزر
        if st.button(f"{emoji} {'&nbsp;'*20} {label} {'&nbsp;'*(40 - len(label))} ›"):
            nav(page)

    # قائمة الأزرار الرئيسية
    settings_btn("🔒", "Change Password", "password")
    settings_btn("🌐", "Change Language", "language")
    settings_btn("⭐", "Rate App", "rate")
    settings_btn("🚪", "Log Out", "main")
    
    st.write("") # مسافة بسيطة

    # السطر الأخير المقسم لزرين
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp;&nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- شاشة تجريبية ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Password</h1>", unsafe_allow_html=True)
