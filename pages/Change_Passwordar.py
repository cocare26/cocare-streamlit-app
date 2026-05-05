import streamlit as st
import time

st.set_page_config(page_title="تغيير كلمة المرور", layout="centered")

# ===== التنسيق (CSS) لضبط شكل المدخلات والأزرار =====
st.markdown("""
<style>
/* ضبط الاتجاه للعربية */
[data-testid="stAppViewContainer"] {
    background:#f0f7ff;
    direction: rtl;
}

#MainMenu, header, footer { visibility:hidden; }

.block-container {
    max-width:400px;
    margin:auto;
    padding:25px;
    background:linear-gradient(180deg,#dff2ff 0%,#c7e7ff 55%,#f4fbff 100%);
    border-radius:40px;
    box-shadow:0 14px 35px rgba(0,0,0,.1);
}

/* تنسيق خانات الإدخال */
.stTextInput > div > div > input {
    border-radius: 100px !important;
    padding: 12px 20px !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05) !important;
}

/* تنسيق زر الحفظ */
div.stButton > button {
    width: 100% !important;
    border-radius: 100px !important;
    padding: 15px !important;
    background: white !important;
    color: #102646 !important;
    font-weight: 900 !important;
    border: none !important;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1) !important;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ===== الهيدر (العنوان وزر الرجوع) =====
col_back, col_title = st.columns([1, 4])
with col_back:
    if st.button("›"):
        st.switch_page("pages/settingar.py") # تأكد من اسم ملف الإعدادات هنا

with col_title:
    st.markdown("<h3 style='text-align:center; color:#102646; margin-top:5px;'>تغيير كلمة المرور</h3>", unsafe_allow_html=True)

st.markdown("---")

# ===== نموذج المدخلات (Streamlit Form) =====
with st.container():
    old_pass = st.text_input("كلمة المرور الحالية", type="password", placeholder="ادخل كلمة المرور الحالية")
    new_pass = st.text_input("كلمة المرور الجديدة", type="password", placeholder="ادخل كلمة المرور الجديدة")
    confirm_pass = st.text_input("تأكيد كلمة المرور الجديدة", type="password", placeholder="اعد كتابة كلمة المرور")

    if st.button("حفظ التغييرات"):
        if not old_pass or not new_pass or not confirm_pass:
            st.error("يرجى ملء جميع الحقول")
        elif new_pass != confirm_pass:
            st.error("كلمات المرور غير متطابقة")
        else:
            # هنا يوضع كود الحفظ الفعلي
            st.success("تم تغيير كلمة المرور بنجاح ✅")
            time.sleep(1) # تأخير بسيط ليتمكن المستخدم من رؤية رسالة النجاح
            
            # الربط: الانتقال لصفحة الإعدادات العربية
            try:
                st.switch_page("pages/settingar.py")
            except:
                st.switch_page("settingar.py")
