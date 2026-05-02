import streamlit as st

# 1. إعدادات الصفحة - جعل العرض واسع جداً
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم للوصول للحواف
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية تماماً لتصل الأزرار لنهاية الشاشة */
    .block-container {
        max-width: 100% !important; 
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 20px !important;
    }

    /* تصميم الزر الممتد (الكبسولة العريضة جداً) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; /* حواف دائرية كاملة */
        border: none !important;
        
        /* امتداد عرضي كامل يغطي الرسم الأحمر */
        width: 100% !important; 
        height: 90px !important; 
        
        font-size: 22px !important;
        font-weight: bold !important;
        margin-bottom: 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 50px !important; /* مكان الأيقونة */
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    }

    /* دفع النص لليمين لزيادة المسافة عن الأيقونة */
    .stButton > button div p {
        width: 100%;
        text-align: left !important;
        margin-left: 100px !important; /* زيادة المسافة بين الإيموجي والنص */
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
    # الهيدر باللون الأسود الداكن
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; position: relative; margin-bottom: 50px; padding: 0 40px;">
            <div style="position: absolute; left: 40px; font-size: 40px; font-weight: 900; color: #000; cursor: pointer;"> < </div>
            <h1 style="color: #000; font-size: 45px; font-weight: bold; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # استخدام فراغات إضافية لجعل المسافة "أطول" كما في الرسم
    extra_gap = "&nbsp;" * 20

    if st.button(f"🔒 {extra_gap} Change Password"): nav('password')
    if st.button(f"🌐 {extra_gap} Change Language"): nav('language')
    if st.button(f"⭐ {extra_gap} &nbsp;&nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {extra_gap} &nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير ممتد أيضاً
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ &nbsp; Report a Problem"): nav('report')
    with col2:
        if st.button("✉️ &nbsp; Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 40px;'>Change Password</h1>", unsafe_allow_html=True)
