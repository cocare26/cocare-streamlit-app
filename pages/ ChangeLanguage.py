import streamlit as st

st.set_page_config(page_title="تغيير اللغة", layout="centered")

st.markdown("""
<style>
#MainMenu, header, footer { visibility:hidden; }
[data-testid="stAppViewContainer"] { background:#f0f7ff; }
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px; direction: rtl;
}
.lang-item { background:white; border-radius:100px; padding:18px 22px; margin-bottom:15px; display:flex; justify-content:space-between; box-shadow:0 4px 12px rgba(0,0,0,0.08); text-decoration:none !important; color:#102646; font-weight:800; }
</style>

<div style="text-align:center; margin-bottom:40px; position:relative; padding-top:10px;">
    <a href="/main_app?page=settings-ar" target="_top" style="position:absolute; right:0; font-size:28px; color:#102646; text-decoration:none;">›</a>
    <h2 style="color:#102646; font-weight:900;">تغيير اللغة</h2>
</div>

<a href="/main_app?page=settings-ar" target="_top" class="lang-item"><span>العربية</span><span style="color:#0d69dd;">✓</span></a>
<a href="/main_app?page=settings-en" target="_top" class="lang-item"><span>English</span><span>‹</span></a>
""", unsafe_allow_html=True)
