import streamlit as st

# 1. إعدادات الصفحة - عرض واسع جداً
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS (التركيز على التنحيف والامتداد لليمين)
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية تماماً لتصل الأزرار للحواف */
    .block-container {
        max-width: 100% !important; 
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 20px !important;
    }

    /* الهيدر */
    .header-style {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        gap: 100px; 
        margin-bottom: 80px;
        padding-left: 40px;
    }

    /* تصميم الزر (نحيف جداً + ممتد لليمين) */
    .stButton > button {
        background-color: #ffffff !important;
        color: #000000 !important; 
        border-radius: 100px !important; 
        border: none !important;
        
        /* جعل الزر ممتد عرضياً بالكامل */
        width: 100% !important; 
        
        /* "تنحيف" الزر (تقليل الارتفاع) */
        height: 60px !important; 
        
        font-size: 20px !important;
        font-weight: bold !important;
        margin-bottom: 15px !important;
        display: flex !important;
        align-items: center !important;
        
        /* دفع المحتوى للأطراف (الإيموجي يسار والنص يمين) */
        justify-content: space-between !important; 
        
        padding-left: 40px !important;
        padding-right: 40px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05) !important;
    }

    /* السطر الأخير */
    [data-testid="column"] {
        padding: 0 5px !important;
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
            <span style="font-size: 40px; font-weight: 900; color: #000; cursor: pointer;">‹</span>
            <span style="font-size: 40px; font-weight: 900; color: #000;">Settings</span>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة لبناء الزر مع "مسافة هائلة" تدفع النص لآخر اليمين
    def slim_mega_button(emoji, label, page):
        # استخدمنا عدد ضخم من المسافات لضمان وصول النص للطرف اليمين
        huge_gap = "&nbsp;" * 100 
        if st.button(f"{emoji} {huge_gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # قائمة الأزرار النحيفة والممتدة
    slim_mega_button("🔒", "Change Password", "password")
    slim_mega_button("🌐", "Change Language", "language")
    slim_mega_button("⭐", "Rate App", "rate")
    slim_mega_button("🚪", "Log Out", "main")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp;&nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- شاشات فرعية ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Password</h1>", unsafe_allow_html=True)
    
