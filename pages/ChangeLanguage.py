import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Language", layout="centered")

# --- التنسيق الأساسي ---
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }
html, body, [data-testid="stAppViewContainer"] { background:#f0f7ff; font-family:'Segoe UI'; }
#MainMenu, header, footer { visibility:hidden; }
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15); min-height:600px;
}
.header { position:relative; text-align:center; margin-bottom:30px; }
.back-style { position:absolute; left:0; top:0; }
.back-style .stButton > button { background:transparent !important; border:none !important; color:black !important; font-size:26px !important; }
.title-text { font-size:20px; font-weight:900; color:#102646; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="header">', unsafe_allow_html=True)
st.markdown('<div class="back-style">', unsafe_allow_html=True)
if st.button("‹"):
    st.switch_page("pages/Settings.py")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="title-text">Change Language</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- UI (HTML/JS) ---
# قمنا بتعريف متغير "sel" لاستقبال الإشارة من الـ HTML
sel = components.html("""
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
    color:#102646; font-weight:800; cursor:pointer; transition:0.2s;
}
.item:hover { transform:translateY(-2px); }
</style>
</head>
<body>
<div class="wrapper">
    <!-- عند الضغط هنا، نرسل إشارة "go_ar" للبايثون -->
    <div class="item" onclick="sendAction('go_ar')">
        <span>🌐 Arabic</span>
        <span>›</span>
    </div>

    <!-- عند الضغط هنا، نرسل إشارة "go_en" للبايثون -->
    <div class="item" onclick="sendAction('go_en')">
        <span>🌐 English</span>
        <span>✔</span>
    </div>
</div>

<script>
function sendAction(val) {
    window.parent.postMessage({
        isStreamlitMessage: true,
        type: "streamlit:setComponentValue",
        value: val
    }, "*");
}
</script>
</body>
</html>
""", height=300)

# --- الانتقال (Logic) ---
# هنا يتم الربط: إذا كانت القيمة "go_ar"، ننتقل لصفحة الإعدادات العربية
if sel == "go_ar":
    st.switch_page("pages/settingar.py")
elif sel == "go_en":
    st.switch_page("pages/Settings.py")
