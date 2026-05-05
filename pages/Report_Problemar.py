import streamlit as st
import streamlit.components.v1 as components

# ... (نفس كود الـ CSS والـ Header السابق)

# ===== UI (HTML Component) =====
components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
/* ... (نفس التنسيقات السابقة) ... */
body { font-family: 'Segoe UI'; background: transparent; margin: 0; display: flex; justify-content: center; }
.main-wrapper { width: 100%; max-width: 290px; height: 480px; display: flex; flex-direction: column; }
.report-textarea { 
    width: 100%; height: 220px; border-radius: 25px; border: none; outline: none; 
    padding: 18px; background: white; font-size: 16px; color: #0f2446; 
    resize: none; box-shadow: 0 4px 12px rgba(0,0,0,0.08); font-family: 'Segoe UI'; 
}
.send-btn { 
    background: white; border-radius: 100px; width: 100%; padding: 14px 22px; 
    display: flex; align-items: center; justify-content: space-between; 
    border: none; margin-top: auto; cursor: pointer; box-shadow: 0 4px 12px rgba(0,0,0,0.08); 
    transition: 0.3s; font-family: 'Segoe UI'; 
}
.send-btn span { color: #0f2446; font-weight: 700; font-size: 14px; }
.main-icon { color: #808080; font-size: 18px; transform: scaleX(-1); }
</style>
</head>
<body>
<div class="main-wrapper">
    <textarea class="report-textarea" placeholder="أنا بحاجة للمساعدة..."></textarea>
    <div style="margin-top:auto;">
        <button class="send-btn" onclick="sendAndRedirect()">
            <i class="fas fa-paper-plane main-icon"></i>
            <span>إرسال التقرير</span>
        </button>
    </div>
</div>

<script>
function sendAndRedirect(){
    // 1. إظهار رسالة النجاح
    alert("تم إرسال التقرير بنجاح ✅");
    
    // 2. التوجيه الإجباري لصفحة الإعدادات العربية
    // ملاحظة: في Streamlit Cloud الرابط يكون عادة اسم الملف بدون .py
    window.parent.location.assign('settingar');
}
</script>

</body>
</html>
""", height=500)
