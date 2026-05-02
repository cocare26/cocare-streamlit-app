import streamlit as st

# 1. إعدادات الصفحة - جعل العرض ممتداً لأقصى حد ممكن
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تنسيق الـ CSS المتقدم للوصول للحواف
st.markdown("""
    <style>
    /* لون الخلفية الأساسي */
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء أي هوامش جانبية للشاشة تماماً لتصل الأزرار للحواف */
    .block-container {
        max-width: 100% !important; 
        padding-left: 0px !important;
        padding-right: 0px !important;
        padding-top: 20px !important;
    }

    /* تصميم الأزرار - ممتدة عرضياً بالكامل (Full Width) */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; 
        border-radius: 100px !important; /* شكل الكبسولة */
        border: none !important;
        
        /* امتداد عرضي كامل يغطي الشاشة من اليمين لليسار */
        width: 100% !important; 
        height: 110px !important; /* ارتفاع ضخم وواضح */
        
        font-size: 26px !important;
        font-weight: 900 !important;
        margin-bottom: 20px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        padding-left: 60px !important; /* مكان الأيقونة من اليسار */
        box-shadow: 0 4px 20px rgba(0,0,0,0.06) !important;
    }

    /* جعل النص في منتصف المساحة العريضة جداً */
    .stButton > button div p {
        width: 100%;
        text-align: center !important;
        margin-right: 100px !important; /* موازنة دقيقة لمركزية النص */
    }

    /* الهيدر: Settings والسهم */
    .header-full {
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        margin-bottom: 60px;
        padding: 0 30px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر: السهم أقصى اليسار و Settings في المنتصف (كلهم بالأسود)
    st.markdown("""
        <div class="header-full">
            <div style="position: absolute; left: 30px; font-size: 50px; font-weight: 900; color: #000000; cursor: pointer;"> < </div>
            <h1 style="color: #000000; font-size: 55px; font-weight: 900; margin: 0;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # مسافات هائلة لجعل النص يتوسط العرض الكامل
    mega_spacer = "&nbsp;" * 65

    if st.button(f"🔒 {mega_spacer} Change Password"): nav('password')
    if st.button(f"🌐 {mega_spacer} Change Language"): nav('language')
    if st.button(f"⭐ {mega_spacer} &nbsp;&nbsp;&nbsp; Rate App"): nav('rate')
    if st.button(f"🚪 {mega_spacer} &nbsp;&nbsp;&nbsp; Log Out"): st.write("Logged Out!")
    
    # السطر الأخير (ممتد أيضاً)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ &nbsp;&nbsp; Report"): nav('report')
    with col2:
        if st.button("✉️ &nbsp;&nbsp; Contact"): nav('contact')

# --- الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: #000; font-size: 50px; margin-top: 100px;'>Change Password</h1>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: #000; font-size: 50px; margin-top: 100px;'>Change Language</h1>", unsafe_allow_html=True)
