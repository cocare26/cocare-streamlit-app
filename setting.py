import streamlit as st

# 1. إعدادات الصفحة - جعل العرض ممتداً لأقصى حد
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* توسيع الحاوية لتغطية الشاشة بالكامل تقريباً */
    .block-container {
        max-width: 95% !important; 
        padding-top: 20px !important;
        margin: auto !important;
    }

    /* جعل الأزرار ممتدة عرضياً وطولياً بشكل هائل */
    .stButton > button {
        background-color: #f8f9fa !important;
        color: #000000 !important; 
        border-radius: 100px !important; /* حواف دائرية انسيابية جداً */
        border: none !important;
        
        /* امتداد عرضي كامل */
        width: 100% !important; 
        /* زيادة الطول الرأسي (الارتفاع) */
        height: 130px !important; 
        
        font-size: 28px !important; /* تكبير الخط ليتناسب مع الحجم الجديد */
        font-weight: 900 !important;
        margin-bottom: 25px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 80px !important; /* إزاحة الأيقونة للداخل */
        box-shadow: 0 10px 20px rgba(0,0,0,0.08) !important;
        transition: transform 0.2s;
    }

    /* موازنة النص في المنتصف تماماً */
    .stButton > button div p {
        width: 100%;
        text-align: center !important;
        margin-right: 120px !important; 
    }

    /* تعديل الهيدر ليناسب العرض الكبير */
    .header-box {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        margin-bottom: 60px;
        width: 100%;
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
    # الهيدر: السهم والكلمة بالأسود الصريح
    st.markdown("""
        <div class="header-box">
            <div style="position: absolute; left: 2%; font-size: 50px; font-weight: 900; color: #000000; cursor: pointer;"> < </div>
            <h1 style="color: #000000; font-size: 55px; font-weight: bold; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # مسافة هائلة بين الإيموجي والنص (حوالي 60 مسافة)
    huge_space = "&nbsp;" * 60

    if st.button(f"🔒 {huge_space} Change Password"): nav('password')
    if st.button(f"🌐 {huge_space} Change Language"): nav('language')
    if st.button(f"⭐ {huge_space} &nbsp;&nbsp;&nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {huge_space} &nbsp;&nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير (ممتد أيضاً)
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"⚠️ &nbsp;&nbsp;&nbsp; Report Problem"): nav('report')
    with col2:
        if st.button(f"✉️ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Contact Us"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 50px;'>Change Password</h1>", unsafe_allow_html=True)
