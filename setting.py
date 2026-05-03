import streamlit as st

st.set_page_config(page_title="Settings", layout="centered")

# 1. إدارة الحالة (Navigation State)
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def navigate_to(page_name):
    st.session_state.page = page_name

# 2. التنسيق (CSS) لتحويل أزرار ستريمليت لتشبه تصميمك
st.markdown("""
<style>
    /* الخلفية العامة */
    [data-testid="stAppViewContainer"] { background:#eef2f7; }
    
    .block-container {
        max-width:400px !important;
        background: linear-gradient(160deg, #d6ecff 0%, #bfe3ff 45%, #eaf6ff 100%);
        border-radius: 42px;
        padding: 40px 20px !important;
    }

    /* تنسيق زر ستريمليت ليصبح مثل الـ setting-item */
    div.stButton > button {
        width: 100%;
        background-color: white !important;
        color: #0f2446 !important;
        border-radius: 100px !important;
        border: none !important;
        padding: 20px 25px !important;
        font-weight: 600 !important;
        text-align: right !important; /* النص يمين */
        box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
        display: flex !important;
        justify-content: flex-end !important;
        transition: 0.3s !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 15px rgba(0,0,0,0.12) !important;
        background-color: #f8f9fa !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. عرض الصفحات
if st.session_state.page == "main":
    st.markdown("<h2 style='text-align: center; color: #0f2446; margin-bottom:30px;'>Settings</h2>", unsafe_allow_html=True)
    
    # الأزرار (أيقونة وهمية عبر Markdown قبل الزر أو داخل الزر إذا دعمت المكتبة)
    # ملاحظة: ستريمليت لا يدعم الأيقونات داخل الزر بسهولة إلا عبر Unicode أو رموز
    
    if st.button("Change Password  ›"):
        navigate_to("change_password")
        st.rerun()

    if st.button("Change Language  ›"):
        navigate_to("change_language")
        st.rerun()

    if st.button("Rate App  ›"):
        pass

    if st.button("Log Out  ›"):
        pass

    # الصف السفلي (Report / Contact)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Report ›"):
            pass
    with col2:
        if st.button("Contact ›"):
            pass

elif st.session_state.page == "change_password":
    st.markdown("### 🔒 Change Password")
    new_pass = st.text_input("New Password", type="password")
    if st.button("Save"):
        st.success("Updated!")
    if st.button("← Back"):
        navigate_to("main")
        st.rerun()
