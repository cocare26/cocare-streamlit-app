import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Language", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

html, body, [data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:430px;
    margin:auto;
    padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px;
}
</style>
""", unsafe_allow_html=True)

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
    background:transparent;
    display:flex;
    justify-content:center;
}

.main-wrapper {
    width:100%;
    max-width:380px;
    display:flex;
    flex-direction:column;
    height:520px;
}

/* HEADER */
.header {
    text-align:center;
    position:relative;
    margin-bottom:40px;
}

.back {
    position:absolute;
    left:0;
    font-size:28px;
    cursor:pointer;
    color:#102646;
}

.title {
    font-weight:900;
    font-size:20px;
    color:#102646;
}

/* ITEM */
.item {
    background:white;
    border-radius:100px;
    padding:14px 22px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    cursor:pointer;
    transition:0.3s;
}

.item:hover {
    transform:translateY(-2px);
    box-shadow:0 6px 15px rgba(0,0,0,0.1);
}

.left {
    display:flex;
    align-items:center;
    gap:12px;
}

.icon {
    color:#102646;
}

.label {
    font-weight:800;
    color:#102646;
}

/* STATUS */
.check {
    color:#0d69dd;
}

.arrow {
    font-size:18px;
    color:#102646;
}
</style>
</head>

<body>

<div class="main-wrapper">

<div class="header">
    <div class="back" onclick="goSettings()">‹</div>
    <h2 class="title">Change Language</h2>
</div>

<!-- Arabic -->
<div class="item" onclick="selectLang('arabic')">
    <div class="left">
        <i class="fas fa-globe icon"></i>
        <span class="label">Arabic</span>
    </div>
    <i class="fas fa-check check"></i>
</div>

<!-- English -->
<div class="item" onclick="selectLang('english')">
    <div class="left">
        <i class="fas fa-globe icon"></i>
        <span class="label">English</span>
    </div>
    <span class="arrow">›</span>
</div>

</div>

<script>
function goSettings(){
    window.parent.location.href = "/?page=settings";
}

function selectLang(lang){
    // هون ممكن مستقبلاً تخزن اللغة

    if(lang === "arabic"){
        window.parent.location.href = "/?page=settings-ar";
    } else {
        window.parent.location.href = "/?page=settings";
    }
}
</script>

</body>
</html>
""", height=600)
