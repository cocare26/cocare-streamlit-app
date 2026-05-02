import streamlit as st

# 1. إعدادات الصفحة - جعل العرض واسع للسماح بالحركة لليمين
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. التنسيق المدمج (ألوانك + حركات الإزاحة والتنحيف)
st.markdown("""
<style>

/* 🎯 ألوانك الأساسية */
:root{
    --navy:#0f2446;
    --accent:#2f80ed;
    --accent2:#1c6fa4;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

/* 📱 خلفية الصفحة */
[data-testid="stAppViewContainer"]{
    background:#eef2f7;
}

/* 📦 البوكس الرئيسي - تم تحريكه لليمين وتنحيف عرضه قليلاً */
.block-container{
    max-width: 80% !important; /* تقليل العرض ليظهر التحرك لليمين */
    margin-left: auto !important;  /* دفع من اليسار */
    margin-right: 2% !important;   /* مسافة بسيطة جداً من اليمين */
    
    padding: 30px 40px;
    background: linear-gradient(160deg,
        var(--bg1) 0%,
        var(--bg2) 45%,
        var(--bg3) 100%
    );
    border-radius: 42px;
    box-shadow: 0 10px 30px rgba(0,0,0,.15);
}

/* 🧠 العناوين */
h1, h2, h3{
    color:var(--navy);
    text-align:center;
    font-weight:900;
}

/* 🔘 الأزرار - تم تنحيفها ومدها لأقصى اليمين */
div.stButton > button{
    width: 100% !important;
    height: 55px !important; /* تنحيف الزر (نحيف جداً وأنيق) */
    border-radius: 100px !important; 
    border: none !important;

    background: white !important;
    color: var(--navy) !important;
    font-weight: bold;
    font-size: 18px !important;

    /* توزيع المحتوى ليكون النص في نهاية اليمين */
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    padding-left: 35px !important;
    padding-right: 35px !important;
    
    box-shadow: 0 4px 10px rgba(0,0,0,0.08) !important;
}

/* ✨ تأثير الـ Hover */
div.stButton > button:hover{
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
    background: #ffffff !important;
}

/* 🧾 Inputs (بناءً على كودك) */
div[data-testid="stTextInput"] input{
    border-radius:25px;
    height:44px;
    border:none !important;
    padding-right:16px;
    background:rgba(255,255,255,0.95);
}

</style>
""", unsafe_allow_html=True)

# 3. إدارة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 4. عرض الصفحة الرئيسية
if st.session_state.page == 'main':
    # الهيدر المنسق (سهم + العنوان)
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: flex-start; gap: 40px; margin-bottom: 50px; padding-left: 20px;">
            <span style="font-size: 40px; font-weight: 900; color: #0f2446; cursor: pointer;">‹</span>
            <h1 style="margin: 0; font-size: 38px;">Settings</h1>
        </div>
    """, unsafe_allow_html=True)
    
    # دالة بناء الأزرار بمسافة داخلية طويلة جداً
    def make_btn(emoji, label, page):
        # المسافة (Nbsp) لضمان دفع النص لليمين
        gap = "&nbsp;" * 110 
        if st.button(f"{emoji} {gap} {label} &nbsp;&nbsp; ›"):
            nav(page)

    make_btn("🔒", "Change Password", "password")
    make_btn("🌐", "Change Language", "language")
    make_btn("⭐", "Rate App", "rate")
    make_btn("🚪", "Log Out", "main")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # السطر الأخير
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚠️ Report a Problem &nbsp; ›"): nav('report')
    with col2:
        if st.button("✉️ Contact Us &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ›"): nav('contact')

# --- شاشات فرعية ---
elif st.session_state.page == 'password':
    if st.button("‹ Back"): nav('main')
    st.markdown("<h1>Change Password</h1>", unsafe_allow_html=True)
