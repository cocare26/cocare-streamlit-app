import streamlit as st

# 1. إعدادات الصفحة - عرض واسع
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية للوصول للحواف */
    .block-container {
        max-width: 100% !important; 
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 20px !important;
    }

    /* هيدر الإعدادات مع مسافة سفلية كبيرة */
    .header-section {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        margin-bottom: 100px !important; 
    }

    /* تصميم الأزرار (الكبسولة) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; 
        border: none !important;
        width: 100% !important;
        height: 100px !important; 
        font-size: 26px !important;
        font-weight: 900 !important;
        margin-bottom: 25px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        
        /* المسافة من حافة الزر اليسرى للإيموجي */
        padding-left: 80px !important; 
        
        box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
    }

    /* التحكم في "المسافة الضخمة" بعد الإيموجي وقبل النص */
    .stButton > button div p {
        width: 100%;
        text-align: left !important;
        /* هذه هي المسافة التي طلبتها (بين الإيموجي والكلام) */
        margin-left: 150px !important; 
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
    # الهيدر بالسهم والكلمة (أسود صريح)
    st.markdown("""
        <div class="header-section">
            <div style="position: absolute; left: 40px; font-size: 50px; font-weight: 900; color: #000; cursor: pointer;"> < </div>
            <h1 style="color: #000; font-size: 50px; font-weight: 900; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # قائمة الأزرار
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")
    
    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report Problem"): nav('report')
    with col2:
        if st.button("✉️ Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 45px;'>Change Password</h1>", unsafe_allow_html=True)
