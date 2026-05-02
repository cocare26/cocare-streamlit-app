import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# التعديلات القوية على الـ CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #cbdbe5;
    }

    /* توسيع الحاوية لتصل للنهاية تقريباً */
    .main-container {
        width: 100%;
        max-width: 500px;
        margin: auto;
    }

    /* تنسيق الأزرار: عرض كامل + سهم أسود بجهة اليسار + تقريب النص */
    .stButton > button {
        background-color: white !important;
        color: #000000 !important; /* نص أسود */
        border-radius: 15px !important;
        border: none !important;
        width: 100% !important; /* تكبير البوكس للنهاية */
        height: 55px !important;
        font-size: 17px !important;
        font-weight: 500 !important;
        text-align: right !important; /* تقريب الحكي لجهة اليمين (العربي) */
        padding-right: 20px !important;
        display: flex !important;
        justify-content: space-between !important; /* توزيع المحتوى */
        align-items: center !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
        margin-bottom: 12px !important;
        flex-direction: row-reverse !important; /* عشان السهم يطلع يسار */
    }

    /* إضافة السهم الأسود يدوياً كأنه أيقونة بجهة اليسار */
    .stButton > button::before {
        content: "←"; 
        font-weight: bold;
        color: black;
        font-size: 20px;
        padding-left: 10px;
    }

    /* تنسيق خاص لشاشة Report و Contact */
    .big-box {
        background-color: white;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        color: black;
        text-align: left; /* تقريب الحكي الإنجليزي */
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }

    .stTextArea > div > div > textarea {
        background-color: #fef8e8 !important;
        border-radius: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# --- الشاشة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h2 style='text-align: center; color: black; margin-bottom: 30px;'>Settings</h2>", unsafe_allow_html=True)
    
    # أزرار بكامل العرض مع الأسهم
    if st.button("Change Password"): nav('password')
    if st.button("Change Language"): nav('language')
    if st.button("Rate App"): nav('rate')
    if st.button("Log Out"): st.write("Done!")
    
    # تكبير Report و Contact
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("⚠️ Report a Problem"): nav('report')
    if st.button("✉️ Contact Us"): nav('contact')

# --- شاشة البلاغات ---
elif st.session_state.page == 'report':
    if st.button("Back"): nav('main')
    st.markdown("<h2 style='color: black;'>Report a Problem</h2>", unsafe_allow_html=True)
    st.text_area("How can we help?", value="I need help...", height=200)
    if st.button("Send Report"):
        st.success("Sent!")
        nav('main')

# --- شاشة التواصل ---
elif st.session_state.page == 'contact':
    if st.button("Back"): nav('main')
    st.markdown("<h2 style='color: black;'>Contact Us</h2>", unsafe_allow_html=True)
    
    # بوكسات كبيرة للتواصل مع سهم
    st.markdown("""
        <div class="big-box"><span>Co.Care26@gmail.com</span><span style="font-weight:bold;">←</span></div>
        <div class="big-box"><span>+962 79 123 4657</span><span style="font-weight:bold;">←</span></div>
    """, unsafe_allow_html=True)
    
