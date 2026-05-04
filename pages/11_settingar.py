import streamlit as st

# 1. إعداد الصفحة
st.set_page_config(page_title="الإعدادات", layout="centered")

# 2. CSS السحري لتحويل أزرار ستريمليت لكبسولات فخمة
st.markdown("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
/* إخفاء عناصر ستريمليت */
#MainMenu, header, footer { visibility:hidden; }
[data-testid="stAppViewContainer"] { background:#f0f7ff; }

/* حاوية الصفحة */
.block-container {
    max-width:430px; margin:auto; padding:18px 16px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100% );
    border-radius:42px; box-shadow:0 14px 35px rgba(0,0,0,.15);
    min-height: 620px; direction: rtl;
}

/* تحويل أزرار ستريمليت لكبسولات */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border-radius: 100px !important;
    padding: 25px 22px !important;
    margin-bottom: 12px !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08) !important;
    text-align: right !important;
    font-weight: 800 !important;
    font-size: 15px !important;
    display: flex !important;
    justify-content: space-between !important;
    align-items: center !important;
    transition: 0.3s !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.12) !important;
}

/* زر الرجوع */
.back-container { display: flex; align-items: center; justify-content: center; margin-bottom: 30px; position: relative; }
.back-btn-wrapper { position: absolute; right: 0; top: 0; }
.back-btn-wrapper div.stButton > button {
    background: transparent !important;
    box-shadow: none !important;
    font-size: 30px !important;
    padding: 0 !important;
    width: auto !important;
    margin: 0 !important;
}

/* الصف السفلي */
.bottom-btns { display: flex; gap: 10px; margin-top: 30px; }
.bottom-btns div.stButton > button {
    padding: 15px !important;
    font-size: 13px !important;
    justify-content: center !important;
    text-align: center !important;
}
</style>
""", unsafe_allow_html=True)

# 3. محتوى الصفحة بأزرار ستريمليت الحقيقية
st.markdown('<div class="back-container">', unsafe_allow_html=True)
col_back, col_title = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-btn-wrapper">', unsafe_allow_html=True)
    if st.button("›", key="back"):
        st.switch_page("pages/userdash_arabic.py")
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<h2 style="color:#102646; font-weight:900; margin:0; text-align:center;">الإعدادات</h2></div>', unsafe_allow_html=True)

# الأزرار الرئيسية مع الأيقونات
if st.button("🔒 تغيير كلمة المرور                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ‹", key="pass"):
    st.switch_page("pages/6_Change_Password.py")

if st.button("🌐 تغيير اللغة                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         صفحات السيتنغ بدنا نفصلهم 


أي خدمة ثانية أنا موجود يا قلبي!
