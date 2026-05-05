import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="تغيير كلمة المرور", layout="centered")

st.markdown("""
<style>
/* ضبط الاتجاه العام */
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

/* زر الرجوع - موضعه يمين */
.back-style .stButton > button {
    background:white !important;
    color:black !important;
    border-radius:50% !important;
    width:40px !important;
    height:40px !important;
    padding:0 !important;
    font-size:20px !important;
    box-shadow:0 4px 10px rgba(0,0,0,0.08) !important;
}

/* 👇 تعديل العنوان ليصبح في المنتصف تماماً 👇 */
.title-wrapper {
    display: flex;
    align-items: center;
    justify-content: center; /* توسيط أفقي */
    position: relative;
    margin-bottom: 25px;
}

.back-container {
    position: absolute;
    right: 0; /* تثبيت زر الرجوع في أقصى اليمين */
}

.title-text {
    font-size:20px;
    font-weight:900;
    color:#102646;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# هيدر الصفحة (زر رجوع يمين + عنوان في النص)
st.markdown('<div class="title-wrapper">', unsafe_allow_html=True)

# زر الرجوع
with st.container():
    st.markdown('<div class="back-container"><div class="back-style">', unsafe_allow_html=True)
    if st.button("›"): 
         st.switch_page("settingar.py")
         st.markdown('</div></div>', unsafe_allow_html=True)

# نص العنوان
st.markdown('<div class="title-text">تغيير كلمة المرور</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

components.html("""
<!DOCTYPE html>
<html dir="rtl">
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body { margin:0; font-family:'Segoe UI'; background:transparent; display:flex; justify-content:center; }
.main-wrapper { width:100%; max-width:380px; display:flex; flex-direction:column; }
.input { background:white; border-radius:100px; padding:12px 18px; margin-bottom:15px; display:flex; align-items:center; box-shadow:0 4px 12px rgba(0,0,0,0.08); transition: transform 0.25s ease; }
.input:hover { transform: translateY(-5px); }
.input i { margin-left:10px; color:#102646; }
.input input { border:none; outline:none; flex:1; font-family: 'Segoe UI'; text-align: right; }
.eye { cursor: pointer; margin-right: 10px; }
.save { margin-top:20px; }
.save button { width:100%; border-radius:100px; padding:16px; border:none; background:white; font-weight:900; cursor:pointer; box-shadow:0 4px 12px rgba(0,0,0,0.08); transition: transform 0.25s ease; font-family: 'Segoe UI'; }
.save button:hover { transform: translateY(-5px); }
</style>
</head>
<body>
<div class="main-wrapper">
<div class="input"> <i class="fas fa-lock"></i> <input type="password" id="old" placeholder="كلمة المرور الحالية"> <i class="fas fa-eye-slash eye"></i> </div>
<div class="input"> <i class="fas fa-lock"></i> <input type="password" id="new1" placeholder="كلمة المرور الجديدة"> <i class="fas fa-eye-slash eye"></i> </div>
<div class="input"> <i class="fas fa-lock"></i> <input type="password" id="new2" placeholder="تأكيد كلمة المرور الجديدة"> <i class="fas fa-eye-slash eye"></i> </div>
<div class="save"> <button onclick="save()">حفظ التغييرات</button> </div>
</div>
<script>
function save(){
    let oldPass = document.getElementById("old").value;
    let p1 = document.getElementById("new1").value;
    let p2 = document.getElementById("new2").value;
    if(oldPass === ""){ alert("يرجى إدخال كلمة المرور الحالية"); return; }
    if(p1 === "" || p2 === ""){ alert("يرجى إدخال كلمة المرور الجديدة"); return; }
    if(p1 !== p2){ alert("كلمات المرور غير متطابقة"); return; }

    
   
alert("تم تغيير كلمة المرور بنجاح ✅");

// هذا هو البديل الصحيح والوحيد داخل الجافاسكريبت للربط
window.parent.location.assign("/settingar");
   
}
document.querySelectorAll(".input").forEach(box => {
    const input = box.querySelector("input");
    const eye = box.querySelector(".eye");
    box.addEventListener("mouseenter", () => { input.type = "text"; eye.classList.replace("fa-eye-slash", "fa-eye"); });
    box.addEventListener("mouseleave", () => { input.type = "password"; eye.classList.replace("fa-eye", "fa-eye-slash"); });
});
</script>
</body>
</html>
""", height=420)
