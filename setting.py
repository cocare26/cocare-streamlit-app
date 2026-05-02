import streamlit as st

# 1. إعدادات الصفحة (يجب أن يكون أول سطر في الكود)
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. تهيئة حالة الصفحة (لحماية التطبيق من أخطاء الـ NameError)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS (ألوانك + التعديلات التصميمية)
st.markdown("""
<style>
/* المتغيرات اللونية الخاصة بك */
:root{
    --navy:#0f2446;
    --bg1:#d6ecff; 
    --bg2:#bfe3ff; 
    --bg3:#eaf6ff;
}

/* خلفية التطبيق */
[data-testid="stAppViewContainer"]{ 
    background:#eef2f7; 
}

/* البوكس الرئيسي: ممتد، نحيف، ومزاح لجهة اليمين */
.block-container{
    max-width: 80% !important; 
    margin-left: auto !important;  
    margin-right: 2% !important;   
    padding: 30px 40px;
    background: linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* تصميم الأزرار: نحيفة جداً، بيضاء، والنص في أقصى اليمين */
div.stButton > button{
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

/* تأثير عند تمرير الماوس */
div.stButton > button:hover{
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
    background: #ffffff !important;
}

/* تنسيق العناوين */
h1 {
    color: var(--navy);
    font-weight: 900;
}
</style>
""", unsafe_allow_html=True)

# 4. منطق عرض الصفحات
if st.session_state.page == 'main':
    # هيدر الصفحة (السهم والعنوان)
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 40px; margin-bottom: 50px; padding-left: 20px;">
            <span style="font-size: 40px; font-weight: 900; color: #0f2446; cursor: pointer;">‹</span>
            <h1 style="margin: 0; font-size: 38px;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة موحدة لإنشاء الأزرار بطول ممتد
    def make_btn(emoji, label, page):
        # مسافة 145 لضمان وصول النص للحافة تماماً في كل الأزرار
        gap = "&nbsp;" * 145 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    # عرض الأزرار (كلها بنفس الطول الآن)
    make_btn("🔒", "Change Password", "password")
    make_btn("🌐", "Change Language", "language")
    make_btn("⭐", "Rate App", "rate")
    make_btn("🚪", "Log Out", "main")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير (أزرار التقارير والتواصل)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- الشاشات الفرعية (مثال) ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Password</h1>", unsafe_allow_html=True)

elif st.session_state.page == 'language':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Language</h1>", unsafe_allow_html=True)
