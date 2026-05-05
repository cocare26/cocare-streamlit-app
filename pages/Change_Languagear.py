import streamlit as st
import streamlit.components.v1 as components

navigate_to = st_javascript("""
    window.addEventListener('message', function(e) {
        if (e.data.type === 'navigate') {
            window.parent.location.href = window.parent.location.origin + '/' + e.data.page;
        }
    });
""")





الانتقال الرسمي

st.set_page_config(page_title="تغيير اللغة", layout="centered")

# ✅ تخزين اللغة
if "lang" not in st.session_state:
    st.session_state.lang = "ar"

# ✅ قراءة اللغة من الرابط
query = st.query_params
if "lang" in query:
    st.session_state.lang = query["lang"]

# ===== CSS =====
st.markdown("""
<style>
/* ضبط الاتجاه للعربية */
* { margin:0; padding:0; box-sizing:border-box; direction:rtl; }

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

/* ===== HEADER ===== */
.header {
    position:relative;
    text-align:center;
    margin-bottom:30px;
}

/* السهم (جهة اليمين في العربي) */
.back-style {
    position:absolute;
    right:0;
    top:0;
}

.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    color:black !important;
    font-size:26px !important;
    width:auto !important;
    padding:0 !important;
}

/* العنوان */
.title-text {
    font-size:20px;
    font-weight:900;
    color:#102646;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="header">', unsafe_allow_html=True)

# السهم
st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("›"):
    st.switch_page("pages/settingar.py")
st.markdown('</div>', unsafe_allow_html=True)

# العنوان
st.markdown('<div class="title-text">تغيير اللغة</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== UI (HTML Component) =====
result = components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body {
    margin:0;
    font-family:'Segoe UI';
    display:flex;
    justify-content:center;
    background: transparent;
}

.wrapper {
    width:100%;
    max-width:380px;
}

/* ITEM */
.item {
    display:flex;
    justify-content:space-between;
    align-items:center;
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    text-decoration:none;
    color:#102646;
    font-weight:800;
    transition:0.2s;
    cursor: pointer;
}

.item:hover {
    transform:translateY(-2px);
}
</style>
</head>

<body>
<div class="wrapper">

    <!-- الخيار العربي (محدد حالياً) -->
    <div class="item" onclick="window.parent.history.back();">
        <span>🌐 العربية</span>
        <span>✔</span>
    </div>

    <!-- الخيار الإنجليزي -->
  <div class="item" onclick="window.top.location.href = window.top.location.origin + '/Settings';">
    <span>🌐 English</span>
    <span>‹</span>
</div>
</div>

<script>
function goArabic(){
    window.parent.postMessage(
        {type: "streamlit:setComponentValue", value: "go_ar"},
        "*"
    );
}
</script>
</body>
</html>
""", height=600)
