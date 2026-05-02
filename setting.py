import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. تنسيق الـ CSS المحدث
st.markdown("""
    <style>
    /* خلفية التطبيق */
    .stApp {
        background-color: #cbdbe5;
    }

    /* تنسيق الأزرار لتكون عريضة جداً (من البداية للنهاية) */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; /* لون النص أسود */
        border-radius: 20px !important;
        border: none !important;
        width: 100% !important; /* هذا السطر يجعل الزر يمتد للعرض الكامل */
        height: 60px !important; /* زيادة الارتفاع قليلاً ليعطي فخامة */
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05) !important;
        margin-bottom: 15px !important;
    }

    /* تحسين شكل المدخلات */
    .stTextInput > div > div > input {
        border-radius: 15px !important;
        border: none !important;
        padding: 12px !important;
    }
    
    .stTextArea > div > div > textarea {
        background-color: #fef8e8 !important;
        border-radius: 20px !important;
        border: none !important;
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
    # العنوان: السهم < وكلمة Settings كلاهما بالأسود
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; margin-bottom: 30px; direction: ltr;">
            <div style="padding-left: 10px;">
                <span style="font-size: 30px; font-weight: bold; color: #000000;"><</span>
            </div>
            <div style="flex-grow: 1; text-align: center; margin-left: -40px;">
                <h2 style="color: #000000; margin: 0; font-weight: bold;">Settings</h2>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # الأزرار الأربعة الأولى (تمتد تلقائياً للعرض الكامل بسبب width: 100% في CSS)
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")
    
    # إذا أردت Report و Contact بجانب بعضهما، نستخدم الأعمدة
    # أما إذا أردتهما كباراً أيضاً، ضع كل واحد في سطر بدون columns
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report"): nav('report')
    with col2:
        if st.button("✉️ Contact"): nav('contact')

# --- باقي الشاشات (تعديل السهم ليصبح متناسقاً) ---
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Change Password</h3>", unsafe_allow_html=True)
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write New Password", type="password")
    if st.button("Save"): nav('main')

elif st.session_state.page == 'language':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Change Language</h3>", unsafe_allow_html=True)
    st.button("English (Active)")
    st.button("العربية")

elif st.session_state.page == 'report':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Report a Problem</h3>", unsafe_allow_html=True)
    st.text_area("Message", value="I need help...")
    if st.button("Send Report"):
        st.success("Report Sent!")
        nav('main')

elif st.session_state.page == 'contact':
    if st.button("< Back"): nav('main')
    st.markdown("<h3 style='color: black;'>Contact Us</h3>", unsafe_allow_html=True)
    st.info("📧 Email: Co.Care26@gmail.com")
    st.info("📞 Phone: +962 79 123 4657")
    
