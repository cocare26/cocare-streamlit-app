import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS الموحد بناءً على "Report a Problem"
st.markdown("""
<style>
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
    --gray-color: #808080;
}

[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"] { background: #eef2f7; }
footer {visibility: hidden;}

/* 📦 الكارد الرئيسي (Main Container) المعتمد */
.block-container {
    max-width: 350px !important;    /* العرض النحيف المعتمد */
    margin: auto !important;
    padding: 30px !important;       /* المسافات الداخلية 30px */
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;            /* الحواف 42px */
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    margin-top: 20px !important;
}

/* 🔝 هيدر الإعدادات */
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 40px;
    position: relative;
}

.back-arrow {
    position: absolute; left: 0;
    font-size: 28px;
    font-weight: bold; color: var(--navy);
    cursor: pointer;
}

.settings-header {
    margin: 0;
    font-weight: 900;
    font-size: 20px;
    color: var(--navy);
}

/* 🔘 تصميم الأزرار (نفس ستايل كبسولة الإرسال) */
div.stButton > button {
    background: white !important;
    border-radius: 100px !important;  
    width: 100% !important;
    height: 50px !important;
    padding: 14px 22px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    border: none !important;
    margin-bottom: 12px !important;
    cursor: pointer !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    color: var(--navy) !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}

/* أيقونة السهم في الأزرار لونه أزرق (Accent Blue) */
.btn-arrow {
    color: #2f80ed;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    # هيدر الصفحة بتنسيق "Report a Problem"
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار بنفس توزيع "الطيارة" والنص
    # هنا تم توزيع الرموز والأسهم لتكون الأطراف متباعدة تماماً
    def make_btn(emoji, label, page):
        # نستخدم markdown بداخل الزر لمحاكاة التوزيع
        if st.button(f"{emoji} {label}"):
            nav(page)

    # الأزرار (تأخذ التصميم الموحد تلقائياً من CSS)
    make_btn("🔒", "Change Password", "password")
    make_btn("🌐", "Change Language", "language")
    make_btn("⭐", "Rate App", "rate")
    make_btn("🚪", "Log Out", "main")
    
    # أزرار السطر الأخير
    if st.button("⚠️ Report a Problem"): nav('report')
    if st.button("✉️ Contact Us"): nav('contact')

# الشاشات الفرعية (كمثال)
elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.markdown("<p style='text-align:center; color: #0f2446; font-weight:900;'>Report Page</p>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<p style='text-align:center; color: #0f2446; font-weight:900;'>Language Page</p>", unsafe_allow_html=True)
