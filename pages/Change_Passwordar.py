import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تغيير كلمة المرور", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:rtl; }

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
    min-height:600px;
}

.title-wrapper {
    display:flex;
    align-items:center;
    justify-content:center;
    position:relative;
    margin-bottom:25px;
}

.back-link {
    position:absolute;
    right:0;
    text-decoration: none;
}

.back-circle {
    background: white;
    color: black;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    cursor: pointer;
}

.title-text {
    font-size:20px;
    font-weight:900;
    color:#102646;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
# تم استبدال زر st.button برابط HTML مباشر لتجنب أخطاء السيرفر
# ---------------- HEADER ----------------
# هذا الجزء يوضع بعد الـ Style وقبل الـ HTML UI
st.markdown(f"""
<div class="title-wrapper">
    <!-- هنا نضع الكود الذي سألت عنه ليعمل كزر رجوع -->
    <a href="/Settingar" target="_self" class="back-link">
        <div class="back-circle">›</div>
    </a>
    <div class="title-text">تغيير كلمة المرور</div>
</div>
""", unsafe_allow_html=True)
# ---------------- HTML UI ----------------
value = components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body { margin:0; font-family:'Segoe UI'; background:transparent; display:flex; justify-content:center; }
.main-wrapper { width:100%; max-width:380px; display:flex; flex-direction:column; }

.input {
    background:white;
    border-radius:100px;
    padding:12px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.25s ease;
}

.input:hover { transform: translateY(-5px); }
.input i { margin-left:10px; color:#102646; }
.input input { border:none; outline:none; flex:1; font-family:'Segoe UI'; text-align:right; }
.eye { cursor:pointer; margin-right:10px; }
.save { margin-top:20px; }
.save button {
    width:100%;
    border-radius:100px;
    padding:16px;
    border:none;
    background:white;
    font-weight:900;
    cursor:pointer;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    transition: transform 0.25s ease;
}
.save button:hover { transform: translateY(-5px); }
</style>
</head>

<body>
<div class="main-wrapper">
    <div class="input">
        <i class="fas fa-lock"></i>
        <input type="password" id="old" placeholder="كلمة المرور الحالية">
        <i class="fas fa-eye-slash eye"></i>
    </div>
    <div class="input">
        <i class="fas fa-lock"></i>
        <input type="password" id="new1" placeholder="كلمة المرور الجديدة">
        <i class="fas fa-eye-slash eye"></i>
    </div>
    <div class="input">
        <i class="fas fa-lock"></i>
        <input type="password" id="new2" placeholder="تأكيد كلمة المرور الجديدة">
        <i class="fas fa-eye-slash eye"></i>
    </div>
    <div class="save">
        <button onclick="save()">حفظ التغييرات</button>
    </div>
</div>

<script>
function save(){
    let oldPass = document.getElementById("old").value;
    let p1 = document.getElementById("new1").value;
    let p2 = document.getElementById("new2").value;

    if(oldPass === "" || p1 === "" || p2 === ""){
        alert("يرجى ملء جميع الحقول");
        return;
    }

    if(p1 !== p2){
        alert("كلمات المرور غير متطابقة");
        return;
    }

    alert("تم تغيير كلمة المرور بنجاح ✅");
    
    // الانتقال المباشر عبر المتصفح
    window.top.location.href = window.top.location.origin + "/Settingar";
}

document.querySelectorAll(".input").forEach(box => {
    const input = box.querySelector("input");
    const eye = box.querySelector(".eye");
    box.addEventListener("mouseenter", () => {
        input.type = "text";
        eye.classList.replace("fa-eye-slash", "fa-eye");
    });
    box.addEventListener("mouseleave", () => {
        input.type = "password";
        eye.classList.replace("fa-eye", "fa-eye-slash");
    });
});
</script>
</body>
</html>
""", height=420)

# ---------------- NAVIGATION ----------------
# تم حذف سطر st.switch_page نهائياً لأنه يسبب الخطأ الأحمر
