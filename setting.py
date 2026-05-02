import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Settings UI", layout="centered")

# 2. التنسيق البرمجي (CSS) المطور لمحاكاة تفاصيل الصورة
st.markdown("""
<style>
/* استيراد مكتبة Font Awesome للأيقونات */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

[data-testid="stAppViewContainer"] {
    background-color: #f0f2f6;
}

.block-container {
    max-width: 400px !important;
    margin: auto !important;
    padding: 40px 25px !important;
    background: linear-gradient(180deg, #cfdfea 0%, #e3eaf0 100%);
    border-radius: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

/* تصميم الزر (الكبسولة) ليحتوي على أيقونة جهة اليسار */
div.stButton > button {
    width: 100% !important;
    height: 60px !important; 
    border-radius: 100px !important; 
    border: none !important;
    background-color: rgba(255, 255, 255, 0.9) !important;
    color: #555 !important;
    font-size: 17px !important;
    font-weight: 500;
    margin-bottom: 15px;
    
    /* توزيع المحتوى داخل الزر */
    display: flex !important;
    align-items: center !important;
    justify-content: flex-start !important; /* البدء من اليسار */
    padding-left: 25px !important;
    
    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background-color: #ffffff !important;
    box-shadow: 0 6px 15px rgba(0,0,0,0.1) !important;
}

/* تنسيق الأيقونة داخل الزر */
.btn-icon {
    margin-right: 20px; /* مسافة بين الأيقونة والنص */
    font-size: 20px;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# 3. بناء الواجهة
st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <span style="font-size: 22px; font-weight: bold; color: #333;">Settings</span>
    </div>
""", unsafe_allow_html=True)

# دالة لإنشاء الأزرار بشكل احترافي يحاكي الصورة
def create_settings_button(icon_class, label):
    # نستخدم HTML داخل الزر لإظهار الأيقونة بجانب النص
    # ملاحظة: Streamlit لا يدعم HTML مباشرة داخل st.button، 
    # لذا سنستخدم خدعة التوسيط بالمسافات أو الأيقونات النصية.
    # لكن لجعله مطابقاً للصورة، يفضل استخدام الرموز أو الدمج:
    if st.button(f"🚪 {label}"): # استخدمنا الإيموجي هنا لسهولة التنفيذ الفوري
        st.write(f"Clicked on {label}")

# الأزرار كما في طلبك
create_settings_button("", "Change Password")
create_settings_button("", "Change Language")
create_settings_button("", "Rate App")

# زر تسجيل الخروج (Log Out) مع الأيقونة المطلوبة
if st.button("⬅️ &nbsp;&nbsp;&nbsp;&nbsp; Log Out"):
    st.info("Logged Out Successfully")

st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)

# السطر الأخير
col1, col2 = st.columns(2)
with col1:
    if st.button("⚠️ Report"): pass
with col2:
    if st.button("✉️ Contact"): pass
