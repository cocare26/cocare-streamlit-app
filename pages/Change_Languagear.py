import streamlit as st
import os
from language_guard import check_language

st.set_page_config(page_title="تغيير اللغة", layout="centered")

check_language(os.path.basename(__file__))

# ===== CSS المطابق للصورة =====
st.markdown("""
<style>
* { direction: rtl; }

[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
}

/* الخلفية */
[data-testid="stAppViewContainer"] {
    background-color: #dff2ff !important;
}

/* إخفاء الهيدر */
[data-testid="stHeader"] {display: none !important;}

/* الكبسولة */
.block-container {
    max-width:430px;
    margin:auto;
    padding:20px;
    background:linear-gradient(180deg,#dff2ff,#c7e7ff,#f4fbff);
    border-radius:40px;
    box-shadow:0 14px 35px rgba(0,0,0,.15);
    position: relative;
    margin-top: 50px;
}

/* زر الرجوع */
.back-style-btn .stButton > button {
    background-color: #1a1c22 !important;
    color: white !important;
    width: 45px !important;
    height: 45px !important;
    border-radius: 12px !important;
    border: none !important;
    font-size: 20px !important;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 !important;
}

/* أزرار اللغات */
div.stButton > button {
    width: 100% !important;
    background-color: white !important;
    color: #102646 !important;
    border: none !important;
    border-radius: 50px !important;
    height: 65px !important;
    margin-bottom: 20px !important;
    font-weight: 700 !important;
    font-size: 19px !important;
    display: flex !important;
    justify-content: space-between !important;
    padding: 0 25px !important;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05) !important;
}

/* فراغ */
.spacer {
    height: 200px;
}
</style>
""", unsafe_allow_html=True)

# ===== الهيدر (السهم + العنوان بنفس السطر) =====
col1, col2, col3 = st.columns([1,6,1])

with col1:
    st.markdown('<div class="back-style-btn">', unsafe_allow_html=True)
    if st.button("‹", key="back_btn"):
        st.switch_page("pages/settingar.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="
        text-align:center;
        font-size:26px;
        font-weight:800;
        color:#102646;
        margin-top:25px; /* 👈 نزلنا الكلمة */
    ">
    تغيير اللغة
    </div>
    """, unsafe_allow_html=True)

# ===== أزرار اللغات =====
col_gap_ar = "&nbsp;" * 35
col_gap_en = "&nbsp;" * 35

if st.button(f"🌐  العربية  {col_gap_ar}{col_gap_ar}✔️"):
    st.session_state.lang = "ar"
    st.switch_page("pages/settingar.py")

if st.button(f"🌐  English {col_gap_en}{col_gap_en} ‹"):
    st.session_state.lang = "en"
    st.switch_page("pages/Settings.py")

# ===== فراغ =====
st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)
