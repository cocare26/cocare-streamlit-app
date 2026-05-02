import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="wide") 

# 2. CSS
st.markdown("""
<style>
.stApp {
    background-color: #cbdbe5;
}

/* عرض كامل */
.block-container {
    max-width: 100% !important; 
    padding-left: 0px !important;
    padding-right: 0px !important;
    padding-top: 20px !important;
}

/* الهيدر */
.header-section {
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    margin-bottom: 100px !important; 
}

/* 🔥 الأزرار الكبيرة */
.stButton > button {
    background-color: #ffffff !important;
    color: #000000 !important; 
    border-radius: 100px !important; 
    border: none !important;
    width: 100% !important;

    height: 120px !important;
    font-size: 28px !important;

    font-weight: 900 !important;
    margin-bottom: 25px !important;

    margin-left: 120px !important;

    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important;
    padding-left: 80px !important; 
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
}

/* 🔥 المسافة بين الإيموجي والكلام */
.stButton > button div p {
    width: 100%;
    text-align: left !important;
    margin-left: 520px !important;
}

/* 🔥 Report + Contact (صغار) */
div[data-testid="column"] .stButton > button {
    height: 55px !important;
    font-size: 15px !important;
    border-radius: 25px !important;
}

/* الأعمدة */
[data-testid="column"] {
    padding: 0 10px !important;
}
</style>
""", unsafe_allow_html=True)

# 3. التنقل
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def nav(p):
    st.session_state.page = p

# 4. الصفحة الرئيسية
if st.session_state.page == 'main':
    st.markdown("""
    <div class="header-section">
        <div style="position:absolute; left:40px; font-size:50px; font-weight:900;"> < </div>
        <h1 style="font-size:50px; font-weight:900;">Settings</h1>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔒 Change Password"): nav('password')
    if st.button("🌐 Change Language"): nav('language')
    if st.button("⭐ Rate App"): nav('rate')
    if st.button("🚪 Log Out"): st.write("Logged Out!")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("⚠️ Report Problem"): nav('report')

    with col2:
        if st.button("✉️ Contact Us"): nav('contact')

# صفحات ثانية
elif st.session_state.page == 'password':
    if st.button("< Back"): nav('main')
    st.markdown("<h1 style='text-align:center;'>Change Password</h1>", unsafe_allow_html=True)
    
