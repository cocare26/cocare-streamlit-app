import streamlit as st

# 1. إعدادات الصفحة - جعل العرض واسع (Wide Mode) لضمان وصول البوكس للأطراف
st.set_page_config(page_title="Settings UI", layout="wide")

# 2. تنسيق الـ CSS (لجعل البوكسات تمتد من الحافة للحافة)
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #cbdbe5;
    }

    /* إلغاء الهوامش الجانبية لصفحة ستريم ليت لتسمح للأزرار بالتمدد */
    .block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }

    /* تنسيق الأزرار لتمتد من بداية السطر لنهايته */
    .stButton > button {
        background-color: #f8f1e5 !important; 
        color: #000000 !important; 
        border-radius: 0px !important; /* جعل الحواف مستقيمة لتمتد تماماً أو 50px لو تبيها دائرية */
        border: none !important;
        width: 100vw !important; /* عرض كامل الشاشة (Viewport Width) */
        height: 80px !important; 
        font-size: 24px !important; 
        font-weight: bold !important;
        margin-left: 0px !important;
        margin-right: 0px !important;
        margin-bottom: 10px !important;
        display: block !important;
    }

    /* تعديل السهم Settings ليكون متناسق مع العرض الكامل */
    .header-container {
        padding: 20px;
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
    # العنوان
    st.markdown("""
        <div class="header-container" style="display: flex; align-items: center; justify-content: flex-start; direction: ltr;">
            <div style="padding-left: 20px;">
                <span style="font-size: 40px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -50px;">
                <h1 style="color: #000000; margin: 0; font-weight: bold; font-size: 35px;">Settings</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # أزرار تمتد من بداية السطر لنهايته (Full Width)
    st.button("🔒   Change Password", on_click=lambda: nav('password'))
    st.button("🌐   Change Language", on_click=lambda: nav('language'))
    st.button("⭐   Rate App", on_click=lambda: nav('rate'))
    st.button("🚪   Log Out")
    
    st.button("⚠️   Report", on_click=lambda: nav('report'))
    st.button("✉️   Contact", on_click=lambda: nav('contact'))

# --- شاشة تغيير كلمة المرور ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='color: black; text-align: center;'>Change Password</h2>", unsafe_allow_html=True)
    # هنا المدخلات ستأخذ أيضاً العرض الكامل
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    if st.button("Save Now"):
        st.success("Done!")
        nav('main')

# --- باقي الشاشات ---
elif st.session_state.page == 'language':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='color: black; text-align: center;'>Select Language</h2>", unsafe_allow_html=True)
    st.button("English")
    st.button("العربية")
