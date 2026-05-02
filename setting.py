import streamlit as st

# 1. إعدادات الصفحة - وضع العرض الواسع ضروري جداً هنا
st.set_page_config(page_title="Settings UI", layout="wide")

# 2. تنسيق الـ CSS (إلغاء الحواف الجانبية تماماً)
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #cbdbe5;
    }

    /* هذا الجزء هو السر: إلغاء أي فراغات تضعها منصة ستريم ليت تلقائياً */
    .main .block-container {
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
        margin: 0px !important;
    }

    /* تنسيق الأزرار لتكون "طويلة بالعرض" من الحافة للحافة */
    .stButton > button {
        background-color: #f8f1e5 !important; 
        color: #000000 !important; 
        border-radius: 0px !important; /* تصفير الحواف يجعلها تلتحم بجوانب الشاشة */
        border: none !important;
        width: 100% !important; /* ملء كامل المساحة المتاحة */
        height: 100px !important; /* ارتفاع ضخم */
        font-size: 26px !important; 
        font-weight: bold !important;
        margin: 0px !important; /* إلغاء أي هوامش جانبية للزر */
        padding: 0px !important;
        display: block !important;
        box-shadow: none !important; /* إلغاء الظل لتبدو كشريط مسطح ممتد */
        border-bottom: 1px solid #d1c7b7 !important; /* خط بسيط للفصل بين الأشرطة */
    }

    /* تكبير حجم النص داخل الزر */
    .stButton > button p {
        font-size: 26px !important;
        font-weight: bold !important;
    }

    /* تنسيق رأس الصفحة (Settings) ليكون له مسافة بسيطة عن الحافة */
    .header-style {
        padding: 20px;
        background-color: transparent;
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
    # العنوان مع مسافة جانبية بسيطة ليكون مرتباً
    st.markdown("""
        <div class="header-style" style="display: flex; align-items: center; justify-content: flex-start; direction: ltr;">
            <div style="padding-left: 10px;">
                <span style="font-size: 40px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -50px;">
                <h1 style="color: #000000; margin: 0; font-weight: bold; font-size: 38px;">Settings</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # أزرار ممتدة من بداية السطر لنهايته تماماً
    if st.button("🔒   Change Password"): nav('password')
    if st.button("🌐   Change Language"): nav('language')
    if st.button("⭐   Rate App"): nav('rate')
    if st.button("🚪   Log Out"): st.write("Logged Out!")
    if st.button("⚠️   Report"): nav('report')
    if st.button("✉️   Contact"): nav('contact')

# --- باقي الشاشات (كمثال) ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='text-align: center; color: black;'>Change Password</h2>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.button("Save")
