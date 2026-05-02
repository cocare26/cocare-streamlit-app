import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية تماماً ليمتد البوكس للحواف */
    .block-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
        margin: 0px !important;
    }

    /* تنسيق الزر ليكون صندوق مرن (Flexbox) */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; 
        border-radius: 0px !important; 
        border: none !important;
        width: 100% !important;
        height: 75px !important;
        font-size: 20px !important;
        font-weight: bold !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        margin-bottom: 2px !important; 
        
        /* جعل المحتوى يتوزع بين الطرفين */
        display: flex !important;
        flex-direction: row !important; /* ترتيب أفقي */
        justify-content: space-between !important; /* دفع العناصر للأطراف */
        align-items: center !important;
        padding: 0 30px !important;
    }

    /* التأكد من أن النص يذهب لليمين */
    .stButton > button div p {
        width: 100%;
        text-align: right !important;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-direction: row-reverse; /* عكس الترتيب ليكون الإيموجي يسار والنص يمين */
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
    
    # القائمة الرئيسية (الإيموجي يسار - النص يمين - السهم يمين)
    # ملاحظة: تم ترتيب النص داخل الزر بحيث يظهر الإيموجي أولاً (يسار) ثم النص (يمين)
    if st.button("🔒                                                                                       Change Password >"): nav('password')
    if st.button("🌐                                                                                       Change Language >"): nav('language')
    if st.button("⭐                                                                                                     Rate App >"): nav('rate')
    if st.button("🚪                                                                                                       Log Out >"): st.write("Logged Out!")
    
    # السطر الأخير (قسمين متساويين)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️       Report a Problem >"): nav('report')
    with col2:
        if st.button("✉️               Contact Us >"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='padding:20px; color: black; text-align: right;'>Change Password</h3>", unsafe_allow_html=True)

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='padding:20px; color: black; text-align: right;'>Report a Problem</h3>", unsafe_allow_html=True)

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='padding:20px; color: black; text-align: right;'>Contact Us</h3>", unsafe_allow_html=True)
