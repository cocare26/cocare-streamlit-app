import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (بناءً على اعتماداتك الأخيرة)
st.markdown("""
<style>
/* 🎯 الألوان الأساسية المعتمدة */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* 📦 الكارد الرئيسي (عرض 420px حسب الاعتمادات) */
.block-container{
    max-width:420px !important;
    margin:auto !important;
    padding:25px 30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    margin-top: 20px !important;
}

/* 🧠 الهيدر (متناسق مع الحجم الجديد) */
.header-container {
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 35px;
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
    font-size: 22px;
    color: var(--navy);
}

/* 🔘 الأزرار الأساسية (تعديل لتناسب توزيع الإيموجي والنص) */
div.stButton > button {
    width: 100% !important;
    height: 50px !important;
    border-radius: 25px !important; /* حواف الأزرار المعتمدة */
    border: none !important;
    background: white !important; /* خلفية بيضاء للأزرار الداخلية */
    color: var(--navy) !important;
    margin-bottom: 10px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    transition: 0.3s ease;
}

/* 🎯 توزيع العناصر داخل الزر (إيموجي يسار .. مسافة .. نص يمين) */
div.stButton > button p {
    display: flex !important;
    width: 100% !important;
    align-items: center !important;
    justify-content: space-between !important; /* المسافة الطويلة بينهم */
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 15px !important;
    padding: 0 10px !important;
}

/* ✨ تأثير الـ Hover المعتمد */
div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,.1) !important;
    background: #f8f9fa !important;
}

/* 🧾 تنسيق خاص لزر اللوج أوت أو الأزرار الملونة إذا رغبت */
/* يمكنك تفعيل التدرج المعتمد لزر معين هنا */

</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى بناءً على الصفحة الحالية
if st.session_state.page == 'main':
    # هيدر الإعدادات
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # بناء الأزرار بنفس الترتيب المعتمد (الإيموجي سيظهر يساراً والنص يميناً بسبب الـ CSS)
    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): nav('main')
    
    # فاصل بسيط
    st.markdown("<div style='margin: 15px 0;'></div>", unsafe_allow_html=True)

    # أزرار السطر الأخير
    if st.button("⚠️ Report a Problem"): nav('report')
    if st.button("✉️ Contact Us"): nav('contact')

# الشاشات الفرعية (أمثلة)
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("### Change Password")
    st.text_input("New Password", type="password")
    st.button("Update")

elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.markdown("### Report a Problem")
    st.text_area("How can we help?", height=150)
    st.button("Send Report")
