import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS المدمج والاحترافي
st.markdown("""
<style>
/* 🎯 الألوان والمتغيرات */
:root {
    --navy: #0f2446;
    --accent: #2f80ed;
    --accent2: #1c6fa4;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"] { 
    background: #eef2f7; 
}

/* 📦 الكارد الرئيسي (البوكس) */
.block-container {
    max-width: 450px !important;
    margin: auto !important;
    padding: 30px 40px !important;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

/* 🧠 العناوين */
h1, h2, h3 {
    color: var(--navy);
    text-align: center;
    font-weight: 900;
}

/* 🧾 تنسيق حقول الإدخال (Inputs) */
div[data-testid="stTextInput"] input {
    border-radius: 25px !important;
    height: 44px;
    border: none !important;
    padding-left: 20px;
    background: rgba(255, 255, 255, 0.95) !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}

/* 📍 تنسيق القوائم المنسدلة (Selectbox) */
div[data-testid="stSelectbox"] > div {
    border-radius: 25px !important;
    background: white !important;
    border: none !important;
}

/* 🔘 تصميم الأزرار (أزرار التنقل الرئيسية) */
div.stButton > button {
    width: 100% !important;
    height: 55px !important; 
    border-radius: 100px !important; 
    border: none !important;
    background: white !important; /* لون الأزرار في القائمة الرئيسية */
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 17px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 25px !important;
    padding-right: 25px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    transition: 0.3s;
}

/* ✨ تأثير الحوم (Hover) */
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 18px rgba(0,0,0,0.15) !important;
}

/* 🔙 تصميم الهيدر (العنوان والسهم) */
.settings-header {
    color: #000000 !important; 
    font-weight: 900 !important;
    font-size: 45px !important;
    margin: 0 !important;
    flex-grow: 1;
    text-align: center;
}

.back-arrow {
    font-size: 40px !important; 
    font-weight: 900 !important; 
    color: #000000 !important;
    cursor: pointer;
}

/* إخفاء عناصر Streamlit غير الضرورية */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى (التنقل بين الصفحات)
if st.session_state.page == 'main':
    # هيدر صفحة الإعدادات
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 30px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة الأزرار
    def make_btn(emoji, label, target_page, spaces):
        if st.button(f"{emoji} {'&nbsp;'*spaces} {label} {'&nbsp;'*spaces} ›"):
            nav(target_page)

    # عرض الأزرار
    make_btn("🔒", "Change Password", "password", 15)
    make_btn("🌐", "Change Language", "language", 15)
    make_btn("⭐", "Rate App", "rate", 22)
    make_btn("🚪", "Log Out", "main", 24)
    
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

    # أزرار السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us ›"): nav('contact')

# --- الشاشات الفرعية ---

elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("### Change Password")
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    if st.button("Save Changes"): 
        st.success("Password Updated!")

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("### Change Language")
    st.selectbox("Select Language", ["English", "Arabic", "French"])

elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.markdown("### Report a Problem")
    st.text_input("Describe the issue")
    st.button("Send Report")
