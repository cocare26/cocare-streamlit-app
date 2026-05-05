import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Language", layout="centered")

# --- تنسيق الـ CSS (نفس التصميم تبعك) ---
st.markdown("""
<style>
    html, body, [data-testid="stAppViewContainer"] { background:#f0f7ff; direction: ltr; }
    #MainMenu, header, footer { visibility:hidden; }
    .header { position:relative; text-align:center; margin-bottom:30px; }
    .title-text { font-size:20px; font-weight:900; color:#102646; }
    .back-btn { position:absolute; left:0; top:0; font-size:26px; cursor:pointer; text-decoration:none; color:black; }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown(f"""
<div class="header">
    <a href="/Settings" target="_top" class="back-btn">‹</a>
    <div class="title-text">Change Language</div>
</div>
""", unsafe_allow_html=True)

# --- الـ UI والـ Logic ---
# بنعرف متغير بنستلم فيه القيمة من الجافاسكريبت
res = components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
    .item {
        display:flex; justify-content:space-between; align-items:center;
        background:white; border-radius:100px; padding:14px 22px;
        margin-bottom:15px; box-shadow:0 4px 12px rgba(0,0,0,0.08);
        color:#102646; font-weight:800; cursor:pointer; font-family:'Segoe UI';
    }
</style>
</head>
<body>
    <div class="item" onclick="sendAction('go_ar')">
        <span>🌐 Arabic</span>
        <span>›</span>
    </div>
    <div class="item" onclick="sendAction('go_en')">
        <span>🌐 English</span>
        <span>✔</span>
    </div>

<script>
    function sendAction(lang) {
        // هاي بتبعت إشارة لستريم ليت
        window.parent.postMessage({
            isStreamlitMessage: true,
            type: "streamlit:setComponentValue",
            value: lang
        }, "*");
    }
</script>
</body>
</html>
""", height=300)

# --- معالجة الانتقال في البايثون ---
# هون السحر! أول ما نضغط عربي، القيمة بتصير 'go_ar' والبايثون بيحولك
if res == "go_ar":
    st.switch_page("pages/settingar.py")
elif res == "go_en":
    st.switch_page("pages/Settings.py")
