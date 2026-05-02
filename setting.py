import streamlit as st

# 1. إعدادات الصفحة - جعل العرض ممتداً
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS لتوسيع الأزرار عرضياً
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* الحاوية المركزية - جعلتها أعرض لتسمح للزر بالامتداد كما في رسمك */
    .block-container {
        max-width: 90% !important; 
        padding-top: 30px !important;
    }

    /* تعديل العرض (Width) ليكون ممتداً جداً */
    .stButton > button {
        background-color: #f8f9fa !important;
        color: #000000 !important; 
        border-radius: 80px !important; /* حواف دائرية انسيابية */
        border: none !important;
        
        /* جعل الزر يمتد عرضياً */
        width: 100% !important; 
        height: 100px !important; /* طول مناسب */
        
        font-size: 24px !important;
        font-weight: 800 !important;
        margin-bottom: 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 60px !important; /* إزاحة الإيموجي للداخل أكثر */
        box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
    }

    /* موازنة النص في منتصف المساحة العريضة */
    .stButton > button div p {
        width: 100%;
        text-align: center !important;
        margin-right: 100px !important; 
    }

    /* الهيدر */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        margin-bottom: 50px;
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
    # الهيدر باللون الأسود
    st.markdown("""
        <div class="header-container">
            <div style="position: absolute; left: 5%; font-size: 45px; font-weight: 900; color: #000000; cursor: pointer;"> < </div>
            <h1 style="color: #000000; font-size: 45px; font-weight: bold; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # مسافة كبيرة بين الإيموجي والنص لتناسب العرض الجديد
    spacer = "&nbsp;" * 40

    if st.button(f"🔒 {spacer} Change Password"): nav('password')
    if st.button(f"🌐 {spacer} Change Language"): nav('language')
    if st.button(f"⭐ {spacer} &nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {spacer} &nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير ممتد أيضاً
    col1, col2 = st.columns(2)
    with col1:
        if st.button(f"⚠️ &nbsp; Report"): nav('report')
    with col2:
        if st.button(f"✉️ &nbsp; Contact"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black;'>Change Password</h1>", unsafe_allow_html=True)
