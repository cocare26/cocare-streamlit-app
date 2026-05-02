import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. تنسيق الـ CSS (التعديلات الضخمة)
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #cbdbe5;
    }

    /* تنسيق الأزرار لتكون ضخمة جداً وكبيرة العرض */
    .stButton > button {
        background-color: #f8f1e5 !important; /* لون فاتح مريح للعين */
        color: #000000 !important; /* النص باللون الأسود */
        border-radius: 50px !important; /* حواف دائرية جداً */
        border: none !important;
        width: 100% !important; /* عرض كامل من البداية للنهاية */
        height: 90px !important; /* ارتفاع ضخم للبوكس */
        font-size: 22px !important; /* حجم خط كبير */
        font-weight: bold !important;
        box-shadow: 0 6px 12px rgba(0,0,0,0.1) !important; /* ظل لإعطاء عمق */
        margin-bottom: 20px !important;
        transition: 0.3s;
    }

    /* تأثير عند تمرير الماوس */
    .stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 16px rgba(0,0,0,0.15) !important;
    }

    /* تحسين شكل النصوص داخل الأزرار */
    .stButton > button p {
        font-size: 22px !important;
        font-weight: bold !important;
    }

    /* تنسيق الحاوية الرئيسية لتوسيع المحتوى */
    .block-container {
        max-width: 850px !important;
        padding-top: 2rem !important;
    }

    /* تنسيق خانات الإدخال */
    .stTextInput > div > div > input {
        border-radius: 20px !important;
        height: 50px !important;
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
    # العنوان: السهم < وكلمة Settings كلاهما باللون الأسود وحجم كبير
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 35px; direction: ltr;">
            <div style="padding-left: 10px;">
                <span style="font-size: 40px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -50px;">
                <h1 style="color: #000000; margin: 0; font-weight: bold; font-size: 36px;">Settings</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # الأزرار الضخمة (كل واحد يأخذ عرض الشاشة بالكامل)
    if st.button("🔒   Change Password"): nav('password')
    if st.button("🌐   Change Language"): nav('language')
    if st.button("⭐   Rate App"): nav('rate')
    if st.button("🚪   Log Out"): st.write("Logged Out!")
    
    # Report و Contact تحت بعض وبنفس الحجم الضخم
    if st.button("⚠️   Report"): nav('report')
    if st.button("✉️   Contact"): nav('contact')

# --- باقي الشاشات ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='color: black; text-align: center;'>Change Password</h2>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Confirm New Password", type="password")
    if st.button("Save Password"):
        st.success("Saved!")
        nav('main')

elif st.session_state.page == 'language':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='color: black; text-align: center;'>Change Language</h2>", unsafe_allow_html=True)
    st.button("English (Active)")
    st.button("العربية")

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='color: black; text-align: center;'>Report a Problem</h2>", unsafe_allow_html=True)
    st.text_area("How can we help?", height=150)
    if st.button("Submit Report"):
        st.success("Sent!")
        nav('main')

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.markdown("<h2 style='color: black; text-align: center;'>Contact Us</h2>", unsafe_allow_html=True)
    st.info("📧 Email: Co.Care26@gmail.com")
    st.info("📞 Phone: +962 79 123 4657")
