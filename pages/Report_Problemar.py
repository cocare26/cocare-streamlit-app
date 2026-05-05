import streamlit as st
import streamlit.components.v1 as components

# 1. تعريف متغير الحالة للتحويل
if "redirect_to_settings" not in st.session_state:
    st.session_state.redirect_to_settings = False

# 2. التحقق من الحاجة للتحويل (هذا السطر هو الذي سينفذ الانتقال فعلياً)
if st.session_state.redirect_to_settings:
    st.session_state.redirect_to_settings = False # تصفير الحالة
    st.switch_page("pages/settingar.py")

# --- كود الـ CSS والـ Header (نفسه بدون تغيير) ---
st.markdown("""<style>/* كود الـ CSS الخاص بك */</style>""", unsafe_allow_html=True)

# --- مكون الـ HTML المحدث ---
# أضفنا سطر يغير رابط الصفحة في الأعلى بشكل يدوي كحل بديل
components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
</head>
<body>
    <textarea id="reportText" style="width:100%; height:200px; border-radius:20px; padding:15px;"></textarea>
    <button onclick="send()" style="width:100%; padding:15px; border-radius:30px; cursor:pointer;">إرسال التقرير</button>

<script>
function send(){
    alert("تم إرسال التقرير بنجاح ✅");
    
    // الحل الأكثر قوة: تغيير مسار الصفحة الأم (Top Window) يدوياً
    // نستخدم الرابط الكامل المسجل في Streamlit
    var currentUrl = window.parent.location.href;
    var baseUrl = currentUrl.substring(0, currentUrl.lastIndexOf('/'));
    window.parent.location.href = baseUrl + '/settingar';
}
</script>
</body>
</html>
""", height=500)
