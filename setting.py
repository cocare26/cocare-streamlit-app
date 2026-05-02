import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    .block-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
        margin: 0px !important;
    }

    /* تنسيق الأزرار الأساسي */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; 
        border-radius: 0px !important; 
        border: none !important;
        width: 100% !important;
        height: 70px !important;
        font-size: 19px !important;
        font-weight: bold !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        margin-bottom: 2px !important; 
        padding: 0 25px !important;
    }

    /* أول 3 أزرار: محاذاة النص لليمين أقصى حد مع السهم */
    .right-align-btn > div > button {
        display: flex !important;
        flex-direction: row-reverse !important; /* عكس الاتجاه ليكون النص يمين */
        justify-content: space-between !important;
        text-align: right !important;
    }

    /* تنسيق الأعمدة للسطر الأخير */
    [data-testid="column"] {
        padding-left: 0px !important;
        padding-right: 0px !important;
    }
    [data-testid="stHorizontalBlock"] {
        gap: 2px !important;
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
    
    # أول 3 بوكسات (محاذاة لليمين أقصى حد)
    st.markdown('<div class="right-align-btn">', unsafe_allow_html=True)
    if st.button(">                                                                                                 🔒 Change Password"): nav('password')
    if st.button(">                                                                                                 🌐 Change Language"): nav('language')
    if st.button(">                                                                                                                 ⭐ Rate App"): nav('rate')
    st.markdown('</div>', unsafe_allow_html=True)

    # البوكس الرابع (Log Out)
    if st.button("🚪 Log Out                                                                                                                       >"): st.write("Logged Out!")
    
    # السطر الأخير (Report و Contact بجانب بعض)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem   >"): nav('report')
    with col2:
        if st.button("✉️ Contact Us   >"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Change Password</h2>", unsafe_allow_html=True)

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align:center;'>Report a Problem</h2>", unsafe_allow_html=True)
