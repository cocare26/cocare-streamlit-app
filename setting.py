import streamlit as st
import streamlit.components.v1 as components

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. قراءة الرابط (navigation)
query_params = st.query_params

if "page" in query_params:
    st.session_state.page = query_params.get("page")
elif 'page' not in st.session_state:
    st.session_state.page = 'main'

# زر الرجوع
def go_back():
    st.query_params.clear()
    st.session_state.page = 'main'
    st.rerun()

# =====================================
# 🔥 الصفحات (هون المكان المهم)
# =====================================

if st.session_state.page == "Change_password":
    st.title("🔒 Change Password")

    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Re-write Password", type="password")

    if st.button("Save"):
        st.success("Saved")

    if st.button("Back to Settings"):
        go_back()

    st.stop()


if st.session_state.page == "Change_language":
    st.title("🌐 Change Language")

    st.button("English")
    st.button("العربية")

    if st.button("Back to Settings"):
        go_back()

    st.stop()

# =====================================
# 🔥 واجهة Settings (HTML)
# =====================================

st.markdown("""
<style>
.block-container{
    max-width:350px !important;
    margin:auto !important;
    padding:30px !important;
    border-radius:42px;
    background:linear-gradient(160deg, #d6ecff, #bfe3ff, #eaf6ff);
}
</style>
""", unsafe_allow_html=True)

components.html("""
<html>
<body style="margin:0;font-family:sans-serif">

<div style="max-width:300px;margin:auto">

<h2 style="text-align:center;">Settings</h2>

<div onclick="goPage('Change_password')" style="background:white;padding:15px;border-radius:30px;margin:10px;cursor:pointer">
🔒 Change Password ›
</div>

<div onclick="goPage('Change_language')" style="background:white;padding:15px;border-radius:30px;margin:10px;cursor:pointer">
🌐 Change Language ›
</div>

<div onclick="goPage('Rate_app')" style="background:white;padding:15px;border-radius:30px;margin:10px">
⭐ Rate App ›
</div>

<div onclick="goPage('logout')" style="background:white;padding:15px;border-radius:30px;margin:10px">
🚪 Log Out ›
</div>

</div>

<script>
function goPage(p){
    window.top.location.href = window.top.location.pathname + "?page=" + p;
}
</script>

</body>
</html>
""", height=500)
