import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Change Password", layout="centered")

# ===== CSS =====
st.markdown("""
<style>
* { margin:0; padding:0; box-sizing:border-box; direction:ltr; }

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
    min-height: 600px;
}

/* 🔥 سهم الرجوع */
.back-style .stButton > button {
    background:transparent !important;
    box-shadow:none !important;
    font-size:26px !important;
    width:auto !important;
    color:#102646 !important;
}
</style>
""", unsafe_allow_html=True)

# ===== 🔙 BACK BUTTON (Streamlit) =====
col_back, _ = st.columns([1, 10])
with col_back:
    st.markdown('<div class="back-style">', unsafe_allow_html=True)
    if st.button("‹"):
        st.switch_page("pages/Settings.py")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== UI =====
components.html("""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<style>
body {
    margin:0;
    font-family:'Segoe UI';
    background:transparent;
    display:flex;
    justify-content:center;
}

.main-wrapper {
    width:100%;
    max-width:380px;
    display:flex;
    flex-direction:column;
    height:520px;
}

/* HEADER */
.header {
    text-align:center;
    margin-bottom:30px;
}

.title {
    font-weight:900;
    color:#102646;
}

/* INPUT */
.input {
    background:white;
    border-radius:100px;
    padding:12px 18px;
    margin-bottom:15px;
    display:flex;
    align-items:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.input i {
    margin-right:10px;
    color:#102646;
}

.input input {
    border:none;
    outline:none;
    flex:1;
}

/* BUTTON */
.save {
    margin-top:auto;
}

.save button {
    width:100%;
    border-radius:100px;
    padding:14px;
    border:none;
    background:white;
    font-weight:900;
    cursor:pointer;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* POPUP */
.modal {
    display:none;
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.4);
    justify-content:center;
    align-items:center;
}

.modal-box {
    background:white;
    padding:25px;
    border-radius:20px;
    text-align:center;
    width:250px;
}

.modal-box p {
    font-weight:800;
    color:#102646;
    margin-bottom:20px;
}

.modal-box button {
    border:none;
    padding:10px 20px;
    border-radius:100px;
    background:#dff2ff;
    cursor:pointer;
    font-weight:700;
}
</style>
</head>

<body>

<div class="main-wrapper">

<div class="header">
    <h2 class="title">Change Password</h2>
</div>

<div class="input">
    <i class="fas fa-lock"></i>
    <input type="password" id="old" placeholder="Current Password">
</div>

<div class="input">
    <i class="fas fa-lock"></i>
    <input type="password" id="new1" placeholder="New Password">
</div>

<div class="input">
    <i class="fas fa-lock"></i>
    <input type="password" id="new2" placeholder="Confirm Password">
</div>

<div class="save">
    <button onclick="save()">Save</button>
</div>

</div>

<!-- POPUP -->
<div class="modal" id="popup">
    <div class="modal-box">
        <p>Password changed successfully ✅</p>
        <button onclick="goSettings()">OK</button>
    </div>
</div>

<script>
function save(){
    let oldPass = document.getElementById("old").value;
    let p1 = document.getElementById("new1").value;
    let p2 = document.getElementById("new2").value;

    if(oldPass === ""){
        alert("Enter current password");
        return;
    }

    if(p1 === "" || p2 === ""){
        alert("Enter new password");
        return;
    }

    if(p1 !== p2){
        alert("Passwords do not match");
        return;
    }

    document.getElementById("popup").style.display = "flex";
}

function goSettings(){
    window.parent.location.href = "/?page=settings";
}
</script>

</body>
</html>
""", height=600)
