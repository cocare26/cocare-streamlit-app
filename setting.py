import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# كود الـ CSS المخصص للتطابق مع الصورة
st.markdown("""
    <style>
    /* 1. تغيير خلفية التطبيق كاملة للون بيبي بلو */
    .stApp {
        background-color: #d1e1e0;
    }

    /* 2. تنسيق الأزرار لتصبح دائرية جداً (Pill Shape) وبيضاء */
    div.stButton > button {
        background-color: #f8f4eb !important; /* لون أبيض مائل للكريمي قليلاً كما في الصورة */
        color: #4a4a4a !important;
        border-radius: 50px !important; /* حواف دائرية بالكامل */
        border: none !important;
        width: 100% !important;
        height: 60px !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
        margin-bottom: 15px !important;
        display: flex;
        justify-content: space-between;
        padding: 0 25px !important;
    }

    /* 3. تنسيق النص داخل الأزرار ليكون عمودياً أو مائلاً كما في الصورة إذا لزم، 
       لكن سنبقيه أفقياً لسهولة القراءة مع محاكاة التباعد */
    .stButton button p {
        margin: 0;
        width: 100%;
        text-align: left;
    }

    /* 4. إخفاء شريط التنقل العلوي لـ Streamlit لزيادة النقاء */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* 5. تنسيق العنوان */
    .settings-title {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        margin-bottom: 30px;
        text-align: left;
    }
    
    /* 6. تنسيق السهم الأسود (محاكاة) */
    .arrow {
        float: right;
        color: black;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    # أيقونة الرجوع والعنوان كما في الصورة
    st.markdown("<div class='settings-title'><span style='font-size:20px;'> < </span> Settings</div>", unsafe_allow_html=True)
    
    # الأزرار مع إضافة رمز السهم الأسود في نهاية كل نص
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.toast("Logged Out")
    
    # الأزرار السفلية (الأسهم التي تفتح صفحات)
    col1, col2, col3 = st.columns([1,1,1])
    with col3: # جهة اليمين كما طلبت
        if st.button("➡️"): nav('report')

# --- صفحات فرعية (أمثلة) ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("### Change Password")
    st.text_input("New Password", type="password")
    if st.button("Save"): nav('main')

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("### Report Details")
    st.write("This is a new page for reports.")
