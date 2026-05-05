import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Language", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }
html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI';
}
#MainMenu, header, footer { visibility:hidden; }
.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height:600px;
}
.header { position:relative; text-align:center; margin-bottom:30px; }
.back-link { position:absolute; left:0; top:0; text-decoration:none; color:black; font-size:26px; }
.title-text { font-size:20px; font-weight:900; color:#102646; }
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown(f"""
<div class="header">
    <a href="/Settings" target="_top" class="back-link">‹</a>
    <div class="title-text">Change Language</div>
</div>
""", unsafe_allow_html=True)

# ===== UI =====
# هنا أضفنا دالة الانتقال المباشر لصفحة الإعدادات العربية
components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
body { margin:0; font-family:'Segoe UI'; display:flex; justify-content:center; background:transparent; }
.wrapper { width:100%; max-width:380px; }
.item {
    display:flex; justify-content:space-between; align-items:center;
    background:white; border-radius:100px; padding:14px 22px;
    margin-bottom:15px; box-shadow:0 4px 12px rgba(0,0,0,0.08);
    color:#102646; font-weight:800; transition:0.2s; cursor:pointer;
}
.item:hover { transform:translateY(-2px); background:#f9f9f9; }
</style>
</head>
<body>
<div class="wrapper">

    <!-- كبسة العربي: ستقوم بتوجيهك فوراً لصفحة الإعدادات العربية -->
    <div class="item" onclick="changeToArabic()">
        <span>🌐 Arabic</span>
        <span>›</span>
    </div>

    <!-- كبسة الإنجليزي: تعيدك لصفحة الإعدادات الإنجليزية -->
    <div class="item" onclick="changeToEnglish()">
        <span>🌐 English</span>
        <span>✔</span>
    </div>

</div>

<script>
// الدالة المسؤولة عن تحويلك للإعدادات العربية
function changeToArabic() {
    window.top.location.href = window.top.location.origin + "/settingar";
}

// الدالة المسؤولة عن تحويلك للإعدادات الإنجليزية
function changeToEnglish() {
    window.top.location.href = window.top.location.origin + "/Settings";
}
</script>

</body>
</html>
""", height=300)
