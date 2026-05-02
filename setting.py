import streamlit as st

# 1. إعدادات الصفحة - العرض الممتد (Wide)
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* توسيع الحاوية لتسمح للأزرار بالامتداد العرضي الكامل */
    .block-container {
        max-width: 95% !important; 
        padding-top: 20px !important;
    }

    /* تصميم الأزرار الممتدة (نفس الشكل الأحمر في صورتك) */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; 
        border-radius: 100px !important; /* حواف دائرية كاملة كالكبسولة */
        border: none !important;
        
        /* امتداد عرضي كامل كما طلبت */
        width: 100% !important; 
        height: 100px !important; /* ارتفاع مريح وواضح */
        
        font-size: 24px !important;
        font-weight: bold !important;
        margin-bottom: 25px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 50px !important; /* مكان الأيقونة من اليسار */
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }

    /* موازنة النص في منتصف المساحة العريضة */
    .stButton > button div p {
        width: 100%;
        text-align: center !important;
        margin-right: 80px !important; /* موازنة لإبقاء النص في المركز */
    }

    /* هيدر الإعدادات */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        margin-bottom: 50px;
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
    # الهيدر: السهم وكلمة Settings باللون الأسود الغامق
    st.markdown("""
        <div class="header-container">
            <div style="position: absolute; left: 2%; font-size: 45px; font-weight: 900; color: #000000; cursor: pointer;"> < </div>
            <h1 style="color: #000000; font-size: 50px; font-weight: bold; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # المسافات الفارغة لإبعاد النص عن الأيقونة في المساحة العريضة
    spacer = "&nbsp;" * 50

    if st.button(f"🔒 {spacer} Change Password"): nav('password')
    if st.button(f"🌐 {spacer} Change Language"): nav('language')
    if st.button(f"⭐ {spacer} &nbsp;&nbsp;&nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {spacer} &nbsp;&nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير ممتد أيضاً ليتناسق مع التصميم
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ &nbsp;&nbsp; Report"): nav('report')
    with col2:
        if st.button("✉️ &nbsp;&nbsp; Contact"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 40px; margin-top: 50px;'>Change Password</h1>", unsafe_allow_html=True)
