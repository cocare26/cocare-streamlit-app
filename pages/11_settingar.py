import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="الإعدادات", layout="centered")

# CSS لإخفاء عناصر ستريمليت والحفاظ على أبعاد الكارد
st.markdown("""
<style>
[data-testid="stAppViewContainer"] { background:#f0f7ff; }
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15);
}
#MainMenu, header, footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# التقاط اسم الصفحة من الرابط للتحويل
page_nav = st.query_params.get("nav", "")
if page_nav:
    st.query_params.clear()
    if page_nav == "logout":
        st.session_state.clear()
        st.switch_page("app.py")
    else:
        st.switch_page(f"pages/{page_nav}.py")

components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family:'Segoe UI', sans-serif; margin:0; background:transparent; direction: rtl; }
        .main-wrapper { width:100%; max-width:380px; display:flex; flex-direction:column; height:550px; }
        .header-container { display:flex; align-items:center; justify-content:center; margin-bottom:35px; position:relative; padding-top:10px; }
        .back-icon { position:absolute; right:0; font-size:28px; font-weight:bold; color:#102646; cursor:pointer; }
        .title { margin:0; font-weight:900; font-size:20px; color:#102646; }
        .setting-item { background:white; border-radius:100px; padding:14px 22px; margin-bottom:15px; display:flex; align-items:center; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.08 ); cursor:pointer; transition:0.3s; }
        .setting-item:hover { transform:translateY(-2px); box-shadow:0 6px 15px rgba(0,0,0,0.12); }
        .item-right { display:flex; align-items:center; gap:12px; }
        .item-right i { color:#102646; font-size:16px; width:20px; text-align:center; }
        .item-text { color:#102646; font-weight:800; font-size:14px; }
        .arrow { color:#102646; font-weight:bold; font-size:18px; }
        .bottom-row { display:flex; gap:10px; margin-top:auto; padding-bottom:10px; }
        .bottom-item { flex:1; background:white; border-radius:100px; padding:12px; display:flex; align-items:center; justify-content:center; gap:8px; box-shadow:0 4px 12px rgba(0,0,0,0.08); cursor:pointer; }
        .bottom-item span { color:#102646; font-weight:800; font-size:12px; }
    </style>
</head>
<body>
    <div class="main-wrapper">
        <div class="header-container">
            <div class="back-icon" onclick="go('userdash_arabic')">›</div>
            <h2 class="title">الإعدادات</h2>
        </div>
        <div class="setting-item" onclick="go('6_Change_Password')">
            <div class="item-right"><i class="fas fa-lock"></i><span class="item-text">تغيير كلمة المرور</span></div>
            <span class="arrow">‹</span>
        </div>
        <div class="setting-item" onclick="go('7_Change_Language')">
            <div class="item-right"><i class="fas fa-globe"></i><span class="item-text">تغيير اللغة</span></div>
            <span class="arrow">‹</span>
        </div>
        <div class="setting-item" onclick="go('8_Rate_App')">
            <div class="item-right"><i class="fas fa-star"></i><span class="item-text">تقييم التطبيق</span></div>
            <span class="arrow">‹</span>
        </div>
        <div class="setting-item" onclick="go('logout')">
            <div class="item-right"><i class="fas fa-sign-out-alt"></i><span class="item-text">تسجيل الخروج</span></div>
            <span class="arrow">‹</span>
        </div>
        <div class="bottom-row">
            <div class="bottom-item" onclick="go('9_Report_Problem')"><span>الإبلاغ عن مشكلة</span></div>
            <div class="bottom-item" onclick="go('10_Contact_Us')"><span>تواصل معنا</span></div>
        </div>
    </div>
    <script>
        function go(p) { window.parent.location.href = window.parent.location.pathname + "?nav=" + p; }
    </script>
</body>
</html>
""", height=600)
