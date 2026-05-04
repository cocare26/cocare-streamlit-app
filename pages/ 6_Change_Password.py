import streamlit as st

st.set_page_config(page_title="تغيير كلمة المرور", layout="centered")

st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
#MainMenu, header, footer { visibility:hidden; }
[data-testid="stAppViewContainer"] { background:#f0f7ff; }
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100% );
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 600px; direction: rtl;
}
.back-icon { position:absolute; right:0; font-size:28px; color:#102646; text-decoration:none; }
.input-capsule { background:white; border-radius:100px; padding:12px 18px; margin-bottom:15px; box-shadow:0 4px 12px rgba(0,0,0,0.08); }
.input-capsule input { border:none; outline:none; width:100%; font-size:14px; color:#102646; text-align:right; }
.save-btn { background:white; border-radius:100px; width:100%; padding:14px; text-align:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); border:none; cursor:pointer; color:#102646; font-weight:900; font-size:16px; margin-top:50px; }
</style>

<div style="text-align:center; margin-bottom:35px; position:relative; padding-top:10px;">
    <a href="/main_app?page=settings-ar" target="_top" class="back-icon">›</a>
    <h2 style="color:#102646; font-weight:900; margin:0;">تغيير كلمة المرور</h2>
</div>

<div class="input-capsule"><input type="password" placeholder="كلمة المرور الحالية"></div>
<div class="input-capsule"><input type="password" placeholder="كلمة المرور الجديدة"></div>
<div class="input-capsule"><input type="password" placeholder="تأكيد كلمة المرور"></div>

<div style="text-align:center; margin-top:10px;">
    <a href="/main_app?page=Report_Problem-ar" target="_top" style="color:#102646; font-size:13px; font-weight:700; text-decoration:none;">Report Password</a>
</div>

<button class="save-btn" onclick="alert('تم الحفظ!')">حفظ</button>
""", unsafe_allow_html=True)
