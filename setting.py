import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered") 

# 2. إدارة حالة التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(page_name):
    st.session_state.page = page_name

# 3. تنسيق الـ CSS المطور والموسع
st.markdown("""
<style>
:root{
    --navy:#0f2446;
    --bg1:#d6ecff;
    --bg2:#bfe3ff;
    --bg3:#eaf6ff;
}

[data-testid="stHeader"] {display: none !important;}
[data-testid="stAppViewContainer"]{ background:#eef2f7; }
footer {visibility: hidden;}

/* 📦 الكارد الرئيسي (ضبط العرض ليكون أوسع قليلاً لاستيعاب الأزرار الضخمة) */
.block-container{
    max-width:420px !important;
    margin:auto !important;
    padding:30px !important;
    background:linear-gradient(160deg, var(--bg1) 0%, var(--bg2) 45%, var(--bg3) 100%);
    border-radius:42px;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
    margin-top: 20px !important;
}

/* 🔝 الهيدر */
.header-container {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 35px; position: relative;
}
.back-arrow { position: absolute; left: 0; font-size: 28px; font-weight: bold; color: var(--navy); }
.settings-header { margin: 0; font-weight: 900; font-size: 22px; color: var(--navy); }

/* 🔘 تنسيق الأزرار الأساسي - تم جعلها تمتد لأقصى الحدود */
div.stButton > button {
    width: 100% !important; /* العرض الكامل */
    border-radius: 25px !important;
    border: none !important;
    background: white !important;
    color: var(--navy) !important;
    margin-bottom: 15px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.06) !important;
    transition: 0.3s ease;
    padding: 0 25px !important; /* زيادة المسافة الجانبية لتمتد العناصر للأطراف */
}

/* 🎯 التوزيع: إيموجي أقصى الشمال وكلام أقصى اليمين */
div.stButton > button p {
    display: flex !important;
    justify-content: space-between !important; 
    width: 100% !important;
    align-items: center !important;
    margin: 0 !important;
    font-weight: 800 !important;
    font-size: 16px !important;
    white-space: pre-line !important;
}

/* 📏 الأزرار العلوية: تكبير الطول (العرض أصلاً 100%) */
div.stButton > button { height: 58px !important; }

/* 🛠️ السطر الأخير: تكبير الطول الرأسي ليتناسب مع السطرين */
[data-testid="stHorizontalBlock"] div.stButton > button {
    height: 90px !important; 
    padding: 10px 20px !important;
}

/* تقليل الفراغ بين أعمدة السطر الأخير لزيادة مساحة العرض للبوكسات */
[data-testid="stHorizontalBlock"] {
    gap: 12px !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,.1) !important;
}
</style>
""", unsafe_allow_html=True)

# 4. عرض المحتوى
if st.session_state.page == 'main':
    st.markdown("""
        <div class="header-container">
            <div class="back-arrow">‹</div>
            <p class="settings-header">Settings</p>
        </div>
    """, unsafe_allow_html=True)
    
    # القائمة الرئيسية الممتدة أفقياً
    st.button("🔒 Change Password")
    st.button("🌐 Change Language")
    st.button("⭐ Rate App")
    st.button("🚪 Log Out")
    
    st.markdown("<div style='margin: 5px 0;'></div>", unsafe_allow_html=True)

    # 🎯 السطر الأخير: ممتد بنفس مستوى الأزرار العلوية
    col1, col2 = st.columns([1.2, 1]) 
    
    with col1:
        if st.button("⚠️ Report\nto Problem"): 
            nav('report')
            
    with col2:
        if st.button("✉️ Contact\nUs"): 
            nav('contact')

# الشاشات الفرعية
elif st.session_state.page == 'report':
    if st.button("‹ Back"): nav('main')
    st.write("Report logic...")

elif st.session_state.page == 'contact':
    if st.button("‹ Back"): nav('main')
    st.write("Contact logic...")
