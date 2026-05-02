import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. إدارة حالة التنقل (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (تكبير ضخم للخطوط + التصميم)
st.markdown("""
<style>
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
}

[data-testid="stAppViewContainer"] { 
    background: #eef2f7; 
}

/* البوكس الرئيسي */
.block-container {
    max-width: 90% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 50px 60px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 50px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
}

/* تصميم الأزرار - تكبير ضخم جداً */
div.stButton > button {
    width: 100% !important;
    height: 90px !important; /* ارتفاع أكبر للخط الضخم */
    border-radius: 100px !important; 
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    font-weight: 900 !important;
    font-size: 32px !important; /* خط ضخم للأزرار */
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 50px !important;
    padding-right: 50px !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12) !important;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2) !important;
}

/* عنوان السيتنج - ضخم جداً ومزاح لليمين */
.settings-header {
    color: #000000 !important; 
    font-weight: 950;
    font-size: 85px; /* حجم ضخم جداً للعنوان */
    margin: 0;
    flex-grow: 1;
    text-align: center;
    padding-left: 70px; 
}

/* أيقونة السهم الجانبي - ضخمة */
.back-arrow {
    font-size: 80px; 
    font-weight: 900; 
    color: #000000; 
}

</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    # هيدر الصفحة مع الخط العملاق
    st.markdown("""
        <div style="display: flex; align-items: center; margin-bottom: 70px; padding-left: 20px;">
            <span class="back-arrow">‹</span>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار بمسافات تتناسب مع حجم الخط
    def make_btn(emoji, label, page, gap_size):
        # قللت الـ gap قليلاً لأن الحروف الكبيرة تأخذ مساحة عرضية أكبر
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # أول زرين: مسافة 50 (كافية للخط الضخم)
    make_btn("🔒", "Change Password", "password", gap_size=50)
    make_btn("🌐", "Change Language", "language", gap_size=50)
    
    # الزرين الأخيرين: مسافة 65
    make_btn("⭐", "Rate App", "rate", gap_size=65)
    make_btn("🚪", "Log Out", "main", gap_size=65)
    
    st.markdown("<br><br>", unsafe_allow_html=True)

    # السطر الأخير (خط ضخم أيضاً)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report ›"): nav('report')
    with col2:
        if st.button("✉️ Contact ›"): nav('contact')

# الشاشات الفرعية
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 70px;'>Change Password</h1>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center; color: black; font-size: 70px;'>Change Language</h1>", unsafe_allow_html=True)
