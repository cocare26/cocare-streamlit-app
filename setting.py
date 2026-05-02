import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية تماماً */
    .block-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
        margin: 0px !important;
    }

    /* تنسيق الأزرار (أشرطة كاملة العرض) */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; 
        border-radius: 0px !important; 
        border: none !important;
        width: 100% !important;
        height: 70px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        margin-bottom: 2px !important; 
        display: flex;
        justify-content: space-between; 
        padding: 0 20px !important;
    }

    /* تنسيق خاص للأعمدة لتقليل الفراغ بين الزرين */
    [data-testid="column"] {
        padding-left: 0px !important;
        padding-right: 0px !important;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 2px !important; /* مسافة بسيطة جداً بين زر ريبورت وكونتاكت */
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
    # هيدر الصفحة
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 20px; direction: ltr; padding: 20px;">
            <div style="padding-left: 10px;">
                <span style="font-size: 30px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -40px;">
                <h2 style="color: #000000; margin: 0; font-weight: bold;">Settings</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # القائمة العلوية (أزرار تحت بعض)
    if st.button("🔒 Change Password                                                                                                             >"): nav('password')
    if st.button("🌐 Change Language                                                                                                           >"): nav('language')
    if st.button("⭐ Rate App                                                                                                                     >"): nav('rate')
    if st.button("🚪 Log Out                                                                                                                       >"): st.write("Logged Out!")
    
    # وضع Report a Problem و Contact Us في نفس السطر
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem   >"): nav('report')
    with col2:
        if st.button("✉️ Contact Us   >"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='padding:20px;'>Change Password</h3>", unsafe_allow_html=True)

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='padding:20px;'>Report a Problem</h3>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='padding:20px;'>Contact Us</h3>", unsafe_allow_html=True)
