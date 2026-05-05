import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Language", layout="centered")
# ✅ تخزين اللغة
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ✅ قراءة اللغة من الرابط
query = st.query_params
if "lang" in query:
    st.session_state.lang = query["lang"]

# ✅ تحديد الصح
arabic_check = "✔" if st.session_state.lang == "ar" else "›"
english_check = "✔" if st.session_state.lang == "en" else "›

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

/* ===== HEADER ===== */
.header {
    position:relative;
    text-align:center;
    margin-bottom:30px;
}

/* السهم */
.back-style {
    position:absolute;
    left:0;
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
if st.button("‹"):
    st.switch_page("pages/Settings.py")
st.markdown('</div>', unsafe_allow_html=True)

# العنوان بالنص
st.markdown('<div class="title-text">Change Language</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ===== UI =====
components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body {
    margin:0;
    font-family:'Segoe UI';
    display:flex;
    justify-content:center;
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
}

.item:hover {
    transform:translateY(-2px);
}
</style>
</head>

<body>

<div class="wrapper">

<!-- Arabic -->
<a href="/?lang=ar" target="_top" class="item">
    <span>🌐 Arabic</span>
    ›
</a>

<a href="/?lang=en" target="_top" class="item">
    <span>🌐 English</span>
    ✔
</a>
</a>

</div>

</body>
</html>
""", height=600)
