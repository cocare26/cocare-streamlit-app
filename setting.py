import streamlit as st

# 1. إعدادات الصفحة - عرض كامل
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الحواف الجانبية تماماً */
    .block-container {
        max-width: 100% !important; 
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 10px !important;
    }

    /* هيدر الإعدادات: سهم Settings */
    .header-style {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        /* مسافة ضخمة بين السهم والكلمة */
        gap: 250px; 
        margin-bottom: 120px;
        padding-left: 50px;
    }

    /* تصميم الأزرار (كبسولة ضخمة وطويلة جداً) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; 
        border: none !important;
        width: 100% !important;
        height: 120px !important; /* زيادة الطول الرأسي (الارتفاع) */
        font-size: 28px !important; /* تكبير الخط */
        font-weight: 900 !important;
        margin-bottom: 30px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        padding: 0 60px !important;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06) !important;
    }

    /* السطر الأخير */
    [data-testid="column"] {
        padding: 0 15px !important;
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
    # الهيدر
    st.markdown("""
        <div class="header-style">
            <span style="font-size: 60px; font-weight: 900; color: #000; cursor: pointer;">‹</span>
            <span style="font-size: 55px; font-weight: 900; color: #000;">Settings</span>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة لبناء الزر بمسافات (Nbsp) "طويلة جداً"
    # زدنا عدد المسافات لتدفع النص لليمين بقوة
    def mega_button(emoji, label, page):
        # 40 مسافة برمجية لزيادة طول الفراغ
        long_space = "&nbsp;" * 40
        arrow_space = "&nbsp;" * 20
        if st.button(f"{emoji} {long_space} {label} {arrow_space} ›"):
            nav(page)

    # قائمة الأزرار الرئيسية الممتدة
    mega_button("🔒", "Change Password", "password")
    mega_button("🌐", "Change Language", "language")
    mega_button("⭐", "Rate App", "rate")
    mega_button("🚪", "Log Out", "main")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير (Report & Contact)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp;&nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- شاشات فرعية ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; font-size:60px; margin-top:100px;'>Change Password</h1>", unsafe_allow_html=True)
