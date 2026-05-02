import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. إدارة حالة التنقل (Session State) لمنع الأخطاء البرمجية
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (التصميم البصري)
st.markdown("""
<style>
/* تعريف متغيرات الألوان الخاصة بك */
:root {
    --navy: #0f2446;
    --bg1: #d6ecff; 
    --bg2: #bfe3ff; 
    --bg3: #eaf6ff;
}

/* خلفية التطبيق الكلية */
[data-testid="stAppViewContainer"] { 
    background: #eef2f7; 
}

/* تصميم البوكس الرئيسي (مزاح لليمين وممتد) */
.block-container {
    max-width: 80% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 30px 40px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* تصميم الأزرار: نحيفة، خلفية بيضاء، وتوزيع المحتوى لليمين */
div.stButton > button {
    width: 100% !important;
    height: 55px !important; 
    border-radius: 100px !important; 
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 18px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 35px !important;
    padding-right: 35px !important;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
    transition: 0.3s;
}

/* تأثير التمرير (Hover) */
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}

/* تنسيق العناوين */
h1 {
    color: var(--navy);
    font-weight: 900;
}
</style>
""", unsafe_allow_html=True)

# 4. منطق عرض المحتوى
if st.session_state.page == 'main':
    # الهيدر (أيقونة الرجوع + العنوان)
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 40px; margin-bottom: 50px; padding-left: 20px;">
            <span style="font-size: 40px; font-weight: 900; color: #0f2446; cursor: pointer;">‹</span>
            <h1 style="margin: 0; font-size: 38px; color: #0f2446; font-weight: 900;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة لبناء الأزرار بمسافات داخلية متغيرة
    def make_btn(emoji, label, page, gap_size):
        # المسافة (Nbsp) هي التي تحدد مدى "طول" الزر
        gap = "&nbsp;" * gap_size 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # الأزرار العلوية: مسافة 100 (أقصر قليلاً بناءً على طلبك)
    make_btn("🔒", "Change Password", "password", gap_size=100) 
    make_btn("🌐", "Change Language", "language", gap_size=100) 
    
    # الأزرار السفلية: مسافة 145 (طول كامل ممتد لليمين)
    make_btn("⭐", "Rate App", "rate", gap_size=145)
    make_btn("🚪", "Log Out", "main", gap_size=145)
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير (أزرار التواصل والتقارير)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- أمثلة على الشاشات الفرعية ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Password</h1>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Language</h1>", unsafe_allow_html=True)
